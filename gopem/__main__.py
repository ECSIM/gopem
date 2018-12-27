from PyQt5.QtWidgets import QApplication

from .mainwindow import MainWindow
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    a = MainWindow()
    if len(sys.argv) > 1 and sys.argv[1] == "--test" and app is not None:
        sys.exit(0)
    a.show()
    if app is not None:
        sys.exit(app.exec_())
