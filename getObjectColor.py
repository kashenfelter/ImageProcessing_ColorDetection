from myro import *
import colorsys

#picture = makePicture(r"C:\Users\Ernest\Desktop\Scribbler Robot Image Processing\test_pictures\test"+str(a)+".jpg")
#picture = compressImage(picture,4)

def compressImage(picture,ratio):
    pic = copyPicture(picture)
    picture = makePicture(getWidth(pic)/ratio,getHeight(pic)/ratio)
    for x in xrange(0,getWidth(pic),ratio):
        for y in xrange(0,getHeight(pic),ratio):
            pixel = getPixel(pic,x,y)
            setPixel(picture,x/ratio,y/ratio,getColor(pixel))
    return picture

def getObjectColor(picture,clrL,clrH):
    avg_x=0
    avg_y=0
    pxs=0
    
    for y in range(getHeight(picture)):
        for x in range(getWidth(picture)):
            pixel = getPixel(picture,x,y)
            
            RGB = [0,0,0]
            for i in xrange(3):
                if getRGB(pixel)[i] != 0:
                    RGB[i] = getRGB(pixel)[i]/255.0
                else:
                    RGB[i] = 0.0
            HSV = colorsys.rgb_to_hsv(RGB[0],RGB[1],RGB[2])
            if (clrL > clrH): #RED
                if (HSV[0] >= clrL/360.0 or HSV[0] <= clrH/360.0) and HSV[1] >= 0.5 and HSV[2] >= 0.5:
                    setColor(pixel,white)
                    avg_x=(avg_x+x)/2
                    avg_y=(avg_y+y)/2
                    pxs+=1
                else:
                    setColor(pixel,black)
            else:
                if (HSV[0] >= clrL/360.0 and HSV[0] <= clrH/360.0) and HSV[1] >= 0.5 and HSV[2] >= 0.5:
                    setColor(pixel,white)
                    avg_x=(avg_x+x)/2
                    avg_y=(avg_y+y)/2
                    pxs+=1
                else:
                    setColor(pixel,black)
    return pxs,avg_x,avg_y

def main():
    for a in range(9,10):
        p = makePicture(r"C:\Users\Ernest\Desktop\PYTHON IMAGE PROCESSING COMPARISON\testpics\p"+str(a)+".jpg")
        #getObjectColor(p,340,5) #RED
        #getObjectColor(p,270,315) #PURPLE
        getObjectColor(p,175,260) #BLUE
        savePicture(p,r"C:\Users\Ernest\Desktop\PYTHON IMAGE PROCESSING COMPARISON\testpics\p"+str(a)+"a.jpg")
    #show(p)
    
main()