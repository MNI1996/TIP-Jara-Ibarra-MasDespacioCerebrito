class Round:
    def __init__(self, question):
        self.question = question

    def resolve(self, answer):
        return self.question.options[answer].valuate()
