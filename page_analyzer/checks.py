from bs4 import BeautifulSoup


def truncate_with_ellipsis(text, max_len=200):
    if text is None:
        return ''
    if len(text) >= max_len:
        return text[:max_len - 3] + '...'
    return text


def get_check(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')
    h1 = soup.h1.string if soup.h1 else ''
    if h1 is None:
        h1 = ''
    title = soup.title.string if soup.title else ''
    if title is None:
        title = ''
    if soup.find('meta', {'name': 'description'}):
        description = soup.find('meta', {'name': 'description'})['content']
        if description is None:
            description = ''
    else:
        description = ''
    h1 = truncate_with_ellipsis(h1)
    title = truncate_with_ellipsis(title)
    description = truncate_with_ellipsis(description)
    return h1, title, description
