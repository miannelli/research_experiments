from PIL import ImageFilter, Image
from pytesseract import pytesseract
import os
import test
import time

preprocessors = [ ImageFilter.BLUR,
                  ImageFilter.SMOOTH,
                  ImageFilter.SHARPEN,
                  ImageFilter.EDGE_ENHANCE,
                  ImageFilter.SMOOTH_MORE
                ]

def timing_val(func):
  def wrapper(*arg, **kw):
    t1 = time.time()
    res = func(*arg, **kw)
    t2 = time.time()
    return (t2 - t1), res
  return wrapper

class Sensor:
  def __init__(self, name, preprocessor):
    self.name = "sensor_" + name
    self.filter = preprocessor

  def preprocess(self, image):
    return image.filter(self.filter)

  @timing_val
  def sense(self, image):
    preprocessed_image = self.preprocess(image)
    return pytesseract.image_to_string(preprocessed_image)

sensors = [Sensor(str(name), preprocessor) for (name, preprocessor) in zip(range(5), preprocessors)]
images =  [image for image in os.listdir('images') if image[-4:] in ['.jpg', '.png']]

for sensor in sensors:
  for image in images:
    stopwatch, output = sensor.sense(Image.open("images/"+image))
    with open("output/" + sensor.name + "_" + image + "_" + "output.txt", "w") as text_file:
      text_file.write(output)
      with open("images/" + image + "_benchmark.txt", "r") as benchmark_file:
        benchmark = benchmark_file.read()
        print sensor.name, image, test.log_test(output, benchmark), stopwatch




