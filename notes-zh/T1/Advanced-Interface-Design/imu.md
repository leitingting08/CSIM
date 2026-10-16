# 高级交互界面设计

# 第一部分　计时、电学基础、按钮、IMU

## A1. Processing 如何绘制一帧

- `setup()` 运行一次；`draw()` 每秒运行约 **60 次**，每次产生一**帧**。
- 所有内容先画在一张**隐藏图像（缓冲区）**上，**`draw()` 结束时**才一次性显示到屏幕上，所以你永远看不到画了一半的画面。
- **为什么 `delay()` 不能让圆闪烁：**
  1. 圆只画在了隐藏图像上。
  2. `delay()` 等待期间，屏幕不会更新。
  3. `background(0)` 把圆擦掉。
  4. `draw()` 结束时，屏幕上只显示最终的黑色画面。
  - 此外，等待期间整个窗口会卡住。
- **规则：`draw()` 里绝对不要用 `delay()`。** 每一帧都要快：看时间 → 做判断 → 画 → 结束。
- Arduino 没有隐藏图像，`digitalWrite` 立即生效，所以用 `delay()` 闪灯是可行的（但会阻塞其他所有操作）。

## A2. 正确的闪烁方式：`millis()` 和 `%`

- `millis()` = 程序启动以来的毫秒数，相当于一个随时可以读、又不会让程序停下来的秒表。
- `%`（取模）= 除法的余数。`millis() % 2000` 从 0 数到 1999 再回到 0，形成一个循环往复的 2 秒周期（锯齿波）。

```java
void draw() {
  background(0);                       // 每帧先涂黑
  if (millis() % 2000 < 1000) {        // 处于每 2 秒周期的前一半吗？
    circle(width/2, height/2, 200);    // 亮 1 秒，灭 1 秒
  }
}
```

| 修改                          | 效果             |
| ----------------------------- | ---------------- |
| `millis() % 500 < 250`        | 闪烁快 4 倍      |
| `millis() % 2000 < 200`       | 短闪、长停       |
| `circle(mouseX, mouseY, 200)` | 闪烁的圆跟随鼠标 |

## A3. 在 Arduino 上用同样的方法：电位器控制闪烁速度

- `delay(sensorValue)` 的问题：等待期间板子什么都做不了。旋钮每闪一次才读一次，按钮按下也可能被漏掉。
- 接线：电位器接 **A0**，LED 接 **D4**（Grove 扩展板）。

```cpp
void loop() {
  int v = analogRead(A0) + 1;            // 1..1024；+1 避免对 0 取模
  if (millis() % (2 * v) < v) digitalWrite(4, HIGH);
  else                        digitalWrite(4, LOW);
}
```

- ⚠️ **两个常见错误**
  1. `millis() % 2*v` 会从左到右计算成 `(millis() % 2) * v`。一定要写成 `millis() % (2 * v)`。
  2. 旋钮转到 0 时会**对 0 取模**。用 `+ 1` 解决。

|             | Processing              | Arduino                  |
| ----------- | ----------------------- | ------------------------ |
| 循环函数    | `draw()`（约 60 次/秒） | `loop()`（每秒数千次）   |
| 时间        | `millis()`              | `millis()`               |
| 输出        | `circle()` 或不画       | `digitalWrite(HIGH/LOW)` |
| `delay()`？ | ❌ 绝不在 `draw()` 中用 | ⚠️ 可用，但会阻塞一切    |

## A4. 电学基础

**水管类比**

| 电学           | 水管                 | 单位        |
| -------------- | -------------------- | ----------- |
| 电压 V         | 水压                 | 伏特 V      |
| 电流 I         | 流量                 | 安培 / 毫安 |
| 电阻 R         | 管道中变窄的一段     | 欧姆 Ω      |
| 5V 引脚 / 电池 | 水泵                 |             |
| GND（地）      | 排水口（0 V）        |             |
| 导线           | 宽水管，几乎没有阻力 |             |

- **欧姆定律：V = I × R**（I = V / R）
- **LED 必须串联电阻**
  - LED 有方向：电流从长脚（+，阳极）流向短脚（−，阴极）。
  - LED 点亮后几乎不限制电流。直接接上会烧坏 LED，还可能损坏引脚（安全电流约 20 mA，绝对上限 40 mA）。
  - 计算：(5 V − 2 V) / 0.015 A ≈ 200 Ω → 用 **220 Ω**（220 Ω–1 kΩ 都可以，电阻越大灯越暗）。
  - Grove LED 模块和 13 号引脚上的板载 LED 都自带电阻。
- **短路**：5 V 直接连到 GND。绝对不要这样做。
- **面包板**
  - 中间每一排 5 个孔是相通的。
  - 两侧标 + / − 的长轨整条相通。
  - 中间的凹槽把左右两半隔开。

## A5. 连接按钮

- `pinMode(pin, INPUT)` + `digitalRead(pin)` → HIGH（约 5 V）或 LOW（约 0 V）。
- ❌ **悬空引脚**：按钮只接在 5 V 和引脚之间。松开时引脚什么都没连，像天线一样接收噪声，读数随机。
- ❌ 再从引脚直接拉一根导线到 GND → 按下按钮就**短路**。
- ✅ 解决办法：用一个电阻（通常 **10 kΩ**）给引脚一个默认值。

|           | 下拉              | 上拉              | 内部上拉             |
| --------- | ----------------- | ----------------- | -------------------- |
| 电阻      | 10 kΩ，引脚 → GND | 10 kΩ，引脚 → 5 V | Arduino 内置         |
| 按钮接在  | 5 V 和引脚之间    | 引脚和 GND 之间   | 引脚和 GND 之间      |
| `pinMode` | `INPUT`           | `INPUT`           | `INPUT_PULLUP`       |
| 按下读数  | **HIGH**          | LOW               | LOW                  |
| 松开读数  | LOW               | HIGH              | HIGH                 |
| 额外元件  | 1 个电阻          | 1 个电阻          | **无**（实际最常用） |

- 下拉电阻接法中，按下时只有 5 V / 10 kΩ = 0.5 mA 的电流流过，所以不会短路。
- **Grove 按钮模块**自带下拉电阻：插在 D2，用 `INPUT`，按下 = HIGH。
- ⚠️ `==` 是比较，`=` 是赋值。`if (state = HIGH)` 永远为真，是新手经典错误。

## A6. IMU 与自由度

- 为什么学 IMU：论文综述中有几个心理物理学实验要测身体运动，例如**睁眼 vs 闭眼的姿势摇摆（实验 8）**、**边走路边用手机（实验 10）**。
- 每部智能手机都有 IMU。串流数据的 App：**Data OSC**（iPhone）；Sensorstream IMU+GPS / Sensors2OSC（安卓）。
- **刚体的 6 个自由度（DOF）**
  - 平移：x（左右）、y（上下）、z（前后）
  - 旋转：**roll 横滚**（头歪向肩膀）、**pitch 俯仰**（点头"是"）、**yaw 偏航**（摇头"不"）
  - VR 手柄追踪手的全部 6 个自由度，另外还有摇杆、扳机、握把、按键等。

| 传感器                     | 测量什么             | 擅长                                                 | 问题                                     |
| -------------------------- | -------------------- | ---------------------------------------------------- | ---------------------------------------- |
| **加速度计**（ax, ay, az） | 加速度，**包含重力** | 静止时判断倾斜方向（哪边是下）；检测晃动、步数、撞击 | 分不清重力和运动；用它估算位置会迅速漂移 |
| **陀螺仪**（ωx, ωy, ωz）   | 旋转速度（°/s）      | 快速、平滑地测量转动                                 | 小误差不断累积 → 角度慢慢漂移            |
| **磁力计**（mx, my, mz）   | 地磁场（三维指南针） | 判断朝向（yaw，哪边是北）                            | 受金属、磁铁、电子设备干扰；需要校准     |

- **6 轴 IMU** = 加速度计 + 陀螺仪；**9 轴** = 再加磁力计。
- **传感器融合**把三者结合起来、互补短板，得到稳定的 roll、pitch、yaw。
- IMU **测姿态很准，测位置不行**：位置要对加速度做两次积分，误差几秒内就会爆炸。追踪位置需要外部参照（摄像头、VR 基站）。

---

# Grove IMU → Arduino → Processing（+ 手机）

## B1. 你手上是哪个模块？

| 模块上印的字                         | 芯片    | 测量            | Arduino 程序                 | 额外库                                  |
| ------------------------------------ | ------- | --------------- | ---------------------------- | --------------------------------------- |
| 3-Axis Digital Accelerometer (±1.5g) | MMA7660 | ax, ay, az      | `IMU_Stream_Arduino_MMA7660` | **需要**：Seeed `Accelerometer_MMA7660` |
| 6-Axis Accelerometer & Gyroscope     | LSM6DS3 | 加速度 + 陀螺仪 | `IMU_Stream_Arduino_LSM6DS3` | 不需要（用内置的 `Wire`）               |

- 两者都以 **115200 波特率、50 Hz、每个采样一行文本**发送数据：
  - 3 轴：`ax,ay,az`（单位 g）
  - 6 轴：`ax,ay,az,gx,gy,gz`（陀螺仪单位 °/s）
- `AccGyroIMUProcessing` 两种格式都能读。

## B2. 接线与上传

1. **先拔掉 USB。** 把 Grove 扩展板完全压到 UNO 上。
2. 扩展板电源开关拨到 **5V**。
3. 插到**任意一个 I2C 插座**（四个是同一条总线），不要插 D、A 或 UART 插座。
4. 仅 3 轴模块：安装 MMA7660 库，可以用 _Sketch › Include Library › Add .ZIP Library…_ 导入 zip，或复制到 `Documents/Arduino/libraries`。否则会报 `MMA7660.h: No such file or directory`。
5. 选择 _Tools › Board: Arduino UNO_ 和 _Port_（Windows 是 `COM3…`，Mac 是 `/dev/cu.usbmodem…`；拔插一次，新出现的就是 Arduino），然后上传。

## B3. 检查数据，然后关闭串口监视器

- 串口监视器设为 **115200**：每 5 秒显示一次传感器名，之后是数字。
- 平放时 **az ≈ 1.0**（重力 = 1 g），倾斜时数值变化。
- ⚠️ **一个串口同一时间只能被一个程序打开。**
  - 运行 Processing 前，先关掉串口监视器 / 绘图器。
  - 再次上传前，先停掉 Processing，否则会报 "port busy"。
- 出现 `# no MMA7660 found` / `# no supported sensor` → 检查是否插在 I2C 插座、开关是否在 5V。

## B4. 运行 AccGyroIMUProcessing

- 通过 _Sketch › Import Library › Manage Libraries…_ 安装 **ControlP5**（界面）和 **oscP5**（接收手机数据）。Serial 库是内置的。
- 打开 `.pde`（共 5 个标签页）→ Run → 点右下角 **SERIAL** 栏 → 选择 Arduino 的端口。
  - Mac 会自动打开 `usbmodem`；Windows 需要手动选。
- 顶部设置：`SERIAL_BAUD = 115200`（必须与 Arduino 一致）；`SERIAL_PORT_INDEX = -1`（自动；填一个编号可以每次启动都打开该端口）。
- 视图：
  - **ACCEL / GYRO / STEPS**
  - 数据源：**PHONE / ARDUINO / BOTH / FUSION**
  - 3 轴模块显示 "ACC only"，GYRO 视图为空。
- **Windows 修复**：旧版程序会打开列表中最后一个 COM 口（常常是蓝牙口）。10 月 15 日前下载的，请重新下载。
  - 在*设备管理器 › 端口*里确认 Arduino 是哪个 COM 口。
  - 廉价 UNO 兼容板需要安装 **CH340 驱动**。

## B5. 通过 OSC 接入手机

1. **同一网络**：学校 Wi-Fi 通常禁止设备互连，最可靠的办法是开**手机热点**，让电脑连上去。
2. 查电脑 IP：程序标题栏会显示；也可以用 `ipconfig`（Windows）/ `ipconfig getifaddr en0`（Mac）。防火墙询问时点"允许"。
3. 手机 App 里填电脑 IP 和**端口 8000**：
   - **iPhone：Data OSC**：打开 Motion → acceleration、gravity、rotation rate
   - **安卓：Sensors2OSC**（F-Droid）：打开 Accelerometer、Gyroscope、Gravity
4. 安卓发送 m/s²，iPhone 发送 g，程序会自动识别并换算。
5. iPhone 方向标签上下颠倒时，把 `DATAOSC_SCALE` 从 −9.81 改成 9.81。

## B6. 故障排查（IMU）

| 现象                               | 解决                                   |
| ---------------------------------- | -------------------------------------- |
| 缺少 `MMA7660.h`                   | 安装库                                 |
| 串口监视器乱码                     | 波特率设为 115200                      |
| 上传报 "port busy"                 | 先停掉 Processing                      |
| ARDUINO 一直是红色                 | 关掉串口监视器；在 SERIAL 菜单里选端口 |
| GYRO 为空                          | 3 轴模块本来就没有陀螺仪，正常         |
| PHONE 一直是红色                   | 用热点；检查 IP、端口 8000、防火墙     |
| ControlP5 / oscP5 "does not exist" | 用 Manage Libraries 安装               |

---

# 用 Python 调用大语言模型写代码

## C1. 准备工作

- **从 python.org 安装 Python 3.9 或以上**（自带 tkinter），不需要 `pip install`。
  - **Windows**：勾选 _Add python.exe to PATH_；用 `py` 运行。
  - **Mac**：运行 _Install Certificates.command_（否则报 `CERTIFICATE_VERIFY_FAILED`）；用 `python3` 运行。
  - 测试窗口工具包：`py -m tkinter` / `python3 -m tkinter`。
- 解压 **AID-LLMs** 文件夹（Windows 上不能直接在 zip 里运行）：

| 文件             | 作用                                               |
| ---------------- | -------------------------------------------------- |
| `llm_md.py`      | 应用本体（约 1200 行），不用改                     |
| `services.json`  | 服务商（Groq、Gemini）：地址、密钥文件名、默认模型 |
| `osc.json`       | 开启 OSC：9000 端口收提问，9001 端口回传答复       |
| `groq-llm-key`   | **你的 API 密钥**，需要自己创建，没有扩展名        |
| `conversations/` | 对话、回复和生成的程序                             |

## C2. Groq API 密钥

- 在 console.groq.com 注册 → _API Keys_ → Create。密钥以 `gsk_` 开头，**只显示一次**。
- **像密码一样保管**：不要截图，不要传到 GitHub。泄露了就删掉重建。
- 在 AID-LLMs 文件夹中打开终端，从剪贴板保存密钥：
  - Windows：`Get-Clipboard | Set-Content groq-llm-key`
  - Mac：`pbpaste > groq-llm-key`
- 绿色 ● key = 找到密钥；红色 ● = 没找到（点击查看原因）。
- 默认模型 `openai/gpt-oss-120b`：约**每分钟 30 次、每天 1000 次**请求。

## C3. 运行应用

- 在该文件夹的终端中运行：`py llm_md.py` / `python3 llm_md.py`。保持终端开着（错误信息会显示在那里）。
- **New conversation** → 输入提问 → **Send**（Ctrl/Cmd+Enter）。回复会逐字出现，状态栏显示代码保存的位置。

## C4. 工作原理（可能考）

```
conversations/blink/
  system.md                        （可选：长期生效的指令）
  001-prompt-....md   001-response-....md
  BlinkSketch_001/BlinkSketch_001.ino
  002-prompt.md
```

按下 **Send** 后：

1. **组装消息**：读取 `system.md` 和所有按编号排列的提问 / 回复文件 → 生成 `{role: system | user | assistant, content}` 列表。
2. **发送**：把**整个列表**连同密钥（放在请求头中）发到 `https://api.groq.com/openai/v1/chat/completions`。
3. **流式接收**：回复分块返回，逐段追加到 `NNN-response.md`。
4. **命名**：让模型给提问和回复各起一个 2–4 个词的标签，加到文件名里。
5. **保存代码**：
   - 含 `setup()` + `loop()` 的 → `.ino`
   - 含 `setup()` + `draw()` 的 → `.pde`
   - 各自放在同名文件夹中（两个 IDE 都要求这样）
   - 最长的代码块同时复制到剪贴板

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

**三个关键结论**

- **模型没有记忆。** 它只知道每次发过去的文件内容。删掉一条回复，它就"忘了"；对话越长越慢，消耗的额度也越多。
- **`system.md` 影响每一次回答。** 把板子型号、传感器、风格要求写在这里一次就行。
- **服务可以互换。** Groq 和 Gemini 都接受同一种请求格式（**OpenAI 兼容**）。

**OSC 桥接**：向 9000 端口发送 `/prompt <文本>`，会成为 `osc` 对话中的新一轮提问。回复以 `/response <文本> <段号> <总段数>` 的形式（每段 2000 字符）或 `/error <文本>` 发回 9001 端口。运行中的 Processing 程序可以借此向 LLM 提问。

## C5. 代码生成循环

描述需求 → 发送 → 打开保存的 `.ino` / `.pde` → 运行 → 出错就把**原样的报错信息**作为新提问发过去 → 修复版保存为 `_002`。旧版本不会丢失。

**写好提问的要点**

- 写明硬件：板子、Grove 模块、引脚或 I2C 口。
- 写明已安装的库，或者要求不用额外的库。
- 用**数字**描述行为：频率（50 Hz）、阈值、波特率（115200）、数据格式（`ax,ay,az`）。
- Arduino + Processing 联动时，在同一个提问里描述**串口两端**，保证格式一致。
- 要求每个程序完整地放在各自的代码块中。
- **小步推进**：先读取并打印传感器数据，再加可视化。

**一定要检查生成的代码**：模型可能编造库函数、写错引脚、波特率对不上。上传前先读一遍。

## C6. 故障排查（LLM 应用）

| 现象                          | 原因 / 解决                                                  |
| ----------------------------- | ------------------------------------------------------------ |
| 找不到 `py` / `python3`       | 重装，勾选 _Add to PATH_                                     |
| 输入 `python` 打开了微软商店  | 改用 `py`                                                    |
| `can't open file 'llm_md.py'` | 终端不在 AID-LLMs 文件夹中                                   |
| `No module named '_tkinter'`  | 从 python.org 安装 Python                                    |
| 红色 ● no key                 | 密钥文件缺失、被存成 `.txt`，或者从别的文件夹启动            |
| HTTP **401**                  | 密钥不完整或已删除 → 新建一个                                |
| HTTP **429**                  | 超出调用频率限制 → 等一分钟，或换 `openai/gpt-oss-20b`       |
| 模型列表为空                  | 检查网络，按 ↻                                               |
| 代码被存成 `.txt`             | 要求"一个完整程序，放在标注 arduino / processing 的代码块中" |

## C7. 课堂练习

1. 检查设置：问"用三句话解释什么是 Arduino。"
2. 让板载 LED 每 500 ms 闪一次 → 上传。
3. 迭代：改成摩尔斯电码 SOS → 对比 `_002` 和 `_001`。
4. 加一个 `system.md` → 在新对话中问同样的问题 → 对比两次回答。
5. Arduino 发送 `ax,ay,az`，Processing 做可视化 → 与 `AccGyroIMUProcessing` 对比。
6. 调试循环：记录修好一个编译错误需要几轮。
7. **记忆实验**：删除一个回复文件 → 问"你之前写过什么代码？"→ 解释它为什么这样回答。
8. 选做：用 oscP5 写一个 Processing 程序，发送 `/prompt` 并显示收到的 `/response`。

---

## 术语表

缓冲区（Buffer）· 帧（Frame）· `millis()` · 取模 `%` · 欧姆定律 · 阳极 / 阴极 · GND（地）· 短路 · 悬空引脚 · 下拉 / 上拉电阻 · `INPUT_PULLUP` · IMU（惯性测量单元）· 自由度（DOF）· 横滚 / 俯仰 / 偏航 · 传感器融合 · I2C 总线 · 波特率 · 串口 · OSC · API 密钥 · 系统提示词（system prompt）· 流式输出 · OpenAI 兼容接口 · 调用频率限制（HTTP 429）
