import mimetypes
from googleapiclient.http import MediaFileUpload
from Google import Create_Service
import os

CLIENT_SECRET_FILE = 'credentials.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive'] 

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

centro_id = '1-QGG3XbZ5LqugUspYgqBEdNX05lASfgA'
sul_id = '14to8vGq742fuge1J1c5HAsqcVcnN9QT9'
serra_id = '1R76bjpF67zBDImVGubt8gqlVdcg6nTNN'

path = os.path.dirname(os.path.realpath(__file__))

centro_folder = path + './Centro Sul/'
sul_folder = path + './Sul/'
serra_folder = path + './Serra Gaucha/'

centro_files = os.listdir(centro_folder)
sul_files = os.listdir(sul_folder)
serra_files = os.listdir(serra_folder)

print(centro_files)
def upload(file_folder, file_id, files_dir):

    mime_types = [] 
    for files in file_folder:
        mime_types.append('image/png')

    for file_name, mime_type in zip(file_folder, mime_types):
        file_metadata = {
            'name': file_name,
            'parents': [file_id]
        }

        media = MediaFileUpload(files_dir + '{0}'.format(file_name), mimetype=mime_type)

        service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id'
        ).execute()

upload(centro_files, centro_id, centro_folder)
upload(sul_files, sul_id, sul_folder)
upload(serra_files, serra_id, serra_folder)