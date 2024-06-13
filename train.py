import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt

# Memuat data citra dan labelnya
tribes = np.load("tribes.npy")
labels = np.load("labels.npy")

# Mengacak data
s = np.arange(tribes.shape[0])
np.random.shuffle(s)
tribes = tribes[s]
labels = labels[s]

# Menghitung jumlah kelas dan panjang data
num_classes = len(np.unique(labels))
data_length = len(tribes)

# Pembagian data menjadi data latih dan data uji
(x_train, x_test) = tribes[(int)(0.1 * data_length):], tribes[:(int)(0.1 * data_length)]
x_train = x_train.astype('float32') / 255
x_test = x_test.astype('float32') / 255
train_length = len(x_train)
test_length = len(x_test)

# Pembagian label menjadi label data latih dan label data uji
(y_train, y_test) = labels[(int)(0.1 * data_length):], labels[:(int)(0.1 * data_length)]

# Membangun model CNN
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(50, 50, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))

model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10))

# Kompilasi model
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# Melatih model
history = model.fit(x_train, y_train, epochs=100, validation_data=(x_test, y_test))

# Plot akurasi model
plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label='val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0.5, 1])
plt.legend(loc='lower right')

# Evaluasi model pada data uji
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)

print("Test accuracy:", test_acc)

# Menyimpan model
model.save("model.h5")






# import numpy as np
# import tensorflow as tf
# from tensorflow.keras import layers, models
# import matplotlib.pyplot as plt

# # Memuat data gambar dan label dari file numpy yang telah disimpan
# tribes = np.load("tribes.npy")
# labels = np.load("labels.npy")

# # Shuffle data untuk memastikan data yang beragam dalam setiap batch
# s = np.arange(tribes.shape[0])
# np.random.shuffle(s)
# tribes = tribes[s]
# labels = labels[s]

# # Menentukan jumlah kelas dan panjang data
# num_classes = len(np.unique(labels))
# data_length = len(tribes)

# # Membagi data menjadi data latih (90% dari data) dan data uji (10% dari data)
# split_index = int(0.1 * data_length)
# x_train, x_test = tribes[split_index:], tribes[:split_index]
# y_train, y_test = labels[split_index:], labels[:split_index]

# # Normalisasi data gambar ke dalam rentang [0, 1]
# x_train = x_train.astype('float32') / 255
# x_test = x_test.astype('float32') / 255

# # Membangun model CNN
# model = models.Sequential([
#     layers.Conv2D(32, (3, 3), activation='relu', input_shape=(50, 50, 3)),
#     layers.MaxPooling2D((2, 2)),
#     layers.Conv2D(64, (3, 3), activation='relu'),
#     layers.MaxPooling2D((2, 2)),
#     layers.Conv2D(64, (3, 3), activation='relu'),
#     layers.Flatten(),
#     layers.Dense(64, activation='relu'),
#     layers.Dense(num_classes)
# ])

# # Menampilkan ringkasan model
# model.summary()

# # Menyusun model dengan optimizer 'adam', fungsi loss 'SparseCategoricalCrossentropy', dan metrik 'accuracy'
# model.compile(optimizer='adam',
#               loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
#               metrics=['accuracy'])

# # Melatih model menggunakan data latih dan validasi menggunakan data uji
# history = model.fit(x_train, y_train, epochs=100, validation_data=(x_test, y_test))

# # Plot akurasi dan val_akurasi selama pelatihan
# plt.plot(history.history['accuracy'], label='accuracy')
# plt.plot(history.history['val_accuracy'], label='val_accuracy')
# plt.xlabel('Epoch')
# plt.ylabel('Accuracy')
# plt.ylim([0.5, 1])
# plt.legend(loc='lower right')

# # Evaluasi model menggunakan data uji dan mencetak akurasi pengujian
# test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
# print("Test accuracy:", test_acc)

# # Menyimpan model yang telah dilatih ke dalam file "model.h5"
# model.save("model.h5")
