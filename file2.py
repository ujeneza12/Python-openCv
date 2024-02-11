import cv2
import pytesseract

# Set the path to the Tesseract executable (change this path according to your installation)
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'


def extract_text_from_image(image_path):

    image = cv2.imread(image_path)

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    extracted_text = pytesseract.image_to_string(gray_image)

    return extracted_text

if __name__ == "__main__":
    # Path to image file
    image_path = 'pic5.png'

    extracted_text = extract_text_from_image(image_path)

    print("Extracted Text:")
    print(extracted_text)