# -*- coding: utf-8 -*-
"""
@author: Jacob Bowers
"""

# PIL extracts pixels for modification.
from PIL import Image

# Decode 
def decode():
    print("\n----- Decoder -----")
    img = input("To decode your image, enter the desired FULL image name. \nDo NOT forget to add the extention: ")
    image = Image.open(img, 'r')
 
    data = ''
    imgdata = iter(image.getdata())
 
    while (True):
        pixels = [value for value in imgdata.__next__()[:3] +
                                imgdata.__next__()[:3] +
                                imgdata.__next__()[:3]]
 
        # string of binary data
        binary_string = ''
    
        for i in pixels[:8]:
            if (i % 2 == 0):
                binary_string += '0'
            else:
                binary_string += '1'
 
        data += chr(int(binary_string, 2))
        if (pixels[-1] % 2 != 0):
          
            password, string = data.split('***&&&') 
            print("\n--- Security Check ---")
            password_check = input("Please Enter the Secret Password:")
          
            if (password == password_check):
                print("The password you entered was correct.")
                print("\n--- Decoding!!! ---\n")
                return string
            else:
                print ("The password you entered was incorrect. \nThis program WILL NOW terminate.")
                raise SystemExit;
            
  
# Main 
def main():
    user_input = int(input("--- CS 409: Steganography System Decoder --- \n"
                  "    Select one of the following options: \n\n"
                  "1: Decode\n"
                  "2: Exit\n"))
    if (user_input == 1):
        print("Decoded Information:  " + decode())
    elif (user_input == 2):
        raise SystemExit;
    else:
        raise Exception("Invalid input.")
 

if __name__ == '__main__' :
    main()