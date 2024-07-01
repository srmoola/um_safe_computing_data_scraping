import os
import random
import shutil

# Path to the source folder
source_folder = '/Users/smoolaga/Desktop/safe_computing/site_data'

# Path to the destination folder
destination_folder = '/Users/smoolaga/Desktop/safe_computing/training_data'

# delete the destination folder if it exists
if os.path.exists(destination_folder):
  shutil.rmtree(destination_folder)

# Create the destination folder
os.makedirs(destination_folder)

# Get a list of all files in the source folder
files = os.listdir(source_folder)

# Shuffle the list of files
random.shuffle(files)

# Select the first 50 files
selected_files = files[:50]

# Copy the selected files to the destination folder
for file in selected_files:
  source_path = os.path.join(source_folder, file)
  destination_path = os.path.join(destination_folder, file)
  shutil.copy(source_path, destination_path)
