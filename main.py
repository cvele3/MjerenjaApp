import sys
import random
import time
#import measureTemperature
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QComboBox
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class LivePlot(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.axes.set_xlabel('Time (s)')
        self.axes.set_ylabel('Temperature (°C)')
        self.axes.set_ylim(20, 35)
        self.line, = self.axes.plot([], [], '-')
        super().__init__(fig)
        self.setParent(parent)

        self.temperature_func = None
        self.anim = None

    def update_plot(self, x, y):
        x, y = zip(*sorted(zip(x, y)))  # add this line to sort x and y in ascending order
        self.line.set_data(x, y)
        self.axes.relim()
        self.axes.autoscale_view(True, True, True)
        self.axes.set_xlim(0, x[-1])  # add this line to set x-axis limits
        self.draw()

    def start_animation(self, temperature_func):
        self.temperature_func = temperature_func
        self.anim = FuncAnimation(self.figure, self._update_animation, interval=100)

    def _update_animation(self, frame):
        xdata, ydata = self.line.get_data()
        xdata = np.append(xdata, frame)
        ydata = np.append(ydata, self.temperature_func())
        self.update_plot(xdata, ydata)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create the buttons
        self.PT100_button = QPushButton("PT100")
        self.PT100_button.clicked.connect(self.PT100_clicked)
        self.Termopar_button = QPushButton("Termopar")
        self.Termopar_button.clicked.connect(self.Termopar_clicked)
        self.Both_button = QPushButton("Both")
        self.Both_button.clicked.connect(self.Both_clicked)

        # Create the Termopar options menu
        self.Termopar_options = QComboBox()
        self.Termopar_options.addItem("Select Termopar type")
        # self.Termopar_options.addItem("T  ->  0 - 350")
        # self.Termopar_options.addItem("J  ->  95 - 760")
        # self.Termopar_options.addItem("E  ->  95 - 900")
        # self.Termopar_options.addItem("K  ->  95 - 1260")
        # self.Termopar_options.addItem("N  ->  95 - 1260")
        # self.Termopar_options.addItem("R  ->  870 - 1450")
        # self.Termopar_options.addItem("S  ->  980 - 1450")
        # self.Termopar_options.addItem("B  ->  871 - 1704")

        # Create the text boxes
        self.PT100_text = QTextEdit()
        self.PT100_text.setReadOnly(True)
        self.Termopar_text = QTextEdit()
        self.Termopar_text.setReadOnly(True)
        self.Both_text_1 = QTextEdit()
        self.Both_text_1.setReadOnly(True)
        self.Both_text_2 = QTextEdit()
        self.Both_text_2.setReadOnly(True)

        # Create the layout
        layout = QVBoxLayout()
        layout.addWidget(self.PT100_button)
        # layout.addWidget(self.PT100_text)
        layout.addWidget(self.Termopar_button)
        layout.addWidget(self.Termopar_options)
        # layout.addWidget(self.Termopar_text)
        layout.addWidget(self.Both_button)
        layout.addWidget(self.Termopar_options)
        # layout.addWidget(self.Both_text_1)
        # layout.addWidget(self.Both_text_2)

        self.setLayout(layout)

    def PT100_clicked(self):
        live_plot = LivePlot()
        live_plot.start_animation(lambda: random.uniform(25, 30))
        live_plot.show()

    def Termopar_clicked(self):
        live_plot = LivePlot()
        live_plot.start_animation(lambda: random.uniform(25, 30))
        live_plot.show()

    def Both_clicked(self):
        #treba napravit da se prikazuju 2 grafa u istom prozoru ili kako god, sam da budu dva grafa


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(500, 300) # set the window size to 500 x 300
    window.show()
    sys.exit(app.exec_())


