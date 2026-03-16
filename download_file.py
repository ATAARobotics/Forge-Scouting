from drive_service import get_drive_service
import io
from googleapiclient.http import MediaIoBaseDownload

def download_file(file_id, destination):
    service = get_drive_service()
    request = service.files().get_media(fileId=file_id)
    fh = io.FileIO(destination, 'wb')
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while not done:
        status, done = downloader.next_chunk()
        print(f"Download {int(status.progress() * 100)}%.")
    print(f"File downloaded to {destination}")

if __name__ == "__main__":
    # Replace with your file ID and desired local path
    file_id = 'YOUR_FILE_ID'
    destination = 'file_name.extension'
    download_file(file_id, destination)