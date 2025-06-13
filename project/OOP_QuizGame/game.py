class Game:
    def __init__(self, quiz_list):
        self.quiz_number = 0
        self.quiz_list = quiz_list # list gồm nhiều obj Quiz
        self.score = 0

    def still_has_quiz(self):
        return self.quiz_number < len(self.quiz_list)

    def show_quiz(self):
        current_quiz = self.quiz_list[self.quiz_number] # current_quiz là 1 obj Quiz
        print(f"\nQ{self.quiz_number+1}: {current_quiz.question} ")
        while True:
            user_ans = input("True/False? ")
            if user_ans.lower() in ["true","false"]:
                break
            else:
                print("\nPlease input valid value ")
        self.quiz_number += 1
        self.check_answer(user_ans,current_quiz.answer)
    
    def check_answer(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            self.score += 1
            print(f"You got it right!\nYour score: {self.score}/{self.quiz_number} ")    
        else:
            print(f"That's wrong\nYour score: {self.score}/{self.quiz_number} ")