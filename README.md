# 🎤 Voice-Controlled Arduino LED

Control an Arduino LED using **voice commands** with Python and [Vosk](https://alphacephei.com/vosk/) speech recognition.  
Works **completely offline** — no internet required! 🌐🚫

---

## ✨ Features

- 🎙 **Say "light on"** → LED turns **ON** 💡  
- 🎙 **Say "light off"** → LED turns **OFF** ❌  
- 🔌 Works with Arduino via serial connection  
- 🖥 Uses offline speech recognition (Vosk)

---

## 🛠 Requirements

- Python **3.8+**
- Arduino (UNO or compatible) with an LED connected
- Installed Python libraries:
  ```bash
  pip install vosk sounddevice pyserial
  ```

---

## 🚀 Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/khaledrouissitech-pixel/voice-controlled-arduino-led.git
   cd voice-controlled-arduino-led
   ```

2. **Install dependencies**
  - Installed libraries:
  - `vosk`
  - `sounddevice`
  - `pyserial`


3. **Download Vosk model**  
   - Get the [English Vosk Model](https://alphacephei.com/vosk/models)  
   - Extract it into the `models/` folder inside the project.

4. **Connect Arduino**  
   - Upload this simple Arduino sketch that listens for `LED_ON` and `LED_OFF` commands over serial:
   ```cpp
   void setup() {
     pinMode(LED_BUILTIN, OUTPUT);
     Serial.begin(9600);
   }

   void loop() {
     if (Serial.available()) {
       String command = Serial.readStringUntil('\n');
       if (command == "LED_ON") {
         digitalWrite(LED_BUILTIN, HIGH);
       } else if (command == "LED_OFF") {
         digitalWrite(LED_BUILTIN, LOW);
       }
     }
   }
   ```

5. **Adjust `SERIAL_PORT` in `led_control.py`**  
   ```python
   SERIAL_PORT = "COM5"  # For Windows
   # or
   SERIAL_PORT = "/dev/ttyUSB0"  # For Linux/Mac
   ```

6. **Run the Python script**
   ```bash
   python led_control.py
   ```

---

## 🗣 Usage

- Say **"light on"** → LED turns **ON**
- Say **"light off"** → LED turns **OFF**

---

## 📌 Notes

- ✅ Make sure to update `SERIAL_PORT` in `led_control.py` for your system.  
- ✅ This project works fully offline.  
- ✅ Tested on **Windows** with Arduino UNO.

---

  <!--## 📷 Demo (Optional)

_Add a GIF or screenshot here showing the project in action._


## 📜 License

MIT License © 2025 [Khaled Rouissi](https://github.com/khaledrouissitech-pixel)----->

