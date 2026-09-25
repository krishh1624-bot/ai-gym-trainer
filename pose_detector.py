import cv2
import mediapipe as mp


class PoseDetector:
    def __init__(self):
        self.mp_pose = mp.solutions.pose
        self.mp_drawing = mp.solutions.drawing_utils
        self.pose = self.mp_pose.Pose(
            static_image_mode=False,
            model_complexity=1,
            smooth_landmarks=True,
            enable_segmentation=False,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5,
        )

    def process(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return self.pose.process(rgb)

    def draw(self, frame, landmarks):
        self.mp_drawing.draw_landmarks(
            frame,
            landmarks,
            self.mp_pose.POSE_CONNECTIONS,
        )

    def close(self):
        self.pose.close()
