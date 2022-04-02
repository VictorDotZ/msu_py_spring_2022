def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1:
            return
        yield start
        start += len(sub)


def find_data_inner_borders(
    close_angle_brackets, open_angle_brackets, close_tag_open_angle_brackets
):
    pair_angle_brackets = zip(open_angle_brackets, close_angle_brackets)
    borders = []
    counter = 0
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


def parse_html(
    html_str: str, open_tag_callback, data_callback, close_tag_callback
):

    first_open_angle_bracket = html_str.find(
        "<",
    )
    first_close_angle_bracket = html_str.find(
        ">",
    )

    open_tag = html_str[
        first_open_angle_bracket : 1 + first_close_angle_bracket  # noqa: E203
    ]

    open_tag_callback(open_tag)

    element_name = open_tag.split(" ")[0][1:]

    if element_name[-1] == ">":
        element_name = element_name[:-1]

    close_tag = f"</{element_name}>"

    close_tag_open_angle_bracket = html_str.find(
        close_tag, first_close_angle_bracket
    )

    close_tag_callback(close_tag)

    tag_content = html_str[
        first_close_angle_bracket
        + 1 : close_tag_open_angle_bracket  # noqa: E203
    ]

    close_angle_brackets = find_all(
        tag_content,
        ">",
    )
    open_angle_brackets = find_all(
        tag_content,
        "<",
    )
    close_tag_open_angle_brackets = find_all(
        tag_content,
        "</",
    )
    borders = (
        [-1]
        + find_data_inner_borders(
            close_angle_brackets,
            open_angle_brackets,
            close_tag_open_angle_brackets,
        )
        + [-1]
    )

    data = []

    for start, end in zip(borders[::2], borders[1::2]):
        data.append(tag_content[start + 1 : end])  # noqa: E203

    data_callback(data)


def print_args(html_str):
    print(html_str)


HTML = (
    '<nav><ul><li><a href="#">Home</a></li><li><a'
    ' href="#">About</a></li><li><a href="#">Clients</a></li><li><a'
    ' href="#">Contact Us</a></li></ul></nav>'
)

# HTML = (
#     '<p>My <span style="color:blue">blue</span> mother has <span'
#     ' style="color:blue">blue</span> eyes.</p>'
# )

print(HTML)

parse_html(HTML, print_args, print_args, print_args)
