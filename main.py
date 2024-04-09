from question_data import questions
from question_modal import Question
from quiz_modal import Question_List
question_bank=[]
for question in questions:
    q_list=question['text']
    a_list=question['answer']
    question_bank.append(Question(q_list,a_list))

quiz=Question_List(question_bank)
while quiz.should_ask_again():
    quiz.ask_question()
print("Your Quiz is Over")
print(f'Your Final Score is {quiz.score}/{quiz.question_number}')