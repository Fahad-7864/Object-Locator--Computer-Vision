# Object-Locator-Computer-Vision
This Python application demonstrates advanced image processing techniques to detect and locate objects based on color within images. Using the OpenCV library, the app performs image reading, color detection using HSV range segmentation, and various transformations to enhance the image for better object identification.

## Features

- **Color Detection:** The application identifies specific colored objects within an image based on the HSV color space.
- **Perspective Warp:** It applies a perspective warp to correct image orientation, ensuring more accurate detection.
- **Contour Detection:** By using contour detection, the app isolates the targeted objects, allowing for precise identification of their position.
- **Coordinates and Bearing Calculation:** After detecting objects, the app calculates and displays the coordinates and the directional bearing between them.
  
## Technologies Used

- **Python**
- **OpenCV** for image processing

## How It Works
1. The user inputs an image.
2. The app reads the image and detects objects based on color segmentation (HSV range).
3. It then applies a perspective warp to rectify the image.
4. Contours are drawn around the detected objects.
5. The coordinates of the detected objects are calculated, and the bearing between them is determined and displayed.

## Current Configuration

The project is currently configured to detect **red** and **blue** colors using specific HSV ranges. These ranges can be modified to suit different images or target objects with different colors. You may also adjust the configuration depending on the shape of the objects you're detecting. Please note that you might need to **change these HSV values** based on the colors present in the images you are working with. 


## Image Description
![image](https://github.com/user-attachments/assets/638a85fe-90cf-4526-9eb2-f35df01d24a7)

The image above showcases the result of the Python Image Processing App in action. In the top section, we see a historical map with a green circle highlighting a detected red circle, pinpointing its position on the image space (not the actual map). Below, the processed image contains a white marker indicating the corresponding contour. This output demonstrates the app's ability to detect, isolate, and highlight objects within a complex image, based on the color segmentation techniques implemented in the project.
