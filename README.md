# Sports balls identification AI
This identifies the presence of a tennis ball, soccer ball, basketball, baseball, or golf ball. It uses the Jetson Nano AI to detect. It can be used for people who are blind or can't see very well to identify that ball.

# How it works
It was custom trained on the Jetson Nano through VS Code and the resnet18 file was made on google colab. The it was trained on a dataset of all five ball types.

# How to use
Simply click the green Code button, then click download ZIP.
make sure you have jetson inference installed on your nano
unzip the file and upload them to visual studio code
start up terminal and type these commands in:
```
  $ cd my-recognition-master
```
```
  $ imagenet.py --model=resnet18.onnx --input_blob=input_0 --output_blob=output_0 --labels=labels.txt ball.jpg ballout.jpg
```
youtube video demonstration:

  https://youtu.be/4f_J2l6UEGE
