#Realce e Ajuste de Intensidade
from PIL import Image, ImageEnhance

img = Image.open("C:/Users/User/Downloads/girafa.jpg")
# Aumentar contraste e brilho
contraste = ImageEnhance.Contrast(img).enhance(1.5)
brilho = ImageEnhance.Brightness(contraste).enhance(1.2)

brilho.save("Ajuste.jpg")
