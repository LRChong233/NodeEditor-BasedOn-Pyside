from PySide2.QtWidgets import *
from PySide2.QtGui import *


class QDMNodeContentWidget(QWidget):
    def __init__(self, node):
        self.node = node
        super().__init__()

        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        self.wdg_label = QLabel("Some Title")
        self.layout.addWidget(self.wdg_label)
        self.layout.addWidget(QDMTextEdit("foo"))

    def setEditingFlag(self, value):
        self.node.scene.grScene.views()[0].editingFlag = value

class QDMTextEdit(QTextEdit):
    def focusInEvent(self, event:QFocusEvent) -> None:
        self.parentWidget().setEditingFlag(True)
        super().focusInEvent(event)

    def focusOutEvent(self, event:QFocusEvent) -> None:
        self.parentWidget().setEditingFlag(False)
        super().focusOutEvent(event)