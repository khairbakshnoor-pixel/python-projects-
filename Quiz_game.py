import random
game =int(input("enter 1 to start the quiz "))
score=0
if game ==1:
    for i in range (1,4):
        questions = {
            "question1": {
                "question": "what is the capital of france",
                "options": ['paris', 'london', 'rome'],
                "answer": "paris"
            },
            "question2": {
                "question": "what is the capital of enland",
                "options": ['paris', 'london', 'rome'],
                "answer": "london"
            },
            "question3": {
                "question": "what is the capital of ban",
                "options": ['paris', 'dhaka', 'rome'],
                "answer": "dhaka"
            },
            "question4": {
                "question": "what is the capital of india",
                "options": ['paris', 'dehli', 'rome'],
                "answer": "dehli"
            },
            "question5": {
                "question": "what is the capital of pak",
                "options": ['lahore', 'london', 'rome'],
                "answer": "lahore"
            }
        }
        
        # Pick a random question
        key = random.choice(list(questions.keys()))
        q_data = questions[key]

        print(q_data["question"])
        print("Options:", q_data["options"])

        #
        user_answer = input("Enter the answer: ").strip().lower()

        # Check the answer
        
        if user_answer == q_data["answer"].lower():
            print("Correct!")
            score=score+10
            score=score
        else:
            print("Wrong! The correct answer is'" ,q_data['answer'])
    print("your sore is ",score)

else:
    print("invalid option ")