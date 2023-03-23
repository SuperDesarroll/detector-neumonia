from tkinter import *
from tkinter import ttk, font, filedialog, Entry
from tkinter.messagebox import askokcancel, showinfo, WARNING
from PIL import ImageTk, Image
import numpy as np
import pydicom as dicom

import cv2
from abc import ABC,abstractmethod

class RX(ABC):
    @abstractmethod
    def read_file(self,path):
        pass

class DCM(RX):
    def read_file(self,path):
        img = dicom.read_file(path)
        img_array = img.pixel_array
        img2show = Image.fromarray(img_array)
        img2 = img_array.astype(float)
        img2 = (np.maximum(img2, 0) / img2.max()) * 255.0
        img2 = np.uint8(img2)
        img_RGB = cv2.cvtColor(img2, cv2.COLOR_GRAY2RGB)
        return img_RGB, img2show

class JPGPNG(RX):
    def read_file(self,path):
        img = cv2.imread(path)
        img_array = np.asarray(img)
        img2show = Image.fromarray(img_array)
        img2 = img_array.astype(float)
        img2 = (np.maximum(img2, 0) / img2.max()) * 255.0
        img2 = np.uint8(img2)
        return img2, img2show

class RXRead():
    def __init__(self,c:RX):
        self.client = c            
    
    def read_file(self,path):        
        self.array, img2show = self.client.read_file(path)
        return self.array, img2show
    

class RXLoadFile():

    def printDato(self):
        print("ok")
        
    def load_img_file(self):
        filepath = filedialog.askopenfilename(
            initialdir="/",
            title="Select image",
            filetypes=(
                ("DICOM", "*.dcm"),
                ("JPEG", "*.jpeg"),
                ("jpg files", "*.jpg"),
                ("png files", "*.png"),
            ),
        )
        if filepath:
            if filepath.endswith("dcm"):
                dcm=DCM()
                rxLoad = RXRead(dcm)
                return rxLoad.read_file(filepath)
            else:
                jpg=JPGPNG()
                rxLoad = RXRead(jpg)
                return rxLoad.read_file(filepath)
            

