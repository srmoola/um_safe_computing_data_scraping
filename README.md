# UM Safe Computing Chatbot

- <a target = "_blank" href="https://umgpt.umich.edu/maizey/Information-Assurance-AI-Chat">Live ChatBot Link</a>
- <a target = "_blank" href="https://srmoola.github.io/um_safe_computing_data_scraping/">Embedded ChatBot UI Prototype</a>

## Description

This chatbot was made to help navigate and make finding information easier for this website: <a target = "_blank" href="https://safecomputing.umich.edu/">safecomputing.umich.edu</a>

### How it works

The 6 steps below can be run with a single shell script: <a target = "_blank" href="https://github.com/srmoola/um_safe_computing_data_scraping/blob/main/scrape.sh">Shell Script</a>

1. Generate sitemap for desired website, in our case: <a target = "_blank" href="https://safecomputing.umich.edu/">safecomputing.umich.edu</a>
2. Extract all links and store in csv file: <a target = "_blank" href="https://github.com/srmoola/um_safe_computing_data_scraping/blob/main/csv_files/links.csv">Links CSV File</a>
3. Scrape HTML content from all links with BeautifulSoup4
4. Parse through HTML and format it to make it easier for chatbot to understand, stored as PDFs
5. Upload all PDFs to Google Drive with script: <a target = "_blank" href="https://github.com/srmoola/um_safe_computing_data_scraping/blob/main/scripts/upload_to_google_drive.py">Script Link</a>
6. Follow Maizey documentation to connect Data Source: <a target = "_blank" href="https://its.umich.edu/computing/ai/maizey-in-depth">U-M ITS Documentation for Maizey</a>
