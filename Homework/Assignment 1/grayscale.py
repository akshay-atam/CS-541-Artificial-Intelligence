#matrix manipulation - convert color image to grayscale
#do not make changes in the function names
#do not use any inbuilt libraries and/or packages to convert image to grayscale, implement the code yourself


from PIL import Image

def to_grayscale(image):
    #Start your code implementation from here
    w, h = image.size

    # create new grayscale image
    image_gray = Image.new("L", (w, h))

    # loop through all pixels of color image
    for i in range(w):
        for j in range(h):
            # get pixel values
            R, G, B = image.getpixel((i,j))

            # convert to grayscale using the equation
            # Value = 0.2989R + 0.5870G + 0.1140B
            value = int((0.2989*R) + (0.587*G) + (0.114*B))

            # put this value in the grayscale image
            image_gray.putpixel((i,j), value)

    # save the image
    image_gray.save("outfile.jpg")

def main():
    #use the already given image only for submission
    #Load the colored image here
    #save the grayscale image as grayscale_image in same folder

    img = Image.open("colorImage.jpg")
    to_grayscale(img)

if __name__ == "__main__":
    main()
