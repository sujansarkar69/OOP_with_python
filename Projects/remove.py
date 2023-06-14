from rembg import remove
from PIL import Image
photo = input()
bgrem_photo = input()
input = Image.open(photo)
output = remove(input)
output.save(bgrem_photo)