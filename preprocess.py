from pathlib import Path

import numpy as np
from PIL import Image
from tensorflow.keras.applications.vgg16 import preprocess_input
from config import IMAGE_SIZE, ALLOWED_EXTENSIONS

# Validate Image Extension
def allowed_file(filename: str) -> bool:
    """
    Check whether the uploaded file has a valid image extension.
    """

    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )

# CNN Preprocessing
# CNN Preprocessing
def preprocess_cnn(image) -> np.ndarray:
    """
    Preprocess image for CNN models.

    Parameters
    ----------
    image
        UploadedFile or image path.

    Returns
    -------
    np.ndarray
        Shape: (1, 100, 100, 1)
    """
    image = Image.open(image).convert("L")

    image = image.resize(IMAGE_SIZE)

    image = np.array(image, dtype=np.float32)

    image /= 255.0

    image = np.expand_dims(image, axis=-1)
    image = np.expand_dims(image, axis=0)

    return image

# VGG16 Preprocessing
def preprocess_vgg(image) -> np.ndarray:
    """
    Preprocess image for VGG16 model.

    Parameters
    ----------
    image
        UploadedFile or image path.

    Returns
    -------
    np.ndarray
        Shape: (1, 100, 100, 3)
    """
    image = Image.open(image).convert("RGB")

    image = image.resize(IMAGE_SIZE)

    image = np.array(image, dtype=np.float32)

    image = preprocess_input(image)

    image = np.expand_dims(image, axis=0)

    return image