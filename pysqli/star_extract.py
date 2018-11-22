
class StarExtract:
    def __init__(self, pattern, shift=0):
        self.pattern = pattern.split('*')
        self.shift = shift
        if len(self.pattern) != 2:
            raise Exception('pattern of StarExtract must contain only one star (*)')

    def __call__(self, response):
        text = response.text[self.shift:]
        print('-' * 45)
        print(text)
        begin = text.find(self.pattern[0]) + len(self.pattern[0])
        end = text[begin:].find(self.pattern[1]) + begin
        return text[begin:end]
