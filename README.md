# Face_extraction

Step 1: We will import opencv and sys for image path as arguments.
Step 2: We will import in face cascade variable a face haar cascade xml file which can be easily installed using "pip install opencv-contrib-python" which is a package that contains all haarcascade files.
Step 3: Then we will give a detectMultiScale object for faces with necessary parameters like minSize, neighbours etc.
Step 4:Then we will coordinates of the faces and draw green square boundary along the borders. Then after reducing the area of the square around face by 10% we will draw a blue line and save the cropped images as separate image files.
Step 5: Save the original file and cropped files and use transparent filters on them.
Step 6: Destroy the windows and look in the working directory for the desired outputs. 
