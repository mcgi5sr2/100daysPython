# # creating classes
# class User:
#     def __init__(self, user_id, username):
#         # initialise attributes
#         print("new user being created...")
#         self.id = user_id
#         self.username = username
#         # names of attributes do not need to be the same in the constructor, but normally are
#         self.followers = 0
#         # above we have set a default value so we don't have to pass it in unless it changes
#         self.following = 0
#
#     def add_follower(self):
#         self.followers += 1
#
#     def follow(self, user):
#         user.followers += 1
#         self.following = + 1
#
#
# # user_1 = User()
# # user_1.id = "001"
# # user_1.username = "angela"
# # print(user_1.username)
# #
# # user_2 = User()
# # user_2.id = "002"
# # this next part is wrong as I have used name not username
# # user_2.name = "jack"
# # print(user_2.name)
#
# user_1 = User("001", "Angela")
# user_2 = User("002", "Jack")
# user_3 = User("003", "Raynor")
# print(user_3.username)
#
# user_1.follow(user_2)


# Quiz Game True/False
from daysPy017question_model import Question
from daysPy017data import question_data
from daysPy017quiz_brain import QuizBrain

question_bank = []

for index, item in enumerate(question_data):
    new_question = Question(question_data[index]["question"],question_data[index]["correct_answer"])
    question_bank.append(new_question)

# for question in question_data:
#     new_question = Question(question["question"], question["correct_answer"])
#     question_bank.append(new_question)

print(question_bank[0].text,question_bank[0].answer)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"You're final score was {quiz.score}/{quiz.question_number}")