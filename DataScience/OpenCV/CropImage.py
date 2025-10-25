import cv2

img=cv2.imread('C:\\Users\\udayd\\OneDrive\\Desktop\\Hello.jpg')
if img is None:
    print("Image nahi mili. Path check karo!")
    exit()

# 2️⃣ Crop coordinates set karo
# y = 300   # top row
# x = 200   # left column
# h = 100   # height of crop
# w = 200   # width of crop
#
# crop = img[y:y+h, x:x+w]

cv2.imshow("Cropped Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 4️⃣ Save cropped image
cv2.imwrite("Desert_Cropped.jpg", img)
print("Cropped image saved successfully!")