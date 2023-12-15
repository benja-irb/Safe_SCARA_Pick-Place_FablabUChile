import cv2
import mediapipe as mp
dispositivoCaptura = cv2.VideoCapture(0) #variable de camara

mpManos = mp.solutions.hands # crea la matriz de puntos de una mano

#una mano por pantalla y enseña la mano con un 90% de confianza. 80% de confianza al tracking
manos = mpManos.Hands(static_image_mode = False, max_num_hands=5, min_detection_confidence = 0.7, min_tracking_confidence = 0.7) 

mpDibujar = mp.solutions.drawing_utils #dibuja la mano en pantalla

while True:
    success,img = dispositivoCaptura.read(0)

    #convertir la imagen en RGB para que mp detecte la mano
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #pasa la img de BGR a RGB

    resultado = manos.process(imgRGB)

    #hay o no hay manos
    if resultado.multi_hand_landmarks:
        for handLms in resultado.multi_hand_landmarks:
            mpDibujar.draw_landmarks(img, handLms, mpManos.HAND_CONNECTIONS) #dinuja las conexiones según la matriz de detección.
        print("Mano Detectada.")

    else:
        print("No hay hand")
    cv2.imshow("Image", img) #variable
    cv2.waitKey(1) #refresh a 1ms

