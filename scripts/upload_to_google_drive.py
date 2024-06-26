from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import os
import sys

# takes folder path as argument (python upload_to_google_drive.py FOLDER_PATH_HERE)
if len(sys.argv) < 2:
  raise Exception("Please provide a valid folder path as an argument.")

local_folder = sys.argv[1]

if not os.path.isdir(local_folder):
  raise Exception(f"The provided path '{local_folder}' is not a valid directory.")

folder_name = os.path.basename(local_folder)

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

file_list = drive.ListFile({'q': "title = '{}' and mimeType = 'application/vnd.google-apps.folder' and trashed=false".format(folder_name)}).GetList()
if file_list:
  for file in file_list:
    file.Delete()

folder_metadata = {'title': folder_name, 'mimeType': 'application/vnd.google-apps.folder'}
folder = drive.CreateFile(folder_metadata)
folder.Upload()
folder_id = folder['id']

for filename in os.listdir(local_folder):
  file_path = os.path.join(local_folder, filename)
  
  with open(file_path, 'r') as file:
    file_content = file.read()
  
  gfile = drive.CreateFile({'title': filename, 'parents': [{'id': folder_id}]})
  gfile.SetContentString(file_content)
  gfile.Upload()
  
  print(f'Uploaded content of: {filename}')
