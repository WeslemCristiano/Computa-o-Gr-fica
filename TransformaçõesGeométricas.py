# Transformações Geométricas

from PIL import Image

img = Image.open("C:/Users/User/Downloads/girafa.jpg")
# Redimensionar e rotacionar
redimensionada = img.resize((img.width // 2, img.height // 2))
transformada = redimensionada.rotate(45)
transformada.save("transformada.jpg")