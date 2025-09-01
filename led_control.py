import serial
import time
import sounddevice as sd
import json
import queue
from vosk import Model, KaldiRecognizer

# --------- Settings ---------
# Path to Vosk model (download from https://alphacephei.com/vosk/models ,i used vosk-model-small-en-us-0.15	)
VOSK_MODEL_DIR = "models/vosk-en"

# Change COM port to match your Arduino
SERIAL_PORT = "COM5"
BAUD_RATE = 9600
# ----------------------------


arduino = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
time.sleep(2)  

# Load Vosk model
model = Model(VOSK_MODEL_DIR)
rec = KaldiRecognizer(model, 16000)
q = queue.Queue()


def callback(indata, frames, time_info, status):
    if rec.AcceptWaveform(bytes(indata)):
        result = rec.Result()
        text = json.loads(result)["text"]
        if text:
            print("You said:", text)
            handle_command(text.lower())


def handle_command(text):
    if "light on" in text or "led on" in text:
        arduino.write(b"LED_ON\n")
        print("💡 Turning LED ON")
    elif "light off" in text or "led off" in text:
        arduino.write(b"LED_OFF\n")
        print("❌ Turning LED OFF")


def main():
    print("🎤 Say 'light on' or 'light off' to control LED")
    with sd.RawInputStream(
        samplerate=16000, blocksize=8000, dtype="int16", channels=1, callback=callback
    ):
        while True:
            pass


if __name__ == "__main__":
    main()
