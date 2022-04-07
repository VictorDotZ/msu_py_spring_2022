from unittest.mock import patch
from unittest.mock import call
import unittest

from itertools import chain

# from ast import literal_eval

from faker import Faker


from html_parser import HTMLParser


class TestHTMLParser(unittest.TestCase):
    def setUp(self) -> None:
        self.parser = HTMLParser(None, None, None)
        self.fake = Faker()

        Faker.seed(123)
        self.uri_pages = [self.fake.uri_page() for _ in range(4)]
        self.sentences = [self.fake.sentence(nb_words=i) for i in range(1, 6)]
        self.first_names = [self.fake.first_name() for _ in range(3)]
        self.last_names = [self.fake.last_name() for _ in range(3)]
        self.random_ints = [
            str(self.fake.random_int(20, 80)) for _ in range(3)
        ]

        self.html = [
            {
                "html_str": "",
                "open_tags_count": 0,
                "close_tags_count": 0,
                "data": [],
            },
            {
                "html_str": " Hello World ",
                "open_tags_count": 0,
                "close_tags_count": 0,
                "data": [],
            },
            {
                "html_str": (
                    "<nav><ul>"
                    f'<li><a href="#">{self.uri_pages[0]}</a></li>'
                    f'<li><a href="#">{self.uri_pages[1]}</a></li>'
                    f'<li><a href="#">{self.uri_pages[2]}</a></li>'
                    f'<li><a href="#">{self.uri_pages[3]}</a></li>'
                    "</ul></nav>"
                ),
                "open_tags_count": 10,
                "close_tags_count": 10,
                "data": self.uri_pages,
            },
            {
                "html_str": (
                    f"<p>{self.sentences[0]}"
                    f"<span>{self.sentences[1]}</span>"
                    f"{self.sentences[2]}"
                    f"<span>{self.sentences[3]}</span>"
                    f"{self.sentences[4]}</p>"
                ),
                "open_tags_count": 3,
                "close_tags_count": 3,
                "data": [
                    self.sentences[1],
                    self.sentences[3],
                    self.sentences[0] + self.sentences[2] + self.sentences[4],
                ],
            },
            {
                "html_str": (
                    "<table>"
                    "<tr>"
                    "<th>Firstname</th>"
                    "<th>Lastname</th>"
                    "<th>Age</th>"
                    "</tr>"
                    "<tr>"
                    f"<td>{self.first_names[0]}</td>"
                    f"<td>{self.last_names[0]}</td>"
                    f"<td>{self.random_ints[0]}</td>"
                    "</tr>"
                    "<tr>"
                    f"<td>{self.first_names[1]}</td>"
                    f"<td>{self.last_names[1]}</td>"
                    f"<td>{self.random_ints[1]}</td>"
                    "</tr>"
                    "<tr>"
                    f"<td>{self.first_names[2]}</td>"
                    f"<td>{self.last_names[2]}</td>"
                    f"<td>{self.random_ints[2]}</td>"
                    "</tr>"
                    "</table>"
                ),
                "open_tags_count": 17,
                "close_tags_count": 17,
                "data": ["Firstname", "Lastname", "Age"]
                + list(
                    chain.from_iterable(
                        zip(
                            self.first_names, self.last_names, self.random_ints
                        )
                    ),
                ),
            },
        ]

    @patch("html_parser.HTMLParser.close_tag_callback")
    def test_close_callback_calls_count(self, mock_close_tag_callback):
        self.parser.close_tag_callback = mock_close_tag_callback
        for html in self.html:
            html_str = html["html_str"]

            self.parser.parse_html(html_str)

            self.assertEqual(
                mock_close_tag_callback.call_count,
                html["close_tags_count"],
            )

            mock_close_tag_callback.call_count = 0

    @patch("html_parser.HTMLParser.open_tag_callback")
    def test_open_callback_calls_count(self, mock_open_tag_callback):
        self.parser.open_tag_callback = mock_open_tag_callback

        for html in self.html:
            html_str = html["html_str"]

            self.parser.parse_html(html_str)

            self.assertEqual(
                mock_open_tag_callback.call_count,
                html["open_tags_count"],
            )

            mock_open_tag_callback.call_count = 0

    @patch("html_parser.HTMLParser.data_callback")
    def test_data_callback_content(self, mock_data_callback):
        self.parser.data_callback = mock_data_callback

        for html in self.html:
            html_str = html["html_str"]

            self.parser.parse_html(html_str)

            expected = [call(x) for x in html["data"]]

            self.assertTrue(mock_data_callback.call_args_list == expected)

            mock_data_callback.call_args_list = []


if __name__ == "__main__":
    unittest.main()
