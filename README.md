# 🚀 ML Model Deployment with FastAPI

## 📌 Overview

This project demonstrates the complete workflow of building a Machine Learning model and deploying it as an API. It covers data preprocessing, model training, serialization, API development, and testing.

---

## 🛠️ Tech Stack

* Python 🐍
* Pandas 📊
* Scikit-learn 🤖
* FastAPI ⚡
* Uvicorn 🌐
* Pydantic 🧠
* Pickle 📦
* Postman 🔗

---

## 📂 Project Workflow

### 1. Data Collection & Preprocessing

* Dataset sourced from Kaggle 📂
* Loaded using Pandas
* Features (X) and target (y) separated

### 2. Train-Test Split

* Used `train_test_split`
* Test size: 0.2
* Random state: 0

### 3. Model Training & Evaluation

* Model trained using Scikit-learn
* Achieved accuracy: **0.997** 🎯

### 4. Model Serialization

* Model saved using Pickle
* Exported as `.pkl` file for reuse

### 5. Input Validation

* Used Pydantic to define input schema
* Ensures structured and validated API input

### 6. API Development

* Built API using FastAPI
* Created POST endpoint for predictions
* Served using Uvicorn

### 7. API Testing

* Tested endpoints using Postman
* Verified HTTP request/response functionality ✅

---

## ⚠️ Common Mistake & Fix

**Mistake:**
Used `dict()` with Pydantic v2

**Fix:**
Use `model_dump()` instead

```python
# ❌ Incorrect (Pydantic v2)
data = request.dict()

# ✅ Correct
data = request.model_dump()
```

---

## ▶️ How to Run

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run FastAPI Server

```bash
uvicorn main:app --reload
```

### 3. Test API

* Open Postman
* Send POST request to:

```
http://127.0.0.1:8000/predict
```

---

## 📌 Key Learnings

* End-to-end ML workflow 🧩
* Model deployment using FastAPI ⚡
* API testing and validation 🔗
* Handling Pydantic v2 changes 🧠

---

## 📈 Future Improvements

* Add Docker support 🐳
* Deploy to cloud (AWS/GCP/Azure) ☁️
* Add frontend interface 🎨
* Improve model performance 🔍

---

## 🙌 Conclusion

This project provides practical experience in deploying a Machine Learning model into a production-ready API.

---

## 📬 Contact

Feel free to connect and collaborate! 🚀
