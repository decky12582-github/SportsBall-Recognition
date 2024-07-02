#!/usr/bin/python3
import jetson_inference
import jetson_utils

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filename", type=str, help="filename of the image to process")
parser.add_argument("--network", type=str, default="googlenet", help="model to use, can be:  googlenet, resnet-18, ect. (see --help for others)")
opt = parser.parse_args()
# Load the image from the disk using the loadImage function. This line will use the image name from the command line.
img = jetson_utils.loadImage(opt.filename)
# Load the recognition network as specified in the command line. 
net = jetson_inference.imageNet(opt.network)

# Now it's time to classify the image. In order to do this, you will run the imageNet.Classify() function. You will get the index of the class the image is, and the confidence.
class_idx, confidence = net.Classify(img)
# Next, get the description for the class that the image belongs to.
class_desc = net.GetClassDesc(class_idx)
# Finally, write a print statement to print out the information that you have gathered including the class index, class description, and confidence. 
# The confidence will be a decimal, so it is recommended to multiply it by 100 to get a percentage
print("image is recognized as "+ str(class_desc) +" (class #"+ str(class_idx) +") with " + str(confidence*100)+"% confidence")

