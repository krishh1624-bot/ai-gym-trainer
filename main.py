import cv2
import json
import time
from pathlib import Path

import mediapipe as mp

from pose_detector import PoseDetector
from exercises.bicep_curl import BicepCurl
from exercises.squat import Squat
from exercises.pushup import PushUp
from utils.display import draw_panel, put_text


DATA_FILE = Path("data/workout_history.json")

EXERCISES = {
    "1": ("Bicep Curl", BicepCurl),
    "2": ("Squat", Squat),
    "3": ("Push-up", PushUp),
}


def load_history():
    if not DATA_FILE.exists():
        return []
    try:
        return json.loads(DATA_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []


def save_session(exercise, reps, score, duration):
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    history = load_history()
    history.append({
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "exercise": exercise,
        "reps": int(reps),
        "performance_score": int(score),
        "duration_seconds": round(duration, 1),
    })
    DATA_FILE.write_text(json.dumps(history, indent=2), encoding="utf-8")


def main():
    detector = PoseDetector()
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("ERROR: Could not open webcam. Check camera permissions or camera index.")
        return

    current_key = "1"
    exercise_name, exercise_class = EXERCISES[current_key]
    exercise = exercise_class()
    session_start = time.time()
    last_saved_reps = -1

    print("AI Gym Trainer started")
    print("1 = Bicep Curl | 2 = Squat | 3 = Push-up | R = Reset | Q = Quit")

    while True:
        ok, frame = cap.read()
        if not ok:
            print("ERROR: Could not read webcam frame.")
            break

        frame = cv2.flip(frame, 1)
        results = detector.process(frame)

        if results.pose_landmarks:
            exercise.update(results.pose_landmarks.landmark)
            detector.draw(frame, results.pose_landmarks)

        score = exercise.performance_score()
        draw_panel(frame, exercise_name, exercise.reps, score, exercise.feedback)
        put_text(frame, "1: Curl  2: Squat  3: Push-up  R: Reset  Q: Quit", (15, 455), 0.55)

        cv2.imshow("AI Gym Trainer", frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break

        if chr(key) in EXERCISES:
            if chr(key) != current_key:
                if exercise.reps > 0:
                    save_session(exercise_name, exercise.reps, exercise.performance_score(), time.time() - session_start)
                current_key = chr(key)
                exercise_name, exercise_class = EXERCISES[current_key]
                exercise = exercise_class()
                session_start = time.time()
                last_saved_reps = -1

        elif key == ord("r"):
            exercise.reset()
            session_start = time.time()
            last_saved_reps = -1

    if exercise.reps > 0 and exercise.reps != last_saved_reps:
        save_session(exercise_name, exercise.reps, exercise.performance_score(), time.time() - session_start)

    cap.release()
    cv2.destroyAllWindows()
    detector.close()
    print("Workout session saved. Goodbye!")


if __name__ == "__main__":
    main()
