class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


new_question = Question("What is the capital of France?", "Paris")
print(f"Question: {new_question.text}")
print(f"Answer: {new_question.answer}")

