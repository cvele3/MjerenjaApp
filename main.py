import sys
import measureTemperature
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QComboBox

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
        self.Termopar_options.addItem("T  ->  0 - 350")
        self.Termopar_options.addItem("J  ->  95 - 760")
        self.Termopar_options.addItem("E  ->  95 - 900")
        self.Termopar_options.addItem("K  ->  95 - 1260")
        self.Termopar_options.addItem("N  ->  95 - 1260")
        self.Termopar_options.addItem("R  ->  870 - 1450")
        self.Termopar_options.addItem("S  ->  980 - 1450")
        self.Termopar_options.addItem("B  ->  871 - 1704")

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
        layout.addWidget(self.PT100_text)
        layout.addWidget(self.Termopar_button)
        layout.addWidget(self.Termopar_options)
        layout.addWidget(self.Termopar_text)
        layout.addWidget(self.Both_button)
        layout.addWidget(self.Termopar_options)
        layout.addWidget(self.Both_text_1)
        layout.addWidget(self.Both_text_2)

        self.setLayout(layout)

    def PT100_clicked(self):
        temperaturePT = measureTemperature.pt100_temperature()
        self.PT100_text.setPlainText("PT100 temperature: " + str(temperaturePT))

    def Termopar_clicked(self):
        temperatureTC = measureTemperature.termopar_temperature()
        self.Termopar_text.setPlainText("ThermoCouple temperature: " + str(temperatureTC))

    def Both_clicked(self):
        temperaturePT = measureTemperature.pt100_temperature()
        temperatureTC = measureTemperature.termopar_temperature()
        self.PT100_text.setPlainText("PT100 temperature: " + str(temperaturePT))
        self.Termopar_text.setPlainText("ThermoCouple temperature: " + str(temperatureTC))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(500, 300) # set the window size to 500 x 300
    window.show()
    sys.exit(app.exec_())


