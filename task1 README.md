## Prerequisites 
* python3
* pip3

# Task 1

- Dropbox demo application

1. Create a virtual environment. If you don't have virtualenv installed, you can download it with the command:
  
    ```
    pip install virtualenv
    ```

2. Create a virtual environment with the following command:
    ```
    virtualenv <virtual environment name>
    ```

3. Activate the virtual environment using the command:

    ```
    source <virtual environment name>/bin/activate
    ```
    # Install the project dependencies by running:
    ```
    pip install -r requirements.txt
    ```
- Create a .env file in the backend directory using the command line:
    ```
    touch .env
    ```
- Open the .env file and update it with the PostgreSQL database credentials as follows:
    ```
    APP_KEY=<DROPBOX_APP_KEY>
    APP_SECRET=<DROPBOX_APP_SECRET>
    
    LOCAL_UPLOAD_FILE_PATH=<UPLOAD FILE LOCAL PATH>
    DROPBOX_UPLOAD_DESTINATION_PATH=<DROPBOX DESTINATION PATH FOR UPLOAD>
    DOWNLOAD_FILE_PATH=<DROPBOX FILE PATH FOR DOWNLOAD>
    LOCAL_DOWNLOAD_DESTINATION_PATH=<LOCAL PATH FOR DOWNLOAD>

    ```
  
Basically this app generate the auth_url for auth_code by visiting url 
by auth_code we can access the dropbox account. Now we can use dropbox account 
from our code.

    -   In this app we show the folder lists.
    - create folder.
    - upload file.
    - download file.

* We should be aware not to share the app_key and app_secret.

* In future we could add some more functionality like:-

        - File sharing.
        - File preview and thumbnail
        - Activity Tracking.
        - Advanced Search
