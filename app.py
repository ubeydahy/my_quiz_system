from fastapi import FastAPI
from question_bank import load_questions, add_question, filter_questions_by_difficulty
from quiz_engine import shuffle_questions, select_number_of_questions, run_quiz, display_results, save_to_leaderboard
from fastapi import Body
from pydantic import BaseModel
from typing import List

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Quiz API is running"}

# Get all questions
@app.get("/questions")
def get_questions():
    return load_questions()

# Add questions (POST)
class QuestionModel(BaseModel):
    question: str
    options: List[str]
    answer: str
    difficulty: str

@app.post("/add-question")
def add_new_question(new_question: QuestionModel):
    questions = load_questions()
    added = add_question(questions, new_question.dict())
    return {"message": "Question added successfully", "data": added}

# Filter by difficulty
@app.get("/questions/filter/{difficulty}")
def get_by_difficulty(difficulty: str):
    questions = load_questions()
    return filter_questions_by_difficulty(questions, difficulty)

# Start quiz
@app.post("/start-quiz")
def start_quiz(count: int = 5):
    questions = load_questions()
    shuffled = shuffle_questions(questions)
    selected = select_number_of_questions(shuffled, count)
    
    return {
        "message": "Quiz Started",
        "questions": selected
    }
    
#Submit answers
class AnswerPayload(BaseModel):
    questions: list
    answers: List[str]
    name: str = "Anonymous"

@app.post("/submit-answers")
def submit_answers(payload: AnswerPayload = Body(...)):
    selected_questions =payload.questions
    user_answers = payload.answers
    name = payload.name
    
    score, wrong = run_quiz(selected_questions, user_answers)
    results = display_results(score, len(selected_questions), wrong)

    save_to_leaderboard(name, score, len(selected_questions))

    return results
