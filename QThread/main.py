import sys
import time

from window import Ui_myWidgets
from PySide6.QtCore import QObject, Signal, Slot, QThread
from PySide6.QtWidgets import QApplication, QWidget


class Worker1(QObject):
    started = Signal(str)
    progressed = Signal(str)
    finished = Signal(str)

    def run(self):
        value = '0'
        self.started.emit(value)
        for i in range(5):
            value = str(i)
            self.progressed.emit(value)
            time.sleep(1)
        self.finished.emit(value)


class MyWidget(QWidget, Ui_myWidgets):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.button1.clicked.connect(self.hardWork1)
        self.button2.clicked.connect(self.hardWork2)

    def hardWork1(self):
        self._worker = Worker1()
        self._thread = QThread()

        # Mover o worker para a thread
        self._worker.moveToThread(self._thread)

        # Run
        self._thread.started.connect(self._worker.run)
        self._worker.finished.connect(self._thread.quit)

        self._thread.finished.connect(self._thread.deleteLater)
        self._worker.finished.connect(self._thread.deleteLater)

        self._worker.started.connect(self.worker1Started)
        self._worker.progressed.connect(self.worker1Progressed)
        self._worker.finished.connect(self.worker1Finished)

        self._thread.start()

    @Slot()
    def worker1Started(self, value):
        self.button1.setDisabled(True)
        self.label1.setText(value)
        print('worker 1 started')

    @Slot()
    def worker1Progressed(self, value):
        self.label1.setText(value)
        print('worker 1 in progressed')

    @Slot()
    def worker1Finished(self, value):
        self.button1.setDisabled(False)
        self.label1.setText(value)
        print('worker 1 finished')

    def hardWork2(self):
        self._worker2 = Worker1()
        self._thread2 = QThread()

        # Mover o worker para a thread
        self._worker2.moveToThread(self._thread2)

        # Run
        self._thread2.started.connect(self._worker2.run)
        self._worker2.finished.connect(self._thread2.quit)

        self._thread2.finished.connect(self._thread2.deleteLater)
        self._worker2.finished.connect(self._thread2.deleteLater)

        self._worker2.started.connect(self.worker2Started)
        self._worker2.progressed.connect(self.worker2Progressed)
        self._worker2.finished.connect(self.worker2Finished)

        self._thread2.start()

    @Slot()
    def worker2Started(self, value):
        self.button2.setDisabled(True)
        self.label2.setText(value)
        print('worker 2 started')

    @Slot()
    def worker2Progressed(self, value):
        self.label2.setText(value)
        print('worker 2 in progressed')

    @Slot()
    def worker2Finished(self, value):
        self.button2.setDisabled(False)
        self.label2.setText(value)
        print('worker 2 finished')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWidget = MyWidget()
    myWidget.show()
    app.exec()
