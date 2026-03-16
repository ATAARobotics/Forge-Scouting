import os.path
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

SCOPES = [
    # Full, unrestricted access to the user's Drive (use with caution; requires restricted scope verification)
    'https://www.googleapis.com/auth/drive',
    # Per-file access to files created or opened with the app (recommended for most apps)
    'https://www.googleapis.com/auth/drive.file',
    # Read-only access to all Drive files
    'https://www.googleapis.com/auth/drive.readonly',
    # View and manage metadata of files in your Drive
    'https://www.googleapis.com/auth/drive.metadata',
    # View metadata for files in your Drive (read-only)
    'https://www.googleapis.com/auth/drive.metadata.readonly',
    # View and manage its own configuration data in your Google Drive
    'https://www.googleapis.com/auth/drive.appdata',
]

def get_drive_service():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('drive', 'v3', credentials=creds)