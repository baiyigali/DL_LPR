#!/usr/bin/python
#-*- coding: UTF-8 -*-   
from libpydarknet import DarknetObjectDetector

from PIL import Image
import numpy as np
import time

class DetBBox(object):

    def __init__(self, bbox):
        self.left = bbox.left
        self.right = bbox.right
        self.top = bbox.top
        self.bottom = bbox.bottom
        self.confidence = bbox.confidence
        self.cls = bbox.cls

class Darknet_ObjectDetector():

    #做好加载
    def __init__(self, spec, weight):
        self._detector = DarknetObjectDetector(spec, weight)

    def detect_object(self, pil_image):
        start = time.time()

        data = np.array(pil_image).transpose([2,0,1]).astype(np.uint8)
	#numpy.transpose():矩阵转换操作
	#numpy.astype() :数据类型转换

	#bp::list detect_object(bp::str img_data, int img_width, int img_height, int img_channel) 返回一个装了bbox的列表
        rst = self._detector.detect_object(data.tostring(), pil_image.size[0], pil_image.size[1], 3)

        end = time.time()

        ret_rst = [DetBBox(x) for x in rst]

        return ret_rst, end-start

    @staticmethod
    def set_device(gpu_id):
        DarknetObjectDetector.set_device(gpu_id)
