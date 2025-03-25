from create_sample import KaggleDatasetHandler, DataSampler

# Step 1: Handle the dataset
dataset_handler = KaggleDatasetHandler(
    dataset_slug='asaniczka/reddit-on-israel-palestine-daily-updated',
    csv_filename='reddit_opinion_PSE_ISR.csv'  # Solo necesitas el CSV
)

try:
    dataset_handler.download_dataset()
    dataset_handler.load_csv()
    dataset_handler.configure_pandas_display()
except Exception as e:
    print(f"Error handling dataset: {e}")
    raise e

# Step 2: Sample the data
try:
    sampler = DataSampler(dataset_handler.df)
    sampler.save_sample_to_csv(output_filename='data/sampled_data.csv')
except Exception as e:
    print(f"Error sampling data: {e}")
    raise e
