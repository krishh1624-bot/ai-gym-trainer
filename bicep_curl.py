from exercises.base import ExerciseBase
from utils.geometry import angle, visible


class BicepCurl(ExerciseBase):
    """Single-arm bicep curl detector using elbow angle."""

    def __init__(self):
        super().__init__()
        self.stage = "down"
        self.side = "right"

    def update(self, lm):
        s = lm[12] if self.side == "right" else lm[11]
        e = lm[14] if self.side == "right" else lm[13]
        w = lm[16] if self.side == "right" else lm[15]

        self.total_frames += 1
        if not visible(s, e, w):
            self.feedback = "Move your arm into view"
            return

        elbow_angle = angle(s, e, w)

        if elbow_angle > 150:
            self.stage = "down"
            self.feedback = "Good extension"
            self.correct_frames += 1
        elif elbow_angle < 55:
            if self.stage == "down":
                self.reps += 1
                self.stage = "up"
            self.feedback = "Good curl"
            self.correct_frames += 1
        else:
            self.feedback = "Control the movement"
