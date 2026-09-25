import cv2


def put_text(frame, text, position, scale=0.7):
    cv2.putText(
        frame,
        text,
        position,
        cv2.FONT_HERSHEY_SIMPLEX,
        scale,
        (255, 255, 255),
        2,
        cv2.LINE_AA,
    )


def draw_panel(frame, exercise, reps, score, feedback):
    overlay = frame.copy()
    cv2.rectangle(overlay, (10, 10), (430, 190), (25, 25, 25), -1)
    cv2.addWeighted(overlay, 0.78, frame, 0.22, 0, frame)

    put_text(frame, "AI GYM TRAINER", (25, 42), 0.85)
    put_text(frame, f"Exercise: {exercise}", (25, 78), 0.62)
    put_text(frame, f"Reps: {reps}", (25, 112), 0.75)
    put_text(frame, f"Performance: {score}/100", (25, 146), 0.62)
    put_text(frame, f"Feedback: {feedback}", (25, 178), 0.55)
