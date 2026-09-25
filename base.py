class ExerciseBase:
    def __init__(self):
        self.reps = 0
        self.feedback = "Get into position"
        self.correct_frames = 0
        self.total_frames = 0

    def reset(self):
        self.reps = 0
        self.feedback = "Get into position"
        self.correct_frames = 0
        self.total_frames = 0

    def performance_score(self):
        if self.total_frames == 0:
            return 0
        accuracy = self.correct_frames / self.total_frames
        score = round(accuracy * 100)
        return max(0, min(100, score))
