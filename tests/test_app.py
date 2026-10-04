import pytest
import sys
from pathlib import Path

# Ensure project root is on Python path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.app import clean_text, predict_news


def test_clean_text_returns_string():
    """Verify clean_text returns a string instance."""
    result = clean_text("This is a sample news article text for testing.")
    assert isinstance(result, str)


def test_clean_text_url_removal():
    """Verify URLs (http and www) are removed from text."""
    input_text = "Breaking news read more at http://example.com/news or www.testsite.org for updates."
    cleaned = clean_text(input_text)
    assert "http" not in cleaned
    assert "www" not in cleaned
    assert "example.com" not in cleaned
    assert "testsite.org" not in cleaned


def test_clean_text_number_removal():
    """Verify numerical digits are stripped from text."""
    input_text = "In 2024 election there were 100 candidates and 5000 votes counted."
    cleaned = clean_text(input_text)
    assert "2024" not in cleaned
    assert "100" not in cleaned
    assert "5000" not in cleaned


def test_clean_text_html_tag_removal():
    """Verify HTML tags are removed from text."""
    input_text = "<h1>Major Update</h1> <p>The government announced new policies today.</p>"
    cleaned = clean_text(input_text)
    assert "<h1>" not in cleaned
    assert "<p>" not in cleaned
    assert "update" in cleaned


def test_predict_news_valid_class_and_confidence():
    """Verify predict_news returns valid binary prediction class (0 or 1) and confidence [0, 100]."""
    sample_article = (
        "WASHINGTON (Reuters) - The United States Senate passed a major economic bill today "
        "following weeks of bipartisan negotiations in Congress."
    )
    prediction, confidence = predict_news(sample_article)

    # Check prediction class is 0 (Fake) or 1 (Real)
    assert prediction in (0, 1)

    # Check confidence is float and within 0% to 100% range
    assert isinstance(confidence, (int, float))
    assert 0.0 <= confidence <= 100.0