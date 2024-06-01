# A hand written images are trained and tested

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt

# Load and preprocess the MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# Create the model
model = Sequential()
model.add(Flatten(input_shape=(28, 28)))  # Flatten the input
model.add(Dense(128, activation='relu'))  # First hidden layer
model.add(Dense(64, activation='relu'))   # Second hidden layer
model.add(Dense(10, activation='softmax'))  # Output layer

# Compile the model
model.compile(optimizer='sgd', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the network
history = model.fit(x_train, y_train, epochs=5, batch_size=64, validation_data=(x_test, y_test))

# Evaluate the network
loss, accuracy = model.evaluate(x_test, y_test)
print(f'Accuracy of the network on the 10000 test images: {accuracy * 100:.2f}%')

# Predict on test data
y_pred = model.predict(x_test)
y_pred_classes = y_pred.argmax(axis=1)
y_true = y_test.argmax(axis=1)

# Plot some of the test images with their predicted labels
fig, axes = plt.subplots(3, 3, figsize=(10, 10))
axes = axes.ravel()

for i in range(9):
    axes[i].imshow(x_test[i], cmap='gray')
    axes[i].set_title(f"True: {y_true[i]}, Pred: {y_pred_classes[i]}")
    axes[i].axis('off')

plt.tight_layout()
plt.show()
