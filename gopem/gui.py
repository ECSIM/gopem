from mainwindow import *
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    a = MainWindow()
    a.show()
    if app is not None:
        sys.exit(app.exec_())
