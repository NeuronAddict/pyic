class HasText:
    def __init__(self, text):
        self.text = text

    def __call__(self, body):
        return self.text in body


class Not:
    def __init__(self, condition):
        self.condition = condition

    def __call__(self, body):
        return not self.condition(body)
