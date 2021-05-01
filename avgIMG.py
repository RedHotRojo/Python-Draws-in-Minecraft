from PIL import Image
import os
files = os.listdir('C:\\Users\\Rohit\\Documents\\21w16a_textures')
f = open(f"C:\\Users\\Rohit\\Documents\\21w16a_textures\\allBlocks.txt", 'w')
for file in files:
    if file.split('.')[1] == "png":
        thisImg = Image.open(f"C:\\Users\\Rohit\\Documents\\21w16a_textures\\{file}").convert("RGBA")
        loaded = thisImg.load()
        width, height = thisImg.size
        clr = [0, 0, 0]
        for i in range(width * height):
            thisClr = loaded[i%width, int(i/width)]
            clr[0] += thisClr[0]
            clr[1] += thisClr[1]
            clr[2] += thisClr[2]
        thisImg.close()
        clr[0] /= width * height
        clr[1] /= width * height
        clr[2] /= width * height
        clr[0] = round(clr[0])
        clr[1] = round(clr[1])
        clr[2] = round(clr[2])
        f.write(f"{file.split('.')[0]}:{clr};")
f.close()