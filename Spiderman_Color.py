import cv2
import numpy as np

def change_red_to_color(image, target_color):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_red1 = np.array([0, 70, 50])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 70, 50])
    upper_red2 = np.array([180, 255, 255])
    mask1 = cv2.inRange(hsv_image, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv_image, lower_red2, upper_red2)
    red_mask = cv2.bitwise_or(mask1, mask2)
    target_hsv_color = cv2.cvtColor(
        np.uint8([[target_color]]), cv2.COLOR_BGR2HSV)[0][0]

    hsv_image[:, :, 0][red_mask > 0] = target_hsv_color[0]  
    hsv_image[:, :, 1][red_mask > 0] = target_hsv_color[1] 
    final_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)
    return final_image


image = cv2.imread('Input\spiderman.jpg')
cv2.imshow('Original Image', image)

green_color = [0, 255, 0]
yellow_color = [0, 255, 255]

green_spiderman = change_red_to_color(image, green_color)
yellow_spiderman = change_red_to_color(image, yellow_color)


cv2.imshow('Green Spiderman', green_spiderman)
cv2.imwrite('Output\Green_Spiderman.jpg', green_spiderman)
cv2.imshow('Yellow Spiderman', yellow_spiderman)
cv2.imwrite('Output\Yellow_Spiderman.jpg', yellow_spiderman)
cv2.waitKey(0)
