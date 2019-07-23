import csv
from sheets import load_sheet
from PyQt5.QtWidgets import QMenu, QAction, QWidget, QMdiSubWindow, QListWidget, QListWidgetItem
from PyQt5.QtGui import QCursor


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

    def contextMenuEvent(self, event):
        print(self.list.selectedItems())
        menu = QMenu(self)
        menu.move(QCursor.pos())
        new = QAction('New')
        edit = QAction('Edit')
        edit.triggered.connect(self.edit_player)
        delete = QAction('Delete')

        menu.addAction(new)
        menu.addAction(edit)
        menu.addAction(delete)

        if self.list.selectedItems() is None:
            edit.setDisabled(True)
            delete.setDisabled(True)
        else:
            edit.setDisabled(False)
            delete.setDisabled(False)

        menu.exec_()

    def edit_player(self):
        player_name = self.list.selectedItems()[0].text()
        for player in load_sheet('sheets/players.csv'):
            if player[0] == player_name:
                player_data = player
        d = PlayerEditDialog(player_data=player_data)


from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton


class PlayerEditDialog(QDialog):
    def __init__(self, player_data):
        super(PlayerEditDialog, self).__init__()
        self.player_data = player_data
        self.setGeometry(0, 0, 200, 100)
        self.setWindowTitle("Edit Player")

        self.player_name_edit = QLineEdit(self)
        self.player_name_edit.setGeometry(10, 10, 120, 30)
        self.player_name_edit.setText(self.player_data[0])

        self.save_button = QPushButton(self)
        self.save_button.setText("Save")
        self.save_button.setGeometry(130, 60, 60, 30)

        self.exec_()