import cv2
import mediapipe as mp


class HandTracker:
    def __init__(
        self,
        max_hands=2,
        detection_confidence=0.7,
        tracking_confidence=0.7
    ):

        self.mp_hands = mp.solutions.hands

        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=max_hands,
            min_detection_confidence=detection_confidence,
            min_tracking_confidence=tracking_confidence
        )

        self.drawer = mp.solutions.drawing_utils

    def detect_hand(self, frame):

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = self.hands.process(rgb_frame)

        all_hands = []

        if results.multi_hand_landmarks:

            h, w, _ = frame.shape

            for hand_landmarks in results.multi_hand_landmarks:

                # Draw landmarks
                self.drawer.draw_landmarks(
                    frame,
                    hand_landmarks,
                    self.mp_hands.HAND_CONNECTIONS
                )

                hand_points = []

                # Store all 21 landmarks
                for idx, lm in enumerate(hand_landmarks.landmark):

                    x = int(lm.x * w)
                    y = int(lm.y * h)

                    hand_points.append((idx, x, y))

                all_hands.append(hand_points)

        return frame, all_hands