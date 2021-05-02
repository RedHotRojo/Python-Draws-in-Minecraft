"""
Only tested in Windows
Note: this file is unrequired; you can just download allBlocks.txt. This is just here to show you how I have created allBlocks.txt
Basically, it gets the average color of **almost** every block.
I got the textures from C:\Users\USER\AppData\Roaming\.minecraft\versions\21w16a\21w16a.jar (extracted the files to a folder)
I deleted textures like glass, doors, plants, the texture for the sides of texture (like crafting_table_side)
I renamed textures like crafting_table_top to crafting_table
"""
from PIL import Image # pip install pillow
import os # built-in
files = os.listdir('C:\\Users\\USER\\Documents\\textures') # This is where I stored the images that I kept
f = open(f"C:\\Users\\USER\\Documents\\textures\\allBlocks.txt", 'w') # The file where the names and colors will the stored.
for file in files: # Iterate through each png file
    if file.split('.')[1] == "png": # Make sure that non-png files are excluded
        thisImg = Image.open(f"C:\\Users\\USER\\Documents\\textures\\{file}").convert("RGBA") # Open the file and convert it to RGBA rather than the automatic RGBa (where alpha is ignored and PIL tries to calculate the color without the alpha; Their calculations are pretty bad :/ )
        loaded = thisImg.load() # Load the image
        width, height = thisImg.size # Easy access
        clr = [0, 0, 0] # Initialize color
        for i in range(width * height): # Iterate through each pixel
            thisClr = loaded[i%width, int(i/width)] # Get the pixel's color
            # Add each RGB; I think these 3 lines can be shortened to something like clr += thisClr, but I'm not entirely sure.
            clr[0] += thisClr[0]
            clr[1] += thisClr[1]
            clr[2] += thisClr[2]
        thisImg.close() # Close the image as soon as we don't need it
        # Average the colors and round them
        clr[0] /= width * height
        clr[1] /= width * height
        clr[2] /= width * height
        clr[0] = round(clr[0])
        clr[1] = round(clr[1])
        clr[2] = round(clr[2])
        f.write(f"{file.split('.')[0]}:{clr};") # Write to the file in a specific format that I understand and break up when I need to use them to draw.
f.close() # Close the file
