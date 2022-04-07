def wrap_tag(tag):
    return f"<{tag}>"


def trim_str(source_str, start, end_char):
    end = source_str.find(end_char, start, -1)
    return source_str[start:end]
