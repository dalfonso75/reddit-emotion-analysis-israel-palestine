from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import pandas as pd
from typing import Union

class EmotionAnalyzer:
    """
    EmotionAnalyzer uses a pre-trained Hugging Face model to classify emotions in text.
    Supported emotions: anger, fear, joy, love, sadness, surprise.

    Attributes:
        model_name (str): Hugging Face model identifier.
        classifier (Pipeline): Hugging Face text classification pipeline.
    """

    def __init__(self, model_name="bhadresh-savani/distilbert-base-uncased-emotion"):
        self.model_name = model_name
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(self.model_name)
        self.classifier = pipeline(
            "text-classification",
            model=self.model,
            tokenizer=self.tokenizer,
            return_all_scores=False
        )

    def predict_emotion(self, text: str) -> str:
        """
        Predict the most likely emotion for a single text input.

        Args:
            text (str): Input text.

        Returns:
            str: Predicted emotion label.
        """
        if not isinstance(text, str) or not text.strip():
            return "unknown"
        try:
            result = self.classifier(text)
            return result[0]['label']
        except Exception as e:
            print(f"Error predicting emotion: {e}")
            return "error"

    def apply_to_dataframe(self, df: pd.DataFrame, text_column: str, output_column: str = "predicted_emotion") -> pd.DataFrame:
        """
        Apply emotion classification to a column in a DataFrame.

        Args:
            df (pd.DataFrame): DataFrame with text data.
            text_column (str): Name of the column containing text to classify.
            output_column (str): Name of the new column to store predicted emotions.

        Returns:
            pd.DataFrame: Updated DataFrame with emotion predictions.
        """
        df[output_column] = df[text_column].apply(self.predict_emotion)
        return df
