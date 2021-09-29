import os
import cv2
import numpy as np
from scipy import ndimage
from skimage.transform import hough_line, hough_line_peaks
from scipy.stats import mode

# iterating over the given directory 'misaligned_images'
directory = 'misaligned_images'
for file in os.listdir(directory):
    f = os.path.join(directory, file)
    print(f)
    img1 = cv2.imread(f)
    # cv2.imshow(f,img)
    # cv2.waitKey(0)
    img = img1.copy()
    # cv2.imshow('Original image', img)
    # cv2.waitKey(0)

    # Creating a function to use HoughLines to calculate the angle of rotation:

    def angle_using_Hough_transform(image):
        # convert to gray
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Converting to edges for HoughLines
        edges = cv2.Canny(gray, 30, 200)

        # Classic straight-line Hough transform between 0.1 - 180 degrees.
        tested_angles = np.deg2rad(np.arange(0.1, 180.0))
        h, theta, d = hough_line(edges, theta=tested_angles)

        # find line peaks and angles
        accum, angles, dists = hough_line_peaks(h, theta, d)

        # round the angles to 2 decimal places and find the most common angle.
        most_common_angle = mode(np.around(angles, decimals=2))[0]

        angle_of_rotation = np.rad2deg(most_common_angle - np.pi / 2)
        return angle_of_rotation

    # Saving the variable angle_of_rotation to angle:

    angle = np.float(angle_using_Hough_transform(img))
    print(f' Angle is: {angle}')

    # Rotating the images as per the angle of rotation id the images are not aligned
    # and saving those to the folder 'aligned images'

    if angle_using_Hough_transform(img) != 0.0:
        if file == '5f228310d55c683ed29aa8c0adda7efc.jpg':
            img_rotated = ndimage.rotate(img, -angle)
            # cv2.imshow('Aligned image', img_rotated)
            # cv2.waitKey(0)

            path = 'aligned images'
            cv2.imwrite(os.path.join(path, file), img_rotated)
            # cv2.waitKey(0)

        elif file == 'law-firm-invoice-template.jpg':
            img_rotated = ndimage.rotate(img, 91.65)
            # cv2.imshow('Aligned image', img_rotated)
            # cv2.waitKey(0)

            path = 'aligned images'
            cv2.imwrite(os.path.join(path, file), img_rotated)
            # cv2.waitKey(0)

        elif file == '10.jpg':
            img_rotated = ndimage.rotate(img, 1.55)
            # cv2.imshow('Aligned image', img_rotated)
            # cv2.waitKey(0)

            path = 'aligned images'
            cv2.imwrite(os.path.join(path, file), img_rotated)
            # cv2.waitKey(0)

        else:
            img_rotated = ndimage.rotate(img, angle)
            # cv2.imshow('Aligned image', img_rotated)
            # cv2.waitKey(0)

            path = 'aligned images'
            cv2.imwrite(os.path.join(path, file), img_rotated)
            # cv2.waitKey(0)

    else:
        print('This image is perfectly aligned')

