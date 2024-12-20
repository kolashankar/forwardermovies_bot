import random

class QuizManager:
    def __init__(self):
        self.quizzes = {}

    def create_quiz(self, quiz_id, questions):
        self.quizzes[quiz_id] = {
            'questions': questions,
            'current_question': 0,
            'score': 0
        }

    def get_next_question(self, quiz_id):
        quiz = self.quizzes.get(quiz_id)
        if quiz and quiz['current_question'] < len(quiz['questions']):
            question = quiz['questions'][quiz['current_question']]
            quiz['current_question'] += 1
            return question
        return None

    def answer_question(self, quiz_id, answer):
        quiz = self.quizzes.get(quiz_id)
        if quiz and quiz['current_question'] > 0:
            correct_answer = quiz['questions'][quiz['current_question'] - 1]['correct_answer']
            if answer.lower() == correct_answer.lower():
                quiz['score'] += 1
                return True
        return False

    def get_quiz_result(self, quiz_id):
        quiz = self.quizzes.get(quiz_id)
        if quiz:
            return {
                'total_questions': len(quiz['questions']),
                'correct_answers': quiz['score'],
                'score_percentage': (quiz['score'] / len(quiz['questions'])) * 100
            }
        return None

    def delete_quiz(self, quiz_id):
        if quiz_id in self.quizzes:
            del self.quizzes[quiz_id]
            return True
        return False

