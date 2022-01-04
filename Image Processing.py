#############################################################################################
#This file contains some basic image processing methods with example
# The file is divided into parts , you run each part individually to see the results
# This file includes image blurring ,Sharpening, Edge Detection etc.
##############################################################################################

#Part 1
# importing opencv
import cv2
import numpy as np

# reading an image
img = cv2.imread("barbara.jpg")
#showing the image
cv2.imshow("image",img)
#waiting for the image to stay on screen where 0 means infinite time and 1000 means 1 sec.
cv2.waitKey(0)


'''
#Part 2
import cv2
import numpy as np

#reading an video
vid = cv2.VideoCapture("whistleblower.mp4")
#as video is a set of frames we have to use while loop to read all frames
while True:
    # we have one variable to check the boolean value as well as we have frame variable to read images from the video
    check_variable,frame = vid.read()
    # showing the readed frames
    cv2.imshow("video",frame)
    # using conditional statement to turn off the video display output by pressing 'q' from keyborad
    if cv2.waitKey(1) & 0XFF == ord("q"):
        break
'''
'''

#Part 3
import cv2
import numpy as np

# some important functions of opencv

# reading an image
img = cv2.imread("Lenna.png")
imgplate = cv2.imread("number plate.jpeg")

kernel = np.ones((5,5),np.uint8)

# to convert the color image into gray image
imggray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# to blur the given image
imgBlur = cv2.GaussianBlur(imggray,(7,7),0)
#to find the edges in the image
imgcanny = cv2.Canny(imgplate,450,450)

#to  change the thickness of edges detected(thicker)
imgdilation = cv2.dilate(imgcanny,kernel,iterations=1)

#to  change the thickness of edges detected(thinner)
imgeroded = cv2.erode(imgdilation,kernel,iterations=1)

cv2.imshow("gray image",imggray)
cv2.imshow("blur image",imgBlur)
cv2.imshow("edges of image",imgcanny)
cv2.imshow("dilation of image",imgdilation)
cv2.imshow("eroded image",imgeroded)

cv2.waitKey(0)
'''
'''
#Part 4
import cv2
import numpy as np

#Image Resizing and cropping

img = cv2.imread("peper.jpg")
# to print the shape of the image feeded
print(img.shape)
# to change the size of the image
imgresize = cv2.resize(img,(640,480))
print(imgresize.shape)
#cropping of the image through matrix of the image
imgcropped = img[0:150,50:350]

cv2.imshow("image",img)
cv2.imshow("resized image",imgresize)
cv2.imshow("cropped image",imgcropped)
cv2.waitKey(0)
'''
'''
#Part 5
import cv2
import numpy as np

#Shapes And Texts
# in a 512 , 512 matrix we are performing the operations
img = np.zeros((512,512,3),np.uint8)
print(img)
#first section is for height and other for width and we use this to apply color on particular section
##img[200:300,100:200] = 0,255,0

# to color the image in green
img[:] = 0,255,0
# to draw a line diagonaly on the image
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,0,255),3)
#to make a rectange on the image of respective size
cv2.rectangle(img,(0,0),(250,350),(255,0,0),3)
# to make a rectangle and fill it with the color
cv2.rectangle(img,(0,0),(225,325),(0,255,255),cv2.FILLED)
# to draw a circle and fill it with a color
cv2.circle(img,(400,50),60,(255,0,0),6)
# to make a circle and fill it with the color
cv2.circle(img,(400,50),45,(199,240,248),cv2.FILLED)

# tu put text on the images
cv2.putText(img,"hello world",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,255),2)

cv2.imshow("image",img)

cv2.waitKey(0) 
'''
'''
#Part 6
import cv2
import numpy as np


#Joining Images

img =cv2.imread("Lenna.png")
#to horizontally join the images
imghor = np.hstack((img,img))
#to vertically joim the images
imgver = np.vstack((img,img))

cv2.imshow("horizontal",imghor)
cv2.imshow("vertical",imgver)

cv2.waitKey(0)

'''