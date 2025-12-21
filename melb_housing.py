
import kaggle
import os, zipfile
import pandas as pd

kaggle.api.authenticate()

dataset = "dansbecker/melbourne-housing-snapshot"
download_path = "data_melb"

os.makedirs(download_path, exist_ok=True)

kaggle.api.dataset_download_files(dataset, path=download_path)

zip_path = os.path.join(download_path, "melbourne-housing-snapshot.zip")
with zipfile.ZipFile(zip_path, "r") as z:
    z.extractall(download_path)

print("Done. Files:", os.listdir(download_path))

# save filepath to variable for easier access
melbourne_file_path = 'data_melb/melb_data.csv'
# read the data and store data in DataFrame titled melbourne_data
melbourne_data = pd.read_csv(melbourne_file_path)
# print a summary of the data in Melbourne data
melbourne_data.describe()

print(melbourne_data.head())
