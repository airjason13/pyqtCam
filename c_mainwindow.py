# coding=UTF-8

import platform
import os
import signal
import threading
from PyQt5 import QtWidgets, QtMultimediaWidgets
from PyQt5.QtWidgets import (QApplication, QMainWindow, QDesktopWidget, QStyleFactory, QWidget, QHBoxLayout,
                             QVBoxLayout, QFormLayout,
                             QGridLayout, QFrame, QHeaderView, QTableWidgetItem, QMessageBox, QFileDialog,
                             QSlider, QLabel, QLineEdit, QPushButton, QTableWidget, QStackedLayout, QSplitter,
                             QTreeWidget, QTreeWidgetItem, QTreeWidgetItemIterator,
                             QFileDialog, QListWidget, QFileSystemModel, QTreeView, QMenu, QAction, QAbstractItemView,
                             QItemDelegate, QShortcut, QSizePolicy, QRadioButton, QButtonGroup)

from PyQt5.QtCore import Qt, QMutex, pyqtSlot, QModelIndex, pyqtSignal, QSize, QTimer

from PyQt5.QtMultimedia import QCamera,QCameraImageCapture,QCameraViewfinderSettings

import qdarkstyle
import socket
from time import sleep


class MainUi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.cwd = os.getcwd()
        self.setWindowTitle('Image Color Adjust')


        self.test_timer = QTimer(self)
        self.test_timer.timeout.connect(self.test_timer_handler)

        self.init_ui()

        self.camera.start()
        self.cameraOpened = True

    def init_ui(self):
        self.setFixedSize(960, 800)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        self.widget = QWidget(self)
        self.setCentralWidget(self.widget)
        self.gridlayout = QGridLayout(self.widget)

        self.camera = QCamera()

        self.camera.setCaptureMode(QCamera.CaptureViewfinder)

        self.cameraOpened = False  # 设置相机打开状态为未打开

        # 设置取景器分辨率

        viewFinderSettings = QCameraViewfinderSettings()

        viewFinderSettings.setResolution(800, 600)

        self.camera.setViewfinderSettings(viewFinderSettings)

        # 初始化取景器

        self.viewCamera = QtMultimediaWidgets.QCameraViewfinder(self)

        self.camera.setViewfinder(self.viewCamera)

        self.gridlayout.addWidget(self.viewCamera)  # 取景器放置到预留的布局中

        self.capImg = QCameraImageCapture(self.camera)

        self.capImg.setCaptureDestination(QCameraImageCapture.CaptureToFile)  # CaptureToBuffer


    def switchCamera(self):
        if not self.cameraOpened:
            self.camera.start()
            self.cameraOpened = True
        else:
            self.camera.stop()
            self.cameraOpened = False





    def start_test_timer(self):
        pass

    def stop_test_timer(self):
        pass

    def test_timer_handler(self):
        pass