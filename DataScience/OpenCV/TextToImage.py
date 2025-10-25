import cv2

# Create or read a black image
img = cv2.imread("C:\\Users\\udayd\\OneDrive\\Desktop\\nature.png", 1)    # Image file ka naam sahi hona chahiye

# Font select
font = cv2.FONT_HERSHEY_SIMPLEX

# Text write karna
cv2.putText(img,
            "Rays Technology",
            (10, 20),               # Text position (x, y)
            font,
            1,                      # Size
            (0, 655, 255),          # Yellow color (BGR)
            2,                      # Thickness
            cv2.LINE_AA)

# Show
cv2.imshow("Text Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save imageD:\Workspace\DataScience\OpenCV
cv2.imwrite("D:\\Workspace\\DataScience\\OpenCVoutput.jpg", img)
print("Image written successfully!")
