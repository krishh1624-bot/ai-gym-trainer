import math


def angle(a, b, c):
    """Return angle ABC in degrees for MediaPipe landmark-like objects."""
    ba = (a.x - b.x, a.y - b.y)
    bc = (c.x - b.x, c.y - b.y)

    dot = ba[0] * bc[0] + ba[1] * bc[1]
    mag_ba = math.hypot(*ba)
    mag_bc = math.hypot(*bc)

    if mag_ba == 0 or mag_bc == 0:
        return 0.0

    value = max(-1.0, min(1.0, dot / (mag_ba * mag_bc)))
    return math.degrees(math.acos(value))


def visible(*landmarks, threshold=0.55):
    return all(getattr(point, "visibility", 1.0) >= threshold for point in landmarks)
