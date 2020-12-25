from question_model import Question
from data import question_data
from quiz_brain import QuestionBrain

question_bank = []
question_data = question_data['results']

for question in question_data:
    # print(x)    # prints {'text': "A slug's blood is green.", 'answer': 'True'}
    # print(x['text'])    # prints A slug's blood is green.
    question_bank.append(Question(question['question'], question['correct_answer']))

qb = QuestionBrain(question_bank)

while qb.still_has_questions():
    qb.next_question()

qb.quiz_completed()
