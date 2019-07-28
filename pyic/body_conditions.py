class HasText:
    """
    Extractor that test if a string is in the reponse body
    """
    def __init__(self, text):
        self.text = text

    def __call__(self, response):
        return self.text in response.text


class Not:
    """
    Negate another extractor.

    example : Not(HasText('blah'))
    """
    def __init__(self, condition):
        self.condition = condition

    def __call__(self, body):
        return not self.condition(body)
