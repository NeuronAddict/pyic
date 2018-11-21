
class StarExtract:
    def __init__(self, pattern):
        self.pattern = pattern.split('*')
        if len(self.pattern) != 2:
            raise Exception('pattern of StarExtract must contain only one star (*)')

    def __call__(self, response):
        begin = response.text.find(self.pattern[0]) + len(self.pattern[0])
        end = response.text[begin:].find(self.pattern[1]) + begin
        return response.text[begin:end]
