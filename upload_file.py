from drive_service import get_drive_service
from googleapiclient.http import MediaFileUpload

def upload_file(local_path, drive_folder_id=None):
    service = get_drive_service()
    file_metadata = {'name': local_path.split('/')[-1]}
    if drive_folder_id:
        file_metadata['parents'] = [drive_folder_id]
    media = MediaFileUpload(local_path, resumable=True)
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print(f"File uploaded. File ID: {file.get('id')}")

if __name__ == "__main__":
    # Replace with your local file path and (optionally) Drive folder ID
    local_path = 'matchdata.csv'
    drive_folder_id = '1P-dYJBZOqcNFtkrX8a1hqG1qisUNq0XK'  # Folder ID, after /folders/ in the URL
    upload_file(local_path, drive_folder_id)