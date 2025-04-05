import pickle

def load_model(model_path='abo_model.pkl'):
    try:
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        return model
    except Exception as e:
        print(f"Failed to load model: {e}")
        return None

def predict_abo(model, features_dict):
    if model is None:
        return {"error": "Model not loaded"}

    feature_list = [
        features_dict["alignment_score"],
        features_dict["overjet"],
        features_dict["occlusion_score"]
    ]

    prediction = model.predict([feature_list])[0]
    return {"prediction": prediction}
