import form
from neopixel import NeoPixel
from USBCamera_OpenCV import Camera

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QObject, pyqtSignal
# , QThread,

import sys
import threading
# import cv2
import time
# import serial


class Widget(QtWidgets.QMainWindow):
    verticalCamera0 = 320
    horizontalCamera0 = 240
    verticalCamera1 = 320
    horizontalCamera1 = 240
    verticalCamera2 = 320
    horizontalCamera2 = 240
    verticalCamera3 = 320
    horizontalCamera3 = 240
    verticalCamera4 = 320
    horizontalCamera4 = 240
#    verticalCamera5 = 320
#    horizontalCamera5 = 240
    cameraLiveLoopStop = True
    toggleLight = False

    signal_UpdateGraphics = pyqtSignal(int)

    # ライト用のArduinoのポート指定。Arduino Studioでポートを確認する。
    # 最初の利用時はライトは同一フォルダ内にあるArduinoのスケッチでコンパイルをする。
    neoPixel0 = NeoPixel('COM3')
    neoPixel1 = NeoPixel('COM4')
    neoPixel2 = NeoPixel('COM6')

    def __init__(self, parent=None):
        # カメラの数を増減させる場合はここをコメントアウト
        self.cameras = []
        self.cameras.append(Camera(0))
        self.cameras.append(Camera(1))
        self.cameras.append(Camera(2))
        self.cameras.append(Camera(3))
        self.cameras.append(Camera(4))
#        self.cameras.append(Camera(5))

        print("finish set up cameras")
        super().__init__(parent)
        self.ui = form.Ui_Widget()
        self.ui.setupUi(self)
        self.signal_UpdateGraphics.connect(self.updateGraphicView)

        self.graphicViewList = []
        self.graphicViewList.append(self.ui.GVCamera0)
        self.graphicViewList.append(self.ui.GVCamera1)
        self.graphicViewList.append(self.ui.GVCamera2)
        self.graphicViewList.append(self.ui.GVCamera3)
        self.graphicViewList.append(self.ui.GVCamera4)
#        self.graphicViewList.append(self.ui.GVCamera5)

    def __del__(self):
        self.cameraLiveLoopStop = True

    def cameraLive(self):
        if self.cameraLiveLoopStop:
            self.cameraLiveLoopStop = False
            print("start Thread")
            self.th = threading.Thread(target=self.cameraLiveMainLoop)
            # self.th.setDaemon(True)
            self.th.start()
        else:
            self.cameraLiveLoopStop = True
            print("finish Thread")

    def cameraLiveMainLoop(self):
        while not self.cameraLiveLoopStop:
            # この部分で実際のカメラに送る台数を制御。
            self.signal_UpdateGraphics.emit(0)
            self.signal_UpdateGraphics.emit(1)
            self.signal_UpdateGraphics.emit(2)
            self.signal_UpdateGraphics.emit(3)
            self.signal_UpdateGraphics.emit(4)
#            self.signal_UpdateGraphics.emit(5)
            time.sleep(1)

    def updateGraphicView(self, cameraI):
        print("update camera {}".format(cameraI))
        self.cameras[cameraI].scanOneImage()
        scene = QtWidgets.QGraphicsScene()
        scene.clear()
        image = QtGui.QImage('./temp_{}.png'.format(cameraI))
        pixmap = QtGui.QPixmap.fromImage(image)
        scene.addPixmap(pixmap)

        self.graphicViewList[cameraI].setScene(scene)
        self.graphicViewList[cameraI].fitInView(scene.sceneRect(),
                                                QtCore.Qt.KeepAspectRatio)
        time.sleep(0.1)

    def lightToggle(self):
        # ライトの個数を変更する場合はここも変更する。
        if self.toggleLight:
            print("Turn off")
            self.toggleLight = False
            self.neoPixel0.rightOff()
            self.neoPixel1.rightOff()
            self.neoPixel2.rightOff()
        else:
            print("Turn on")
            self.toggleLight = True
            self.neoPixel0.rightOnAll()
            self.neoPixel1.rightOnAll()
            self.neoPixel2.rightOnAll()
        return 0

    def setMark(self):
        # カメラのマークを付ける関数。カメラの個数を変更する場合はここも変更。
        self.cameras[0].vl0 = int(self.ui.LEHorizontalCamera0.text())
        self.cameras[0].hl0 = int(self.ui.LEVerticalCamera0.text())
        self.cameras[1].vl0 = int(self.ui.LEHorizontalCamera1.text())
        self.cameras[1].hl0 = int(self.ui.LEVerticalCamera1.text())
        self.cameras[2].vl0 = int(self.ui.LEHorizontalCamera2.text())
        self.cameras[2].hl0 = int(self.ui.LEVerticalCamera2.text())
        self.cameras[3].vl0 = int(self.ui.LEHorizontalCamera3.text())
        self.cameras[3].hl0 = int(self.ui.LEVerticalCamera3.text())
        self.cameras[4].vl0 = int(self.ui.LEHorizontalCamera4.text())
        self.cameras[4].hl0 = int(self.ui.LEVerticalCamera4.text())
#        self.cameras[5].vl0 = int(self.ui.LEHorizontalCamera5.text())
#        self.cameras[5].hl0 = int(self.ui.LEVerticalCamera5.text())
        return 0


if __name__ == "__main__":
    print("Start Camera System")
    app = QtWidgets.QApplication(sys.argv)
    wmain = Widget()
    wmain.show()
    app.exec_()
