
class StarExtract:
    """
    Extractor that use a simple syntax with a start.

    For example, to extract the first <h2> content, use StarExtract("<h2></h2>").

    Be careful, the first match is returned.
    If you want read the body to the nth char, use shift
    """

    def __init__(self, pattern, shift=0):
        """
        Create a new Extractor with the start technique.
        For example, to extract the first <h2> content, use StarExtract("<h2></h2>").

        Be careful, the first match is returned.
        If you want read the body to the nth char, use shift
        :param pattern: pattern to extract, the star represent the string part that will be return.
        :param shift: if set, the body will be read only after this index.
        """
        self.pattern = pattern.split('*')
        self.shift = shift
        if len(self.pattern) != 2:
            raise Exception('pattern of StarExtract must contain only one star (*)')

    def __call__(self, response):
        text = response.text[self.shift:]
        begin = text.find(self.pattern[0]) + len(self.pattern[0])
        end = text[begin:].find(self.pattern[1]) + begin
        return text[begin:end]
