import os
from PIL import Image


path = './photos'
secpath = './secphotos'

training_data = []
for image in os.listdir(path):
    img = Image.open(os.path.join(path,image)).convert('L')
    img.save(os.path.join(secpath,image))
