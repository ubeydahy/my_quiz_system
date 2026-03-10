# Question Bank

questions = [
    {
        "id": 1,
        "question": "Which Linux command is used to change the current directory?",
        "options": ["A. pwd", "B. cd ", "C. ls", "D. mv"],
        "answer": "B",
        "difficulty": "Easy"
    },

    {
        "id": 2,
        "question": " Which command displays the current working directory in Linux?",
        "options": ["A. pwd", "B. whoami", "C. dir", "D. where"],
        "answer": "A",
        "difficulty": "Easy"
    },

    {
        "id": 3,
        "question": "What does the /etc/passwd file store in Linux?",
        "options": ["A. System passwords", "B. User account information", "C. Installed packages", "D. Kernel logs"],
        "answer": "B",
        "difficulty": "Medium"
    },

    {
        "id": 4,
        "question": "Which command shows the path of a command executable in Linux?",
        "options": ["A. whereis", "B. locate", "C. which", "D. find"],
        "answer": "C",
        "difficulty": "Hard"
    },

    {
        "id": 5,
        "question": " Which command lists files and directories in Linux?",
        "options": ["A. show", "B. list", "C. ls", "D. dir"],
        "answer": "C",
        "difficulty": "Easy"
    },

    {
        "id": 6,
        "question": "Which command is used to create a new directory in Linux?",
        "options": ["A. newdir", "B. createdir", "C. mkdir", "D. makedir"],
        "answer": "C",
        "difficulty": "Easy"
    },

    {
        "id": 7,
        "question": "What does the sudo command do in Linux?",
        "options": ["A. Switch user directory", "B. Run commands with superuser priviliges", "C. Shut down the system", "D. Show disk usage"],
        "answer": "B",
        "difficulty": "Medium"
    },

    {
        "id": 8,
        "question": "What Git command is used to download changes from a remote repository and merge them into the current branch?",
        "options": ["A. git fetch", "B. git pull", "C. git merge", "D. git clone"],
        "answer": "B",
        "difficulty": "Hard"
    },

    {
        "id": 9,
        "question": "Which Linux command removes a file?",
        "options": ["A. delete", "B. rm", "C. erase", "D. removefile"],
        "answer": "B",
        "difficulty": "Easy"
    },

    {
        "id": 10,
        "question": "Which Git command initializes a new repository?",
        "options": ["A. git create", "B. git init", "C. git start", "D. git new"],
        "answer": "B",
        "difficulty": "Easy"
    },

    {
        "id": 11,
        "question": "Which command installs packages on Ubuntu or Debian systems?",
        "options": ["A. yum install", "B. rpm install", "C. pacman install", "D. apt install"],
        "answer": "D",
        "difficulty": "Medium"
    },

    {
        "id": 12,
        "question": "Which command is used to change file permissions in Linux?",
        "options": ["A. chmod", "B. chown", "C. perm", "D. access"],
        "answer": "A",
        "difficulty": "Hard"
    },

    {
        "id": 13,
        "question": "Which Git command checks the status of files in a repository?",
        "options": ["A. git check", "B. git status", "C. git info", "D. git state"],
        "answer": "B",
        "difficulty": "Easy"
    },

    {
        "id": 14,
        "question": "What is the default branch name in a new Git repository?",
        "options": ["A. main", "B. master", "C. default", "D. origin"],
        "answer": "A",
        "difficulty": "Easy"
    },

    {
        "id": 15,
        "question": " Which Python function prints output to the screen?",
        "options": ["A. show()", "B. display()", "C. print", "D. echo()"],
        "answer": "C",
        "difficulty": "Easy"
    },

    {
        "id": 16,
        "question": "What is a Git merge conflict?",
        "options": ["A. When Git deletes files automatically", "B. When two branches modify the same part of a file", "C. When GitHub server is down", "D. When Git cannot find a repository"],
        "answer": "B",
        "difficulty": "Medium"
    },

    {
        "id": 17,
        "question": "Which Python data structure stores key-value pairs?",
        "options": ["A. List", "B. Tuple", "C. Dictionary", "D. Set"],
        "answer": "C",
        "difficulty": "Hard"
    },

    {
        "id": 18,
        "question": "Which Python keyword is used to define a function?",
        "options": ["A. define", "B. function", "C. def", "D. func"],
        "answer": "C",
        "difficulty": "Easy"
    },

    {
        "id": 19,
        "question": "Which Python function returns the number of items in a list?",
        "options": ["A. size()", "B. length()", "C. count()", "D. len()"],
        "answer": "D",
        "difficulty": "Medium"
    },

    {
        "id": 20,
        "question": "What command clones a GitHub repository to your local machine?",
        "options": ["A. git download", "B. git copy", "C. git fork", "D. git clone"],
        "answer": "D",
        "difficulty": "Hard"
    }
]

#Function for Saving Questions to questions.txt file

def save_questions(questions):
    with open ("question.txt", "w") as file:
        for question in questions:
            file.write(f"ID: {question['id']} \n")
            file.write(f"Question: {question['question']} \n")
            file.write(f"Options: \n")
            for option in question['options']:
                file.write(f"{option} \n")
            file.write(f"Answer: {question['answer']} \n")
            file.write(f"Difficulty: {question['difficulty']} \n")
            file.write("\n")

#Function for loading questions from questions.txt file

def load_questions():
    questions = []
    with open("question.txt", "r") as file:
        lines = file.readlines()
        # print(lines)
        for i in range(0, len(lines), 10):
            question = {
                "id": int(lines[i].split(": ")[1].strip()),
                "question": lines[i + 1].split(": ")[1].strip(),
                "options": [lines[i + 3].strip(), lines[i + 4].strip(), lines[i + 5].strip(), lines[i + 6].strip()],
                "answer": lines[i + 7].split(": ")[1].strip(),
                "difficulty": lines[i + 8].split(": ")[1].strip()
            }
            questions.append(question)
    
    return questions

save_questions(questions)
loaded_questions = load_questions()
print(loaded_questions)