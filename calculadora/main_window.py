from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # Configurando o layout básico
        self.cw = QWidget()
        self.vLayout = QVBoxLayout()
        self.cw.setLayout(self.vLayout)
        self.setCentralWidget(self.cw)

        # Título da janela
        self.setWindowTitle('Calculadora')

    def adjustFixedSize(self):
        """
            Ajusta o tamanho da janela ao conteudo e fixa esse tamanho
        """
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addWidgetToVLayout(self, widget: QWidget):
        """
            Adiciona um widget ao layout (v_layout)
        """
        self.vLayout.addWidget(widget)

    def makeMsgBox(self):
        return QMessageBox(self)
