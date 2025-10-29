# 🖥️ ESP8266 OLED Display (SSD1306 I²C) — MicroPython

## 🧠 Overview
This project demonstrates how to interface an **SSD1306 OLED Display** (128x64 pixels) with the **ESP8266** using **I²C communication** and **MicroPython**.  
The display shows simple text output — “Hello World” — as an introduction to using graphical displays with embedded systems.

---

## ⚙️ Hardware Setup

| Component | ESP8266 Pin | Description |
|------------|-------------|--------------|
| OLED (SCL) | GPIO5 (D1) | Serial Clock Line |
| OLED (SDA) | GPIO4 (D2) | Serial Data Line |
| VCC | 3.3V | Power supply |
| GND | GND | Common ground |

🪛 **Connections:**
- **D1 (GPIO5)** → **SCL**  
- **D2 (GPIO4)** → **SDA**  
- **3.3V** → **VCC**  
- **GND** → **GND**

---

## 🧩 Code

```python
from machine import Pin
from machine import I2C
import ssd1306

# D1 = SCL = GPIO5
# D2 = SDA = GPIO4

i2c = I2C(sda=Pin(4), scl=Pin(5))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

display.fill(0)  # Clear display
display.text('Hello', 20, 10, 1)
display.text('World', 40, 50, 1)
display.show()
