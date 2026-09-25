# AI Gym Trainer

Intermediate-level computer-vision fitness trainer for the AI Gym & Fitness Assistant project.

## Features

- Real-time webcam pose detection with MediaPipe
- Bicep curl repetition counting
- Squat repetition counting
- Push-up repetition counting
- Basic form feedback
- Simple performance score
- Workout session history saved to JSON

## Requirements

- Windows
- Python 3.11
- Webcam

## Installation

Open PowerShell in this folder:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

If MediaPipe 1.x is already installed in the environment, remove it first:

```powershell
pip uninstall mediapipe -y
pip install -r requirements.txt
```

Verify:

```powershell
python -c "import cv2, mediapipe, numpy; print(cv2.__version__, mediapipe.__version__, numpy.__version__)"
```

## Run

```powershell
python main.py
```

### Controls

- `1` - Bicep Curl
- `2` - Squat
- `3` - Push-up
- `R` - Reset current exercise
- `Q` - Quit

## Project structure

```text
ai-gym-trainer/
├── main.py
├── pose_detector.py
├── exercises/
│   ├── base.py
│   ├── bicep_curl.py
│   ├── squat.py
│   └── pushup.py
├── utils/
│   ├── geometry.py
│   └── display.py
├── data/
│   └── workout_history.json
├── requirements.txt
└── setup.ps1
```

## How it works

```text
Webcam
  -> OpenCV frame capture
  -> MediaPipe pose landmarks
  -> Joint-angle calculation
  -> Exercise state machine
  -> Rep counter + form feedback
  -> Performance score
  -> Workout history
```

This is a rule-based computer-vision implementation rather than a custom-trained neural network. It is intentionally kept at an intermediate coding level and can later be extended with a React/FastAPI dashboard, ML-based form classification, authentication, and database storage.

## Notes

The angle thresholds are starting values, not medical or professional coaching standards. Camera position, body proportions, visibility, and exercise technique can affect detection accuracy.
