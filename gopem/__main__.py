from .mainwindow import *
import sys

if __name__ == "__main__":
    print('1')
    app = QApplication(sys.argv)
    print('2')
    a = MainWindow()
    print('3')
    if len(sys.argv) > 0 and sys.argv[0] == "--test" and app is not None:
        print('4')
        sys.exit(app.exec_())
    print('5')
    a.show()
    if app is not None:
        sys.exit(app.exec_())
