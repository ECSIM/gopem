from .mainwindow import *
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    a = MainWindow()
    if len(sys.argv) > 0 and sys.argv[0] == "--test" and app is not None:
        sys.exit(app.exec_())
    a.show()
    if app is not None:
        sys.exit(app.exec_())
