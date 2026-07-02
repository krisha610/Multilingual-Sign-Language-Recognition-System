import cv2


def draw_count(frame, count):

    cv2.rectangle(frame, (20, 20), (220, 120), (0, 255, 0), -1)

    cv2.putText(
        frame,
        f'Count : {count}',
        (40, 85),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.5,
        (255, 255, 255),
        3
    )

    return frame