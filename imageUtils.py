import cv2
import numpy as np
from EniPy import colors

from enum import Enum

class VerticalAlign(Enum):
    Top = 0
    Center = 1
    Bottom = 2

def getScaledImage(image, targetWidth = 1920):
    scale = targetWidth / image.shape[1]
    width = int(image.shape[1] * scale)
    height = int(image.shape[0] * scale)
    dim = (width, height)
    scaled = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    return scaled

def getBlankImage(width, height, color = colors.Black):
    blankImage = np.zeros((height, width, 3), np.uint8)
    blankImage[:] = color
    return blankImage

#
def matchHeightOrdered(input, ref, align = VerticalAlign.Center):
    heightInput = input.shape[0]
    heightRef = ref.shape[0]
    diff = heightRef - heightInput
    top = 0
    bottom = 0
    if align == VerticalAlign.Top:
        bottom = diff
    if align == VerticalAlign.Bottom:
        top = diff
    if align == VerticalAlign.Center:
        top = int(diff / 2)
        bottom = diff - top
    result = cv2.copyMakeBorder(input, top, bottom, 0, 0, cv2.BORDER_CONSTANT, value=colors.Black)
    return result

def addRight(source, right, align = VerticalAlign.Center):
    heightL = source.shape[0]
    heightR = right.shape[0]
    l = source
    r = right
    if heightL != heightR:
        if(heightR > heightL):
            l = matchHeightOrdered(source, right, align)
        else:
            r = matchHeightOrdered(right, source, align)
    result = np.hstack([l, r])
    return result