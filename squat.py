from exercises.base import ExerciseBase
from utils.geometry import angle, visible


class Squat(ExerciseBase):
    """Squat detector using hip-knee-ankle angle."""

    def __init__(self):
        super().__init__()
        self.stage = "up"
        self.side = "right"

    def update(self, lm):
        hip = lm[24] if self.side == "right" else lm[23]
        knee = lm[26] if self.side == "right" else lm[25]
        ankle = lm[28] if self.side == "right" else lm[27]

        self.total_frames += 1
        if not visible(hip, knee, ankle):
            self.feedback = "Show your full leg"
            return

        knee_angle = angle(hip, knee, ankle)

        if knee_angle > 160:
            self.stage = "up"
            self.feedback = "Stand tall"
            self.correct_frames += 1
        elif knee_angle < 100:
            if self.stage == "up":
                self.reps += 1
                self.stage = "down"
            self.feedback = "Good depth"
            self.correct_frames += 1
        else:
            self.feedback = "Go a little lower"
