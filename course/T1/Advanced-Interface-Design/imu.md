# Advanced Interface Design

# Part A: timing, electricity, buttons, IMUs

## A1. How Processing draws a frame

- `setup()` runs once; `draw()` runs about **60 times per second**, and each run produces one **frame**.
- Everything is drawn onto a **hidden image (buffer)**. The screen is updated only **when `draw()` ends**, so you never see a half-drawn picture.
- **Why `delay()` cannot make a circle blink:**
  1. The circle is drawn on the hidden image.
  2. `delay()` waits, but the screen is not updated during the wait.
  3. `background(0)` erases the circle.
  4. When `draw()` ends, only the final black frame is shown.
  - In addition, the window freezes during the wait.
- **Rule: never use `delay()` inside `draw()`.** Each frame should be quick: check the time → decide → draw → finish.
- Arduino has no hidden image, so `digitalWrite` takes effect immediately and `delay()` blinking does work there (but it blocks everything else).

## A2. Blinking the right way: `millis()` and `%`

- `millis()` = milliseconds since the program started. It is a stopwatch you can read without stopping the program.
- `%` (modulo) = the remainder of a division. `millis() % 2000` counts 0 → 1999 and then restarts: a repeating 2-second cycle (sawtooth).

```java
void draw() {
  background(0);                       // every frame starts black
  if (millis() % 2000 < 1000) {        // first half of each 2 s cycle?
    circle(width/2, height/2, 200);    // ON for 1 s, OFF for 1 s
  }
}
```

| Change                        | Effect                            |
| ----------------------------- | --------------------------------- |
| `millis() % 500 < 250`        | Blinks 4 times faster             |
| `millis() % 2000 < 200`       | Short flash, long pause           |
| `circle(mouseX, mouseY, 200)` | Blinking circle follows the mouse |

## A3. The same idea on Arduino: a potentiometer controls the speed

- The problem with `delay(sensorValue)`: the board does nothing while it waits. The knob is read only once per blink, and button presses can be missed.
- Wiring: potentiometer on **A0**, LED on **D4** (Grove Base Shield).

```cpp
void loop() {
  int v = analogRead(A0) + 1;            // 1..1024; +1 avoids modulo by 0
  if (millis() % (2 * v) < v) digitalWrite(4, HIGH);
  else                        digitalWrite(4, LOW);
}
```

- ⚠️ **Two common mistakes**
  1. `millis() % 2*v` is evaluated left to right as `(millis() % 2) * v`. Always write `millis() % (2 * v)`.
  2. **Modulo by zero** when the knob is at 0. Fix it with `+ 1`.

|                    | Processing            | Arduino                         |
| ------------------ | --------------------- | ------------------------------- |
| Repeating function | `draw()` (~60/s)      | `loop()` (thousands/s)          |
| Time               | `millis()`            | `millis()`                      |
| Output             | `circle()` or nothing | `digitalWrite(HIGH/LOW)`        |
| `delay()`?         | ❌ never in `draw()`  | ⚠️ works, but blocks everything |

## A4. Electricity basics

**Water-pipe analogy**

| Electricity      | Water                           | Unit         |
| ---------------- | ------------------------------- | ------------ |
| Voltage V        | Pressure                        | volts        |
| Current I        | Flow                            | amperes / mA |
| Resistance R     | A narrow section of pipe        | ohms Ω       |
| 5V pin / battery | Pump                            |              |
| GND              | Drain (0 V)                     |              |
| Wire             | Wide pipe, almost no resistance |              |

- **Ohm's law: V = I × R** (I = V / R)
- **An LED needs a resistor in series**
  - An LED has a direction: current flows from the long leg (+, anode) to the short leg (−, cathode).
  - Once lit, an LED barely limits the current. Connected directly, it burns out and can damage the pin (safe ≈ 20 mA, absolute maximum 40 mA).
  - Calculation: (5 V − 2 V) / 0.015 A ≈ 200 Ω → use **220 Ω** (anything from 220 Ω to 1 kΩ is fine; larger = dimmer).
  - The Grove LED module and the built-in LED on pin 13 already have their own resistors.
- **Short circuit**: 5 V connected straight to GND. Never do this.
- **Breadboard**
  - Each short row of 5 holes in the middle is connected.
  - The long + / − rails along the edges are connected along their full length.
  - The central gap separates the left and right halves.

## A5. Connecting a button

- `pinMode(pin, INPUT)` + `digitalRead(pin)` → HIGH (≈5 V) or LOW (≈0 V).
- ❌ **Floating pin**: button between 5 V and the pin only. When released, the pin is connected to nothing, picks up noise like an antenna, and reads random values.
- ❌ Adding a direct wire from the pin to GND → pressing the button causes a **short circuit**.
- ✅ The fix: use a resistor (typically **10 kΩ**) to give the pin a default value.

|                | Pull-down             | Pull-up               | Internal pull-up                   |
| -------------- | --------------------- | --------------------- | ---------------------------------- |
| Resistor       | 10 kΩ from pin to GND | 10 kΩ from pin to 5 V | Inside the Arduino                 |
| Button between | 5 V and pin           | pin and GND           | pin and GND                        |
| `pinMode`      | `INPUT`               | `INPUT`               | `INPUT_PULLUP`                     |
| Pressed reads  | **HIGH**              | LOW                   | LOW                                |
| Released reads | LOW                   | HIGH                  | HIGH                               |
| Extra parts    | 1 resistor            | 1 resistor            | **none** (most common in practice) |

- With a pull-down, pressing lets only 5 V / 10 kΩ = 0.5 mA flow, so there is no short circuit.
- The **Grove Button** has its own pull-down: plug it into D2, use `INPUT`, pressed = HIGH.
- ⚠️ `==` compares; `=` assigns. `if (state = HIGH)` is always true, a classic mistake.

## A6. IMUs and degrees of freedom

- Why IMUs: several psychophysics setups measure body movement, e.g. **postural sway with eyes open vs closed (experiment 8)** and **walking while using a phone (experiment 10)** in the paper review.
- Every smartphone has an IMU. Apps to stream it: **Data OSC** (iPhone), Sensorstream IMU+GPS / Sensors2OSC (Android).
- **6 DOF of a rigid body**
  - Translation: x (left/right), y (up/down), z (forward/back)
  - Rotation: **roll** (tilt toward a shoulder), **pitch** (nod "yes"), **yaw** (shake "no")
  - A VR controller tracks all 6 DOF, plus a thumbstick, trigger, grip and buttons.

| Sensor                         | Measures                              | Good for                                                    | Problem                                                                  |
| ------------------------------ | ------------------------------------- | ----------------------------------------------------------- | ------------------------------------------------------------------------ |
| **Accelerometer** (ax, ay, az) | Acceleration, **including gravity**   | Tilt (which way is down) when still; shakes, steps, impacts | Can't separate gravity from movement; position estimates drift very fast |
| **Gyroscope** (ωx, ωy, ωz)     | Rotation speed (°/s)                  | Fast, smooth measurement of turning                         | Small errors add up → the angle slowly drifts                            |
| **Magnetometer** (mx, my, mz)  | Earth's magnetic field (a 3D compass) | Heading (yaw, which way is North)                           | Disturbed by metal, magnets and electronics; needs calibration           |

- **6-axis IMU** = accelerometer + gyroscope; **9-axis** = + magnetometer.
- **Sensor fusion** combines them so each covers the others' weaknesses, giving a stable roll, pitch and yaw.
- An IMU measures **orientation well, but not position**. Position needs double integration of acceleration, and the error explodes within seconds. Tracking position requires external references (cameras, VR base stations).

---

# Part B: Grove IMU → Arduino → Processing (+ phone)

## B1. Which module do you have?

| Printed on the module                | Chip    | Measures   | Arduino sketch               | Extra library                          |
| ------------------------------------ | ------- | ---------- | ---------------------------- | -------------------------------------- |
| 3-Axis Digital Accelerometer (±1.5g) | MMA7660 | ax, ay, az | `IMU_Stream_Arduino_MMA7660` | **Yes**: Seeed `Accelerometer_MMA7660` |
| 6-Axis Accelerometer & Gyroscope     | LSM6DS3 | acc + gyro | `IMU_Stream_Arduino_LSM6DS3` | No (uses the built-in `Wire`)          |

- Both send **one text line per sample, 50 Hz, 115200 baud**:
  - 3-axis: `ax,ay,az` (in g)
  - 6-axis: `ax,ay,az,gx,gy,gz` (gyro in °/s)
- `AccGyroIMUProcessing` reads either format.

## B2. Wiring and upload

1. **Unplug USB first.** Press the Grove Base Shield fully onto the UNO.
2. Set the shield's power switch to **5V**.
3. Plug into **any I2C socket** (they are all the same bus), not D, A or UART.
4. 3-axis only: install the MMA7660 library, as a .ZIP via _Sketch › Include Library › Add .ZIP Library…_ or by copying it to `Documents/Arduino/libraries`. Otherwise you get `MMA7660.h: No such file or directory`.
5. Select _Tools › Board: Arduino UNO_ and _Port_ (`COM3…` on Windows, `/dev/cu.usbmodem…` on Mac; to find it, unplug and replug and see which entry appears). Then Upload.

## B3. Check the data, then close the Serial Monitor

- Serial Monitor at **115200**: you should see the sensor name every 5 s, then numbers.
- Lying flat, **az ≈ 1.0** (gravity = 1 g). Tilt the module and the values change.
- ⚠️ **A serial port can be open in only one program at a time.**
  - Close the Serial Monitor/Plotter before running Processing.
  - Stop Processing before uploading again, or you get "port busy".
- `# no MMA7660 found` / `# no supported sensor` → check the I2C socket and the 5V switch.

## B4. Running AccGyroIMUProcessing

- Install **ControlP5** (UI) and **oscP5** (phone data) via _Sketch › Import Library › Manage Libraries…_. Serial is built in.
- Open the `.pde` (5 tabs) → Run → click the **SERIAL** bar at the bottom right → choose the Arduino's port.
  - Mac opens `usbmodem` automatically; on Windows you must choose it.
- Settings at the top: `SERIAL_BAUD = 115200` (must match the Arduino); `SERIAL_PORT_INDEX = -1` (automatic; set a number to open that port every time).
- Views:
  - **ACCEL / GYRO / STEPS**
  - Sources: **PHONE / ARDUINO / BOTH / FUSION**
  - The 3-axis module shows "ACC only" and an empty GYRO view.
- **Windows fix**: the old sketch opened the last COM port (often Bluetooth). Re-download the sketch if you got it before 15 Oct.
  - Check _Device Manager › Ports_ to find the Arduino's COM port.
  - Cheap UNO clones need the **CH340 driver**.

## B5. Adding a phone over OSC

1. **Same network**: university Wi-Fi blocks device-to-device traffic, so use the **phone's hotspot**.
2. Find the computer's IP: the sketch header shows it; or use `ipconfig` (Windows) / `ipconfig getifaddr en0` (Mac). Allow the firewall prompt.
3. Configure the phone app with the computer's IP and **port 8000**:
   - **iPhone: Data OSC**: turn on Motion → acceleration, gravity, rotation rate
   - **Android: Sensors2OSC** (F-Droid): turn on Accelerometer, Gyroscope, Gravity
4. Android sends m/s² and iPhone sends g; the sketch detects which and converts.
5. If iPhone orientation labels are upside down, change `DATAOSC_SCALE` from −9.81 to 9.81.

## B6. Troubleshooting (IMU)

| Symptom                          | Fix                                                      |
| -------------------------------- | -------------------------------------------------------- |
| `MMA7660.h` missing              | Install the library                                      |
| Garbage in Serial Monitor        | Set 115200 baud                                          |
| Upload "port busy"               | Stop the Processing sketch                               |
| ARDUINO stays red                | Close Serial Monitor; choose the port in the SERIAL menu |
| GYRO empty                       | Normal for the 3-axis module                             |
| PHONE stays red                  | Use the hotspot; check IP, port 8000 and firewall        |
| ControlP5/oscP5 "does not exist" | Install via Manage Libraries                             |

---

# Part C: using an LLM from Python to write code

## C1. Setup

- **Python ≥ 3.9 from python.org** (it includes tkinter). No `pip install` needed.
  - **Windows**: tick _Add python.exe to PATH_; run with `py`.
  - **Mac**: run _Install Certificates.command_ (otherwise `CERTIFICATE_VERIFY_FAILED`); run with `python3`.
  - Test the window toolkit: `py -m tkinter` / `python3 -m tkinter`.
- Unzip the **AID-LLMs** folder (on Windows, don't run it from inside the zip):

| File             | Role                                                            |
| ---------------- | --------------------------------------------------------------- |
| `llm_md.py`      | The app (~1,200 lines); don't edit                              |
| `services.json`  | Providers (Groq, Gemini): URL, key file, default model          |
| `osc.json`       | Turns on OSC: prompts in on port 9000, replies out on port 9001 |
| `groq-llm-key`   | **Your API key**; create it yourself, with no extension         |
| `conversations/` | Chats, replies and generated sketches                           |

## C2. Groq API key

- Sign up at console.groq.com → _API Keys_ → Create. The key starts with `gsk_` and is **shown only once**.
- **Treat it like a password**: no screenshots, no GitHub. If it leaks, delete it.
- Save it from the clipboard in a terminal opened in the AID-LLMs folder:
  - Windows: `Get-Clipboard | Set-Content groq-llm-key`
  - Mac: `pbpaste > groq-llm-key`
- Green ● key = found; red ● = not found (click it for the reason).
- Default model `openai/gpt-oss-120b`: about **30 requests per minute, 1,000 per day**.

## C3. Running the app

- In a terminal in the folder: `py llm_md.py` / `python3 llm_md.py`. Keep the terminal open (errors appear there).
- **New conversation** → type a prompt → **Send** (Ctrl/Cmd+Enter). The reply streams in. The status bar shows where the code was saved.

## C4. How it works (exam-worthy)

```
conversations/blink/
  system.md                        (optional standing instructions)
  001-prompt-....md   001-response-....md
  BlinkSketch_001/BlinkSketch_001.ino
  002-prompt.md
```

When you press **Send**:

1. **Build messages**: `system.md` plus every prompt/response file in number order → a list of `{role: system | user | assistant, content}`.
2. **Send** the **whole list** to `https://api.groq.com/openai/v1/chat/completions`, with the key in the header.
3. **Stream** the reply in pieces, appending them to `NNN-response.md`.
4. **Name** the files: ask the model for a 2–4 word label.
5. **Save the code**:
   - a sketch with `setup()` + `loop()` → `.ino`
   - a sketch with `setup()` + `draw()` → `.pde`
   - each goes in a folder of the same name (both IDEs require this)
   - the longest code block is copied to the clipboard

```json
{
  "model": "openai/gpt-oss-120b",
  "stream": true,
  "messages": [
    {
      "role": "system",
      "content": "You write Arduino code for an Arduino UNO."
    },
    { "role": "user", "content": "Blink the LED on pin 13 every 500 ms." }
  ]
}
```

**Three key ideas**

- **The model has no memory.** It knows only what is in the files sent each time. Delete a reply and it "forgets" it; long chats are slower and use more quota.
- **`system.md` steers every answer.** Put your board, sensors and style rules there once.
- **Services are interchangeable.** Groq and Gemini both accept the **OpenAI-compatible** format.

**OSC bridge**: `/prompt <text>` → port 9000 becomes a turn in the `osc` conversation. The reply returns on port 9001 as `/response <text> <part> <parts>` (in 2,000-character chunks) or `/error <text>`. A running Processing sketch can use this to ask the LLM questions.

## C5. The code-generation loop

Describe → Send → open the saved `.ino`/`.pde` → run → if it fails, paste the **exact error** as a new prompt → the fix arrives as `_002`. Earlier versions are never lost.

**Writing a good prompt**

- Name the hardware: board, Grove module, pins or I2C port.
- Name the installed libraries, or ask for code that needs none.
- Give **numbers**: rate (50 Hz), thresholds, baud rate (115200), data format (`ax,ay,az`).
- For Arduino + Processing, describe **both ends of the serial link** in one prompt so the formats match.
- Ask for each sketch complete, in its own code block.
- Work in **small steps**: first read and print the sensor, then add visuals.

**Always check the output**: models invent library functions, use the wrong pins, or mismatch baud rates. Read the code before uploading.

## C6. Troubleshooting (LLM app)

| Symptom                            | Cause / fix                                                             |
| ---------------------------------- | ----------------------------------------------------------------------- |
| `py`/`python3` not found           | Reinstall with _Add to PATH_ ticked                                     |
| `python` opens the Microsoft Store | Use `py`                                                                |
| `can't open file 'llm_md.py'`      | Terminal is not in the AID-LLMs folder                                  |
| `No module named '_tkinter'`       | Install Python from python.org                                          |
| Red ● no key                       | Key file missing, named `.txt`, or app started from another folder      |
| HTTP **401**                       | Key incomplete or deleted → make a new one                              |
| HTTP **429**                       | Rate limit reached → wait, or use `openai/gpt-oss-20b`                  |
| Empty model list                   | Check the internet connection, press ↻                                  |
| Code saved as `.txt`               | Ask for "one complete sketch in a code block tagged arduino/processing" |

## C7. In-class exercises

1. Setup check: "Explain in three sentences what an Arduino is."
2. Blink the built-in LED every 500 ms → upload.
3. Iterate: change it to SOS in Morse code → compare `_002` with `_001`.
4. Add a `system.md` → ask the same question in a new conversation → compare.
5. Arduino sends `ax,ay,az` + Processing visualises it → compare with `AccGyroIMUProcessing`.
6. Debug loop: count how many rounds it takes to fix a compile error.
7. **Memory experiment**: delete a response file → ask "What code did you write before?" → explain the answer.
8. Optional: a Processing + oscP5 sketch that sends `/prompt` and shows `/response`.

---

## Glossary

Buffer · Frame · `millis()` · Modulo `%` · Ohm's law · Anode/cathode · GND · Short circuit · Floating pin · Pull-down/pull-up · `INPUT_PULLUP` · IMU · DOF · Roll/pitch/yaw · Sensor fusion · I2C · Baud rate · Serial port · OSC · API key · System prompt · Streaming · OpenAI-compatible API · Rate limit (HTTP 429)
