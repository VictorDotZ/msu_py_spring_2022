from utils import trim_str, wrap_tag


class HTMLParser:
    def __init__(self, open_tag_callback, data_callback, close_tag_callback):
        self.open_tag_callback = open_tag_callback
        self.data_callback = data_callback
        self.close_tag_callback = close_tag_callback

    @property
    def close_tag_callback(self):
        return self._close_tag_callback

    @close_tag_callback.setter
    def close_tag_callback(self, callback):
        self._close_tag_callback = callback

    @property
    def open_tag_callback(self):
        return self._open_tag_callback

    @open_tag_callback.setter
    def open_tag_callback(self, callback):
        self._open_tag_callback = callback

    @property
    def data_callback(self):
        return self._data_callback

    @data_callback.setter
    def data_callback(self, callback):
        self._data_callback = callback

    def parse_html(self, html_str: str):

        text_content = [""]
        for i in range(1, len(html_str)):
            if html_str[i - 1] == "<":
                if html_str[i].isalpha():
                    open_tag = wrap_tag(trim_str(html_str, i, ">"))
                    if open_tag and callable(self.open_tag_callback):
                        self.open_tag_callback(open_tag)
                    i += len(open_tag) - 1

                    content = trim_str(html_str, i, "<")
                    text_content.append(content)
                    i += len(content) - 1

                if html_str[i] == "/":
                    close_tag = wrap_tag(trim_str(html_str, i, ">"))
                    i += len(close_tag) - 1

                    content = text_content.pop()
                    if content and callable(self.data_callback):
                        self.data_callback(content)

                    content = trim_str(html_str, i, "<")
                    text_content[-1] += content
                    i += len(content) - 1

                    if close_tag and callable(self.close_tag_callback):
                        self.close_tag_callback(close_tag)
