from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import os
import sys

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

# takes folder path as argument (python upload_to_google_drive.py FOLDER_PATH_HERE)
local_folder = sys.argv[1]
folder_name = os.path.basename(local_folder)

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
