# tests/test_preprocessing.py
import pytest
from src.preprocessing import extract_text, clean_text

def test_extract_text():
    text = extract_text("data/sample.pdf")
    assert isinstance(text, str)
    assert len(text) > 0

def test_clean_text():
    text = "  This is a test.  \n\n"
    cleaned_text = clean_text(text)
    assert cleaned_text == "This is a test."