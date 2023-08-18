import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon

from main_window import MainWindow
from display import Display
from buttons import ButtonsGrid
from info import Info
from style import setupTheme
from variables import WINDOW_ICON_PATH

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    # Define o style
    setupTheme()

    # Define um ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info('Sua conta')
    window.addWidgetToVLayout(info)

    # Display
    display = Display()
    # display.setPlaceholderText('Calculadora')
    window.addWidgetToVLayout(display)

    # Grid
    buttonsGrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsGrid)

    window.adjustFixedSize()
    window.show()
    app.exec()
