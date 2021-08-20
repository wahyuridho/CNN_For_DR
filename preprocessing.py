import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras import optimizers
import tensorflow as tf
import cv2
import os

class preprocess():
    def resize(self,image):
        img = cv2.imread(image, cv2.IMREAD_UNCHANGED)
        output = os.path.dirname('./preprocess/resize/')

        width = 224
        height = 224
        dim = (width, height)

        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
        cv2.imwrite(output + '/resize.png', resized)
        return resized

    def CLAHE(self, img):
        img = cv2.imread(img)
        out = os.path.dirname('./preprocess/clahe/')

        lab_img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab_img)

        equ = cv2.equalizeHist(l)
        updated_lab_img1 = cv2.merge((equ, a, b))
        hist_eq_img = cv2.cvtColor(updated_lab_img1, cv2.COLOR_LAB2BGR)

        clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
        clahe_img = clahe.apply(l)

        updated_lab_img2 = cv2.merge((clahe_img, a, b))
        CLAHE_img = cv2.cvtColor(updated_lab_img2, cv2.COLOR_LAB2BGR)
        cv2.imwrite(out + '/clahe.png', CLAHE_img)
        return CLAHE_img

    def gaussian_filter(self, img):
        output = os.path.dirname('./preprocess/filter/')
        sigmaX = 5

        image = cv2.imread(img)
        gaussian = cv2.addWeighted(image, 4, cv2.GaussianBlur(image, (0, 0), sigmaX), -4, 128)
        cv2.imwrite(output + '/filter.png', gaussian)

    def clasifikasi(self, enable, path):
        if enable:
            filepath = './c2'
            model = tf.keras.models.load_model(filepath)
            model.compile(loss='categorical_crossentropy',
                              optimizer = optimizers.Adam(learning_rate=0.00001),
                              metrics = ['accuracy'])

            img = image.load_img(path, target_size=(224, 224))
            x = image.img_to_array(img)
            x = np.expand_dims(x, axis=0)
            images = np.vstack([x])
            classes = model.predict(images, batch_size=32)

            class_list = os.listdir('F:/Code/train_images - Asli/train')
            print(class_list)
            for j in range(42):
                if classes[0][j] == 1.:
                    print('This image belongs to class', class_list[j])
                    return class_list[j]
                    break