import cv2 
class UploadImage:
    def __init__(self, image_path:str):
        self.image_path = image_path
        cv2.namedWindow("Uploaded Image", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Uploaded Image", 800, 600)

    def upload(self):
        image = cv2.imread(self.image_path)
        
        if image is None:
            raise ValueError("Image not found or unable to read the image.")
        else:
            print("Image uploaded successfully.")
            print(f"Image shape: {image.shape}") 
            
            cv2.imshow("Uploaded Image", image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()