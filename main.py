import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QMdiArea, QMdiSubWindow, QTextEdit
from PyQt5.QtGui import QIcon

from subwindows.players import PlayersSubWindow

class App(QMainWindow):
    count = 0

    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        self.title = "DndTool"
        self.width, self.height = 1280, 720
        self.x, self.y = 100, 100
        self.mdi = QMdiArea()
        self.subwindows = {}
        self.menu = self.menuBar()
        self.status = self.statusBar()

        windows_menu = self.menu.addMenu('Windows')
        windows_menu.addAction("Players")
        windows_menu.triggered.connect(self.open_windows)

        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setCentralWidget(self.mdi)

        self.show()

    def open_windows(self, action):
        if action.text() == "Players":
            App.count += 1
            sub = PlayersSubWindow()
            self.mdi.addSubWindow(sub)
            sub.show()
            self.subwindows["Players"] = sub



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())