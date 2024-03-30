import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import os

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the layout
        self.layout = QVBoxLayout()

        # Load background image
        self.background_label = QLabel(self)
        pixmap = QPixmap('img\\background_car.jpg')  # Thay đổi đường dẫn tại đây
        self.background_label.setPixmap(pixmap)
        self.background_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.background_label)

        # Create start camera button
        self.start_button = QPushButton('Start Camera', self)
        self.start_button.clicked.connect(self.start_camera)
        self.start_button.setGeometry(100, 100, 200, 50)
        self.start_button.setStyleSheet("font-size: 20px")
        self.layout.addWidget(self.start_button)

        self.setLayout(self.layout)

    def start_camera(self):
        # Lấy đường dẫn của file main.py
        current_dir = os.path.dirname(os.path.abspath(__file__))
        main_py_path = os.path.join(current_dir, 'main.py')
        
        # Chạy file main.py
        subprocess.Popen(['python', main_py_path])



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setGeometry(100, 100, 800, 600)  # Adjust the window size as needed
    window.setWindowTitle('Eye Tracking App')
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()