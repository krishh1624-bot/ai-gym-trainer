# Run this script from the project folder in PowerShell.
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python -c "import cv2, mediapipe, numpy; print('Setup successful:', cv2.__version__, mediapipe.__version__, numpy.__version__)"
