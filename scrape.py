from bs4 import BeautifulSoup
import requests

from failed_links import write_to_failed_links_csv
from format_text import format_text
from read_all_links import read_all_links_from_csv

all_links = read_all_links_from_csv()
failed_links = []
request_error_links = []
body_type_none_links = []

text_tags = ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'div', 'span', 'li', 'blockquote']

for link in all_links:
    url = link

    file_name = url.replace("https://", "").replace("/", "_")

    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    if r.status_code != 200:
        request_error_links.append(url)
        print(f"{url}.txt FAILED")
        continue

    body_content = soup.find('section', {'role': 'main', 'aria-label': 'Page Content'})

    if body_content is None:
        body_type_none_links.append(url)
        print(f"{url}.txt FAILED")
        continue

    content_tags = body_content.find_all(text_tags)

    with open(f"site_data/{file_name}", 'w', encoding='utf-8') as file:
        for tag in content_tags:
            formatted_text = format_text(tag)
            file.write(formatted_text)

    print(f"Successfully write to {url}.txt")

write_to_failed_links_csv(request_error_links, "request_error")
write_to_failed_links_csv(body_type_none_links, "body_type_none")

    
