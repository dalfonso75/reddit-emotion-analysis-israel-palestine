# type: ignore
from transformers import (
    AutoTokenizer,
    T5Tokenizer,
    AutoModelForSequenceClassification,
    AutoModelForSeq2SeqLM,
    pipeline,
)
import pandas as pd


class EmotionAnalyzer:
    """
    EmotionAnalyzer uses a pre-trained Hugging Face modsel to classify emotions in text.
    Supported emotions: anger, fear, joy, love, sadness, surprise.

    Attributes:
        model_name (str): Hugging Face model identifier.S
        classifier (Pipeline): Hugging Face text classification pipeline.
    """

    def __init__(
        self,
        model_name="bhadresh-savani/distilbert-base-uncased-emotion",
        device: int = -1,
    ):
        """
        Args:
            model_name (str): Pretrained model from Hugging Face Hub.
            device (int): -1 for CPU, 0 or positive integer for GPU (e.g. 0 for CUDA:0).
        """
        self.model_name = model_name
        self.device = device
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(self.model_name)
        self.classifier = pipeline(
            "text-classification",
            model=self.model,
            tokenizer=self.tokenizer,
            return_all_scores=False,
            truncation=True,
            max_length=512,
            device=self.device,
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
            return result[0]["label"]
        except Exception as e:
            print(f"Error predicting emotion: {e}")
            return "error"

    def apply_to_dataframe(
        self,
        df: pd.DataFrame,
        text_column: str,
        output_column: str = "predicted_emotion",
    ) -> pd.DataFrame:
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


class EmotionAnalyzerT5:
    """
    EmotionAnalyzerT5 uses the 'mrm8488/t5-base-finetuned-emotion' model to predict emotions.
    It is a generative model that outputs a text label like: joy, sadness, etc.
    """

    def __init__(
        self, model_name="mrm8488/t5-base-finetuned-emotion", device: int = -1
    ):
        """
        Args:
            model_name (str): Hugging Face model identifier.
            device (int): -1 for CPU, 0 or positive integer for GPU.
        """
        self.model_name = model_name
        self.device = device
        self.tokenizer = T5Tokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_name)
        self.pipeline = pipeline(
            "text2text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
            device=self.device,
            truncation=True,
            max_length=512,
        )

    def predict_emotion(self, text: str) -> str:
        """
        Predict the emotion of the input text.
        Args:
            text (str): The input sentence.
        Returns:
            str: Predicted emotion label.
        """
        if not isinstance(text, str) or not text.strip():
            return "unknown"
        try:
            prompt = f"emotion: {text.strip()}"
            result = self.pipeline(
                prompt, max_length=5, clean_up_tokenization_spaces=True
            )
            return result[0]["generated_text"].strip()
        except Exception as e:
            print(f"Error predicting emotion: {e}")
            return "error"

    def apply_to_dataframe(
        self,
        df: pd.DataFrame,
        text_column: str,
        output_column: str = "predicted_emotion",
    ) -> pd.DataFrame:
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


class EmotionAnalyzerRoBERTa:
    def __init__(self, model_name="j-hartmann/emotion-english-distilroberta-base", device: int = -1):
        self.model_name = model_name
        self.device = device
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)
        self.pipeline = pipeline(
            "text-classification",
            model=self.model,
            tokenizer=self.tokenizer,
            device=self.device,
            return_all_scores=False,
            truncation=True,
            max_length=512,
        )

    def predict_emotion(self, text: str) -> str:
        if not isinstance(text, str) or not text.strip():
            return "unknown"
        try:
            result = self.pipeline(text)
            return result[0]["label"]
        except Exception as e:
            print(f"Error predicting emotion: {e}")
            return "error"

    def apply_to_dataframe(self, df: pd.DataFrame, text_column: str, output_column: str = "predicted_emotion") -> pd.DataFrame:
        df[output_column] = df[text_column].apply(self.predict_emotion)
        return df