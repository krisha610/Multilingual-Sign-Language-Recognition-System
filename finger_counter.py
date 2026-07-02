class FingerCounter:

    def count_fingers(self, landmarks):

        if not landmarks:
            return 0

        fingers = []

        # ---------------------------------
        # Determine Hand Orientation
        # ---------------------------------
        is_right_hand = landmarks[17][1] < landmarks[5][1]

        # ---------------------------------
        # Improved Thumb Detection
        # ---------------------------------
        thumb_tip_x = landmarks[4][1]
        thumb_ip_x = landmarks[3][1]

        thumb_distance = abs(thumb_tip_x - thumb_ip_x)

        if is_right_hand:
            thumb_open = (
                thumb_tip_x < thumb_ip_x and
                thumb_distance > 25
            )
        else:
            thumb_open = (
                thumb_tip_x > thumb_ip_x and
                thumb_distance > 25
            )

        fingers.append(1 if thumb_open else 0)

        # ---------------------------------
        # Index Finger
        # ---------------------------------
        fingers.append(
            1 if landmarks[8][2] < landmarks[6][2] else 0
        )

        # ---------------------------------
        # Middle Finger
        # ---------------------------------
        fingers.append(
            1 if landmarks[12][2] < landmarks[10][2] else 0
        )

        # ---------------------------------
        # Ring Finger
        # ---------------------------------
        fingers.append(
            1 if landmarks[16][2] < landmarks[14][2] else 0
        )

        # ---------------------------------
        # Pinky Finger
        # ---------------------------------
        fingers.append(
            1 if landmarks[20][2] < landmarks[18][2] else 0
        )

        count = sum(fingers)

        return count