# uarm-teleop
Web-based teleoperation of a uARM robotic manipulator. 
Project is currently on hold to migrate serial communication to JavaScript for simplicity.
Currently supports HTTP calls to move the manipulator with out a UI.

# Running
You will need Python 3 and pip, as well as a uARM Metal.
I suggest using a virtual environment but this isn't needed.
Install the dependencies with
```
pip install requirements.txt
```

Run the app with 

```
python run.py
```