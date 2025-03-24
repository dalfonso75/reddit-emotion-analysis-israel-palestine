import os
import zipfile
import pandas as pd

class KaggleDatasetHandler:
    def __init__(self, dataset_slug: str, zip_filename: str, extract_folder: str, csv_filename: str):
        """
        Initializes the dataset handler.

        Parameters:
        - dataset_slug: The Kaggle dataset slug (e.g., 'asaniczka/reddit-on-israel-palestine-daily-updated').
        - zip_filename: The name of the downloaded zip file.
        - extract_folder: The folder to extract the dataset to.
        - csv_filename: The name of the CSV file inside the extracted folder.
        """
        self.dataset_slug = dataset_slug
        self.zip_filename = zip_filename
        self.extract_folder = extract_folder
        self.csv_filename = csv_filename
        self.df = None

    def download_dataset(self):
        """Downloads the dataset from Kaggle."""
        try:
            exit_code = os.system(f'kaggle datasets download -d {self.dataset_slug}')
            if exit_code != 0:
                raise Exception("Kaggle download command failed.")
        except Exception as e:
            raise Exception(f"Error downloading dataset: {e}")

    def extract_dataset(self):
        """Extracts the downloaded zip file."""
        try:
            with zipfile.ZipFile(self.zip_filename, 'r') as zip_ref:
                zip_ref.extractall(self.extract_folder)
        except (zipfile.BadZipFile, FileNotFoundError) as e:
            raise Exception(f"Error extracting zip file: {e}")

    def load_csv(self):
        """Loads the CSV file into a DataFrame."""
        try:
            csv_path = os.path.join(self.extract_folder, self.csv_filename)
            self.df = pd.read_csv(csv_path)
        except FileNotFoundError as e:
            raise Exception(f"CSV file not found: {e}")
        except pd.errors.EmptyDataError as e:
            raise Exception(f"CSV file is empty: {e}")
        except Exception as e:
            raise Exception(f"Error loading CSV: {e}")

    def configure_pandas_display(self):
        """Configures pandas display options to show all columns."""
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)

class DataSampler:
    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe
    
    def get_sample(self, sample_size=1000, random_state=42):
        """Returns a random sample from the DataFrame."""
        try:
            sampled_df = self.df.sample(n=sample_size, random_state=random_state).reset_index(drop=True)
            return sampled_df
        except (ValueError, TypeError, pd.errors.EmptyDataError) as e:
            raise Exception(f"Error while sampling rows: {e}")
    
    def save_sample_to_csv(self, output_filename='sampled_data.csv', sample_size=1000, random_state=42):
        """Takes a random sample and saves it as a CSV file."""
        try:
            sampled_df = self.get_sample(sample_size=sample_size, random_state=random_state)
            sampled_df.to_csv(output_filename, index=False)
        except (OSError, IOError) as e:
            raise Exception(f"Error while saving CSV file: {e}")
        except Exception as e:
            raise Exception(f"Unexpected error during sampling process: {e}")
