import os
import dropbox
from dropbox.exceptions import AuthError, ApiError
from requests.exceptions import HTTPError
from dotenv import load_dotenv

load_dotenv()


app_key = os.environ.get("APP_KEY")
app_secret =os.environ.get("APP_SECRET")

local_file_path = os.environ.get("LOCAL_UPLOAD_FILE_PATH")
dropbox_destination_path = os.environ.get("DROPBOX_UPLOAD_DESTINATION_PATH")
dropbox_file_path = os.environ.get("DOWNLOAD_FILE_PATH")
local_destination_path = os.environ.get("LOCAL_DOWNLOAD_DESTINATION_PATH")

auth_flow = dropbox.DropboxOAuth2FlowNoRedirect(app_key, app_secret)
auth_url = auth_flow.start()

print("Please visit this URL to authorize the app:")
print(auth_url)

auth_code = input("Enter the authorization code: ")

try:
    oauth_result = auth_flow.finish(auth_code)
    access_token = oauth_result.access_token
    dbx = dropbox.Dropbox(access_token)
    user = dbx.users_get_current_account()
    print(f"Successfully authorized as {user.name.display_name}")
except HTTPError as e:
    print("Wrong authorization code !")
    exit(1)


def folder_list():
    try:
        files = dbx.files_list_folder('')
        print("Files in the root folder:")
        for file in files.entries:
            print(file.name)
    except dropbox.exceptions.BadInputError as e:
        print("Your app is not permitted to access this endpoint because it does not have the required scope")


def create_folder():
    try:
        folder_path = '/noname'
        response = dbx.files_create_folder(folder_path)
        if response:
            print("Folder created successfully")
    except ApiError as e:
        if e.error.is_path() and e.error.get_path().is_conflict():
            print("Folder already exists!")
        else:
            print("Unknown exception occurred")


def upload_file():
    try:
        # Open the file in read mode
        with open(local_file_path, 'rb') as file:
            # Upload the file to Dropbox
            dbx.files_upload(file.read(), dropbox_destination_path)

        print("File uploaded successfully!")
    except ApiError as e:
        if isinstance(e.error, dropbox.files.UploadError):
            if isinstance(e.error.is_path(), dropbox.files.WriteConflictError):
                print("A file or folder with the same name already exists at the destination path.")
            else:
                print("An error occurred while uploading the file:", e)
        else:
            print("An error occurred while uploading the file:", e)
    except AuthError as e:
        print("Authentication error:", e)


def download_file():
    try:
        metadata = dbx.files_get_metadata(dropbox_file_path)

        # Check if the metadata indicates that it's a file
        if isinstance(metadata, dropbox.files.FileMetadata):
            print("File exists!")
        else:
            print("The specified path exists, but it's not a file.")
        dbx.files_download_to_file(local_destination_path, dropbox_file_path)
        print("File downloaded successfully!")
    except dropbox.exceptions.ApiError as e:
        print("An error occurred while downloading the file:", e)
    except dropbox.exceptions.AuthError as e:
        print("Authentication error:", e)
