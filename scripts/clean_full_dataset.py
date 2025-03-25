import pandas as pd

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.text_cleaner import RedditTextCleaner


class DataCleaner:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path
        self.cleaner = RedditTextCleaner()

    def load_data(self):
        print(f"Loading data from {self.input_path}...")
        self.df = pd.read_csv(self.input_path)
        print(f"Dataset loaded with {len(self.df)} rows.")

    def clean_text_column(self):
        print("Cleaning text data...")
        self.df["clean_text"] = self.df["self_text"].apply(self.cleaner.clean)
        print("Text cleaning completed.")

    def select_columns(self):
        print("Selecting required columns...")
        required_columns = [
            "comment_id",
            # "self_text",
            "clean_text",
            "created_time",
            "subreddit",
            "score",
            "post_title",
        ]
        self.df = self.df[required_columns]
        print("Columns selected.")

    def save_cleaned_data(self):
        print(f"Saving cleaned data to {self.output_path}...")
        self.df.to_csv(self.output_path, index=False)
        print("Cleaned data saved.")

    def run(self):
        self.load_data()
        self.clean_text_column()
        self.select_columns()
        self.save_cleaned_data()
        print("Data cleaning process completed.")


if __name__ == "__main__":
    input_file = "data/reddit_opinion_PSE_ISR.csv"
    output_file = "data/reddit_opinion_PSE_ISR_cleaned.csv"

    # input_file = "data/sampled_data.csv"
    # output_file = "data/cleaned_data.csv"

    cleaner = DataCleaner(input_file, output_file)
    cleaner.run()
