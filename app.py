from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import numpy as np
import cv2

app = Flask(__name__, template_folder="templates")  
# Load model
model = tf.keras.models.load_model("pneumonia_detector.h5")
IMG_SIZE = 128

@app.route('/')
def home():
    return render_template("index.html") 
@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['image']
    image = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (IMG_SIZE, IMG_SIZE)).reshape(1, IMG_SIZE, IMG_SIZE, 1) / 255.0
    
    prediction = model.predict(image)
    result = "PNEUMONIA" if np.argmax(prediction) == 1 else "NORMAL"
    
    return jsonify({"prediction": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


