import logging
from io import BytesIO
from time import sleep
from picamera import PiCamera
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    stream = BytesIO()
    camera = PiCamera()
    camera.resolution = (1024, 768)
    camera.start_preview()
    # Camera warm-up time
    sleep(2)
    camera.capture(stream, format='jpeg')
    camera.close()
    return func.HttpResponse(stream.getvalue(), mimetype="image/jpg", status_code=200)
