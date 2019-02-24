import html2text


class TextExtract:

    def __call__(self, response):
        return html2text.html2text(response.text)

