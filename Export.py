
from tkinter import *
from tkinter import ttk, font, filedialog, Entry
from tkinter.messagebox import askokcancel, showinfo, WARNING
import getpass
from PIL import ImageTk, Image
import csv
import pyautogui
import tkcap
import img2pdf
import numpy as np
import time
import pydicom as dicom
from abc import ABC,abstractmethod
from datetime import datetime

class Export(ABC):
    @abstractmethod
    def save_results(self,selfpadre,root,reportID,text1,label,proba):
        pass

class PDF(Export):
    def save_results(self,selfpadre,root,reportID,text1,label,proba):
        try:            
            now = datetime.now() 
            idFecha = now.strftime("%Y-%m-%d-%H-%M%s")
            cap = tkcap.CAP(selfpadre.root)
            ID = "./reportes/Reporte" + str(reportID) + "_" + idFecha + ".png"
            img = cap.capture(ID)
            img = Image.open(ID)
            img = img.convert("RGB")
            pdf_path = r"./reportes/Reporte" + str(reportID) + "_" + idFecha + ".pdf"
            img.save(pdf_path)
        except Exception as e:
            print(e)        

class CSV(Export):
    def save_results(self,selfpadre,root,reportID,text1,label,proba):
        with open("./reportes/historial.csv", "a") as csvfile:
            w = csv.writer(csvfile, delimiter="-")
            w.writerow(
                [text1, label, "{:.2f}".format(proba) + "%"]
            )            

class Report():
    def __init__(self,c:Export):
        self.client = c            
    
    def save_results(self,selfpadre,root,reportID,text1,label,proba):        
        self.client.save_results(selfpadre,root,reportID,text1,label,proba)

class GenerateReport():
        
    def save_results(self,selfpadre,root,reportID,text1,label,proba):                
        csvSave = Report(CSV())
        csvSave.save_results(selfpadre,root,reportID,text1,label,proba)        
        csvSave = Report(PDF())
        csvSave.save_results(selfpadre,root,reportID,text1,label,proba)
        showinfo(title="PDF", message="El PDF y el CSV fueron generados con éxito.")
            

