# Detecção de Bordas
from PIL import Image, ImageFilter

img = Image.open("C:/Users/User/Downloads/girafa.jpg")
bordas = img.filter(ImageFilter.FIND_EDGES)
bordas.save("Teste de Bordas.jpg")
# Exibir a imagem resultante