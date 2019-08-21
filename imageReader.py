import pytesseract

from PIL import Image


def imageORC(file_path):

    text = Image.open(file_path)
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    result = pytesseract.image_to_string(text)

    file = open("Output", 'w+')
    file.write(result)
    file.close()

    return result
