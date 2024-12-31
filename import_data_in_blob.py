import os
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Retrieve connection information from environment variables
BLOB_STORAGE_NAME = os.getenv("BLOB_STORAGE_NAME")
BLOB_STORAGE_KEY = os.getenv("BLOB_STORAGE_KEY")

def get_service_client(account_name, account_key):
    """Create a BlobServiceClient instance.
    
    Args:
        account_name (str): Azure Storage account name.
        account_key (str): Azure Storage account key.
        
    Returns:
        BlobServiceClient: A client for interacting with the Blob service.
    """
    service_client = BlobServiceClient(
        account_url=f"https://{account_name}.blob.core.windows.net/",
        credential=account_key
    )
    return service_client

# Initialize the Blob service client
service_client = get_service_client(BLOB_STORAGE_NAME, BLOB_STORAGE_KEY)

# Define the local root folder containing files to upload
local_root_folder_path = "mocks/blob_storage/students"

# Get the container client for the target container
container_client = service_client.get_container_client("students")

# Iterate through each file in the local root folder
for file in os.listdir(local_root_folder_path):
    local_file_path = os.path.join(local_root_folder_path, file)

    if not os.path.isfile(local_file_path):
        # Skip if the path is not a file
        continue

    print(f"Uploading file: {local_file_path}")

    # Get the blob client for the current file
    blob_client = container_client.get_blob_client(file)

    # Upload the file contents 
    with open(local_file_path, "rb") as file_data:
        blob_client.upload_blob(file_data, overwrite=True)