#Aplying random shuffle to the question list to make the quiz more dynamic

#Calling the load_questions function from question_bank.py to get the list of questions and then shuffling them using random.shuffle() before returning the shuffled list.
import random 
from question_bank import load_questions

#using random.shuffle to shuffle the questions
def get_shuffled_questions():
    questions = load_questions()
    random.shuffle(questions)
    return questions

#Function to ask the user how many questions
def select_questions(questions, count):
    if count > len(questions):
        print(f"Only {len(questions)} questions available. Selecting all questions.")
        return questions
    else:
        return questions[:count]

print(questions)