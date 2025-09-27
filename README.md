# Görüntü İşleme ile görselleri siyah-beyaz

Bu Python kodu, yüklenen görselleri otomatik olarak siyah-beyaz hale getirir.

## Gereksinim olarak python ve opencv ihtiyaç duyulur

## Kullanım
```python
import cv2
img = cv2.imread("gorsel1.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("resultgorsel.jpg", gray)
