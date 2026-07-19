from huggingface_hub import hf_hub_download
from tensorflow.keras.models import load_model
import streamlit as st

from config import HF_REPO_ID, MODEL_FILES


@st.cache_resource
def load_models():
    """Download and load all models from Hugging Face."""

    print("Downloading models from Hugging Face...")

    model_paths = {
        model_name: hf_hub_download(
            repo_id=HF_REPO_ID,
            filename=model_file
        )
        for model_name, model_file in MODEL_FILES.items()
    }

    print("Loading models...")

    models = {
        model_name: load_model(model_path)
        for model_name, model_path in model_paths.items()
    }

    print("Models loaded successfully.")

    return models


MODELS = load_models()


def get_model(model_name: str):
    """
    Returns the selected model.
    """
    if model_name not in MODELS:
        raise ValueError(f"Invalid model: {model_name}")

    return MODELS[model_name]