
import time

from rpi_ws281x import *

import argparse

#csv to work with csvfile

import csv

import time

#os to clear terminal

import os


#-------------------------------------------------------

# function to clear terminal and clearing it

LED_COUNT      = 9999     # Number of LED pixels.

LED_PIN        = 21      # GPIO pin connected to the pixels (18 uses PWM!).

#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).

LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)

LED_DMA        = 10      # DMA channel to use for generating signal (try 10)

LED_BRIGHTNESS = 255    # Set to 0 for darkest and 255 for brightest

LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

LED_STRIP = ws.SK6812_STRIP_GRBW    # the GRBW order is correct for addressing the corrosponding channels on the BTF-Lighting LED strips. The order of the GRBW letters can be rearranged to accommodate another RGBW protocol. 


# Define functions which animate LEDs in various ways.



# Define functions which animate LEDs in various ways.

def gettime():
    etime = time.time()
    ltime = time.localtime(etime)
    return (time.strftime("%Y", ltime),
            time.strftime("%m", ltime),
            time.strftime("%d", ltime),
            time.strftime("%H", ltime),
            time.strftime("%M", ltime),
            time.strftime("%S", ltime))

def getclcstr():

    etime=time.time()

    ltime= time.localtime(etime)

    tstring= time.strftime("%M")

    #sformat=str(month)+"/"+str(day)+"/"+str(year)+" "+str(hour)+":"+str(minute)

       

    return tstring



def timestart():

    etime=time.time()

    ltime= time.ctime(etime)

    

    return etime

def timestop():

    netime=time.time()

    print(etime, "- ", netime)

    dif=netime-etime

    print(dif)

class led:

    def __init__(self,r,g,b,w):

        self.r=r

        self.g=g

        self.b=b

        self.w=w

def printled(strip,i):



  print("----------------------------")

  print('| led ' + str(i) + ' r ' + str(strip[i].r) + ' g ' +str(strip[i].g) + ' b ' +str(strip[i].b) + ' w ' + str(strip[i].w) + '|')

  print("----------------------------")

 

def fillvstrip(LED_COUNT,STRIP,rfill,rfine,gfill,gfine,bfill,bfine,wfill,wfine):

    for i in range(LED_COUNT):

        STRIP[i].r =rfill;

        STRIP[i].g =gfill;

        STRIP[i].b= bfill;

        STRIP[i].w= wfill;

    rcount1,rcount2=1,1

    gcount1,gcount2=1,1

    bcount1,bcount2=1,1 

    wcount1,wcount2=1,1

    for i in range(rfine):

       if i%2!=0:

           STRIP[i-rcount2].r = rfill+1

           rcount2 +=1

       else:

            STRIP[i+int((LED_COUNT/2))-rcount1+1].r = rfill+1 

            rcount1 +=1

          

    for i in range(gfine):

       if i%2!=0:

           STRIP[i-gcount2].g = gfill+1

           gcount2 +=1

       else:

            STRIP[i+int((LED_COUNT/2))-gcount1+1].g = gfill+1 

            gcount1 +=1     

    

    for i in range(bfine):

       if i%2!=0:

           STRIP[i-bcount2].b = bfill+1

           bcount2 +=1

       else:

            STRIP[i+int((LED_COUNT/2))-bcount1+1].b = bfill+1 

            bcount1 +=1

    for i in range(wfine):

        if i % 2 != 0:

            STRIP[i - wcount2].w = wfill + 1

            wcount2 += 1

        else:

            STRIP[i + int((LED_COUNT / 2)) - wcount1 + 1].w = wfill + 1

            wcount1 += 1

            #start main



    return STRIP 

def colorWipe3(strip, vstrip):

    """Wipe color across display a pixel at a time."""

    for i in range(strip.numPixels()):

        color=Color(vstrip[i].r,vstrip[i].g,vstrip[i].b,vstrip[i].w)

       # print(i," color set to:",vstrip[i].r,vstrip[i].g,vstrip[i].b,vstrip[i].w)

        strip.setPixelColor(i, color)

    strip.show()

    #print("shown")

def colorclear(strip):

    """Wipe color across display a pixel at a time."""

    for i in range(strip.numPixels()):

        color=Color(0, 0, 0,0)

        strip.setPixelColor(i, color)

    strip.show()    

       

def clear():

    command = 'clear'

    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls

        command = 'cls'

    os.system(command)

    clear()





#funtion to report the row in which a search term in found a specific column

#inputs are csv file, the term being searched for, and the title of the row you are searching in

def search(filename,term):

    with open(filename, newline='') as csvfile:

        reader = csv.DictReader(csvfile)

        search=1  

        for row in reader:

            if row['datetime'] == term:

                print("found at ",term," ",row['crudered'],row['rfine'],row['crudegreen'],row['gfine'],row['crudeblue'],row['bfine'],row['crudewhite'],row['wfine'])

                search=0

                return (row['crudered'],row['rfine'],row['crudegreen'],row['gfine'],row['crudeblue'],row['bfine'],row['crudewhite'],row['wfine'])

  

    

# Main program logic follows:

if __name__ == '__main__':

    # Process arguments

    parser = argparse.ArgumentParser()

    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')

    args = parser.parse_args()



    # Create NeoPixel object with appropriate configuration.

    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)

    # Intialize the library (must be called once before other functions).

    strip.begin()

    rfill,rfine,gfill,gfine,bfill,bfine,wfill,wfine=0,0,0,0,0,0,0,0

    #virtual strip

    vstrip=[]

    #in range of number of lights

    vstrip = [led(0,1,2,3) for i in range(LED_COUNT)]

    vstrip = fillvstrip(LED_COUNT,vstrip,rfill,rfine,gfill,gfine,bfill,bfine,wfill,wfine)

    colorclear(strip)

    

                     

            


