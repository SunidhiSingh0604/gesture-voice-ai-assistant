
import threading
from voice.assistant import run_voice_assistant
from gesture.gesture_control import run_gesture_control

def main():
    print("Starting AI Assistant...")

    voice_thread = threading.Thread(
        target=run_voice_assistant,
        daemon=True
    )
    voice_thread.start()

    run_gesture_control()

if __name__ == "__main__":
    main()
