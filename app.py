import PIL.Image
import collections

try:
    collectionsAbc = collections.abc
except AttributeError:
    collectionsAbc = collections

#the ascii characters used to represent the pixels of varying intensity/brightness
ASCII_CHARS = ["@","#","S","%","?", "*", "+", ";", ":", ",","."]


#function to resize the given image
def resize(image, newWidth=100):
    width = image.width
    height = image.height
    aspectRatio = height/width
    newHeight = int(newWidth * aspectRatio) #because we want to maintain the aspect ratio
    resizedImage = image.resize((newWidth, newHeight))
    return resizedImage


#function to convert image into greyscale
def greyscale(image):
    greyscaleImage = image.convert('L')
    return greyscaleImage


#convert each greyscale pixel to an ASCII character
def convertToAscii(image):
    pixels = image.getdata() #returns a list of greyscale values for each pixel in the image

    asciiList = [];
    finalString = "";

    for pixel in pixels:

        #Each pixel's data value is in range (0 to 255)
        #floor dividing by 25, because list of ascii characters is 11 in size.
        asciiList.append(ASCII_CHARS[pixel//25])
        finalString = ''.join(asciiList)
    
    return finalString



def main(newWidth = 100):
    #asking the user to enter the path to the image
    path = input("Enter pathname: \n")
    try:
        image = PIL.Image.open(path)
    except:
        print(path + "is not a valid path to the file\n")

    newImageData = convertToAscii(greyscale(resize(image)))

    totalLengthData = len(newImageData)
    finalImage = "\n".join(newImageData[i:(i+newWidth)] for i in range(0, totalLengthData, newWidth));

    print(finalImage)


main()
