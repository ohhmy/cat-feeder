from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.annotate_text_size = 100
camera.resolution = (2592, 1944)
camera.framerate = 15
#camera.brightness =50
camera.start_preview()
camera.annotate_text = "Hello world!"
#camera.image_effect = 'deinterlace2'
#camera.meter_mode = 'average'
camera.meter_mode = 'spot'
# Camera warm-up time
sleep(2)

camera.capture('foo1.jpg')
