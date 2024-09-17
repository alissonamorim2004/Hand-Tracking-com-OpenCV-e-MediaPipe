import cv2
import mediapipe as mp

#  câmera
wCam, hCam = 1200, 400
video = cv2.VideoCapture(0)
video.set(3, wCam)
video.set(4, hCam)

# Inicializar Hands
mp_hands = mp.solutions.hands
hand = mp_hands.Hands(max_num_hands=2)
mp_draw = mp.solutions.drawing_utils

while True:
    
    check, img = video.read()
    if not check:
        break

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    results = hand.process(img_rgb)
    
    hands_points = results.multi_hand_landmarks
    h, w, _ = img.shape
    
    if hands_points:
        for hand_landmarks in hands_points:
            # Desenhar marcos das mãos e suas conexões
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Iterar sobre marcos das mãos
            for id, landmark in enumerate(hand_landmarks.landmark):
                cx, cy = int(landmark.x * w), int(landmark.y * h)
                cv2.putText(img, str(id), (cx, cy + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
    
    # Mostrar imagem com marcos desenhados
    cv2.imshow("Hand Tracking", img)
    
    # Sair do loop se a tecla 'q' for pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#captura de vídeo e fechar todas as janelas
video.release()
cv2.destroyAllWindows()
