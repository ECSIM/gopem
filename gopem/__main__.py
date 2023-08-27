# -*- coding: utf-8 -*-
"""GOPEM main."""
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication
from art import tprint
from gopem.mainwindow import MainWindow
from gopem.helper import Version, CiteMessage
from opem.Functions import line
import sys


def console_start():
    """
    Print information in console.

    :return: None
    """
    tprint("GOPEM")
    tprint("v" + str(Version))
    line(32)
    print("GOPEM Console")
    line(32)
    print("Please don't close this window!")
    line(32, "*")


def main():
    """
    CLI main function.

    :return: None
    """
    console_start()
    try:
        QtCore.Qt.AA_EnableHighDpiScaling = 1
    except Exception as e:
        print(str(e))
    app = QApplication(sys.argv)
    a = MainWindow()
    a.showMaximized()
    a.location_on_screen()
    if len(sys.argv) > 1 and sys.argv[1] == "--test" and app is not None:
        sys.exit(0)
    a.show()
    a.message_box("Welcome", CiteMessage)
    if app is not None:
        sys.exit(app.exec_())


if __name__ == "__main__":
    main()
