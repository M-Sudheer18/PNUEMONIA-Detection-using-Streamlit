<div align="center">

# 🩻 AI Chest X-Ray Pneumonia Detection

### *Deep Learning Powered Pneumonia Detection from Chest X-Ray Images*

<img src="assets/banner.png" width="900"/>

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge\&logo=python)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange?style=for-the-badge\&logo=tensorflow)
![Keras](https://img.shields.io/badge/Keras-Deep%20Learning-red?style=for-the-badge\&logo=keras)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?style=for-the-badge\&logo=streamlit)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Model%20Hub-yellow?style=for-the-badge\&logo=huggingface)
![License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)

### 🚀 Detect Pneumonia from Chest X-Ray Images using Multiple Deep Learning Models

*A modern AI-powered web application built with TensorFlow, Streamlit, and Hugging Face.*

</div>

---

# 🌟 Overview

Chest X-Ray Pneumonia Detection is an end-to-end Deep Learning application that predicts whether a Chest X-Ray belongs to a **NORMAL** patient or one affected by **PNEUMONIA**.

The application allows users to:

* 🩻 Upload Chest X-Ray images
* 🤖 Select different Deep Learning models
* ⚡ Perform real-time inference
* 📊 View confidence scores
* 📈 Analyze class probabilities
* ☁ Automatically download models from Hugging Face
* 🚀 Deploy seamlessly on Streamlit Community Cloud

---

# ✨ Key Features

| Feature                     | Description                             |
| --------------------------- | --------------------------------------- |
| 🩻 Image Upload             | Supports JPG, JPEG and PNG              |
| 🤖 Multiple Models          | CNN (10 Epochs), CNN (20 Epochs), VGG16 |
| ⚡ Fast Inference            | Cached TensorFlow model loading         |
| 📊 Confidence Score         | Displays prediction confidence          |
| 📈 Probability Distribution | Shows probabilities for each class      |
| ☁ Hugging Face Hub          | Automatic model downloads               |
| 🎨 Modern UI                | Responsive Streamlit interface          |
| 🚀 Cloud Ready              | Deployable on Streamlit Cloud           |

---

# 🎬 Application Workflow

```text
                🩻 Upload Chest X-Ray
                          │
                          ▼
                 🧹 Image Preprocessing
                          │
          ┌───────────────┴───────────────┐
          │                               │
     CNN Models                     VGG16 Model
 (Grayscale 100×100)        RGB + preprocess_input
          │                               │
          └───────────────┬───────────────┘
                          ▼
                  🤖 TensorFlow Prediction
                          │
                          ▼
              📊 Confidence + Probabilities
                          │
                          ▼
                  ✅ Final Diagnosis
```

---

# 🧠 Deep Learning Models

| Model           | Architecture      | Input     | Output             |
| --------------- | ----------------- | --------- | ------------------ |
| CNN (10 Epochs) | Custom CNN        | Grayscale | Pneumonia / Normal |
| CNN (20 Epochs) | Improved CNN      | Grayscale | Pneumonia / Normal |
| VGG16           | Transfer Learning | RGB       | Pneumonia / Normal |

---

# 📂 Project Structure

```text
XRAY
│
├── assets/
│   ├── banner.png
│   ├── architecture.png
│   ├── workflow.png
│   └── demo.gif
│
├── app.py
├── config.py
├── model_loader.py
├── predictor.py
├── preprocess.py
├── style.css
├── requirements.txt
└── README.md
```

---

# ⚙ Prediction Pipeline

## 🩻 Step 1 — Upload Image

Supported formats

* JPG
* JPEG
* PNG

---

## 🤖 Step 2 — Choose Model

Select one of the available trained models:

* CNN (10 Epochs)
* CNN (20 Epochs)
* VGG16 Transfer Learning

---

## 🧹 Step 3 — Image Preprocessing

### CNN Models

```text
Input Image
      │
      ▼
Grayscale
      │
      ▼
Resize (100×100)
      │
      ▼
Normalize
      │
      ▼
Expand Dimensions

Output Shape

(1,100,100,1)
```

---

### VGG16

```text
Input Image
      │
      ▼
RGB
      │
      ▼
Resize (100×100)
      │
      ▼
preprocess_input()

Output Shape

(1,100,100,3)
```

---

## ☁ Step 4 — Automatic Model Download

Models are stored on **Hugging Face Hub**.

At the first launch:

```text
Launch App
      │
      ▼
Check Cache
      │
      ▼
Download Model
      │
      ▼
Save Locally
      │
      ▼
Load TensorFlow Model
```

Benefits:

* Smaller GitHub repository
* Faster deployments
* Version control
* Cached downloads
* Easy updates

---

## 🤖 Step 5 — Prediction

The predictor automatically detects the model output layer.

### Binary Sigmoid

```python
Dense(1, activation="sigmoid")
```

```text
Probability ≥ 0.5

↓

PNEUMONIA
```

```text
Probability < 0.5

↓

NORMAL
```

---

### Two-Class Softmax

```python
Dense(2, activation="softmax")
```

Prediction:

```python
prediction = np.argmax(probabilities)
```

This unified prediction pipeline supports both architectures without code modification.

---

# 📊 Output

The application displays

* ✅ Predicted Class
* 📈 Confidence Score
* 📊 Class Probabilities
* 🤖 Selected Model

---

# 💻 Technology Stack

| Category         | Technologies              |
| ---------------- | ------------------------- |
| Programming      | Python                    |
| Deep Learning    | TensorFlow, Keras         |
| Frontend         | Streamlit                 |
| Image Processing | Pillow, NumPy             |
| Model Hosting    | Hugging Face Hub          |
| Deployment       | Streamlit Community Cloud |

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/your_username/Chest-XRay-Pneumonia-Detection.git

cd Chest-XRay-Pneumonia-Detection
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
streamlit run app.py
```

---

# 🌍 Deployment

The project is optimized for **Streamlit Community Cloud**.

```text
GitHub Repository
        │
        ▼
Streamlit Cloud
        │
        ▼
Install Requirements
        │
        ▼
Download Models
        │
        ▼
Deploy Application
```

---

# 📈 Future Roadmap

* 🎯 Grad-CAM Visualization
* 🧠 Explainable AI (XAI)
* 📄 PDF Medical Reports
* 📦 Batch Predictions
* 📊 Model Performance Dashboard
* 🔬 Additional Architectures (ResNet, EfficientNet, DenseNet)
* 🐳 Docker Support
* ☁ CI/CD Pipeline
* 🌐 REST API

---

# 👨‍💻 Developer

## Sudheer Muthyala

**B.Tech – Electronics & Communication Engineering**

AI • Machine Learning • Deep Learning • Computer Vision

> Passionate about building intelligent healthcare applications powered by Deep Learning.

---

<div align="center">

## ⭐ Support the Project

If this repository helped you,

**Please leave a ⭐ on GitHub!**

It motivates future development and helps others discover the project.

**Happy Coding! 🚀**

</div>
