# Redução de Ruído e Suavização

from PIL import Image, ImageFilter

img = Image.open("C:/Users/User/Downloads/girafa.jpg")
suavizada = img.filter(ImageFilter.SMOOTH_MORE)
suavizada.save("RuidoSuavização.jpg")
