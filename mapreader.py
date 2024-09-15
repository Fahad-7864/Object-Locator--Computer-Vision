#!/usr/bin/env python3
# This is template for your program, for you to expand with all the correct
# functionality.

import sys
import cv2
import numpy as np
import math
import numpy


# Place  file in the same directory as the develop for the
# program to work


"""This is a program that helps identify two colored objects in a given image
 and locates the position they are in on the image and outputs its x and y   
 coordinates along with its bearing as an output. this program also segments
 the image so that only the map is represented in a proper format as referenced
 in the assignment (making the image straight and presentable)
 """

""" this assignment is broken down into several sections, this will be detailed
below
  1. the image is read in via the command line
  2. the hsv values for the green background is calculated and then is 
  color segmented
  3. through the use of perspective/warp transform and finding the 
  coordinates of the edges of the map the image,a contour is drawn around
  the map and segmentation of the green background is then processed,this
  is to ensure only the map is left to perform further calculations
  4. The HSV value for the blue square is found and then color segmented
     through the use of cv2.inrange 
  5. The Midpoint of the blue square is calculated through the use of 
     the cv2 moments function, its values are stored
  6. The HSV value for the red circle is found and then color segmented
     through the use of cv2.inrange
  7. The Midpoint of the red circle is calculated through the use of 
     the cv2 moments function, its values are stored
  8. The Bearings is then calculated by using the midpoint of the blue
     square with the midpoint of the red circle
  9. The program then displays the x ,y and bearings of the two given
     objects in the image 
  """

def handleShowingStuff():
    key = cv2.waitKey(0)
    # quit if escape (27) or q (113) are pressed
    if key == 27 or key == 113:
        cv2.destroyAllWindows()
        print("quitting!")
        sys.exit(0)
        
# Define a function to show contours and wait for key press
def show_contours_and_wait(image, contours_red, contours_blue):
    # Draw and show contours on the segmented map
    red_contours_window = f"{fn} - Red Contours"
    blue_contours_window = f"{fn} - Blue Contours"
    draw_and_show_contours(image, contours_red, red_contours_window)
    draw_and_show_contours(image, contours_blue, blue_contours_window)
    
    # Wait for a key press to close the contour windows and move on
    handleShowingStuff()


def Segment_Map(Segment_Map):
        # this method is necessary in segmenting the edges of the map from
        # the the green background
        # and it cuts out any of the unnecesary parts of the image

        contours, heirarchy = cv2.findContours(Segment_Map_From_Background,\
                                    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        #list to store edges
        Edges_of_Map_Lst = []
        Maximum_Area = 0
        for i in contours:
            Area_of_Cont = cv2.contourArea(i)
            if Area_of_Cont > 800:
                peri = cv2.arcLength(i, True)
                approx = cv2.approxPolyDP(i, 0.01 * peri, True)
                #print(len(approx))
                #find the four corners of the map
                if Area_of_Cont > Maximum_Area and len(approx) == 4:
                    for i in approx:
                        i = i[0]
                        #insert the edges into a list
                        Edges_of_Map_Lst.append(i)
                        Maximum_Area = Area_of_Cont

                    x = len(Edges_of_Map_Lst)
                    if x != 4:
                        continue
                    for i in range(x):
                        """ how pixels are located in an image, 
                         the top left corner of the map is 0,0
                         the values would be displayed in the format y,x
                         bottom right would be the total 
                         dimensions of the image
                         this is calculated through the function im.shape()
                         in the assignment the dimensions of the image 
                         before any calculations
                         is 806,1435 with three channels
                         806 is the height
                         1435 is the width
                         the top right corner just displays 
                         the width so the values
                         would be 1435,0 in the top right corner of the image.
                         the bottom left corner just displays the 
                         height of the image
                         so the values would be 806,0 in the bottom left corner
                         of the image
                         in this assignment the all the corresponding edges
                         of the map must be
                         calculated in order to segment the map from the image
                         this will be done in the section below

                         there are three points in the first array
                         for the first image,
                         1216,125 is top right of the map
                         248,130 is top left of the map
                         214,702 is bottom left of the map

                         there are three points in the first array 
                         for the second image,
                         1201,44 is the top right of the image
                         268, 154 is the top left of the map
                         304, 696 is the bottom left

                         there are three points in the second array 
                         for the first image,
                         248, 130 is top left of the map
                         214,702 is bottom left of the map
                         1239, 703 is bottom right

                         there are three points in the second array 
                         for the second image,
                         268, 154 is top left of the map
                         304,696 is the bottom left
                         1274,607 is the bottom right
                         """

                        # top left and top right
                        a1, b1, = Edges_of_Map_Lst[0]
                        a2, b2 = Edges_of_Map_Lst[1]

                        # this code is influenced by by the
                        # distance formula between two points
                        # https://www.cuemath.com/geometry/distance-between-two-points/
                        space_between_first = \
                            ((a2 - a1) ** 2 + (b2 - b1) ** 2) ** (1 / 2)

                        # bottom left and bottom right
                        c1, d1, = Edges_of_Map_Lst[2]
                        c2, d2 = Edges_of_Map_Lst[3]
                        space_between_second = \
                            ((c2 - c1) ** 2 + (d2 - d1) ** 2) ** (1 / 2)

                        # list to store how far apart the edges
                        # are from each other
                        space_between_edges = []
                        space_between_edges.append(space_between_first)
                        space_between_edges.append(space_between_second)

                        # this is to find the distance between
                        # top right and bottom right
                        e1, f1, = Edges_of_Map_Lst[0]
                        e2, f2 = Edges_of_Map_Lst[3]
                        space_between_third = \
                            ((e2 - e1) ** 2 + (f2 - f1) ** 2) ** (1 / 2)

                        space_between_edges.append(space_between_third)

                        Height_of_Map = int(min(space_between_edges))
                        Width_of_Map = int(max(space_between_edges))



        Points_of_Edges = np.float32(Edges_of_Map_Lst)
        Points_Desired = np.float32([[Width_of_Map, 0], [0, 0],\
        [0, Height_of_Map], [Width_of_Map, Height_of_Map]])

        PersTransform = cv2.getPerspectiveTransform\
        (Points_of_Edges, Points_Desired)

        Segment_Map = cv2.warpPerspective\
        (im, PersTransform, (Width_of_Map, Height_of_Map))
        #this method was influenced by lecture 9
        # which explains perspective transformation
        #resources used to create this method
        #https://docs.opencv.org/4.x/da/d54/group__imgproc__transform.html
        #https://docs.opencv.org/4.x/da/d54/group__imgproc__transform.html#gaf73673a7e8e18ec6963e3774e6a94b87

        return Segment_Map


def Color_hsv_converter(img, HSV_RANGE):
    """this function is needed in order to color
     segment objects in the map.
     It converts the given image to a HSV space
     it then takes in values given by an array that contains the minimum
     and maximum values of Hue, Saturation and value and then uses the
     cv2 in range function to color segment the objects
    """
    BGR_TO_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # Huemin, Saturationmin, Valuemin,
    HSV_MIN = np.array([HSV_RANGE[0], HSV_RANGE[1], HSV_RANGE[2]])
    # HueMax, Saturationmax, ValueMax
    HSV_MAX = np.array([HSV_RANGE[3], HSV_RANGE[4], HSV_RANGE[5]])
    # it takes in the given image and the min and max values of Hue,Saturation
    # and Value
    HSVMASK = cv2.inRange(BGR_TO_HSV, HSV_MIN, HSV_MAX)

    return HSVMASK

def angle_between_points(fn, arr, arr1):
        """This function is necessary to this program as it is required
        to calculate the bearing of the Blue square to the Red circle,
        it takes in the midpoint position of the two given objects in
        the image and then finds out what the angle is, Bearings will
        always be measured clockwise from north (0 degrees), however
        the math.atan2 function calculates angles from the x axis.
        So the addition of 90 and 450 is necessary to get the correct bearing.
        This function may not be as accurate as getting a protractor and
        measuring it yourself clockwise from north however it will be
        relatively close to the value you get from measuring it manually
        (this was done via drawing a linefrom the midpoint of the two given
        objects and printing the given imagesand then using a protractor
        measure the bearing"""
        #this method is influenced by 
        #https://www.w3schools.com/python/ref_math_atan2.asp

        #x1-x
        #y1-y
        A1 = arr1[0] - arr[0]
        A2 = arr1[1] - arr[1]
        


        Degrees = math.atan2(A2,A1) /math.pi*180
        #print ("Degrees before addition",Degrees)

        if  (Degrees > 0):
            Degrees += 90
        if (Degrees<0 ):
            Degrees+= 450
        """addition by 450 is necessary to make the
        #number not negative, since atan2 calculates
        #from the east we must add 90 degrees since
        #bearings are from 90   #addition by 450 is necessary to make the
        #number not negative, since atan2 calculates
        #from the east we must add 90 degrees since
        #bearings are measured from north, we must
        also add 360 in order to make a negative number
        positive and make the presentation of the output
        more appropriate."""
        
        print(fn,"BEARING:",round(Degrees, 1))
        
        
        """
        This was how the angle was calculated before
        it used math.atan instead of math.atan2
        this is because math.atan2 takes into account
        negative signs and will help find a more 
        accurate bearing
        Degrees = math.atan(A2 / A1) / math.pi * 180
        # print ("Degrees before addition",Degrees)

        if (Degrees < 0) or (Degrees > 0):
            Degrees += 270
        else:
        """
        return Degrees

# Define a function to generate file names
def generate_file_names():
    file_names = ['develop-001.jpg', 'develop-002.jpg']
    return file_names

# Call the function if no arguments are provided
if len(sys.argv) == 1:
    sys.argv.extend(generate_file_names())
    print("No command-line arguments were provided. Using default files.")


def draw_and_show_contours(image, contours, window_name):
    # Draw all contours
    cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
    # Display the image with contours
    cv2.imshow(window_name, image)

# go over images.
for fn in sys.argv[1:]:
    print(f"Image file: {fn}")

    # Read in the image as 
    im = cv2.imread(fn)
    if im is None:
       print(f"Failed to load image {fn}")
       continue
    else:
       print(f"Loaded image {fn}, shape: {im.shape}")

    # Huemin, Saturationmin, Valuemin, HueMax, Saturationmax, ValueMax
    Dark_Green_HSV_Range = [0, 50, 0, 100, 255, 252]

    # Blue square HSV value
    # Huemin, Saturationmin, Valuemin, HueMax, Saturationmax, ValueMax
    Blue_Square_HSV_Range = [89, 100, 53, 160, 255, 255]
    #    Blue_Square_HSV_Range = [89, 122, 53, 160, 255, 255]


    #need two hsv values for red as the circle was not completly segmenting
    # with just one, this may be due to the fact that reds hue value must
    # be in the range of 0-10 and 160-179
    
    # Huemin, Saturationmin, Valuemin, HueMax, Saturationmax, ValueMax
    Red_Circle_HSV_Range = [0, 60, 40, 10, 255, 255]

    # Huemin, Saturationmin, Valuemin, HueMax, Saturationmax, ValueMax
    Red_Circle_HSV_Range2 = [160, 90, 40, 179, 255, 255]





    # Color segment the green background
    Dark_Green_mask = Color_hsv_converter(im, Dark_Green_HSV_Range)
    Segment_Map_From_Background = cv2.bitwise_not(Dark_Green_mask)
    # use function to segment the map from the background
    Segmented_Map = Segment_Map(Segment_Map_From_Background)

    # show segmented map
    segmented_map_window = f"{fn} - Segmented Map"
    #cv2.imshow(segmented_map_window, Segmented_Map)
    print("Segmented_Map shape ", Segmented_Map.shape)

    # red circle code
    # bitwise or to fit in both the hsv ranges as using one makes red circle
    redsquaremask = Color_hsv_converter(Segmented_Map, Red_Circle_HSV_Range)
    redsquaremask2 = Color_hsv_converter(Segmented_Map, Red_Circle_HSV_Range2)
    result = cv2.bitwise_or(redsquaremask, redsquaremask2)

    # potential printing
    #cv2.imshow("result", result)

    # blue square code
    bluesquaremask = Color_hsv_converter(Segmented_Map, Blue_Square_HSV_Range)

    # printing the blue square mask
    cv2.imshow("bluesquaremask",bluesquaremask)
    cv2.imshow("redsquaremask",result)
    # bluesquarebitwise = cv2.bitwise_not(bluesquaremask)
    #  zcv2.imshow("bluesquaremaskbitwise",bluesquarebitwise)



    contours_red, heirarchy = cv2.findContours(result, cv2.RETR_EXTERNAL,\
                                               cv2.CHAIN_APPROX_NONE)

    contours_blue, heirarchy = cv2.findContours(bluesquaremask,\
                               cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    Height_of_Map, Width_of_Map = Segmented_Map.shape[:2]
 # Draw and show contours on the segmented map
 
 # Debugging print for contours
    print(f"{fn} - Number of Red Contours: {len(contours_red)}")
    print(f"{fn} - Number of Blue Contours: {len(contours_blue)}")
    red_contours_window = f"{fn} - Red Contours"
    blue_contours_window = f"{fn} - Blue Contours"

  # Draw and show contours on the segmented map
    draw_and_show_contours(Segmented_Map.copy(), contours_red, "Red Contours")
    draw_and_show_contours(Segmented_Map.copy(), contours_blue, "Blue Contours")
    #cv2.waitKey(500)  # Wait 500 ms
    
    
    #show_contours_and_wait(Segmented_Map.copy(), contours_red, contours_blue)

    #this next section uses the cv2 function moments to help
    # calculate the midpoint of the given contour
    #https://docs.opencv.org/3.1.0/d3/dc0/group__imgproc__shape.html#ga556a180f43cab22649c23ada36a8a139

    #This next section is also influenced/taken from
    #https: // www.geeksforgeeks.org / python - opencv - find - center - of - contour /
    # to find the center of the an object in an image
    #x =(M10 / M00 )
    #y=( M01 / M00 )
    #calculating the midpoints of the blue square
    #and calculating the midpoint of the red circle
    for j in contours_blue:
    	for s in contours_red :
    		Moments = cv2.moments(j)
    		moments1= cv2.moments(s)
    	
    	if Moments['m00'] > 0:
            ##BLUE SQUARE midpoint calculation
                midpoint_of_x = int(Moments['m10'] / Moments['m00'])
                midpoint_of_y = int(Moments['m01'] / Moments['m00'])
                xpos = float(round(midpoint_of_x / Width_of_Map, 2))
                ypos = 1 - float(midpoint_of_y / Height_of_Map)
                ypos = round(ypos, 2)
                arr = (midpoint_of_x, midpoint_of_y)

            ###RED CIRCLE midpoint calculatuib
                midpoint_of_x1 = int(moments1['m10'] / moments1['m00'])
                midpoint_of_y1 = int(moments1['m01'] / moments1['m00'])
                xpos1 = float(round(midpoint_of_x1 / Width_of_Map, 2))
                ypos1 = 1 - float(round(midpoint_of_y1 / Height_of_Map, 2))
                arr1 = (midpoint_of_x1, midpoint_of_y1)








#   printing the values to the command line
#   this will print the x and y values with the bearing
#   of the two objects in the map
    print(fn,f"BLUE {xpos} {ypos} ")
    print(fn,f"RED {xpos1} {ypos1}")
    angle_between_points(fn, arr, arr1)


"""
This section was used to draw a line from
the blue square to the red circle
this was helpful for measuring the angles
Blue_Square = (midpoint_of_x, midpoint_of_y)
Red_Circle = (midpoint_of_x1, midpoint_of_y1)
color = (0, 0, 255)
thickness = 3
image = cv2.line(Segmented_Map, Blue_Square, Red_Circle, color, thickness)
"""

#print("mapIMG = " + str((Segmented_Map.shape)))

#used to see how many contours are in the image

#print("Number of Contours found = " + str(len(contours_blue)))
#print("Number of Contours found = " + str(len(contours_red)))

handleShowingStuff()
cv2.destroyAllWindows()
