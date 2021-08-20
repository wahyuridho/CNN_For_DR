# CNN_For_DR
Projek ini merupakan tugas akhir saya yang berjudul : KLASIFIKASI TINGKAT PENYAKIT DIABETEIC RETINOPATHY PADA CITRA RETINA FUNDUS MENGGUNAKAN CONVOLUTIONAL NEURAL NETWORK

please install additional package:
1. Tensorflow 2.5.0
2. OpenCV 4.5.2.52	
3. PyQT5 5.9.2


Cara melakukan cek DR:
1. Jalankan Program
2. Masuk ke halaman home
3. klik browser
4. cari foto retina yang akan di deteksi
5. klik ok
6. tunggu beberapa saat file akan menampilkan hasil dari preprocessing data dan kemudian menampilkan hasil prediksi di bagian bawah


Proses Preprocessing gambar pada projek ini adalah:
1. Resize (224x224)
2. Peningkatan kontras dengan metode CLAHE
3. Penghilangan noise dengan gaussian filter
