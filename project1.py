class Questions:
    def __init__(self,Question,options):
        self.Question=Question
        self.options=options
class Personality_quiz:
    def __init__(self):
        self.questions=[]
        self.user_answers=[]
    def take_question(self,your_question):
        self.questions.append(your_question)
    def start_quiz(self):
        print("Welcome to the quiz")
        for i,question in enumerate(self.questions):
            print(f"\nQuestion {i+1}: {question.Question}")
            for k,option in enumerate(question.options):
                print(f"{k+1}. {option}")
            user_input=int(input("your choice: "))
            self.user_answers.append(user_input - 1)
    def calculate_personality(self):
        score=sum(self.user_answers)
        return score
        
