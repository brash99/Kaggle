import kaggle
import os
import zipfile

print("libraries imported successfully")

# Authenticate (looks for the kaggle.json file automatically)
kaggle.api.authenticate()

# Define dataset or competition details (example for Titanic competition)
competition_name = 'titanic'
download_path = 'data_' + competition_name

# Create directory if it doesn't exist
if not os.path.exists(download_path):
    os.makedirs(download_path)

# Download the files to the specified directory
kaggle.api.competition_download_files(competition_name, path=download_path)

# Unzip the files
with zipfile.ZipFile(os.path.join(download_path, f'{competition_name}.zip'), 'r') as zip_ref:
    zip_ref.extractall(download_path)