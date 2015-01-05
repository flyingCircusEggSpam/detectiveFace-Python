# -*- coding: utf-8 -*-

import os
import sys
import shutil
import cv2
import numpy as np

#指定のフォルダパス
folderImage_path = "srcImage/"
folderOutPutFaceImage_path = "faceImage/"
folderOutPutNoFaceImage_path = "noFaceImage/"

cascade_path = "cascade/haarcascade_frontalface_alt.xml"
color = (255, 0, 0) #赤

files = os.listdir(folderImage_path)

#フォルダ作成
def makeFolder(file):
	if os.path.exists(file) == False:
		os.mkdir(file)
#-----------------------------------------------------------

#顔認識
def detectiveFace(file):
	faceCount = 0
	image = cv2.imread(folderImage_path + file)
	image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	cascade = cv2.CascadeClassifier(cascade_path)
	facerect = cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))

	faceCount = len(facerect)
	if faceCount > 0:
	    #検出した顔を囲む矩形の作成
	    for rect in facerect:
	        cv2.rectangle(image, tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]), color, thickness=2)
	    	#認識結果の保存
	    	cv2.imwrite(folderOutPutFaceImage_path + file, image)
	else:
		cv2.imwrite(folderOutPutNoFaceImage_path + file, image)

#-----------------------------------------------------------

#------メイン関数------
if __name__ == '__main__':
	makeFolder(folderOutPutFaceImage_path)
	makeFolder(folderOutPutNoFaceImage_path)

	for file in files:
		root, ext = os.path.splitext(file)
		if ext == '.png' or ext == '.png': 
			detectiveFace(file)
			
