import pymupdf

def extract_text(pdf_path):
    """Extracts text from a PDF, handling potential errors."""
    try:
        doc = pymupdf.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text("text") # Explicitly get "text" output
        doc.close()  # Important: Close the document
        return text
    except FileNotFoundError:
        print(f"Error: File not found: {pdf_path}")
        return None  # Or raise the exception if you prefer
    except pymupdf.PdfError as e:
        print(f"Error reading PDF: {e}")
        return None  # Or raise the exception
    except Exception as e:  # Catch other potential errors
        print(f"An unexpected error occurred: {e}")
        return None

def clean_text(text):
    """Cleans and formats extracted text."""
    if text is None:  # Handle cases where extraction failed
        return None

    cleaned_text = text.replace('\n', ' ').replace('\r', '') # Remove newlines and carriage returns
    cleaned_text = ' '.join(cleaned_text.split()) # Normalize whitespace

    # Example of removing non-printable characters
    import re
    cleaned_text = re.sub(r'[^\x00-\x7F]+',' ', cleaned_text) #remove all non-ASCII characters

    # other cleaning logic
    #... remove headers, footers, etc. if needed

    return cleaned_text



# i wii cod from tommrow