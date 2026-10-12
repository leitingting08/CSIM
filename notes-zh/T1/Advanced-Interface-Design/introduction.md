# Advanced Interface Design (AID) — Course Introduction (EN)

## The hardware landscape ("all interfaces / hardware revolution")

- **Boards and computers**: Arduino (Uno WiFi, Yún), Raspberry Pi (including Pi Zero), Particle-type boards, Intel Edison, smartphones
- **Sensors**: accelerometers / IMUs, ultrasonic distance sensors, RFID readers, rotary encoders, cameras
- **Body and behaviour sensors**: eye trackers, EEG headsets, physiological finger sensors (heart rate / skin conductance)
- **Off-the-shelf interaction devices**: Wii remote (6-axis), Kinect (depth camera + mic array), Leap Motion (hand tracking), Myo armband (EMG)
- **Microcontroller vs computer**: Arduino runs a single program on a microcontroller. Raspberry Pi is a full computer running an OS.

### Vision and audio processing hardware

- **JeVois camera**: small camera with an on-board processor and GPU that runs neural networks
- **Sound devices**: Matrix Voice, Seeed Studio ReSpeaker (microphone arrays)
- **Newer chips**: ESP32 devices and the **M5Stack** series, e.g. M5StickV with a RISC-V CPU and a neural network processor (KPU), plus MicroPython support

### CPU vs GPU and edge AI

- Deep learning runs much faster on **GPUs** (massively parallel) than on CPUs.
- **Hardware with an integrated GPU or accelerator**: **NVIDIA Jetson**; the **Raspberry Pi AI Kit (Hailo-8L)** that mounts on a Pi.

---

## Machine learning for interaction

- **Machine learning for artists** (Gene Kogan), e.g. neural style transfer with CNNs
- **Wekinator 2.0**: interactive ML. Record examples → train → map inputs to outputs in real time, communicating via OSC.
- **p5.js**: JavaScript library based on Processing; makes coding accessible for artists, designers and beginners; uses the whole browser page as a sketch
- **ml5.js**: friendly ML library for the browser, built to work with p5.js
- **Hugging Face Spaces**: community-made AI demo apps (deep learning models to try)

## Natural language interfaces (LLMs)

| Proprietary                                            | Open source / local                          |
| ------------------------------------------------------ | -------------------------------------------- |
| Google AI Studio, GPT-5, Claude Opus, Grok, Perplexity | BERT, GPT-2, LM Studio, Ollama, Llama, Gemma |

- Course interest: **real-time, free API access**, or **local execution** (possible but computationally costly)
- Provocation: _"The end of programming?"_

---

## Software and languages

| Language           | Environment                                        | Where it runs                             | Notes                                             |
| ------------------ | -------------------------------------------------- | ----------------------------------------- | ------------------------------------------------- |
| C / C++            | Arduino IDE                                        | On the Arduino board                      | `setup()` once, `loop()` forever                  |
| Java               | Processing IDE                                     | On the OS (desktop)                       | `setup()` once, `draw()` every frame              |
| JavaScript + p5.js | Edit `sketch.js` (no IDE needed)                   | In the browser: double-click `index.html` | Same `setup()` / `draw()` structure as Processing |
| Python             | `python code.py`, Jupyter (`.ipynb`), Google Colab | OS or browser                             | Good for ML and data; **not great for real-time** |

**Shared program structure**: Arduino, Processing and p5.js all follow the same pattern: _initialise once_ (`setup`) + _repeat forever_ (`loop` / `draw`).

**Example code from the slides**

- **Arduino Blink**: `pinMode(LED_BUILTIN, OUTPUT)` in setup; in loop, `digitalWrite` HIGH → `delay(1000)` → LOW → `delay(1000)`.
- **Processing Hue**: `colorMode(HSB, …)`. In `draw()`, the bar under `mouseX` is filled with a hue that depends on `mouseY`.

### Discussion questions from the slide, with suggested answers

_(My own answers; the slide only poses the questions.)_

- **Object-oriented?** Java, C++, JavaScript and Python support OOP. Plain C does not.
- **Compiled or interpreted?** C/C++: compiled to machine code. Java: compiled to bytecode and run on the JVM. JavaScript: interpreted / JIT-compiled in the browser. Python: interpreted.
- **Which can produce an app?** Java (desktop, and Android via Java/Kotlin), JavaScript (web apps that run anywhere), C++ (native apps).
- **Best for deep learning / math?** Python (PyTorch, TensorFlow, NumPy). In the browser: ml5.js / TensorFlow.js.
- **Which run on phones?** JavaScript / p5.js in the mobile browser; Java/Kotlin natively on Android.

---

## Behaviour capture: the system loop

**Person behaves** → sensors (Arduino; Raspberry Pi; camera and microphone + deep learning for vision and hearing) → **System** (several computers communicating over a **network via OSC**) → **feedback** to the person through actuators: LEDs, displays, sounds, haptics (often via Arduino).

### What we track (Person ⇄ System)

- **Behaviour tracking**: hand, head, body, eye tracking; quantity of movement
  - Example: a HandPose app sends hand landmarks via **OSC** to a Processing sketch (oscP5, netP5, MIDI, ControlP5).
- **Action tracking**: decisions / button presses, reaction times
- **Physiological signals**: heart rate, heart rate variability (HRV), EDR (electrodermal response)

---

## LLMs in interactive systems and experiments

### Person → System: LLM interaction control

- **Text-based interaction**: real-time sentiment / emotion analysis, topic classification, linguistic complexity (syntax, lexical diversity, fluency, pauses)
- **Speech-based interaction**: free speech → microphone + **ASR** (automatic speech recognition) → the LLM processes the transcript for tool use, mode activation, triggering
- **Conversational agents / virtual experimenters**: the LLM as simulated partner or interviewer; adaptive dialogue; context-sensitive branching tasks (decision-making, negotiation, persuasion)
- **Adaptive experimental control**: LLM-generated stimuli, personalised difficulty, real-time response validation

### System → Person: LLM feedback, adaptation and generation

- **Adaptive instructions**: rewritten in real time based on performance; simpler wording when the participant struggles; personalised scaffolding
- **Conversational guidance**: a "virtual experimenter" giving prompts, clarifications and encouragement via text, synthetic voice or an embodied avatar
- **Context-sensitive feedback**: immediate performance feedback ("you responded faster this time"); reinforcement (praise, correction, motivation); emotionally adaptive responses
- **Generated stimuli**: on-the-fly questions, scenarios, dilemmas, story continuations; dynamic opponents in games and negotiations

---

## Key terms

Arduino · Firmata · Processing · p5.js · ml5.js · Wekinator · IMU · DTW · OSC · HandPose · ESP32 · M5Stack · Raspberry Pi · Jetson · Hailo-8L · ASR · HRV · EDR · LLM agent
