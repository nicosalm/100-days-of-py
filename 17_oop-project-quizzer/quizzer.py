import os

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
        
    def check(self, user_answer):
        return user_answer.lower() == self.answer.lower()
    
class Quiz:
    def __init__(self, questions: list):
        self.questions = questions
        self.score = 0
        
    def run(self):
        for question in self.questions:
            user_answer = input(question.prompt)
            Quiz.clear()
            if question.check(user_answer):
                self.score += 1
        print("You got " + str(self.score) + "/" + str(len(self.questions)) + " correct.")
        
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
        
questions = [
    Question("What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n", "a"),
    Question("What is the capital of Vietnam?\n(a) Hanoi\n(b) Ho Chi Minh City\n(c) Da Nang\n\n", "a"),
    Question("Who conquered the Inca Empire?\n(a) Francisco Pizarro\n(b) Hernan Cortes\n(c) Vasco Nunez de Balboa\n\n", "a"),
    Question("What is the largest country in the world?\n(a) Russia\n(b) Canada\n(c) China\n\n", "a"),
    Question("Where did Sir Francis Drake die?\n(a) Cartagena\n(b) Portobelo\n(c) Panama City\n\n", "a"),
    Question("What is the capital of the Philippines?\n(a) Manila\n(b) Cebu\n(c) Davao\n\n", "a"),
    Question("What is the longitute of the International Date Line?\n(a) 180 degrees\n(b) 0 degrees\n(c) 90 degrees\n\n", "a"),
    Question("What longitude is the capital of the United Kingdom?\n(a) 0 degrees\n(b) 180 degrees\n(c) 90 degrees\n\n", "a"),
    Question("What is the name of the First Emperor of Japan?\n(a) Jimmu\n(b) Hirohito\n(c) Akihito\n\n", "a"),
    Question("What did Sun Tzu write? (in English)\n(a) The Art of War\n(b) The Art of Peace\n(c) The Art of Love\n\n", "a"),
    ]

if __name__ == "__main__":
    quiz = Quiz(questions)
    quiz.run()