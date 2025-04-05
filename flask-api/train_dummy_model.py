# train_model.py
import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# 🔧 Dummy training data (replace with real if available)
# Format: [alignment_score, overjet, occlusion_score]
X = np.array([
    [0.02, 0.03, 10.5],
    [0.05, 0.01, 12.1],
    [0.01, 0.02, 11.3],
    [0.04, 0.04, 9.8],
    [0.03, 0.01, 13.2],
    [0.06, 0.05, 10.7]
])
y = np.array([0, 1, 0, 1, 0, 1])  # 0 = No surgery needed, 1 = Surgery recommended

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "abo_model.pkl")
print("✅ Model trained and saved as abo_model.pkl")
