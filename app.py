import cv2
import time
from gtts import gTTS
import threading
import pygame
import os

from gtts import gTTS

from utils.language_data import LANGUAGE_MAP, LANGUAGE_CODES
from models.hand_tracker import HandTracker
from utils.finger_counter import FingerCounter


# -----------------------------------
# Speech Function
# -----------------------------------
def speak(text):

    def run():
        try:
            language_code = LANGUAGE_CODES[selected_language]

            filename = "voice.mp3"

            tts = gTTS(
                text=text,
                lang=language_code,
                slow=False
            )

            tts.save(filename)

            pygame.mixer.init()

            pygame.mixer.music.load(filename)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                continue

            pygame.mixer.quit()

            if os.path.exists(filename):
                os.remove(filename)

        except Exception as e:
            print("Voice Error:", e)

    threading.Thread(
        target=run,
        daemon=True
    ).start()


# -----------------------------------
# Camera Initialization
# -----------------------------------
cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)


# -----------------------------------
# Hand Tracker
# -----------------------------------
tracker = HandTracker(
    max_hands=2,
    detection_confidence=0.7,
    tracking_confidence=0.7
)

counter = FingerCounter()
selected_language = "English"


# -----------------------------------
# Voice Mapping
# -----------------------------------
speech_map = {
    0: "Zero",
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    10: "Ten"
}


gesture_names = {
    0: "Closed Fist",
    1: "One Finger",
    2: "Two Fingers",
    3: "Three Fingers",
    4: "Four Fingers",
    5: "Open Palm",
    6: "Six Fingers",
    7: "Seven Fingers",
    8: "Eight Fingers",
    9: "Nine Fingers",
    10: "Ten Fingers"
}


# -----------------------------------
# Variables
# -----------------------------------
last_spoken_count = -1
last_speech_time = 0
speech_delay = 1.0

stable_count = -1
stable_start_time = time.time()
required_stable_time = 0.8

p_time = 0


# -----------------------------------
# Main Loop
# -----------------------------------
while True:

    success, frame = cap.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    # Detect hands
    frame, hands = tracker.detect_hand(frame)

    # Count fingers from all hands
    total_count = 0

    for hand in hands:
        total_count += counter.count_fingers(hand)

    count = total_count

    # -------------------------------
    # Gesture Stabilization
    # -------------------------------
    if count != stable_count:
        stable_count = count
        stable_start_time = time.time()

    current_time = time.time()

    # Speak after gesture is stable
    if (
        len(hands) > 0 and
        count == stable_count and
        current_time - stable_start_time > required_stable_time and
        count != last_spoken_count and
        current_time - last_speech_time > speech_delay
    ):

        spoken_text = LANGUAGE_MAP[selected_language][count]
        speak(spoken_text)

        last_spoken_count = count
        last_speech_time = current_time

    # -------------------------------
    # Gesture Name
    # -------------------------------
    gesture = gesture_names.get(count, "Unknown")

    # -------------------------------
    # FPS Calculation
    # -------------------------------
    c_time = time.time()

    fps = 1 / (c_time - p_time) if p_time != 0 else 0

    p_time = c_time

    # -------------------------------
    # UI Panel
    # -------------------------------
    overlay = frame.copy()

    cv2.rectangle(
    overlay,
    (20, 20),
    (520, 360),
    (40, 40, 40),
    -1
    )

    frame = cv2.addWeighted(
        overlay,
        0.75,
        frame,
        0.25,
        0
    )

    # Title
    cv2.putText(
    frame,
    f"Language : {selected_language}",
    (40, 280),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.8,
    (0, 255, 255),
    2
    )

    # Finger Count
    cv2.putText(
    frame,
    "1-EN  2-HI  3-GU  4-MR  5-FR",
    (40, 320),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.7,
    (255, 255, 255),
    2
    )

    # Gesture
    cv2.putText(
        frame,
        f"Gesture : {gesture}",
        (40, 145),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    # Hands Detected
    cv2.putText(
        frame,
        f"Hands Detected : {len(hands)}",
        (40, 190),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2
    )

    # Voice Output
    cv2.putText(
        frame,
        f"Voice : {speech_map.get(last_spoken_count, '-')}",
        (40, 235),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 200, 0),
        2
    )

    # FPS
    cv2.putText(
        frame,
        f"FPS : {int(fps)}",
        (1100, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 0),
        2
    )

    # Exit Message
    cv2.putText(
        frame,
        "Press Q to Exit",
        (1030, 690),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 255),
        2
    )

    # Show Window
    cv2.imshow(
        "Real-Time Hand Gesture Recognition",
        frame
    )

    # Exit Condition
    key = cv2.waitKey(1) & 0xFF

    if key == ord("1"):
        selected_language = "English"

    elif key == ord("2"):
        selected_language = "Hindi"

    elif key == ord("3"):
        selected_language = "Gujarati"

    elif key == ord("4"):
        selected_language = "Marathi"

    elif key == ord("5"):
        selected_language = "French"

    elif key == ord("q"):
        break    


# -----------------------------------
# Cleanup
# -----------------------------------
cap.release()
cv2.destroyAllWindows()