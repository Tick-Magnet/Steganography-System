# -*- coding: utf-8 -*-
"""
@author: Jacob Bowers
"""

# We use PIL for pixel modification.
from PIL import Image


#Creates the list using the given data converted to 8-bit form using ASCII.
def generate_new_data(data):
 
        #Create new data
        generaded_data = []
 
        #Loop over Data and Converting it.
        for i in data:
            generaded_data.append(format(ord(i), '08b'))
        #print(generaded_data)
        return generaded_data
 
    
# Here we modify the Pixels
def modify_the_pixel(pxl, data):
 
    #Generate our data
    data_binary_list = generate_new_data(data)
    
    list_length = len(data_binary_list)
    
    current_point = iter(pxl)
 
    for i in range(list_length):
 
        # Pull out the three needed pixels (I.E. Red Blue or Green)
        pxl = [x for x in current_point.__next__()[:3] + current_point.__next__()[:3] + current_point.__next__()[:3]]
 
    
        # The list important pixel value must be made odd for 1's and even for the 0's
        for k in range(0, 8):
            if (data_binary_list[i][k] == '0' and pxl[k]% 2 != 0):
                pxl[k] -= 1
 
            elif (data_binary_list[i][k] == '1' and pxl[k] % 2 == 0):
                if(pxl[k] != 0):
                    pxl[k] -= 1
                else:
                    pxl[k] += 1
 
        # The Eighth pixel means that the current pixel is over and the next one must begin.
        if (i == list_length - 1):
            # The 0 means keep reading, while 1 means the message is over.
            if (pxl[-1] % 2 == 0):
                if(pxl[-1] != 0):
                    pxl[-1] -= 1
                else:
                    pxl[-1] += 1
 
        else:
            if (pxl[-1] % 2 != 0):
                pxl[-1] -= 1
 
        pxl = tuple(pxl)
        yield pxl[0:3]
        yield pxl[3:6]
        yield pxl[6:9]
 
    
 
    
def encode_enc(newimgage, data):
    w = newimgage.size[0]
    (x, y) = (0, 0)
 
    for pixel in modify_the_pixel(newimgage.getdata(), data):
 
        # Putting modified pixels in the new image
        newimgage.putpixel((x, y), pixel)
        if (x == w - 1):
            x = 0
            y += 1
        else:
            x += 1 
    
 
    
# Encode 
def encode():
    
    print("\n----- Encoder -----")
    
    print("--- Image Input ---")
    
    img = input("To encode your image, enter the desired FULL image name. \nDo NOT forget to add the extention: ")
    if (len(img) == 0):
        raise ValueError('An image is required!')    
    
    
    #PIL is required to read and write images!
    image = Image.open(img, 'r')
    
    #Used to stop data overflow.
    width, height = Image.open(img).size
    pixels = width*height
    
    #print(pixels)
    
    print("\n--- Security Check ---")
    print("A password is required.")
    password = input("Password: ")   
    if (len(password) == 0):
        raise ValueError('A Password is required!')
    if (password.find('***&&&') !=  -1):
        raise ValueError('Illegal Password')
    
    print("\n--- Encoded Data ---")
    string = input("Now enter in the data string you wish to encode: ")

    #Check if to much data is entered!
    if (len(string) > pixels):
        raise ValueError('To much data was entered!')
        
    data = password + "***&&&" + string;
    
    
    
    
    #print(data) #Testing Print!
    
    
    
    if (len(data) == 0):
        raise ValueError('Data is empty')
 
    newimgage = image.copy()
    encode_enc(newimgage, data)
    print("\n--- Create New Image ---")
    new_img_name = input("Finally, enter the name of the new image. \nDo NOT forget to add the extention: ")
    print("\n--- Encoded!!! ---\n")
    newimgage.save(new_img_name, str(new_img_name.split(".")[1].upper()))
    
    
    
 
# Main 
def main():
    user_input = int(input("--- CS 409: Steganography System Encoder --- \n"
                  "    Select one of the following options: \n\n"
                  "1: Encode\n"
                  "2: Exit\n"))
    if (user_input == 1):
        encode()
    elif (user_input == 2):
        print ('Exit:')
        raise SystemExit;
    else:
        raise Exception("Invalid input.")
 

if __name__ == '__main__' :
    main()