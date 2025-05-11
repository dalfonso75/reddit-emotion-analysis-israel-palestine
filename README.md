# reddit-emotion-analysis-israel-palestine

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/dalfonso75/reddit-emotion-analysis-israel-palestine)

## 📄 Project Overview

This project focuses on analyzing the emotional dynamics expressed in Reddit comments related to the Israel-Palestine conflict. By leveraging pre-trained Natural Language Processing (NLP) models from Hugging Face, we aim to classify and visualize the predominant emotions in the digital conversation, as well as observe their evolution over time.

## 🚀 Objectives

- Clean and preprocess the Reddit dataset containing user comments.
- Apply a pre-trained NLP model to classify emotions such as joy, sadness, anger, fear, and surprise.
- Analyze temporal patterns and trends in the expressed emotions.
- Present the results using clear visualizations and an interactive dashboard.

## 📖 Dataset Variables Description

The following table provides a description of each of the **24 variables** in the dataset and their meaning:

| **Variable**                   | **Description**                                                                                  |
|--------------------------------|--------------------------------------------------------------------------------------------------|
| `comment_id`                   | Unique ID of the Reddit comment.                                                                 |
| `score`                        | Total score of the comment (upvotes minus downvotes).                                            |
| `self_text`                    | Text content of the comment. May contain user-written text or be empty (NaN).                    |
| `subreddit`                    | Name of the subreddit where the comment was posted.                                              |
| `created_time`                 | Date and time when the comment was created (format: YYYY-MM-DD HH:MM:SS).                        |
| `post_id`                      | Unique ID of the post to which the comment belongs.                                              |
| `author_name`                  | Username of the comment author.                                                                  |
| `controversiality`             | Indicator of controversy (0 = not controversial, 1 = controversial).                            |
| `ups`                          | Number of upvotes the comment received.                                                          |
| `downs`                        | Number of downvotes. In Reddit, usually not displayed, may be 0.                                 |
| `user_is_verified`             | Indicates whether the user is verified (True/False).                                             |
| `user_account_created_time`    | Date and time when the user's account was created.                                               |
| `user_awardee_karma`           | Karma accumulated by the user from giving awards.                                                |
| `user_awarder_karma`           | Karma accumulated by the user from receiving awards.                                             |
| `user_link_karma`              | Karma accumulated by the user from sharing links.                                                |
| `user_comment_karma`           | Karma accumulated by the user from comments.                                                     |
| `user_total_karma`             | Total karma (sum of link, comment, awardee, and awarder karma).                                   |
| `post_score`                   | Total score of the post to which the comment belongs.                                            |
| `post_self_text`               | Text content of the post, if available.                                                          |
| `post_title`                   | Title of the post.                                                                               |
| `post_upvote_ratio`            | Proportion of upvotes on the post (value between 0 and 1).                                       |
| `post_thumbs_ups`              | Number of upvotes the post received.                                                             |
| `post_total_awards_received`   | Total number of awards received by the post.                                                     |
| `post_created_time`            | Date and time when the post was created (format: YYYY-MM-DD HH:MM:SS).                           |

---

## 🎯 Selected Variables for Analysis

For the purpose of emotion classification and temporal analysis, we have selected a subset of variables from the dataset that provide meaningful information while preserving the full dataset for potential future exploration. Below is a description of the key variables used:

| **Variable**            | **Reason for Inclusion**                                                                                     |
|------------------------|-------------------------------------------------------------------------------------------------------------|
| `comment_id`           | Unique identifier for each comment, used to maintain data integrity and avoid duplicates.                   |
| `self_text`            | Main text content of the comment, serving as the input for emotion classification using NLP models.          |
| `created_time`         | Timestamp of the comment, essential for analyzing temporal trends in expressed emotions.                    |
| `subreddit`            | Indicates the community where the comment was posted, useful for comparing emotional patterns across topics. |
| `score`                | Total score of the comment (upvotes minus downvotes), useful to correlate engagement with specific emotions.  |
| `post_title`           | Title of the original post, provides additional context that may influence the emotions expressed in comments. |

---

These selected variables allow us to:
- **Classify emotions** such as joy, sadness, anger, fear, and surprise.
- **Analyze temporal patterns** of expressed emotions.
- **Perform sub-analyses** to understand how engagement (score) and subreddit categories relate to emotional content.

The remaining variables are preserved in the dataset for potential future analyses.


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
