import tensorflow as tf
import pathlib

path = '/home/kbuilder/.keras/datasets/flower_photos/sunflowers/14646282112_447cc7d1f9.jpg'
path = '.'

path = pathlib.Path(path)
print(path)

print(str(path/'*'))
