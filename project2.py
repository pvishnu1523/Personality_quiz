Questions=[ "1. How would you describe your social personality?\n1. Introverted\n2. Extroverted\n3. Balanced\n",
    "2. What's your preferred leisure activity?\n1. Reading a book\n2. Attending parties\n3. Outdoor sports\n",
    "3. How do you handle stress?\n1. Meditating\n2. Talking to friends\n3. Exercising\n",
    "4. What's your ideal vacation destination?\n1. Relaxing on a beach\n2. Exploring a bustling city\n3. Adventure in nature\n",
    "5. What's your favorite type of cuisine?\n1. Italian\n2. Mexican\n3. Japanese\n"]
user_answers={
    "social_personality":"",
    "leisure_activity":"",
    "stress_handling":"",
    "vacation_destination":"",
    "favourite_cuisine":""
    }
def calculate_personality(answers):
    score=0
    score+=int(answers["social_personality"])
    score+=int(answers["leisure_activity"])
    score+=int(answers["stress_handling"])
    score+=int(answers["vacation_destination"])
    score+=int(answers["favourite_cuisine"])
    temp=" "
    if score<=4:
        temp="Find friends and try to interact with others"
    elif score>4 and score<=8:
        temp="try to spend some time with yourself"
    else:
        temp="your life is awesome keep going on...."
    return temp    
def start_quiz():
    print("welcome to the program")
    for i,question in enumerate(Questions):
        answer=input(question)
        while answer not in["1","2","3"]:
            print("please select select a valid option(1,2,0r 3).")
            answer=input(question)
        choice=["social_personality","leisure_activity","stress_handling","vacation_destination","favourite_cuisine"][i]
        user_answers[choice]=answer
    personality_type=calculate_personality(user_answers)
    print(f"\n based on the options you choose we recommend:{personality_type}")
if __name__=="__main__":
    start_quiz()
            
    
