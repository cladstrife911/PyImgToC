# convert 32*32 image in C source file

from PIL import Image
import numpy as np

####################
#convert a 2D numpy array in C/h source files
def convertNumpyTableToC(numpyTable, fileName):
    print("## convertNumpyTableToC ## " , numpyTable.shape , fileName)
    f = open(fileName+".c", "w")
    fh = open(fileName+".h", "w")

    sourceHead = "const boolean cba_"+ fileName + \
                "[" + str(numpyTable.shape[0]) + "][" + str(numpyTable.shape[0]) + "];"

    fh.write("extern "+sourceHead)
    sourceHead.replace(";","={")
    #print(sourceHead)
    f.write(sourceHead)

    for x in range(0, numpyTable.shape[0]):
        f.write("\n  {")
        for y in range(0, numpyTable.shape[1]):
            if numpyTable[x,y]==0:
                # 0 is for Black color so convert to 1
                f.write("1,")
            else:
                # non Black color are considered white
                f.write("0,")            
        f.write("},")
    f.write("\n};\n")       
    return

####################
def main():
    imgpil = Image.open("test.png",'r')  
    print(imgpil.filename)
    #convert into numpy array
    img = np.array(imgpil)

    print(img.shape)
    if (img.shape[0] != 32) and (img.shape[1]!=32):
        print("error on img size.")
    else:
        print("img size ok.")

    #convert into a 2D table
    v=img[0:32,0:32,0]

    name = imgpil.filename.replace(".png","") 
    convertNumpyTableToC(v, name)

if __name__ == "__main__":
    main()