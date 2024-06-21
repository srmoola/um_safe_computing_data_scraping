import aiohttp
import asyncio
from bs4 import BeautifulSoup
import aiofiles
from failed_links import write_to_failed_links_csv
from format_text import format_text
from read_all_links import read_all_links_from_csv

all_links = read_all_links_from_csv()
failed_links = []
request_error_links = []
body_type_none_links = []

text_tags = ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'div', 'span', 'li', 'blockquote']

async def fetch(session, url):
    try:
        async with session.get(url) as response:
            if response.status != 200:
                request_error_links.append(url)
                print(f"{url} FAILED with status {response.status}")
                return None
            return await response.text()
    except Exception as e:
        request_error_links.append(url)
        print(f"{url} FAILED with exception {e}")
        return None

async def scrape_and_save(session, url):
    html_content = await fetch(session, url)
    if html_content is None:
        return

    soup = BeautifulSoup(html_content, 'html.parser')
    body_content = soup.find('section', {'role': 'main', 'aria-label': 'Page Content'})

    if body_content is None:
        body_type_none_links.append(url)
        print(f"{url} FAILED to find main content")
        return

    content_tags = body_content.find_all(text_tags)
    file_name = url.replace("https://", "").replace("/", "_")
    async with aiofiles.open(f"site_data/{file_name}.txt", 'w', encoding='utf-8') as file:
        for tag in content_tags:
            formatted_text = format_text(tag)
            await file.write(formatted_text + '\n')

    print(f"Successfully written to {url}.txt")

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [scrape_and_save(session, url) for url in all_links]
        await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())
    write_to_failed_links_csv(request_error_links, "request_error")
    write_to_failed_links_csv(body_type_none_links, "body_type_none")
