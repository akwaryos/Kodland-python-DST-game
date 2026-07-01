class Score:
    def __init__(self):
        self.score = 0

    def increment(self):
        self.score += 1

    def decrement(self):
        if self.score != 0:
            self.score -= 1

    def get_score(self):
        return self.score
