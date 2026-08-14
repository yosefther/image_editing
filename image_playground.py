import cv2 
import numpy as np

class UploadImage:
    def __init__(self, image_path:str):
        self.image_path = image_path
        cv2.namedWindow("controle_window", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("controle_window", 800, 600)

        self.controle_windows = [
             "light 0.1 Channel",
             "light 0.5 Channel",
             "light 2 Channel"
         ]
        for controle_window in self.controle_windows:
            cv2.namedWindow(controle_window, cv2.WINDOW_NORMAL)
            cv2.resizeWindow(controle_window, 800, 600)


    def upload(self):
        image = cv2.imread(self.image_path)
        
        if image is None:
            raise ValueError("Image not found or unable to read the image.")
        else:
            print("Image uploaded successfully.")
            print(f"Image shape: {image.shape}")
            mshow = cv2.imshow("controle_window", image) 
            mshow = cv2.imshow("light 0.1 Channel", image *255)
            # mshow = cv2.imshow("light 0.5 Channel", image * 0.5)
            # mshow = cv2.imshow("light 2 Channel", image * 2)
                
            cv2.waitKey(0)
            cv2.destroyAllWindows()

            # return image 

