import cv2
cam = cv2.VideoCapture(0)
cam.set(3, 1920)  # video width
cam.set(4, 1080)  # video height
model = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


def borronear_caras(photo):

    caras = model.detectMultiScale(photo)

    if len(caras) != 0:
        for cara in caras:
            photo[cara[1]:cara[1]+cara[3], cara[0]:cara[0]+cara[2]] = cv2.blur(
                photo[cara[1]:cara[1]+cara[3], cara[0]:cara[0]+cara[2]], (20, 20))
        return photo
    else:
        return photo

while True:
    _, photo = cam.read()
    cv2.imshow("Caras borroneadas!", borronear_caras(photo))
    if cv2.waitKey(10) == 13:
        break

cv2.destroyAllWindows()
cam.release()
