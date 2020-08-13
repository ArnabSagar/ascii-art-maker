import PIL.Image

#the ascii characters used to represent the pixels of varying intensity/brightness
ASCII_CHARS: ["@","#","S","%","?", "*", "+", ";", ":", ",","."]


#converts





#convert each pizel to greyscale:
def greyscale(image):
    grayscale_image = image.convert("L")
    return grayscale_image




#convert each pixel to an ASCII character
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
