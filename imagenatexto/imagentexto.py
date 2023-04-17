from PIL import Image
from deep_translator import GoogleTranslator
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'D:\Programas\Tesseract-OCR\tesseract'

img='Captura.JPG'
resultado ='texto.txt'
f=open(resultado,"a")
t=str(((pytesseract.image_to_string(Image.open(img)))))
t=t.replace('-\n', '')
f.write(t)

print(t)

translation = GoogleTranslator(source="english", target="spanish").translate(t).strip()

print(translation)

f.write(translation)

