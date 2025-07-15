# 🧠 Pneumonia Detection using Deep Learning on CT Scan Images

This project detects pneumonia using **CT scan images** through a Convolutional Neural Network (CNN). Unlike traditional methods that use chest X-rays, this model leverages **CT scans for deeper analysis**, making it a unique and potentially more accurate diagnostic approach. A Flask-based web interface allows users to upload CT images and receive predictions.

---

## 📁 Project Structure

```
├── .ipynb_checkpoints/                # Jupyter notebook autosaves
├── dataset/
│   └── pneumonia_dataset/            # Dataset used for training/testing
├── model/                            # Model utilities (optional)
├── templates/                        # HTML files for Flask frontend
├── app.py                            # Flask app entry point
├── confusion_matrix.png              # Confusion matrix result image
├── pneumonia_detection.ipynb         # Jupyter notebook for model training
├── pneumonia_detector.h5             # Trained model saved in Keras format
├── render.yaml                       # Deployment config file (for Render)
├── requirements.txt                  # Python package requirements
├── results.txt                       # Model training output/accuracy info
├── runtime.txt                       # Python version specification
├── README.md                         # This file
```

---

## ✅ Features

- Upload CT scan images for pneumonia prediction
- Utilizes a deep learning model trained on CT data
- Flask-based web UI for easy interaction
- Visualizes confusion matrix of predictions
- Render deployment-ready with minimal setup

---

## 🚀 Installation & Usage

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/pneumonia-detection.git
cd pneumonia-detection
```

### 2. Create a Virtual Environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask App Locally

```bash
python app.py
```

Then open `http://127.0.0.1:5000/` in your browser.

---

## 🧠 Model Info

* **Model Type**: Convolutional Neural Network (CNN)
* **Input**: CT scan images
* **Output**: Pneumonia prediction (Positive/Negative)
* **Framework**: TensorFlow & Keras
* **Trained in**: `pneumonia_detection.ipynb`
* **Model File**: `pneumonia_detector.h5`

---

## 📊 Evaluation

* Accuracy, loss, and metrics are saved in `results.txt`
* Confusion matrix visualization: `confusion_matrix.png`

---

## 🌍 Deployment (Render)

### 1. Required files:

* `render.yaml`
* `runtime.txt`
* `requirements.txt`
* `app.py`

### 2. Sample `render.yaml`

```yaml
services:
  - type: web
    name: pneumonia-detector
    env: python
    buildCommand: "pip install -r requirements.txt"
    startCommand: "python app.py"
    region: oregon
    plan: free
```

### 3. Sample `runtime.txt`

```
python-3.8.13
```

---

## ⚙️ Requirements

See `requirements.txt`, which includes:

* Flask
* TensorFlow
* Pillow
* NumPy
* Werkzeug

---

## 👨‍💻 Authors

* **Bhanu Kiran Kumar Reddy**
* **Harshitha Gubba**

---

## 📜 License

This project is licensed under the MIT License.

---

## 🌟 Show Some Love

Star this repo if you found it useful, insightful, or inspiring!
