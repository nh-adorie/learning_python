from data import open_api
from quiz import Quiz
from game import Game

# Lấy dữ liệu câu đố từ data
question_bank = []
question_list = open_api["results"]
for ques_dict in question_list:
    new_quiz = Quiz(ques_dict["question"],ques_dict["correct_answer"])
    question_bank.append(new_quiz)

game = Game(question_bank)
while game.still_has_quiz():
    game.show_quiz()

print("You've completed the quiz")
print(f"Your final score: {game.score}/{game.quiz_number}")