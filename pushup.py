from exercises.base import ExerciseBase
from utils.geometry import angle, visible


class PushUp(ExerciseBase):
    """Push-up detector using elbow angle and body alignment."""

    def __init__(self):
        super().__init__()
        self.stage = "up"
        self.side = "right"

    def update(self, lm):
        shoulder = lm[12] if self.side == "right" else lm[11]
        elbow = lm[14] if self.side == "right" else lm[13]
        wrist = lm[16] if self.side == "right" else lm[15]
        hip = lm[24] if self.side == "right" else lm[23]

        self.total_frames += 1
        if not visible(shoulder, elbow, wrist, hip):
            self.feedback = "Keep your upper body in view"
            return

        elbow_angle = angle(shoulder, elbow, wrist)

        if elbow_angle > 155:
            self.stage = "up"
            self.feedback = "Good extension"
            self.correct_frames += 1
        elif elbow_angle < 90:
            if self.stage == "up":
                self.reps += 1
                self.stage = "down"
            self.feedback = "Good push-up"
            self.correct_frames += 1
        else:
            self.feedback = "Lower with control"
