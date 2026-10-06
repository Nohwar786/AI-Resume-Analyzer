from pypdf import PdfReader
import pymupdf
import pytesseract
from PIL import Image
import io


# Tesseract installation path
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


def extract_text_from_pdf(pdf_file):
    """
    Extract text from a PDF.

    First tries normal PDF text extraction.
    If no text is found, uses OCR on the PDF pages.
    """

    # Read the PDF bytes
    pdf_bytes = pdf_file.read()

    # ---------------------------------
    # Method 1: Normal PDF text extraction
    # ---------------------------------

    reader = PdfReader(io.BytesIO(pdf_bytes))

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    text = text.strip()

    # If normal extraction worked, return the text
    if text:
        return text

    # ---------------------------------
    # Method 2: OCR
    # ---------------------------------

    ocr_text = ""

    document = pymupdf.open(
        stream=pdf_bytes,
        filetype="pdf"
    )

    for page in document:

        # Convert PDF page to image
        pix = page.get_pixmap(
            matrix=pymupdf.Matrix(2, 2)
        )

        image_bytes = pix.tobytes("png")

        image = Image.open(
            io.BytesIO(image_bytes)
        )

        # Extract text using Tesseract
        page_text = pytesseract.image_to_string(
            image
        )

        ocr_text += page_text + "\n"

    document.close()

    return ocr_text.strip()