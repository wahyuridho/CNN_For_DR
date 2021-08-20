from main import *
from preprocessing import *

class UIFunctions(MainWindow):

    def slideLeftMenu(self, newwidth, enable):
        if enable:
            width = self.ui.left_side_menu.width()

            if width == 50:
                newwidth = newwidth
            else:
                newwidth = 50

            self.animation = QPropertyAnimation(self.ui.left_side_menu, b"minimumWidth")
            self.animation.setDuration(250)
            self.animation.setStartValue(width)
            self.animation.setEndValue(newwidth)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    def select_file(self, enable):
        if enable:
            from tkinter import Tk
            from tkinter.filedialog import askopenfilename
            self.ui.hasil_deteksi.setText("Please Wait")

            Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
            uploaded = askopenfilename()
            img = preprocess.resize(self,uploaded)
            self.ui.path_dir.setText(uploaded)
            self.ui.original_image.setPixmap(QtGui.QPixmap(uploaded))

            resize_dir = os.path.dirname('./preprocess/resize/')
            resize_name = os.listdir('./preprocess/resize/')
            img_clahe = preprocess.CLAHE(self, resize_dir + '/' + resize_name[0])

            clahe_dir = os.path.dirname('./preprocess/clahe/')
            clahe_name = os.listdir('./preprocess/clahe/')
            img_filter = preprocess.gaussian_filter(self, clahe_dir + '/' + clahe_name[0])
            self.ui.img_after.setPixmap(QtGui.QPixmap(os.path.dirname('./preprocess/filter/') + '/filter.png'))

            filter_dir = os.path.dirname('./preprocess/filter/')
            filter_name = os.listdir('./preprocess/filter/')
            pri = preprocess.clasifikasi(self, True, filter_dir + '/' + filter_name[0])

            self.ui.hasil_deteksi.setText(pri)