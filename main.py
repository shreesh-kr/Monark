__version__ = 0.1 # version history of the app
# Project Monark
# Installing Python packages through GUI
# NO CLI, GO GUI

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication
from PyQt5 import uic
import sys, os

form_1, base_1 = uic.loadUiType('resources/window.ui')

class Window(base_1, form_1):
    def __init__(self):
        super(base_1, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pack_install)

    # package install facility
    def pack_install(self):
        pack_name = str(self.lineEdit.text())
        try:
            print(f'Starting to download {pack_name}...')
            command = f'pip3 install {pack_name}'
            os.system(command)
            print(f'{pack_name} successfully downloaded')
        except Exception as E:
            print(E)


# to load the window widget

def start_app():     
    ex = QApplication(sys.argv)
    app = Window()
    app.show()
    sys.exit(ex.exec_())


if __name__ == '__main__':
    start_app()