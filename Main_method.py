from Personality_quiz import Questions
from Personality_quiz import Personality_quiz
if __name__=="__main__":
    q1=Questions("How do you describe your social personality?",["Introverted","Extroverted","Balanced"])
    q2=Questions("What is your preffd leisure activity?",["Reading a book","Attending parties","Outdoor sports"])
    q3=Questions("How do you handle stress?",["Meditating","Talking to friends","Exercising"])
    q4=Questions("Whats your ideal vacation destination?",["Relaxing on a beach","Exploring a blusting city","Adventure in nature"])
    q5=Questions("Whats your favourite type of cuisine?",["Italian","Mexican","Japanese"])
    quiz=Personality_quiz()
    quiz.take_question(q1)
    quiz.take_question(q2)
    quiz.take_question(q3)
    quiz.take_question(q4)
    quiz.take_question(q5)
    quiz.start_quiz()
    final_result=quiz.calculate_personality()
    print("based on your options we recommend that:",end="")
    if final_result<=4:
        print("Find friends and try to interact with others")
    elif final_result>4 and final_result<=8:
        print("try to spend some time with yourself")
    else:
        print("your life is awesome keep going on....")
