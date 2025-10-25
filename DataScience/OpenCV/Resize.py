import cv2

# 1️⃣ Image read karo
img = cv2.imread("C:\\Users\\udayd\\OneDrive\\Desktop\\Dog.jpg", 0)  # 1 matlab color image

if img is None:
    print("Image nahi mili. Path check karo!")
    exit()

# 2️⃣ Scale factor
scale = 60  # percentage

# 3️⃣ Resize ke liye new width aur height calculate karo
width = int(img.shape[1] * scale / 40)  # shape[1] = width
height = int(img.shape[0] * scale / 40) # shape[0] = height
dim = (width, height)

print("Initial dimensions:", img.shape)  # original size (height, width, channels)

# 4️⃣ Resize image
resized = cv2.resize(img, dim)
print("Resized dimensions:", resized.shape)

# 5️⃣ Show image
cv2.imshow("Resized Image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
