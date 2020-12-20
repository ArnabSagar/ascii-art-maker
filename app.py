import PIL.Image

#the ascii characters used to represent the pixels of varying intensity/brightness
ASCII_CHARS: ["@","H","$","%","?", "\"", "+", ";", ":", ",","."]


#function to resize the given image
def resize(image, newWidth=200):
    width = image.width
    height = image.height
    aspectRatio = height/width   
    newHeight = (newWidth * aspectRatio) #because we want to maintain the aspect ratio
    resizedImage = image.resize(newWidth, newHeight)
    return resizedImage


#function to convert image into greyscale
def greyscale(image):
    greyscaleImage = image.covert('L')
    return greyscaleImage


#convert each greyscale pixel to an ASCII character
def convert_to_ascii():
    pixels = image.getdata()
    



def main():
    #asking the user to enter the path to the image
    path = input("Enter pathname: \n")
    try:
        image = PIL.Image.open(path)
    except:
        print(path + "is not a valid path to the file\n")


main()
