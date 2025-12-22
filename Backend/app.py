from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler,OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

data_store = {}

# ---------- DATASET UPLOAD ----------
@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return jsonify({"error": "No file part in request"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    allowed_extensions = (".csv", ".xlsx")

    if not file.filename.lower().endswith(allowed_extensions):
        return jsonify({
            "error": "Invalid file type. Please upload a CSV or Excel (.xlsx) file."
        }), 400

    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    try:
        df = (
            pd.read_csv(path)
            if file.filename.lower().endswith(".csv")
            else pd.read_excel(path)
        )
    except Exception:
        return jsonify({
            "error": "File could not be read. Please upload a valid CSV or Excel file."
        }), 400

    data_store["df"] = df

    return jsonify({
        "rows": df.shape[0],
        "columns": df.shape[1],
        "column_names": list(df.columns)
    })

# ---------- PREPROCESSING ----------
# @app.route("/preprocess", methods=["POST"])
# def preprocess():
#     method = request.json.get("method")
#     target = request.json.get("target")

#     df = data_store["df"]

#     X = df.drop(columns=[target])
#     y = df[target]

#     numeric_cols = X.select_dtypes(include=["int64", "float64"]).columns
#     categorical_cols = X.select_dtypes(include=["object", "category"]).columns

#     scaler = StandardScaler() if method == "standardize" else MinMaxScaler()

#     # Numeric pipeline
#     numeric_pipeline = Pipeline(steps=[
#         ("imputer", SimpleImputer(strategy="mean")),
#         ("scaler", scaler)
#     ])

#     # Categorical pipeline
#     categorical_pipeline = Pipeline(steps=[
#         ("imputer", SimpleImputer(strategy="most_frequent")),
#         ("encoder", OneHotEncoder(handle_unknown="ignore"))
#     ])

#     # Full preprocessor
#     preprocessor = ColumnTransformer(
#         transformers=[
#             ("num", numeric_pipeline, numeric_cols),
#             ("cat", categorical_pipeline, categorical_cols)
#         ]
#     )

#     # Fit + transform
#     X_processed = preprocessor.fit_transform(X)

#     data_store["X"] = X_processed
#     data_store["y"] = y.values

#     return jsonify({
#         "status": "Preprocessing applied",
#         "method": "scaler",
#         "numeric_features": list(numeric_cols),
#         "categorical_features": list(categorical_cols),
#         "final_feature_count": X_processed.shape[1]
#     })
@app.route("/preprocess", methods=["POST"])
def preprocess():
    method = request.json.get("method")   # "standardize" or "normalize"
    target = request.json.get("target")

    df = data_store["df"]
    X = df.drop(columns=[target])
    y = df[target]

    numeric_cols = X.select_dtypes(include=["int64", "float64"]).columns
    categorical_cols = X.select_dtypes(include=["object", "category"]).columns

    # Choose scaler
    if method == "standardize":
        scaler = StandardScaler()
        scaling_name = "Standardization (StandardScaler)"
    elif method == "normalize":
        scaler = MinMaxScaler()
        scaling_name = "Normalization (MinMaxScaler)"
    else:
        return jsonify({"error": "Invalid scaling method"}), 400

    # Numeric pipeline
    numeric_pipeline = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="mean")),
        ("scaler", scaler)
    ])

    # Categorical pipeline
    categorical_pipeline = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore"))
    ])

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_pipeline, numeric_cols),
            ("cat", categorical_pipeline, categorical_cols)
        ]
    )

    X_processed = preprocessor.fit_transform(X)

    data_store["X"] = X_processed
    data_store["y"] = y.values

    return jsonify({
        "status": "Preprocessing applied",
        "scaling_method": scaling_name,
        "numeric_features": list(numeric_cols),
        "categorical_features": list(categorical_cols),
        "final_feature_count": X_processed.shape[1]
    })

# ---------- TRAIN TEST SPLIT ----------
@app.route("/split", methods=["POST"])
def split():
    ratio = float(request.json.get("ratio"))
    X_train, X_test, y_train, y_test = train_test_split(
        data_store["X"], data_store["y"], test_size=1-ratio, random_state=42
    )

    data_store.update({
        "X_train": X_train,
        "X_test": X_test,
        "y_train": y_train,
        "y_test": y_test
    })

    return jsonify({"status": "Dataset split complete"})

# ---------- MODEL TRAIN ----------
# @app.route("/train", methods=["POST"])
# def train():
#     model_type = request.json.get("model")

#     if model_type == "logistic":
#         model = LogisticRegression()
#     else:
#         model = DecisionTreeClassifier()

#     model.fit(data_store["X_train"], data_store["y_train"])
#     preds = model.predict(data_store["X_test"])

#     acc = accuracy_score(data_store["y_test"], preds)
#     cm = confusion_matrix(data_store["y_test"], preds).tolist()

#     return jsonify({
#         "accuracy": acc,
#         "confusion_matrix": cm
#     })

@app.route("/train", methods=["POST"])
def train():
    model_type = request.json.get("model")

    if model_type == "logistic":
        model = LogisticRegression(max_iter=1000)
        model_name = "Logistic Regression"
    else:
        model = DecisionTreeClassifier()
        model_name = "Decision Tree Classifier"

    model.fit(data_store["X_train"], data_store["y_train"])
    preds = model.predict(data_store["X_test"])

    acc = accuracy_score(data_store["y_test"], preds)
    cm = confusion_matrix(data_store["y_test"], preds).tolist()
    class_labels = model.classes_.tolist()

    return jsonify({
        "model": model_name,
        "accuracy": acc,
        "confusion_matrix": cm,
        "class_labels": class_labels
    })

if __name__ == "__main__":
    app.run(debug=True)
