import os
import glob
import cv2
import time
import warnings
import png
import matplotlib.pyplot as plt
import numpy as np
import pydicom
import IPython
from PIL import Image
from fastai2.basics import *
from fastai2.medical.imaging import *

# grab all dcm file paths
cts = glob.glob('data/brain_cts/**/*.dcm', recursive=True)

# sample print
sample = cts[99090]
dcm = pydicom.dcmread(sample)
dcm = dcm.windowed(*dicom_windows.brain)
img = dcm.numpy().astype(float)
scaled_img = cv2.convertScaleAbs(img-np.min(img), alpha=(255.0 / min(np.max(img)-np.min(img), 10000.0)))
plt.imshow(scaled_img, cmap=plt.cm.bone)
im = Image.fromarray(scaled_img)
im.save("test.png")

# convert all images to png
start = time.time()
dst_path = 'data/brain_cts/ct_pngs'
for i, path in enumerate(cts):
    dcm = pydicom.dcmread(path, force=True)
    if("PixelData" in dcm): # avoids .dcms without pixeldata that drew error
        # windowing using fastai for brain
        dcm = dcm.windowed(*dicom_windows.brain)
        img = dcm.numpy().astype(float)

        # rescaling to [0,255]
        scaled_img = cv2.convertScaleAbs(img - np.min(img), alpha=(255.0 / min(np.max(img) - np.min(img), 10000.0)))

        # replace with png
        im = Image.fromarray(scaled_img)
        name = os.path.join(dst_path, str(i) + '.png')
        im.save(name)
        print(name)
print("{} seconds elapsed.".format(time.time() - start)) # takes ~30min

