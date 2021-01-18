# SM64ObjectDetection



Training Haar Cascades to recognize certain objects in Super Mario 64.

I used Cascade Trainer GUI (Version 3.3.1) (https://amin-ahmadi.com/cascade-trainer-gui) to train the cascades
1. Created positives and negatives of each object using screenshots from the game

> Positives are images that contain the object. Negatives are images that do NOT contain the object
> Positive images were cropped so that the object took up the entirety of the frame.
2. Organized the images into separate folders, titled 'P' and 'N', selected the root folder on the main screen of Cascade Trainer GUI, and began training.
3. Once training is complete, the cascade is output into a folder named 'classified' and saved as a file named 'cascade.xml'.


---
**To do:**
[ ] I'm currently working on writing a script to detect multiple objects in a single video and output the results to a seperate video file using Python and OpenCV. Progress can be viewed in the 'detect.py' file.
