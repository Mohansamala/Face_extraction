import sys
import cv2
from PIL import Image
# Get user supplied values
imagePath = sys.argv[1]

#cascPath = sys.argv[2]
# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades+ 'haarcascade_frontalface_default.xml')
# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.35,
    minNeighbors=5,
    minSize=(30, 30),
    flags =0 
    #cv2.cv.CV_HAAR_SCALE_IMAGE
)
#print "Found {0} faces!".format(len(faces))

#im = Image.open("test.jpg")

crop_rectangle = (50, 50, 200, 200)
#cropped_im = im.crop(crop_rectangle)
count=0
# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    count=count+1
    windowName = None
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    x1=int(x+0.0514*w)
    y1=int(y+0.0514*h)
    x2=int(x+(w)*0.9486)
    y2=int(y+(h)*0.9486)
    cv2.rectangle(image, (x1,y1),(x2,y2),(255, 0, 0), 2)
    crop_img = image[y1:y2, x1:x2]
    cv2.imshow("cropped", crop_img)
    filename = "file_%d.jpg"%count
    cv2.imwrite(filename,crop_img)
    cv2.waitKey(0)
cv2.imshow("Faces found" ,image)
cv2.imwrite("overall.png",image)
cv2.waitKey(0)
cv2.destroyAllWindows()