int data;
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  lcd.init();
  lcd.setCursor(0, 8);

}

void loop() {

  while(Serial.available())
  {
    data = Serial.read();
  }

  if(data == '0')
  {
    lcd.backlight();
    lcd.print("O");
    delay(5000);
    lcd.lcd.noBacklight();
  }
  else 
  {
    lcd.backlight();
    lcd.print("X");
    delay(5000);
    lcd.lcd.noBacklight();
  }

}