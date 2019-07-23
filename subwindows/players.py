import csv
from sheets import load_sheet
from PyQt5.QtWidgets import QWidget, QMdiSubWindow, QListWidget, QListWidgetItem


class PlayersSubWindow(QMdiSubWindow):
    def __init__(self):
        super(PlayersSubWindow, self).__init__()
        self.predicate = QWidget(self)
        self.setWidget(self.predicate)
        self.predicate.setFixedSize(250, 325)
        self.list = QListWidget(self.predicate)
        self.list.setGeometry(5, 5, 240, 315)
        self.setWindowTitle("Players")
        self.generate_player_list()

    def generate_player_list(self):
        for player in load_sheet('sheets/players.csv'):
            item = QListWidgetItem()
            item.setText(player[0])
            self.list.addItem(item)

