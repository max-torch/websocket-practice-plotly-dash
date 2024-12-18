import sounddevice as sd
import numpy as np

def get_volume(indata, frames, time, status):
    volume_norm = np.linalg.norm(indata) * 10
    print(f"Volume: {volume_norm:.2f}")  # Real-time volume output

# Stream audio from the microphone indefinitely
try:
    print("Starting microphone stream. Press Ctrl+C to stop.")
    with sd.InputStream(callback=get_volume):
        while True:  # Keep the program running
            sd.sleep(20)  # Prevent high CPU usage by sleeping briefly
except KeyboardInterrupt:
    print("\nMicrophone stream stopped.")
