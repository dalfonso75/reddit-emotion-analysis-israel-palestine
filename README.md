# reddit-emotion-analysis-israel-palestine

## 📄 Project Overview

This project focuses on analyzing the emotional dynamics expressed in Reddit comments related to the Israel-Palestine conflict. By leveraging pre-trained Natural Language Processing (NLP) models from Hugging Face, we aim to classify and visualize the predominant emotions in the digital conversation, as well as observe their evolution over time.

## 🚀 Objectives

- Clean and preprocess the Reddit dataset containing user comments.
- Apply a pre-trained NLP model to classify emotions such as joy, sadness, anger, fear, and surprise.
- Analyze temporal patterns and trends in the expressed emotions.
- Present the results using clear visualizations and an interactive dashboard.

## 🗂 Project Structure

```
📂 reddit-emotion-analysis-israel-palestine
 ├── 📂 data                  # Raw and processed dataset files
 │    └── reddit_comments.csv  # Original dataset
 ├── 📂 models                # Pre-trained models and output files
 ├── 📂 notebooks             # Jupyter notebooks for exploration and testing
 ├── 📂 src                   # Source code
 │    ├── text_cleaner.py      # Class for cleaning Reddit comments
 │    ├── sentiment_model.py   # Class for loading and applying Hugging Face model
 │    ├── visualizer.py        # Class for generating visualizations
 │    ├── dashboard.py         # Streamlit app for interactive visualization
 │    └── utils.py             # Utility functions
 ├── 📂 outputs               # Intermediate cleaned data and results
 ├── 📜 requirements.txt      # Python dependencies
 ├── 📜 README.md             # Project description
 ├── 📜 .gitignore            # Files/folders to ignore in Git
 └── 📜 LICENSE               # License
```

2. **Create a virtual environment and install dependencies:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. **Place the dataset:**
Put the `reddit_comments.csv` file inside the `data/` folder.

## 🧠 Technologies & Libraries

- Python 3.x
- Pandas
- Numpy
- SpaCy / NLTK
- Transformers (Hugging Face)
- Matplotlib / Seaborn
- Streamlit (for dashboard)

## 📊 Results

Final deliverables will include:
- Emotion classification results.
- Temporal trend visualizations.
- Interactive dashboard.
- Final report with methodology, findings, and conclusions.

---

## 📌 License

[MIT License](LICENSE)
