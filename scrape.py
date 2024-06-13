from bs4 import BeautifulSoup
import requests

from format_text import format_text

url = "https://safecomputing.umich.edu/protect-yourself/be-safe-online/practice-online-hygiene"
file_name = url.replace("https://", "").replace("/", "_")
text_tags = ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'div', 'span', 'li', 'blockquote']

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

if r.status_code != 200:
    print(f"Failed to retrieve content. Status code: {r.status_code}")
    exit()

body_content = soup.find('section', {'class': 'col-sm-6', 'role': 'main', 'aria-label': 'Page Content'})

content_tags = body_content.find_all(text_tags)

with open(f"site_data/{file_name}", 'w', encoding='utf-8') as file:
    for tag in content_tags:
        formatted_text = format_text(tag)
        file.write(formatted_text)

print(f"Formatted text content has been written to {url}.txt")
    
