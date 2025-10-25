import cv2
import numpy as np

# 1️⃣ Image read karo
img = cv2.imread("C:\\Users\\udayd\\OneDrive\\Desktop\\Dog.jpg")

if img is None:
    print("Image nahi mili. Path check karo!")
    exit()

# 2️⃣ Image resize
img_resized = cv2.resize(img, (300, 300))

# 3️⃣ Image shape
h, w, c = img_resized.shape
print("Height:", h, "Width:", w, "Channels:", c)

# 4️⃣ Create a mask (black background, white circle)
mask = np.zeros((h, w), dtype=np.uint8)
center = (w // 2, h // 2)
radius = 100
cv2.circle(mask, center, radius, 255, -1)  # filled white circle

# 5️⃣ Apply mask to image
# Convert mask to 3 channels
mask_3ch = cv2.merge([mask, mask, mask])
circular_crop = cv2.bitwise_and(img_resized, mask_3ch)

# 6️⃣ Show circular cropped image
cv2.imshow("Circular Crop", circular_crop)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 7️⃣ Save image
cv2.imwrite("Dog_Circle_Cropped.jpg", circular_crop)
print("Circular cropped image saved successfully!")
