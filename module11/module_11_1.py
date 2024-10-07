# pillow
from PIL import Image

with Image.open('pict1.jpg') as image:
    image = image.rotate(120, expand=True)
    image = image.transpose(method=Image.Transpose.FLIP_TOP_BOTTOM)
    image = image.resize((1024, 640))
    image.save('pict(1024x640).png')

# numpy
import numpy as np

a = np.arange(5, 14, 2)
b = np.arange(1, 6)
c = a + b
c = c * 2
print('массив c:', c)

# requests
from pprint import pprint

import requests

r = requests.get('http://api.weatherapi.com/v1/current.json',
                 params={'key': '1967e86f09c84c419db124846240710',
                         'q': 'Moscow',
                         'lang': 'ru'})
pprint(r.json())
