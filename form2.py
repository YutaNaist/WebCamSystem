# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\form.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.setWindowModality(QtCore.Qt.WindowModal)
        Widget.resize(2800, 1300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        self.layoutWidget = QtWidgets.QWidget(Widget)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 50, 2700, 1200))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setSizeConstraint(
            QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.GVCamera0 = QtWidgets.QGraphicsView(self.layoutWidget)
        self.GVCamera0.setObjectName("GVCamera0")
        self.horizontalLayout.addWidget(self.GVCamera0)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_8.addWidget(self.label_5)
        self.GVCamera4 = QtWidgets.QGraphicsView(self.layoutWidget)
        self.GVCamera4.setObjectName("GVCamera4")
        self.horizontalLayout_8.addWidget(self.GVCamera4)
        self.gridLayout.addLayout(self.horizontalLayout_8, 1, 1, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.GVCamera3 = QtWidgets.QGraphicsView(self.layoutWidget)
        self.GVCamera3.setObjectName("GVCamera3")
        self.horizontalLayout_6.addWidget(self.GVCamera3)
        self.gridLayout.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20,
                                           QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.GVCamera1 = QtWidgets.QGraphicsView(self.layoutWidget)
        self.GVCamera1.setObjectName("GVCamera1")
        self.horizontalLayout_2.addWidget(self.GVCamera1)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.GVCamera2 = QtWidgets.QGraphicsView(self.layoutWidget)
        self.GVCamera2.setObjectName("GVCamera2")
        self.horizontalLayout_5.addWidget(self.GVCamera2)
        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 2, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20,
                                            QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.PBCameraLive = QtWidgets.QPushButton(self.layoutWidget)
        self.PBCameraLive.setObjectName("PBCameraLive")
        self.verticalLayout_2.addWidget(self.PBCameraLive)
        self.PBLight = QtWidgets.QPushButton(self.layoutWidget)
        self.PBLight.setObjectName("PBLight")
        self.verticalLayout_2.addWidget(self.PBLight)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_9.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_9.addWidget(self.label_7)
        self.LEVerticalCamera0 = QtWidgets.QLineEdit(self.layoutWidget)
        self.LEVerticalCamera0.setObjectName("LEVerticalCamera0")
        self.horizontalLayout_9.addWidget(self.LEVerticalCamera0)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_9.addWidget(self.label_8)
        self.LEHorizontalCamera0 = QtWidgets.QLineEdit(self.layoutWidget)
        self.LEHorizontalCamera0.setObjectName("LEHorizontalCamera0")
        self.horizontalLayout_9.addWidget(self.LEHorizontalCamera0)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_10.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_10.addWidget(self.label_10)
        self.LEVerticalCamera1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.LEVerticalCamera1.setObjectName("LEVerticalCamera1")
        self.horizontalLayout_10.addWidget(self.LEVerticalCamera1)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_10.addWidget(self.label_11)
        self.LEHorizontalCamera1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.LEHorizontalCamera1.setObjectName("LEHorizontalCamera1")
        self.horizontalLayout_10.addWidget(self.LEHorizontalCamera1)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_15 = QtWidgets.QLabel(self.layoutWidget)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_12.addWidget(self.label_15)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_12.addWidget(self.label_16)
        self.LEVerticalCamera2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.LEVerticalCamera2.setObjectName("LEVerticalCamera2")
        self.horizontalLayout_12.addWidget(self.LEVerticalCamera2)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_12.addWidget(self.label_17)
        self.LEHorizontalCamera2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.LEHorizontalCamera2.setObjectName("LEHorizontalCamera2")
        self.horizontalLayout_12.addWidget(self.LEHorizontalCamera2)
        self.verticalLayout.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_24 = QtWidgets.QLabel(self.layoutWidget)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_15.addWidget(self.label_24)
        self.label_25 = QtWidgets.QLabel(self.layoutWidget)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_15.addWidget(self.label_25)
        self.LEVerticalCamera3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.LEVerticalCamera3.setObjectName("LEVerticalCamera3")
        self.horizontalLayout_15.addWidget(self.LEVerticalCamera3)
        self.label_26 = QtWidgets.QLabel(self.layoutWidget)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_15.addWidget(self.label_26)
        self.LEHorizontalCamera3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.LEHorizontalCamera3.setObjectName("LEHorizontalCamera3")
        self.horizontalLayout_15.addWidget(self.LEHorizontalCamera3)
        self.verticalLayout.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_27 = QtWidgets.QLabel(self.layoutWidget)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_16.addWidget(self.label_27)
        self.label_28 = QtWidgets.QLabel(self.layoutWidget)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_16.addWidget(self.label_28)
        self.LEVerticalCamera4 = QtWidgets.QLineEdit(self.layoutWidget)
        self.LEVerticalCamera4.setObjectName("LEVerticalCamera4")
        self.horizontalLayout_16.addWidget(self.LEVerticalCamera4)
        self.label_29 = QtWidgets.QLabel(self.layoutWidget)
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_16.addWidget(self.label_29)
        self.LEHorizontalCamera4 = QtWidgets.QLineEdit(self.layoutWidget)
        self.LEHorizontalCamera4.setObjectName("LEHorizontalCamera4")
        self.horizontalLayout_16.addWidget(self.LEHorizontalCamera4)
        self.verticalLayout.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Widget)

        self.PBCameraLive.clicked.connect(Widget.cameraLive)
        self.PBLight.clicked.connect(Widget.lightToggle)

        QtCore.QMetaObject.connectSlotsByName(Widget)


    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.label.setText(_translate("Widget", "Camera0"))
        self.label_5.setText(_translate("Widget", "Camera4"))
        self.label_4.setText(_translate("Widget", "Camera3"))
        self.label_2.setText(_translate("Widget", "Camera1"))
        self.label_3.setText(_translate("Widget", "Camera2"))
        self.PBCameraLive.setText(_translate("Widget", "Camera Live On/Off"))
        self.PBLight.setText(_translate("Widget", "Light On/Off"))
        self.label_6.setText(_translate("Widget", "Camera0"))
        self.label_7.setText(_translate("Widget", "Vertical"))
        self.label_8.setText(_translate("Widget", "Holozontal"))
        self.label_9.setText(_translate("Widget", "Camera1"))
        self.label_10.setText(_translate("Widget", "Vertical"))
        self.label_11.setText(_translate("Widget", "Holozontal"))
        self.label_15.setText(_translate("Widget", "Camera2"))
        self.label_16.setText(_translate("Widget", "Vertical"))
        self.label_17.setText(_translate("Widget", "Holozontal"))
        self.label_24.setText(_translate("Widget", "Camera3"))
        self.label_25.setText(_translate("Widget", "Vertical"))
        self.label_26.setText(_translate("Widget", "Holozontal"))
        self.label_27.setText(_translate("Widget", "Camera4"))
        self.label_28.setText(_translate("Widget", "Vertical"))
        self.label_29.setText(_translate("Widget", "Holozontal"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())
