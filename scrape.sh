#!/bin/sh

DATA_FOLDER_PATH="site_data"
export PYTHONPATH=/Users/smoolaga/Desktop/safe_computing
source venv/bin/activate

pip install -r requirements.txt

echo "Getting Site Links"
python scripts/get_links.py

echo "Starting Scraping Process"
python scrapers/async_scrape.py

echo "Uploading to Google Drive"
python scripts/upload_to_google_drive.py $DATA_FOLDER_PATH

