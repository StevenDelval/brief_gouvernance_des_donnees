import os
from azure.storage.filedatalake import DataLakeServiceClient
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Retrieve connection information from environment variables
STORAGE_ACCOUNT_NAME = os.getenv("STORAGE_ACCOUNT_NAME")
STORAGE_ACCOUNT_KEY = os.getenv("STORAGE_ACCOUNT_KEY")

def get_service_client(account_name, account_key):
    """Create a DataLakeServiceClient instance.
    
    Args:
        account_name (str): Azure Storage account name.
        account_key (str): Azure Storage account key.
        
    Returns:
        DataLakeServiceClient: A client for interacting with the Data Lake service.
    """
    service_client = DataLakeServiceClient(
        account_url=f"https://{account_name}.dfs.core.windows.net",
        credential=account_key
    )
    return service_client

# Initialize the Data Lake service client
service_client = get_service_client(STORAGE_ACCOUNT_NAME, STORAGE_ACCOUNT_KEY)

# Define the local root folder containing files to upload
local_root_folder_path = "mocks/data_lake"

# Iterate through each folder in the local root folder
for local_folder in os.listdir(local_root_folder_path):
    local_folder_path = os.path.join(local_root_folder_path, local_folder)
    
    if not os.path.isdir(local_folder_path):
        # Skip if the path is not a folder
        continue

    print(f"Processing folder: {local_folder}")

    # Get the file system client for the current folder
    file_system_client = service_client.get_file_system_client(file_system=local_folder)

    # Iterate through each file in the current folder
    for file in os.listdir(local_folder_path):
        local_file_path = os.path.join(local_folder_path, file)
        
        if not os.path.isfile(local_file_path):
            # Skip if the path is not a file
            continue

        print(f"Uploading file: {local_file_path}")

        # Get the file client for the current file
        file_client = file_system_client.get_file_client(file)

        # Read and upload the file contents
        with open(local_file_path, "rb") as file_data:
            file_contents = file_data.read()
            file_client.upload_data(file_contents, overwrite=True)

        

