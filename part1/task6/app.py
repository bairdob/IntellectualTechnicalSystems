import cv2 
import numpy as np

image = 255 * np.ones(shape=[512, 512, 3], dtype=np.uint8)
points = []
delta = 5

def on_left_click_add_point(event,x,y,flags,param):
    """
    по нажатию левой клавиши добавляет выводит точку в список
    """
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x,y))
        print(points)

cv2.namedWindow(winname='this_window') 
cv2.setMouseCallback('this_window', on_left_click_add_point)

while True:
    for point in points:
        x, y = point[0], point[1]
        cv2.rectangle(image, (x-delta, y-delta),(x+delta, y+delta), (255, 0, 0), 1)

    
    # по нажатию 'с' сбрасывает точки и очищается картинку
    if cv2.waitKey(99) & 0xFF == ord('c'):
        image = 255 * np.ones(shape=[512, 512, 3], dtype=np.uint8)
        points.clear()

    # по нажатию кнопки 'q' завершает приложение
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break 

    cv2.imshow('this_window', image) 

cv2.destroyAllWindows()
