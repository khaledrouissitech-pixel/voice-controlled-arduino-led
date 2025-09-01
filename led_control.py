import serial
import time
import sounddevice as sd
import json
import queue
from vosk import Model, KaldiRecognizer

# --------- Settings ---------
VOSK_MODEL_DIR = r"C:\Users\KshiKamaru\Desktop\A.R.I.S\models\vosk-en"
SERIAL_PORT = "COM5"  # change this to your Arduino COM port
BAUD_RATE = 9600
# ----------------------------

# Setup serial connection
arduino = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
time.sleep(2)  # wait for Arduino to reset

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
    if "light" in text or "led on" in text:
        arduino.write(b"LED_ON\n")
        print("💡 Turning LED ON")
    elif "off" in text or "led off" in text:
        arduino.write(b"LED_OFF\n")
        print("❌ Turning LED OFF")


def main():
    print("🎤 Say 'light on' or 'light off' to control LED")
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype="int16",
                           channels=1, callback=callback):
        while True:
            pass


if __name__ == "__main__":
    main()
