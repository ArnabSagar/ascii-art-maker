# ASCII ART MAKER

The following program takes a photo as an input<br/>
and then converts it to ASCII art<br/>
It does so while making use of the Python Imaging Library (PIL).  

The art maker works through the following steps:  <br/>
1. The original image is resized while maintaining the aspect ratio.  <br/>
2. The resized image is converted into greyscale.  <br/>
3. Finally, each greyscale pixel is coneveted to an ASCII character. <br/>


To run the program, use:
```
$ python3 app.py 
```
on the command line in the root folder


This will generate an img.txt file with the final art.