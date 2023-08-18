# O básico sobre Signal e Slot (eventos e documentação)
import sys
from typing import Callable

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (
    QApplication, QPushButton, QWidget, QGridLayout, QMainWindow, QStatusBar)


@Slot()
def exec_func(status_bar: QStatusBar) -> Callable[[], None]:
    def slot_example() -> None:
        status_bar.showMessage('O meu slot foi executado')
    return slot_example


@Slot()
def outro_slot(checked):
    print('Está marcado?', checked)


@Slot()
def terceiro_slot(action):
    def inner():
        outro_slot(action.isChecked())
    return inner


app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle('Titulo da janela')

botao1 = QPushButton('Texto do Botão')
botao1.setStyleSheet('font-size: 80px')

botao2 = QPushButton('Botão 2')
botao2.setStyleSheet('font-size: 40px')

botao3 = QPushButton('Botão 3')
botao3.setStyleSheet('font-size: 40px')

layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(botao1, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 3, 1, 1, 2)

# statusBar
status_bar = window.statusBar()
status_bar.showMessage('Mostrar mensagem na barra')

# menuBar
menu = window.menuBar()
primeiro_menu = menu.addMenu('Primeiro menu')
segunda_acao = primeiro_menu.addAction('Primeira ação')  # type: ignore
segunda_acao.triggered.connect(
    exec_func(status_bar)
)

segunda_acao = primeiro_menu.addAction('Segunda ação')  # type: ignore
segunda_acao.setCheckable(True)
segunda_acao.toggled.connect(outro_slot)
segunda_acao.hovered.connect(terceiro_slot(segunda_acao))

botao1.clicked.connect(terceiro_slot(segunda_acao))

window.show()
app.exec()
