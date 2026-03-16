from drive_service import get_drive_service

def list_all_files():
    service = get_drive_service()
    page_token = None
    while True:
        response = service.files().list(
            fields="nextPageToken, files(id, name, mimeType)",
            pageToken=page_token
        ).execute()
        for file in response.get('files', []):
            print(f"{file['name']} ({file['id']}) - {file['mimeType']}")
        page_token = response.get('nextPageToken', None)
        if page_token is None:
            break

if __name__ == "__main__":
    list_all_files()