#  No-Code ML Pipeline Builder

A web-based **No-Code Machine Learning Pipeline Builder** that allows users to create, run, and understand a complete ML workflow **without writing any code**.

The application provides a **step-by-step guided interface** inspired by tools like *Orange Data Mining*, making machine learning accessible to beginners and non-technical users.

---

##  Key Features

-  Upload datasets in **CSV** or **Excel (.xlsx)** format  
-  Automatic data preprocessing  
  - Missing value handling  
  - Feature scaling (Standardization / Normalization)  
  - Categorical feature encoding  
-  Train–Test Split (70–30, 80–20)  
-  Model selection  
  - Logistic Regression  
  - Decision Tree Classifier  
-  Clear and interpretable results  
  - Accuracy score  
  - Confusion matrix with meaningful class labels  
-  Step-based UI (each step appears only after the previous step is completed)

---

##  Tech Stack

### Backend
- Python  
- Flask  
- Pandas  
- Scikit-learn  

### Frontend
- Vue.js (Vue 3)  
- Axios  
- HTML / CSS  

---

##  Application Workflow

Upload Dataset
↓
Data Preprocessing
↓
Train–Test Split
↓
Model Selection
↓
Results & Evaluation

##  How to Run the Application

###  Backend Setup (Flask)

```bash
cd backend
pip install -r requirements.txt
python app.py

Backend will run at:
http://localhost:5000
```

###  Frontend Setup (Vue)
```bash
cd frontend
npm install
npm run dev

Frontend will run at:
http://localhost:5173
```
