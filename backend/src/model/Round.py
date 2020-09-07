


class Round:
    def __init__(self, question, point=5):
        self.question = question
        self.point = point

    def resolve(self, answer):
        return self.question.options[answer].valuate()
