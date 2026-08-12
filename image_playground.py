import cv2 
import numpy as np

class UploadImage:
    def __init__(self, image_path:str):
        self.image_path = image_path
        self.window_names = [
             "Blue Channel",
             "Green Channel",
             "Red Channel"
         ]
        for window_name in self.window_names:
            cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
            cv2.resizeWindow(window_name, 800, 600)


    def upload(self):
        image = cv2.imread(self.image_path)
        
        if image is None:
            raise ValueError("Image not found or unable to read the image.")
        else:
            print("Image uploaded successfully.")
            print(f"Image shape: {image.shape}") 
            return image 

    def channel_split (self):
        image = self.upload()        
        blue , green, red = cv2.split(image)
        zeros = np.zeros_like(blue)
        print(type(blue), type(green), type(red))
        cv2.imshow("Blue Channel", cv2.merge([blue, green, zeros]))
        cv2.imshow("Green Channel", cv2.merge([zeros, green, zeros]))
        cv2.imshow("Red Channel", cv2.merge([blue, zeros, red]))
        cv2.waitKey(0)
        cv2.destroyAllWindows()