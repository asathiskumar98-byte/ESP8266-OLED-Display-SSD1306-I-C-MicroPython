from machine import Pin
from machine import I2C
import ssd1306

#D1 = scl = GPIO5
#D2 = sda = GPIO4

i2c = I2C(sda=Pin(4), scl=Pin(5))

display = ssd1306.SSD1306_I2C(128, 64, i2c)

display.fill(0) #Empty the display
display.text('Sathiskumar', 20, 10, 1)
display.text('Santhiya', 30, 30, 1)
display.text('Eswari', 40, 50, 1)
display.show()
