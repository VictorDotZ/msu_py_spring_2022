def parse_html(
    html_str: str, open_tag_callback, data_callback, close_tag_callback
):

    text_content = [""]
    for i in range(1, len(html_str)):
        if html_str[i - 1] == "<" and html_str[i].isalpha():
            open_tag = (
                f"<{html_str[i : html_str.find('>', i, -1)]}>"  # noqa: E203
            )
            open_tag_callback(open_tag)
            i += len(open_tag) - 1

            content = html_str[i : html_str.find("<", i, -1)]  # noqa: E203
            text_content.append(content)

            i += len(content) - 1

        if html_str[i - 1] == "<" and html_str[i] == "/":
            close_tag = (
                f"<{html_str[i : html_str.find('>', i, -1)]}>"  # noqa: E203
            )

            i += len(close_tag) - 1

            data_callback(text_content.pop())

            content = html_str[i : html_str.find("<", i, -1)]  # noqa: E203
            text_content[-1] += content

            i += len(content) - 1

            close_tag_callback(close_tag)


def print_args(html_str):
    print(html_str)


HTML = (
    '<nav><ul><li><a href="#">Home</a></li><li><a'
    ' href="#">About</a></li><li><a href="#">Clients</a></li><li><a'
    ' href="#">Contact Us</a></li></ul></nav>'
)

HTML = (
    '<p>My <span style="color:red">blue</span> mother has <span'
    ' style="color:red">blue</span> eyes.</p>'
)

# print(HTML)

parse_html(HTML, print_args, print_args, print_args)
