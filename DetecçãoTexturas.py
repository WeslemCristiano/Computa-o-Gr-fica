# Detecção de Formas e Texturas

from PIL import Image, ImageFilter

img = Image.open("C:/Users/User/Downloads/girafa.jpg")
formas = img.filter(ImageFilter.CONTOUR)
formas.save("Texturas.jpg")
# Exibir a imagem resultante
# img.show()