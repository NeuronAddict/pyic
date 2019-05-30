import html2text


class Html2TextFilter:

    def __call__(self, response):
        return html2text.html2text(response.text)

