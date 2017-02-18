# importing libraries
import cv2
import glob
import os
import time
import sys
import numpy as np
from PIL import Image
import imutils
import argparse
from imutils.object_detection import non_max_suppression

# initialising variables
subject_label = 1
total_count = 0
subject_one_count = 0
font = cv2.FONT_HERSHEY_SIMPLEX
list_of_videos = []
cascade_path = "haarcascade_profileface.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


# people detection


class people:

    def detect_people(frame):
        """
        Detect Humans using HOG descriptor
        Args:
                frame:

        Returns:
                processed frame
        """
    
        rects=[]    
        rectangle=[]
        
        (rects, weights) = hog.detectMultiScale(
            frame, winStride=(4, 4), padding=(8, 8), scale=1.15)
        

        rects = non_max_suppression(rects, probs=None, overlapThresh=0.65)
        '''
        number=0        
        for (x, y, w, h) in rects:
            number=len(rects)
        
        i=0
        rects[number+1][0]=0   
        rects[number+1][1]=0           
        rects[number+1][2]=0   
        rects[number+1][3]=0   
        while i<number:
            area_rect[i]=rects[i][2]*rects[i][3]
            area_rect[i+1]=rects[i+1][2]*rects[i+1][3]
            max_rect=area_rect[i]
            j=i
            if area_rect[i+1]>area_rect[i]:
                max_rect=area_rect[i+1]
                j=i
            i=i+1
            
          ''' 
        if len(rects)!=0:

            rectangle.append(rects[0])  
        else:
            rectangle=rects
        '''
        area_rect=[]  
        for i in range(0,number):
            area_rect.append(rects[i][2]*rects[i][3])
            
        if number!=0:  
            max_rect=np.max(area_rect) 
            max_index=area_rect.index(max_rect)
            #print(max_index)
        '''
        print(rectangle)    
        for (x, y, w, h) in rectangle:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            #cv2.line(frame,(int(x+0.5*w),y),(int(x+0.5*w),int(y+h)),(0,0,255),2)
        return frame



if __name__ == '__main__':
    """
    main function
    """

    camera = cv2.VideoCapture(0)
    #camera = cv2.VideoCapture('abc.mp4')
    while True:
        starttime = time.time()
        grabbed, frame = camera.read()
        if not grabbed:
            break
        frame_orginal = imutils.resize(
            frame, width=min(500, frame.shape[1]))
        frame_orginal1 = cv2.cvtColor(
            frame_orginal, cv2.COLOR_BGR2GRAY)
        frame_processed = people.detect_people(frame_orginal1)

        
        cv2.imshow("window", frame_processed)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break
    camera.release()
    cv2.destroyAllWindows()
    endtime = time.time()
 