from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from hyperlpr import *
# 导入OpenCV库
import cv2
import requests
import numpy as np


def hello(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET and request.GET['q']:
        message = request.GET['q']
    else:
        return HttpResponse("q is null")

    url = message
    # resp = urllib.urlopen(url)
    # image = np.asarray(bytearray(resp.read()), dtype="uint8")

    # 读入图片
    try:
        file = requests.get(url)

        image = cv2.imdecode(np.fromstring(file.content, np.uint8), 1)
        # 识别结果
        list = HyperLPR_plate_recognition(image)
        res = list[0][0]
    except BaseException:
        res = "error"

    return HttpResponse(res)
