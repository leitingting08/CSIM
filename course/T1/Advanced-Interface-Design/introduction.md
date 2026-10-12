# 高级交互界面设计（Advanced Interface Design, AID）

## 硬件全景（"所有界面 / 硬件革命"）

- **开发板与计算机**：Arduino（Uno WiFi、Yún）、树莓派（包括 Pi Zero）、Particle 类开发板、Intel Edison、智能手机
- **传感器**：加速度计 / IMU、超声波测距、RFID 读卡器、旋转编码器、摄像头
- **身体与行为传感器**：眼动仪、脑电（EEG）头戴设备、指尖生理传感器（心率 / 皮电）
- **现成交互设备**：Wii 手柄（六轴）、Kinect（深度相机 + 麦克风阵列）、Leap Motion（手部追踪）、Myo 臂环（肌电）
- **微控制器 vs 计算机**：Arduino 在微控制器上运行单个程序；树莓派是一台运行操作系统的完整计算机。

### 视觉与音频处理硬件

- **JeVois 相机**：小型相机，带处理器和 GPU，可在本地运行神经网络
- **声音设备**：Matrix Voice、Seeed Studio ReSpeaker（麦克风阵列）
- **新型芯片**：ESP32 设备和 **M5Stack** 系列，例如 M5StickV，带 RISC-V CPU 和神经网络处理器（KPU），支持 MicroPython

### CPU vs GPU 与边缘 AI

- 深度学习在 **GPU**（大规模并行）上远快于 CPU。
- **集成 GPU 或加速器的硬件**：**NVIDIA Jetson**；可装在树莓派上的 **Raspberry Pi AI Kit（Hailo-8L）**。

---

## 面向交互的机器学习

- **艺术家的机器学习**（Gene Kogan），例如用卷积神经网络做风格迁移
- **Wekinator 2.0**：交互式机器学习。录制样例 → 训练 → 实时把输入映射为输出，通过 OSC 通信。
- **p5.js**：基于 Processing 的 JavaScript 库，让艺术家、设计师和初学者也能编程；整个浏览器页面都可以作为画布
- **ml5.js**：面向浏览器的友好机器学习库，与 p5.js 配合使用
- **Hugging Face Spaces**：社区发布的 AI 应用演示，可以直接试用各种深度学习模型

## 自然语言界面（大语言模型）

| 商业闭源                                               | 开源 / 本地运行                              |
| ------------------------------------------------------ | -------------------------------------------- |
| Google AI Studio、GPT-5、Claude Opus、Grok、Perplexity | BERT、GPT-2、LM Studio、Ollama、Llama、Gemma |

- 课程关注：**实时、免费的 API 调用**，或**本地运行**（可行，但计算成本高）
- 思考题：_"编程的终结？"_

---

## 软件与编程语言

| 语言               | 开发环境                                            | 运行位置                      | 备注                                         |
| ------------------ | --------------------------------------------------- | ----------------------------- | -------------------------------------------- |
| C / C++            | Arduino IDE                                         | 在 Arduino 板上               | `setup()` 运行一次，`loop()` 无限循环        |
| Java               | Processing IDE                                      | 在操作系统（电脑）上          | `setup()` 运行一次，`draw()` 每帧运行        |
| JavaScript + p5.js | 编辑 `sketch.js`（不需要 IDE）                      | 在浏览器中：双击 `index.html` | 与 Processing 结构相同：`setup()` / `draw()` |
| Python             | `python code.py`、Jupyter（`.ipynb`）、Google Colab | 操作系统或浏览器              | 适合机器学习和数据处理；**不太适合实时交互** |

**共同的程序结构**：Arduino、Processing、p5.js 都是"_初始化一次_（`setup`）+ _无限重复_（`loop` / `draw`）"。

**课件中的示例代码**

- **Arduino Blink**：在 setup 中用 `pinMode(LED_BUILTIN, OUTPUT)` 设置引脚；在 loop 中依次执行 `digitalWrite` 高电平 → `delay(1000)` → 低电平 → `delay(1000)`。
- **Processing Hue**：使用 `colorMode(HSB, …)`。在 `draw()` 中，鼠标横坐标 `mouseX` 所在的竖条，颜色由纵坐标 `mouseY` 决定。

### 课件讨论题及参考答案

_（以下是我的补充，课件只提出了问题。）_

- **都是面向对象吗？** Java、C++、JavaScript、Python 都支持面向对象；纯 C 不支持。
- **编译型还是解释型？** C/C++ 编译为机器码；Java 编译为字节码，在 JVM 上运行；JavaScript 在浏览器中解释执行或即时编译；Python 是解释型。
- **哪些能做成 App？** Java（桌面应用；安卓用 Java/Kotlin）、JavaScript（跨平台网页应用）、C++（原生应用）。
- **深度学习、数学计算用什么？** Python（PyTorch、TensorFlow、NumPy）；在浏览器中可以用 ml5.js / TensorFlow.js。
- **哪些能在手机上运行？** JavaScript / p5.js 可在手机浏览器运行；Java/Kotlin 可在安卓原生运行。

---

## 行为捕捉：系统闭环

**人做出行为** → 传感器采集（Arduino；树莓派；摄像头和麦克风 + 深度学习做视觉与听觉识别）→ **系统**（多台电脑通过**网络以 OSC 协议**通信）→ 通过执行器**反馈**给人：LED、显示屏、声音、触觉（通常经由 Arduino）。

### 追踪什么（人 ⇄ 系统）

- **行为追踪**：手部、头部、身体、眼动追踪；运动量
  - 例：HandPose 程序把手部关键点通过 **OSC** 发送给 Processing 程序（用到 oscP5、netP5、MIDI、ControlP5）。
- **动作追踪**：决策 / 按键、反应时
- **生理信号**：心率、心率变异性（HRV）、EDR（皮肤电反应）

---

## LLM 在交互系统与实验中的应用

### 人 → 系统：用 LLM 控制交互

- **文本交互**：实时进行情感 / 情绪分析、主题分类、语言复杂度测量（句法、词汇多样性、流畅度、停顿）
- **语音交互**：自由说话 → 麦克风 + **ASR**（自动语音识别）→ LLM 处理转录文本，用于调用工具、切换模式、触发事件
- **对话智能体 / 虚拟主试**：LLM 充当模拟伙伴或访谈者；根据被试的回答调整对话；按情境分支的任务（决策、谈判、说服）
- **自适应实验控制**：LLM 生成刺激材料；按个人调整难度；实时验证回答

### 系统 → 人：LLM 的反馈、自适应与生成

- **自适应指导语**：根据表现实时改写；被试遇到困难时换用更简单的措辞；个性化的学习支架
- **对话式引导**："虚拟主试"提供提示、解释和鼓励，可以用文字、合成语音或具身化身
- **情境化反馈**：即时表现反馈（"这次你反应更快了"）；强化策略（表扬、纠正、激励）；根据被试情绪调整回应
- **生成刺激**：即时生成问题、情境、两难困境、故事续写；在游戏或谈判中扮演动态对手

---

## 关键术语

Arduino · Firmata · Processing · p5.js · ml5.js · Wekinator · IMU（惯性测量单元）· DTW（动态时间规整）· OSC（开放声音控制协议）· HandPose · ESP32 · M5Stack · 树莓派 · Jetson · Hailo-8L · ASR · HRV · EDR · LLM 智能体
