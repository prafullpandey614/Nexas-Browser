import sys
from PyQt5.QtCore import  *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        navigation_bar = QToolBar()
        self.addToolBar(navigation_bar)

        back_button = QAction("<---",self)
        back_button.triggered.connect(self.browser.back)
        navigation_bar.addAction(back_button)

        forward_button = QAction("--->", self)
        forward_button.triggered.connect(self.browser.forward)
        navigation_bar.addAction(forward_button)

        reload_button = QAction("Reload", self)
        reload_button.triggered.connect(self.browser.reload)
        navigation_bar.addAction(reload_button)

        home_button = QAction("home",self)
        home_button.triggered.connect(self.return_to_home)
        navigation_bar.addAction(home_button)

        self.website_bar = QLineEdit()
        self.website_bar.returnPressed.connect(self.go_to_website)
        navigation_bar.addWidget(self.website_bar)
        self.browser.urlChanged.connect(self.update_website)
    def update_website(self,q):
        self.website_bar.setText(q.toString())

    def go_to_website(self):
        url = self.website_bar.text()
        self.browser.setUrl(QUrl(url))
    def return_to_home(self):
        self.browser.setUrl(QUrl('http://google.com'))

nexas = QApplication(sys.argv)
QApplication.setApplicationName("NEXAS BROWSER")
window = MainWindow()
nexas.exec()