# 📰 TruthLens AI

> An NLP-based Machine Learning application that classifies **political and world news articles** as **Fake** or **Real** using **TF-IDF** and **Linear SVM**.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red)
![NLP](https://img.shields.io/badge/NLP-TF--IDF-green)

---

## 📌 Project Overview

TruthLens AI is an end-to-end Natural Language Processing (NLP) project developed to detect whether a **political or world news article** is **Fake** or **Real**.

The project follows the complete Machine Learning pipeline:

- Data Collection
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Text Preprocessing
- Feature Extraction using TF-IDF
- Model Training
- Model Evaluation
- Streamlit Web Application

---

## 🎯 Objectives

- Detect fake political news articles.
- Compare multiple Machine Learning algorithms.
- Build an interactive web application.
- Demonstrate an end-to-end NLP workflow.

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- NLTK
- Joblib
- Streamlit

---

## 📂 Dataset

**Dataset:** Fake and Real News Dataset

Files used:

- Fake.csv
- True.csv

The dataset primarily contains **political and world news articles**.

---

## 📊 Machine Learning Workflow

### 1. Data Loading

- Load Fake.csv
- Load True.csv
- Merge datasets
- Assign labels

---

### 2. Data Cleaning

- Remove missing values
- Remove duplicate records
- Combine title and article text
- Calculate article length

---

### 3. Exploratory Data Analysis (EDA)

- Dataset distribution
- Label distribution
- Subject distribution
- Article length analysis

---

### 4. Text Preprocessing

The following NLP preprocessing steps were applied:

- Convert text to lowercase
- Remove URLs
- Remove HTML tags
- Remove punctuation
- Remove numbers
- Remove extra spaces
- Remove stopwords
- Lemmatization

---

### 5. Feature Extraction

TF-IDF Vectorization

Maximum Features:

```
5000
```

---

### 6. Models Trained

- Logistic Regression
- Multinomial Naive Bayes
- Linear Support Vector Machine (Linear SVM)

---

## 📈 Model Performance

| Model | Accuracy |
|--------|---------:|
| Logistic Regression | 98.77% |
| Naive Bayes | 92.81% |
| **Linear SVM** | **99.58%** |

**Best Model:** Linear SVM

---

## 📁 Project Structure

```
TruthLens-AI
│
├── app
│   └── app.py
│
├── data
│   ├── Fake.csv
│   ├── True.csv
│   ├── news_dataset.csv
│   └── clean_news_dataset.csv
│
├── models
│   ├── fake_news_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── notebook
│   ├── 01_Data_Loading.ipynb
│   ├── 02_EDA.ipynb
│   ├── 03_Text_Preprocessing.ipynb
│   ├── 04_Model_Training.ipynb
│   └── 05_Model_Evaluation.ipynb
│
├── results
│   └── model_comparison.csv
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🚀 Running the Project

### Clone Repository

```bash
git clone <repository-url>
```

### Move into Project

```bash
cd TruthLens-AI
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start Streamlit

```bash
streamlit run app/app.py
```

---

## 📸 Application Features

- Interactive Streamlit Interface
- Paste complete news articles
- Detect Fake or Real News
- NLP-based preprocessing
- Linear SVM prediction
- Model information sidebar

---

## 📊 Results

The Linear SVM model achieved an accuracy of **99.58%** on the test dataset.

The application successfully classifies political and world news articles using TF-IDF feature extraction and supervised machine learning.

---

## ⚠ Limitations

- The model is trained on a dataset focused primarily on **political and world news**.
- It is **not a real-time fact-checking system**.
- Performance may decrease on articles outside the training domain (for example, technology, sports, or entertainment news).

---

## 🔮 Future Improvements

- Deep Learning (LSTM/BERT)
- Explainable AI (LIME/SHAP)
- Confidence Score
- News Source Verification
- Real-time News API Integration
- Multi-language Support

---

## 👩‍💻 Author

**Dhruvi Patel**

B.Tech Computer Science Engineering

Dronacharya College of Engineering

Developed as part of the **IIT Jammu Summer Internship Project**.

---

## 📜 License

This project is intended for **educational and research purposes**.