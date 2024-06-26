import os
import requests
from bs4 import BeautifulSoup
import pandas as pd

path_to_save = 'csv_files/links.csv'
website = 'https://safecomputing.umich.edu'
base_url = website
if website.endswith('/'):
    base_url = website[:-1]

scanned = []


def clean(a_eles):
    links = []
    skip_links = []
    for a in a_eles:
        link = a['href']
        if link.startswith('#') or link.startswith('mailto:') or link == '/':
            skip_links.append(link)
            continue

        if link.startswith('/'):
            link = '{}{}'.format(base_url, link)

        if link.startswith('http://') != True and link.startswith('https://') != True:
            link = '{}/{}'.format(base_url, link)

        if link.startswith(base_url) is False:
            continue

        if link not in links:
            links.append(link)

    return [links, skip_links]


def get_next_scan_urls(urls):
    links = []
    for u in urls:
        if u not in scanned:
            links.append(u)
    return links


def scan(url):
    if url not in scanned:
        print('Scan url: {}'.format(url))
        scanned.append(url)
        data = requests.get(url)
        soup = BeautifulSoup(data.text, 'html5lib')
        a_eles = soup.find_all('a', href=True)
        links, skip_links = clean(a_eles)

        next_scan_urls = get_next_scan_urls(links)
        print('Count next scan: {}'.format(len(next_scan_urls)))
        if len(next_scan_urls) != 0:
            for l in next_scan_urls:
                scan(l)
    return scanned


def main():
    if os.path.exists(path_to_save):
        print("links.csv already exists. Exiting the program.")
        return
    
    links = scan(website)

    df = pd.DataFrame({"links":links}) 
    df.to_csv(path_to_save)


if __name__ == '__main__':
    main()
