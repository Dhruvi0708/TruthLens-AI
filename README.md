# 📰 TruthLens AI

> An end-to-end NLP Machine Learning application that classifies **political and world news articles** as **Fake** or **Real** using **TF-IDF** and **Linear SVM**, packaged with modern software engineering practices (Automated Unit Testing, GitHub Actions CI/CD, and Docker Containerization).

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red)
![NLP](https://img.shields.io/badge/NLP-TF--IDF-green)
![pytest](https://img.shields.io/badge/pytest-5%20passed-brightgreen)
![CI/CD](https://img.shields.io/badge/GitHub%20Actions-CI-blue)
![Docker](https://img.shields.io/badge/Docker-Container-blue)

---

## 📌 Project Overview

TruthLens AI is an end-to-end Natural Language Processing (NLP) application developed to detect whether a news article is **Fake** or **Real**.

The project encompasses the complete Machine Learning & Software Engineering lifecycle:
- **Data Collection & Cleaning**: Merging political & world news datasets and removing noise.
- **Exploratory Data Analysis (EDA)**: Understanding word counts, subject distributions, and class balance.
- **Text Preprocessing**: Lowercasing, URL removal, HTML stripping, punctuation/number cleanup, stopword filtering, and lemmatization.
- **Feature Extraction & Modeling**: TF-IDF Vectorization with Linear SVM classification achieving **99.58% accuracy**.
- **Interactive UI**: Streamlit web frontend with real-time confidence scores and progress visualization.
- **Software Engineering Standards**: Automated unit tests via `pytest`, GitHub Actions CI pipeline, and Docker containerization.

---

## 🏗 System Architecture

```
                       +-----------------------------------+
                       |        User Input Article         |
                       +-----------------------------------+
                                         |
                                         v
                       +-----------------------------------+
                       |   NLP Preprocessing (clean_text)  |
                       |  - Lowercase, Regex URL/Digit     |
                       |  - Punctuation removal            |
                       |  - NLTK Stopwords & Lemmatization |
                       +-----------------------------------+
                                         |
                                         v
                       +-----------------------------------+
                       |    TF-IDF Vectorizer Transform    |
                       +-----------------------------------+
                                         |
                                         v
                       +-----------------------------------+
                       |     Linear SVM Decision Model     |
                       +-----------------------------------+
                                         |
                                         v
                       +-----------------------------------+
                       |     Prediction & Confidence %     |
                       |        (Streamlit UI Display)     |
                       +-----------------------------------+
```

---

## 🛠 Technologies Used

- **Programming Language**: Python 3.11+
- **Machine Learning & Data**: Scikit-learn, Pandas, NumPy, Joblib
- **Natural Language Processing**: NLTK (Stopwords, WordNet Lemmatizer)
- **Web Interface**: Streamlit
- **Testing**: pytest
- **CI/CD**: GitHub Actions
- **Containerization**: Docker

---

## 📂 Project Structure

```
TruthLens-AI/
├── .github/
│   └── workflows/
│       └── ci.yml               # GitHub Actions CI workflow configuration
├── app/
│   ├── __init__.py             # App package initializer
│   └── app.py                  # Streamlit web application & core NLP functions
├── data/
│   ├── Fake.csv                # Fake news dataset
│   ├── True.csv                # Real news dataset
│   ├── news_dataset.csv        # Merged dataset
│   └── clean_news_dataset.csv  # Preprocessed dataset
├── models/
│   ├── fake_news_model.pkl     # Trained Linear SVM model
│   └── tfidf_vectorizer.pkl    # Trained TF-IDF Vectorizer
├── notebook/
│   ├── 01_Data_Loading.ipynb
│   ├── 02_EDA.ipynb
│   ├── 03_Text_Preprocessing.ipynb
│   ├── 04_Model_Training.ipynb
│   └── 05_Model_Evaluation.ipynb
├── results/
│   └── model_comparison.csv    # Comparative model evaluation results
├── tests/
│   └── test_app.py             # Automated pytest unit test suite
├── .dockerignore               # Files excluded from Docker build context
├── .gitignore                  # Git ignore rules
├── Dockerfile                  # Container build instructions for deployment
├── README.md                   # Project documentation
└── requirements.txt            # Python dependencies
```

---

## 💻 Local Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Dhruvi0708/TruthLens-AI.git
cd TruthLens-AI
```

### 2. Create and Activate Virtual Environment (Optional but Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Streamlit App

Launch the interactive web application locally using Streamlit:

```bash
streamlit run app/app.py
```

Once executed, open your browser at `http://localhost:8501`.

---

## 🧪 Running Automated Unit Tests

Automated tests are written using `pytest` to verify text cleaning (URL removal, number stripping, type checking) and ML prediction pipeline behavior.

Run the test suite locally:

```bash
pytest
```

To run with verbose output:

```bash
pytest -v
```

---

## 🐳 Docker Setup & Container Execution

TruthLens-AI is fully containerized using Docker for consistent execution across environments.

### 1. Build Docker Image

```bash
docker build -t truthlens-ai .
```

### 2. Run Container

```bash
docker run -p 8501:8501 truthlens-ai
```

Access the containerized application by visiting `http://localhost:8501` in your browser.

---

## 🔄 CI/CD Pipeline & GitHub Branch Protection

### Continuous Integration (CI) Workflow

The project uses **GitHub Actions** defined in `.github/workflows/ci.yml`. On every `push` or `pull_request` targeting the `main` branch, the pipeline automatically:
1. Checks out the repository.
2. Sets up Python 3.11.
3. Installs dependencies from `requirements.txt`.
4. Runs the automated `pytest` test suite.
5. Builds the Docker image to verify containerization integrity.

### Enforcing Mandatory Passing CI Before Merging (GitHub Settings)

To prevent code from being merged into `main` when tests fail:
1. Go to your GitHub repository: `https://github.com/Dhruvi0708/TruthLens-AI`.
2. Click **Settings** > **Branches**.
3. Under **Branch protection rules**, click **Add branch protection rule** (or edit rule for `main`).
4. Set **Branch pattern name** to `main`.
5. Check **Require a pull request before merging**.
6. Check **Require status checks to pass before merging**.
7. In the search bar for status checks, search for `Run Automated Tests & Build Docker` (or `test`) and select it.
8. Click **Save changes**.

Once enabled, pull requests cannot be merged into `main` unless all `pytest` test cases and build steps succeed.

---

## 📊 Results & Model Performance

| Model | Accuracy |
|:---|:---:|
| Logistic Regression | 98.77% |
| Naive Bayes | 92.81% |
| **Linear SVM** | **99.58%** |

---

## 👩‍💻 Author

**Dhruvi Patel**  
B.Tech Computer Science Engineering  
Dronacharya College of Engineering  
*Developed as part of the IIT Jammu Summer Internship Project.*

---

## 📜 License

This project is intended for educational and research purposes.