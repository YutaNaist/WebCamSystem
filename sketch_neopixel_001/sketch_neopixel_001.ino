#include <Adafruit_NeoPixel.h>

const int DIN_PIN = 2; // D1
const int LED_COUNT = 9; // LEDの数

Adafruit_NeoPixel pixels(LED_COUNT, DIN_PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  pixels.begin();
  Serial.begin(9600);   // シリアルポートを9600 bps[ビット/秒]で初期化
  pinMode(DIN_PIN, OUTPUT);
  Serial.println( "Hello Arduino!" );   // 最初に1回だけメッセージを表示する
}

void loop() {
  while (Serial.available() > 0) {  // 入力された文字が何バイトか調べその回数分繰り返す
    int val = Serial.read();        // 1バイト分のデータを読み取る
    int intVal = val - '0';
    if (intVal == LED_COUNT){
      pixels.clear();
      pixels.show();
      digitalWrite(DIN_PIN, LOW);
    }else{
        pixels.setPixelColor(intVal, pixels.Color(255, 255, 255));
        pixels.show();
    }

    /*
    if (val == '1') {               // "1"ならLEDを点灯,"0"ならLEDを消灯
      digitalWrite(DIN_PIN, HIGH);
      for (int i = 0; i < LED_COUNT; i++) {
        //pixels.clear();
        pixels.setPixelColor(i, pixels.Color(255, 255, 255));
        pixels.show();
        delay(1000);
      }
    }
    else if(val == '0') {
      pixels.clear();
      pixels.show();
      digitalWrite(DIN_PIN, LOW);
    }
        */
  }
}
