import os
import pandas as pd
import kagglehub


class KaggleDatasetHandler:
    def __init__(self, dataset_slug: str, csv_filename: str):
        """
        Initializes the dataset handler.

        Parameters:
        - dataset_slug: The Kaggle dataset slug (e.g., 'asaniczka/reddit-on-israel-palestine-daily-updated').
        - csv_filename: The name of the CSV file inside the downloaded folder.
        """
        self.dataset_slug = dataset_slug
        self.csv_filename = csv_filename
        self.downloaded_path = None
        self.df = None

    def download_dataset(self):
        """Downloads the dataset from Kaggle using kagglehub."""
        try:
            print(f"Downloading dataset: {self.dataset_slug}")
            self.downloaded_path = kagglehub.dataset_download(self.dataset_slug)
            print(f"Dataset downloaded to: {self.downloaded_path}")
        except Exception as e:
            raise Exception(f"Error downloading dataset: {e}")

    def load_csv(self):
        """Loads the CSV file into a DataFrame."""
        try:
            csv_path = os.path.join(self.downloaded_path, self.csv_filename)
            print(f"Loading CSV from: {csv_path}")
            self.df = pd.read_csv(csv_path)
        except FileNotFoundError as e:
            raise Exception(f"CSV file not found: {e}")
        except pd.errors.EmptyDataError as e:
            raise Exception(f"CSV file is empty: {e}")
        except Exception as e:
            raise Exception(f"Error loading CSV: {e}")

    def configure_pandas_display(self):
        """Configures pandas display options to show all columns."""
        pd.set_option("display.max_columns", None)
        pd.set_option("display.width", None)


class DataSampler:
    """
    Handles random sampling of a pandas DataFrame and saving samples to CSV.

    Parameters:
    - dataframe: pandas DataFrame to sample from.
    """

    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe

    def get_sample(self, sample_size=1000, random_state=42):
        """Returns a random sample from the DataFrame."""
        try:
            sampled_df = self.df.sample(
                n=sample_size, random_state=random_state
            ).reset_index(drop=True)
            return sampled_df
        except (ValueError, TypeError, pd.errors.EmptyDataError) as e:
            raise Exception(f"Error while sampling rows: {e}")

    def save_sample_to_csv(
        self, output_filename="sampled_data.csv", sample_size=1000, random_state=42
    ):
        """Takes a random sample and saves it as a CSV file."""
        try:
            sampled_df = self.get_sample(
                sample_size=sample_size, random_state=random_state
            )
            sampled_df.to_csv(output_filename, index=False)
            print(f"Sample saved to: {output_filename}")
        except (OSError, IOError) as e:
            raise Exception(f"Error while saving CSV file: {e}")
        except Exception as e:
            raise Exception(f"Unexpected error during sampling process: {e}")
