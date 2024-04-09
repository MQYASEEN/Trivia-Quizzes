class Question_List:
    def __init__(self,q_list):
        self.question_number=0
        self.score=0
        self.question_list=q_list
    
    def should_ask_again(self):
        return len(self.question_list)>self.question_number


    def ask_question(self):
        current_question=self.question_list[self.question_number]
        self.question_number+=1
        answer=input(f"Q.{self.question_number}:{current_question.question} (True/False):")
        self.check_answer(answer,current_question.answer)

    def check_answer(self,answer,correct_answer):
        if answer.lower()==correct_answer.lower():
            print("You got it Right")
            self.score+=1
        else:
            print("You are Wrong That's not correct answer!")
        print(f"Correct Answer is {correct_answer}")
        print(f"Your Score :{self.score}/{self.question_number}")
        print("\n")