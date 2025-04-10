# Filtros Morfológicos
from PIL import Image, ImageFilter

img = Image.open("C:/Users/User/Downloads/girafa.jpg").convert("L")  # Escala de cinza
morfologico = img.filter(ImageFilter.MinFilter(3))
morfologico.save("Morfologicos.jpg")