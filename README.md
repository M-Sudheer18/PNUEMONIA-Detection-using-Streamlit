<div align="center">

# 🩻 AI Chest X-Ray Pneumonia Detection

### *Deep Learning Powered Pneumonia Detection from Chest X-Ray Images*

<!-- Optional: Add a banner image in assets/banner.png -->
<img src="assets/banner.png" width="400"/> 

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://pnuemonia-detection-cnn-vgg.streamlit.app/)
![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange?style=for-the-badge&logo=tensorflow)
![Keras](https://img.shields.io/badge/Keras-Deep%20Learning-red?style=for-the-badge&logo=keras)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-success?style=for-the-badge&logo=streamlit)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Model%20Hub-yellow?style=for-the-badge&logo=huggingface)
![License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)

### 🚀 Detect Pneumonia from Chest X-Ray Images using Multiple Deep Learning Models

*A Deep Learning-powered web application for automatic Pneumonia detection using CNN and VGG16 models.*

### 🌐 **Live Demo**

### 👉 https://pnuemonia-detection-cnn-vgg.streamlit.app/

</div>

---

# 🌟 Overview

Chest X-Ray Pneumonia Detection is an AI-powered web application that predicts whether a Chest X-Ray image belongs to a **NORMAL** patient or one affected by **PNEUMONIA** using Deep Learning.

The application enables users to:

- 🩻 Upload Chest X-Ray images
- 🤖 Choose among multiple trained models
- ⚡ Perform real-time inference
- 📊 View prediction confidence
- 📈 Analyze class probabilities
- ☁️ Automatically download models from Hugging Face Hub
- 🚀 Access the application directly through Streamlit Cloud

---

# 🌐 Live Demo

🚀 Try the deployed application instantly:

## 🔗 https://pnuemonia-detection-cnn-vgg.streamlit.app/

### Features Available Online

- 📤 Upload Chest X-Ray images
- 🤖 Choose CNN or VGG16 model
- 📊 View prediction confidence
- 📈 Check probability distribution
- ⚡ Instant AI prediction

No installation required.

---

# 🔗 Quick Links

| Resource | Link |
|----------|------|
| 🌐 Live Application | https://pnuemonia-detection-cnn-vgg.streamlit.app/ |
| 💻 GitHub Repository | https://github.com/M-Sudheer18/PNUEMONIA-Detection-using-Streamlit |

---

# ✨ Key Features

| Feature | Description |
|---------|-------------|
| 🩻 Image Upload | Supports JPG, JPEG and PNG |
| 🤖 Multiple Models | CNN (10 Epochs), CNN (20 Epochs), VGG16 |
| ⚡ Fast Inference | Cached TensorFlow model loading |
| 📊 Confidence Score | Displays prediction confidence |
| 📈 Probability Distribution | Shows probabilities for each class |
| ☁️ Hugging Face Hub | Automatic model downloads |
| 🎨 Modern UI | Responsive Streamlit interface |
| 🚀 Cloud Ready | Deployed on Streamlit Community Cloud |

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
              📊 Confidence + Probability
                          │
                          ▼
                  ✅ Final Diagnosis
```

---

# 🧠 Deep Learning Models

| Model | Architecture | Input | Output |
|-------|-------------|-------|--------|
| CNN (10 Epochs) | Custom CNN | Grayscale | Normal / Pneumonia |
| CNN (20 Epochs) | Improved CNN | Grayscale | Normal / Pneumonia |
| VGG16 | Transfer Learning | RGB | Normal / Pneumonia |

---

# 📂 Project Structure

```text
PNUEMONIA-Detection-using-Streamlit
│
├── assets/
│   ├── banner.png
│   ├── home.png
│   ├── result.png
│   ├── architecture.png
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

# ⚙️ Prediction Pipeline

## 🩻 Step 1 — Upload Image

Supported image formats:

- JPG
- JPEG
- PNG

---

## 🤖 Step 2 — Select Model

Choose one of the following:

- CNN (10 Epochs)
- CNN (20 Epochs)
- VGG16 Transfer Learning

---

## 🧹 Step 3 — Image Preprocessing

### CNN Models

```text
Input Image
      │
      ▼
Convert to Grayscale
      │
      ▼
Resize (100×100)
      │
      ▼
Normalize
      │
      ▼
Expand Dimensions

Output Shape:
(1,100,100,1)
```

### VGG16

```text
Input Image
      │
      ▼
Convert to RGB
      │
      ▼
Resize (100×100)
      │
      ▼
preprocess_input()

Output Shape:
(1,100,100,3)
```

---

## ☁️ Model Download

Models are hosted on **Hugging Face Hub** and downloaded automatically.

```text
Launch App
      │
      ▼
Check Local Cache
      │
      ▼
Download Model
      │
      ▼
Store Locally
      │
      ▼
Load TensorFlow Model
```

### Benefits

- Smaller GitHub Repository
- Faster Deployment
- Automatic Updates
- Cached Downloads
- Easy Version Management

---

## 🤖 Prediction Logic

### Binary Sigmoid

```python
Dense(1, activation="sigmoid")
```

```text
Probability ≥ 0.5

↓

🫁 PNEUMONIA
```

```text
Probability < 0.5

↓

✅ NORMAL
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

The application automatically detects the output layer and supports both architectures without changing the prediction code.

---

# 📊 Output

The application displays:

- ✅ Predicted Class
- 📈 Confidence Score
- 📊 Class Probabilities
- 🤖 Selected Model

---

# 💻 Technology Stack

| Category | Technologies |
|----------|--------------|
| Programming | Python |
| Deep Learning | TensorFlow, Keras |
| Web Framework | Streamlit |
| Image Processing | Pillow, NumPy |
| Model Hosting | Hugging Face Hub |
| Deployment | Streamlit Community Cloud |

---

# 📸 Application Preview

> Add screenshots inside the **assets** folder.

```markdown
<p align="center">
  <img src="assets/home.png" width="900">
</p>

<p align="center">
  <img src="assets/result.png" width="900">
</p>
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/M-Sudheer18/PNUEMONIA-Detection-using-Streamlit.git

cd PNUEMONIA-Detection-using-Streamlit
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
streamlit run app.py
```

---

# ☁️ Deployment

The application is successfully deployed on **Streamlit Community Cloud**.

### 🌐 Live Application

https://pnuemonia-detection-cnn-vgg.streamlit.app/

### Deployment Workflow

```text
GitHub Repository
        │
        ▼
Streamlit Community Cloud
        │
        ▼
Install Requirements
        │
        ▼
Download Models from Hugging Face
        │
        ▼
Launch Application
```

---

# 📈 Future Roadmap

- 🎯 Grad-CAM Visualization
- 🧠 Explainable AI (XAI)
- 📄 PDF Report Generation
- 📦 Batch Image Prediction
- 📊 Model Performance Dashboard
- 🔬 ResNet, EfficientNet & DenseNet Support
- 🐳 Docker Deployment
- ☁️ CI/CD Integration
- 🌐 REST API

---

# 👨‍💻 Developer

## Sudheer Muthyala

**B.Tech – Electronics & Communication Engineering**

**Artificial Intelligence • Machine Learning • Deep Learning • Computer Vision**

> Passionate about building intelligent healthcare applications powered by Artificial Intelligence.

---

<div align="center">

## ⭐ Support the Project

If you found this project useful,

⭐ **Please Star this Repository**

🌐 **Try the Live Demo**

### https://pnuemonia-detection-cnn-vgg.streamlit.app/

Made with ❤️ by **Sudheer Muthyala**

</div>
