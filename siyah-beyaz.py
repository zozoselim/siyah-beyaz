import cv2

# Görüntüyü yüklemek için
img = cv2.imread("gorsel1.jpg")

# Siyah beyaz hel getirmek için 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Sonucu göstermek için
cv2.imshow("Grayscale", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Sonucu kaydetmek için
cv2.imwrite("resultgorsel.jpg", gray)
