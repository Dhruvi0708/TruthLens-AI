import streamlit as st
import joblib
import re
import string
import nltk

from pathlib import Path
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="TruthLens AI",
    page_icon="📰",
    layout="wide"
)

st.markdown("""
<style>

/* App Background */
.stApp{
    background:#f5f7fb;
}

/* Main Container */
.main{
    background-color:#f5f7fa;
}

/* Heading */
.big-font{
    font-size:42px !important;
    font-weight:700;
    color:#1e3a8a;
}

/* Subtitle */
.small-font{
    font-size:18px;
    color:#555;
}

/* Prediction Card */
.result-card{
    padding:25px;
    border-radius:18px;
    background:white;
    box-shadow:0 8px 20px rgba(0,0,0,0.12);
}

/* Text Area */
textarea{
    border-radius:15px !important;
    border:2px solid #2563eb !important;
    font-size:17px !important;
}

/* Button */
.stButton > button{
    width:100%;
    height:55px;
    border-radius:12px;
    border:none;
    background:linear-gradient(90deg,#2563eb,#1d4ed8);
    color:white;
    font-size:18px;
    font-weight:bold;
}

.stButton > button:hover{
    background:linear-gradient(90deg,#1d4ed8,#1e40af);
}

/* Metric Cards */
div[data-testid="metric-container"]{
    background:white;
    border-radius:15px;
    padding:20px;
    box-shadow:0 6px 15px rgba(0,0,0,.12);
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:#ffffff;
}

/* Success Box */
.stSuccess{
    border-radius:15px;
}

/* Error Box */
.stError{
    border-radius:15px;
}

/* Info Box */
.stInfo{
    border-radius:15px;
}

/* Warning Box */
.stWarning{
    border-radius:15px;
}

@keyframes fadeIn{
    from{
        opacity:0;
        transform:translateY(20px);
    }
    to{
        opacity:1;
        transform:translateY(0);
    }
}

@keyframes shake{
    0%{transform:translateX(0);}
    20%{transform:translateX(-8px);}
    40%{transform:translateX(8px);}
    60%{transform:translateX(-8px);}
    80%{transform:translateX(8px);}
    100%{transform:translateX(0);}
}


</style>
""", unsafe_allow_html=True)

# -----------------------------
# Download NLTK Resources
# -----------------------------
nltk.download("stopwords", quiet=True)
nltk.download("wordnet", quiet=True)
nltk.download("omw-1.4", quiet=True)

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

# -----------------------------
# Load Model & Vectorizer
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "fake_news_model.pkl"
VECTORIZER_PATH = BASE_DIR / "models" / "tfidf_vectorizer.pkl"

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

# -----------------------------
# Text Cleaning Function
# -----------------------------
def clean_text(text):

    text = text.lower()

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)

    # Remove HTML tags
    text = re.sub(r"<.*?>", "", text)

    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Remove numbers
    text = re.sub(r"\d+", "", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    # Tokenize
    words = text.split()

    # Remove stopwords + Lemmatization
    words = [
        lemmatizer.lemmatize(word)
        for word in words
        if word not in stop_words
    ]

    return " ".join(words)

# -----------------------------
# Prediction Function
# -----------------------------
import math

import math

def predict_news(text):

    cleaned_text = clean_text(text)

    text_vector = vectorizer.transform([cleaned_text])

    prediction = model.predict(text_vector)[0]

    score = model.decision_function(text_vector)[0]

    confidence = 1 / (1 + math.exp(-abs(score)))
    confidence = confidence * 100

    return prediction, confidence

# -----------------------------
# User Interface
# -----------------------------


st.markdown("""
<div style="
background:linear-gradient(135deg,#2563eb,#1e40af);
padding:40px;
width:100%;
border-radius:20px;
text-align:center;
color:white;
box-shadow:0px 10px 25px rgba(0,0,0,0.2);
margin-bottom:25px;
">

<h1 style="font-size:48px;margin-bottom:10px;">
📰 TruthLens AI
</h1>

<h3 style="margin-top:0;">
AI-Powered Fake News Detection
</h3>

<p style="font-size:18px;">
Detect whether a news article is <b>Real</b> or <b>Fake</b> using
Natural Language Processing (NLP) and Machine Learning.
</p>

</div>
""", unsafe_allow_html=True)

st.info(
    "📌 Paste a complete political or world news article below and click **Analyze Article**."
)

news_text = st.text_area(
    "Paste News Article",
    height=250,
    placeholder="Paste the complete news article here..."
)

st.markdown("""
<style>
div.stButton > button{
    background: linear-gradient(90deg,#2563eb,#1e40af);
    color:white;
    font-size:20px;
    font-weight:bold;
    border:none;
    border-radius:12px;
    height:55px;
}

div.stButton > button:hover{
    background: linear-gradient(90deg,#1e40af,#1d4ed8);
    color:white;
}
</style>
""", unsafe_allow_html=True)

if st.button(
    "🔍 Analyze Article",
    use_container_width=True
):

    if news_text.strip() == "":
        st.warning("Please enter a news article.")

    else:

        prediction, confidence = predict_news(news_text)

        st.markdown("---")

        if prediction == 1:

            st.markdown("""
                <div style="
                background:linear-gradient(135deg,#22c55e,#16a34a);
                padding:25px;
                border-radius:18px;
                text-align:center;
                color:white;
                font-size:34px;
                font-weight:bold;
                box-shadow:0px 10px 25px rgba(34,197,94,0.4);
                margin-bottom:20px;
                ">
                ✅ REAL NEWS
                </div>
                """, unsafe_allow_html=True)

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    label="Prediction",
                    value="Real News"
                )

            with col2:
                st.metric(
                    label="Confidence",
                    value=f"{confidence:.2f}%"
                )

            with col3:
                st.metric(
                    label="Model",
                    value="Linear SVM"
                )

            st.progress(min(confidence / 100, 1.0))

            st.balloons()

        else:

            st.markdown("""
                <div style="
                background:linear-gradient(135deg,#ef4444,#b91c1c);
                padding:25px;
                border-radius:18px;
                text-align:center;
                color:white;
                font-size:34px;
                font-weight:bold;
                box-shadow:0px 10px 25px rgba(239,68,68,0.45);
                margin-bottom:20px;
                ">
                ❌ FAKE NEWS
                </div>
                """, unsafe_allow_html=True)

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    label="Prediction",
                    value="Fake News"
                )

            with col2:
                st.metric(
                    label="Confidence",
                    value=f"{confidence:.2f}%"
                )

            with col3:
                st.metric(
                    label="Model",
                    value="Linear SVM"
                )

            st.progress(min(confidence / 100, 1.0))

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("📊 Model Information")

st.sidebar.write("**Model:** Linear SVM")
st.sidebar.write("**Accuracy:** 99.58%")
st.sidebar.write("**Vectorizer:** TF-IDF")
st.sidebar.write("**Dataset:** Fake & Real News Dataset")

st.sidebar.markdown("---")

st.sidebar.write("### Technologies Used")

st.sidebar.write("✅ Python")
st.sidebar.write("✅ Scikit-learn")
st.sidebar.write("✅ NLP")
st.sidebar.write("✅ Streamlit")

st.markdown("---")
st.markdown("---")

st.markdown(
"""
<center>

Made with ❤️ using Python, NLP, Scikit-learn & Streamlit

</center>
""",
unsafe_allow_html=True
)

st.caption(
"Developed by Dhruvi Patel | IIT Jammu Summer Internship Project"
)