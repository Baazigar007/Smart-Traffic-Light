# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 01:12:51 2019

@author: Baazigar
"""
import cv2
def counting():
    img = "C:\\Users\\Baazigar\\Desktop\\Images for project\\cars front.jpg"
    cascade_src = 'C:\\Users\\Baazigar\\Desktop\\Images for project\\opencv-samples-master\\vehicle-detection-haar\\cars3.xml'
    car_cascade = cv2.CascadeClassifier(cascade_src)
    
    img = cv2.imread(img,1)
    #img = cv2.resize(img,(16*100,9*100))
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    cars = car_cascade.detectMultiScale(gray, 1.05 ,2)
    print (len(cars))
    for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)  
        
    cv2.imshow('rectangled', img)
    cv2.waitKey(0)
    

counting()