from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import joblib
from werkzeug.utils import secure_filename
from extract_features import extract_features  # Your STL logic

app = Flask(__name__)
CORS(app)

app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

try:
    model = joblib.load("abo_model.pkl")
except Exception as e:
    print(f"Failed to load model: {e}")
    model = None

@app.route("/")
def home():
    return "✅ Flask API for Orthodontic STL Prediction"

@app.route("/predict", methods=["POST"])
def predict():
    if "upper_file" not in request.files or "lower_file" not in request.files:
        return jsonify({"error": "Please upload both upper and lower STL files."}), 400

    upper_file = request.files["upper_file"]
    lower_file = request.files["lower_file"]

    if upper_file.filename == "" or lower_file.filename == "":
        return jsonify({"error": "One or both STL files are empty."}), 400

    upper_path = os.path.join(app.config["UPLOAD_FOLDER"], secure_filename("upper.stl"))
    lower_path = os.path.join(app.config["UPLOAD_FOLDER"], secure_filename("lower.stl"))
    upper_file.save(upper_path)
    lower_file.save(lower_path)

    try:
        features = extract_features(upper_path, lower_path)
        if model is None:
            return jsonify({"error": "Model not loaded."}), 500

        prediction = model.predict([features])
        return jsonify({
            "features": {
                "alignment_score": features[0],
                "overjet": features[1],
                "occlusion_score": features[2]
            },
            "class": int(prediction[0])
        })
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
