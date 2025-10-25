import cv2

# Image read karna
img = cv2.imread("C:\\Users\\udayd\\OneDrive\\Desktop\\nature.png")  # yaha tum apni file ka naam likhna

# Image show karna
cv2.imshow("Nature Image", img)
cv2.waitKey(0)  # kisi bhi key ka wait
cv2.destroyAllWindows()  # windows close kar dega
res = cv2.imwrite("D:\\Workspace\\DataScience\\OpenCVNature.png", img)  # image ko save karna
print("Image saved successfully.",res)
