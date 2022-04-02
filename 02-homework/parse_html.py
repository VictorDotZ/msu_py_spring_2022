from utils import find_all


def find_open_tag(html_str):
    return html_str.find("<"), html_str.find(">")


def get_open_tag(html_str):
    start, end = find_open_tag(html_str)

    return html_str[start : end + 1]  # noqa: E203 `>` belongs to tag


def get_element_name(open_tag):
    element_name = open_tag.split(" ")[0][1:]

    # space before element name is unacceptable, but not after
    return element_name[:-1] if element_name[-1] == ">" else element_name


def get_close_tag(open_tag):
    return f"</{get_element_name(open_tag)}>"


def get_tag_content(html_str, open_tag, close_tag):
    start = html_str.find(open_tag)
    end = html_str.find(close_tag)

    return html_str[start + len(open_tag) : end]  # noqa: E203


def find_data_inner_borders(
    close_angle_brackets, open_angle_brackets, close_tag_open_angle_brackets
):
    """Tag content may be mixed with nested tags and their content,
    needs to separate this content from content of nested tags.

    Args:
        close_angle_brackets (list): All indices of `>` in string
        open_angle_brackets (list): All indices of `<` in string
        close_tag_open_angle_brackets (list): All indices of `</` in string

    Returns:
        list: of inner borders. Between each pair indices contained tag content
    """
    pair_angle_brackets = zip(open_angle_brackets, close_angle_brackets)
    borders = []

    counter = 0  # keeps track of inheritance depth
    for pair in pair_angle_brackets:
        if counter == 0:
            borders.append(pair[0])
            counter += 1
            continue

        if pair[0] in close_tag_open_angle_brackets:
            counter -= 1
            borders.append(pair[1])
        else:
            counter += 1

    return borders


def get_text_between_tags(tag_content):
    close_angle_brackets = find_all(tag_content, ">")
    open_angle_brackets = find_all(tag_content, "<")
    close_tag_open_angle_brackets = find_all(tag_content, "</")

    borders = (
        [-1]
        + find_data_inner_borders(
            close_angle_brackets,
            open_angle_brackets,
            close_tag_open_angle_brackets,
        )
        + [len(tag_content)]
    )

    data = []

    for start, end in zip(borders[::2], borders[1::2]):
        data.append(tag_content[start + 1 : end])  # noqa: E203

    return "".join(data)


def parse_html(
    html_str: str, open_tag_callback, data_callback, close_tag_callback
):
    open_tag = get_open_tag(html_str)

    if not open_tag:
        return

    open_tag_callback(open_tag)

    close_tag = get_close_tag(open_tag)

    close_tag_callback(close_tag)

    tag_content = get_tag_content(html_str, open_tag, close_tag)

    data_callback(get_text_between_tags(tag_content))

    parse_html(
        html_str[
            find_open_tag(html_str)[1]
            + 1 : html_str.find(close_tag)  # noqa: E203
        ],
        open_tag_callback,
        data_callback,
        close_tag_callback,
    )

    parse_html(
        html_str[html_str.find(close_tag) + len(close_tag) :],  # noqa: E203
        open_tag_callback,
        data_callback,
        close_tag_callback,
    )


def print_args(html_str):
    print(html_str)


HTML = (
    '<nav><ul><li><a href="#">Home</a></li><li><a'
    ' href="#">About</a></li><li><a href="#">Clients</a></li><li><a'
    ' href="#">Contact Us</a></li></ul></nav>'
)

HTML = (
    '<p>My <span style="color:blue">blue</span> mother has <span'
    ' style="color:blue">blue</span> eyes.</p>'
)

# print(HTML)

parse_html(HTML, print_args, print_args, print_args)
