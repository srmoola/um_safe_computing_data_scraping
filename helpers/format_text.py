def format_text(tag):
    """
    Formats the text content based on the HTML tag type.

    Args:
    tag (bs4.element.Tag): A BeautifulSoup Tag object.

    Returns:
    str: Formatted text string.
    """
    tag_name = tag.name
    text = tag.get_text(strip=True)

    if tag_name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
        level = int(tag_name[1])
        return "\n\n" + '#' * level + ' ' + text
    elif tag_name == 'p':
        return text + '\n\n'
    elif tag_name == 'li':
        return '- ' + text + '\n'
    elif tag_name in ['div', 'span']:
        return text + '\n'
    elif tag_name == 'blockquote':
        return '> ' + text + '\n\n'
    else:
        return text + '\n'