import youtube_dl
from google.oauth2 import service_account
from googleapiclient.http import MediaFileUpload # pip install --upgrade google-api-python-client
from googleapiclient.discovery import build


def download_video(text):
    SAVE_PATH = r'/downloadsForVideoBot'
    ydl_opts = {
        'outtmpl': SAVE_PATH + '/%(id)s.%(ext)s',
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download({text})
        url = text
        info_dict = ydl.extract_info(url, download=False)
        id = info_dict.get('id', None)

    SCOPES = ['https://www.googleapis.com/auth/drive']
    SERVICE_ACCOUNT_FILE = r'tgBot\downloader-forb0t-debc97e716bb.json'
    credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('drive', 'v3', credentials=credentials)

    folder_id = '1o0sNMb5kIZtjcgME8yKx1AuY3Ma5j-k3'
    name = id + '.mp4'

    p = 'downloadsForVideoBot//' + name
    file_path = p
    file_metadata = {
        'name': name,
        'parents': [folder_id]
    }
    media = MediaFileUpload(file_path, resumable=True)
    r = service.files().create(body=file_metadata, media_body=media,
                                   fields='id').execute()

    urlForUser = 'https://drive.google.com/uc?export=download&id=' + r.get('id')

    return urlForUser












