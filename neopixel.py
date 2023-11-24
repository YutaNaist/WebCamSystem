import serial
# import time


class NeoPixel:
    LED_COUNT = 9
    ser = serial.Serial()

    def __init__(self, serialPort='/dev/cu.usbserial-14320'):
        self.ser = serial.Serial(serialPort, 9600, timeout=1)

    def __del__(self):
        self.ser.close()

    def rightOff(self):
        flag = bytes(str(self.LED_COUNT), 'utf-8')
        self.ser.write(flag)

    def rightOn(self, LEDPosition):
        flag = bytes(str(LEDPosition), 'utf-8')
        self.ser.write(flag)

    def rightOnAll(self):
        for i in range(self.LED_COUNT):
            flag = bytes(str(i), 'utf-8')
            self.ser.write(flag)


def main():
    with serial.Serial('COM3', 9600,
                       timeout=1) as ser:  # シリアルポートとボーレートを設定
        while True:
            print("Input Char (q:quit)", end=' > ')
            p = input()
            print(type(p))

            if p == 'q':
                break

            flag = bytes(p, 'utf-8')
            ser.write(flag)  # 入力した文字を送信

        ser.close()


if __name__ == "__main__":
    main()
    # neopix = NeoPixel('COM3')
    # print("Input Char (q:quit)", end=' > ')
    # p = input()
    # if p == 'q':
    #     break
    # else:
    #     neopix.rightOn(int(p))
    # time.sleep(1)
    # for i in range(10):
    #     neopix.rightOff()
    #     time.sleep(1)
    #     neopix.rightOnAll()
    #     time.sleep(1)
    # neopix.rightOff()
    # print("finish")
