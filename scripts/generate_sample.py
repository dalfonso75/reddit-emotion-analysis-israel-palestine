from create_sample import KaggleDatasetHandler, DataSampler   
# Step 1: Handle the dataset
dataset_handler = KaggleDatasetHandler(
    dataset_slug='asaniczka/reddit-on-israel-palestine-daily-updated',
    zip_filename='reddit-on-israel-palestine-daily-updated.zip',
    extract_folder='reddit_dataset',
    csv_filename='reddit_opinion_PSE_ISR.csv'
)

try:
    dataset_handler.download_dataset()
    dataset_handler.extract_dataset()
    dataset_handler.load_csv()
    dataset_handler.configure_pandas_display()
except Exception as e:
    # Handle exceptions as needed (log, raise, etc.)
    raise e

# Step 2: Sample the data
try:
    sampler = DataSampler(dataset_handler.df)
    sampler.save_sample_to_csv(output_filename='data/sampled_data.csv')
except Exception as e:
    # Handle exceptions as needed
    raise e
