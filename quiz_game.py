from data import question_data

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

print(f"Total questions loaded: {len(question_bank)}")
score = 0
for i, q in enumerate(question_bank):
    user_answer = input(f"Q.{i+1}: {q.text}: ")
    if user_answer.lower() == q.answer.lower():
        score += 1
        print("Correct!")
    else:
        print(f"Wrong! The correct answer was: {q.answer}")
    
    print(f"Your current score is: {score}/{i+1}")
    print("\n")

print("You've completed the quiz!")
print(f"Your final score is: {score}/{len(question_bank)}")
