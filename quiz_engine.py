import random

# Function to shuffle questions
def shuffle_questions(questions):
    random.shuffle(questions)
    return questions

# Function to select number of questions (API version for selecting number of questions)
def select_number_of_questions(questions, count):
    if count == 5:
        return questions[:5]
    elif count == 10:
        return questions[:10]
    elif count == 15:
        return questions[:15]
    else:
        print("Invalid number of questions selected. Defaulting to 5.")
        return questions[:5]
    
# Function to run the quiz (API version for running the quiz)
def run_quiz(selected_questions, user_answers):
    score = 0
    wrong_answers = []
    
    for i, question in enumerate(selected_questions):
        correct_answer = question['answer'].strip().upper()
        user_answer = user_answers[i].strip().upper()
        
        if user_answer == correct_answer:
            score += 1
        else:
            wrong_answers.append({
                "question": question['question'],
                "correct_answer": correct_answer,
                "user_answer": user_answer
            }) 
    
    return score, wrong_answers

# Function for displaying results (API version for displaying results)
def display_results(score, total_questions, wrong_answers):
    incorrect_answer = total_questions - score
    percentage = (score / total_questions) * 100
    
    if percentage >= 80:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 40:
        grade = "C"
    else:
        grade = "F" 
        
    return {
        "total": total_questions,
        "correct": score,
        "incorrect": incorrect_answer,
        "percentage": round(percentage, 2),
        "grade": grade,
        "wrong_answers": wrong_answers
    }
    
# Function to save to the leaderboard (API version for saving to the leaderboard)
def save_to_leaderboard(name, score, total_questions):
    try:
        with open("leaderboard.txt", "a") as file:
            file.write(f"{name}: {score}/{total_questions}\n")
    except Exception as e:
        print("Error saving to leaderboard:", e)
        
