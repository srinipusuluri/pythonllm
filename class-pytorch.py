

import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt

# 1. Load the MNIST Dataset
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])

trainset = torchvision.datasets.MNIST(root='./data', train=True, download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=64, shuffle=True)

testset = torchvision.datasets.MNIST(root='./data', train=False, download=True, transform=transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=64, shuffle=False)

# 2. Define the Neural Network
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(28 * 28, 128)
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 10)

    def forward(self, x):
        x = x.view(-1, 28 * 28)  # Flatten the input tensor
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x

net = SimpleNN()

# 3. Define the Loss Function and Optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=0.01, momentum=0.9)

# 4. Train the Network
for epoch in range(5):  # Number of epochs
    running_loss = 0.0
    for i, data in enumerate(trainloader, 0):
        inputs, labels = data
        optimizer.zero_grad()  # Zero the parameter gradients

        outputs = net(inputs)  # Forward pass
        loss = criterion(outputs, labels)  # Compute loss
        loss.backward()  # Backward pass
        optimizer.step()  # Update weights

        running_loss += loss.item()
        if i % 100 == 99:  # Print every 100 mini-batches
            print(f"[{epoch + 1}, {i + 1}] loss: {running_loss / 100:.3f}")
            running_loss = 0.0

print("Finished Training")

# 5. Test the Network
correct = 0
total = 0
all_preds = torch.tensor([])
with torch.no_grad():
    for data in testloader:
        images, labels = data
        outputs = net(images)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()
        all_preds = torch.cat((all_preds, predicted), dim=0)

print(f'Accuracy of the network on the 10000 test images: {100 * correct / total:.2f}%')

# Plot some of the test images with their predicted labels
fig, axes = plt.subplots(3, 3, figsize=(10, 10))
axes = axes.ravel()

for i in range(9):
    image, label = testset[i]
    axes[i].imshow(image.squeeze(), cmap='gray')
    axes[i].set_title(f"True: {label}, Pred: {all_preds[i].item()}")
    axes[i].axis('off')

plt.tight_layout()
plt.show()




"""

Overview
Purpose:
The code trains a simple neural network to classify handwritten digits from the MNIST dataset. The MNIST dataset is a collection of 70,000 images of handwritten digits (0-9), with 60,000 images for training and 10,000 images for testing.

Step-by-Step Explanation
Importing Libraries:

torch: The main library for PyTorch.
torch.nn: Contains modules and classes for building neural networks.
torch.optim: Provides optimization algorithms.
torchvision: Contains datasets and transforms for computer vision.
matplotlib.pyplot: Used for plotting images and graphs.
Loading the MNIST Dataset:

The dataset is downloaded and transformed using transforms.ToTensor() and transforms.Normalize().
trainloader: Loads the training dataset in batches of 64 images.
testloader: Loads the test dataset in batches of 64 images.
Defining the Neural Network:

A simple feedforward neural network is defined with three fully connected (dense) layers:
fc1: Takes the 28x28 input image and maps it to 128 neurons.
fc2: Takes 128 inputs and maps to 64 neurons.
fc3: Takes 64 inputs and maps to 10 output neurons (one for each digit 0-9).
Activation Function: ReLU (Rectified Linear Unit) is used for non-linearity.
Loss Function and Optimizer:

Loss Function: CrossEntropyLoss which is suitable for classification tasks.
Optimizer: SGD (Stochastic Gradient Descent) with a learning rate of 0.01 and momentum of 0.9.
Training the Network:

The network is trained for 5 epochs. Each epoch means the network sees the entire training dataset once.
For each batch, the following steps are performed:
Zero Gradients: Clear previous gradients.
Forward Pass: Compute the network output.
Compute Loss: Calculate the difference between predicted and actual labels.
Backward Pass: Calculate gradients.
Optimizer Step: Update network weights.
Loss is printed every 100 batches for monitoring training progress.
Testing the Network:

The trained network is evaluated on the test dataset.
Accuracy Calculation: Compares the network's predictions to actual labels to compute accuracy.
Plotting Predictions:

Matplotlib is used to plot a 3x3 grid of test images.
Each image is displayed with its true label and the predicted label from the network.
Visualizing the Code's Purpose
Data: Handwritten digit images from the MNIST dataset.
Model: A simple feedforward neural network with three layers.
Training: Adjusting the network's weights to minimize classification error.
Evaluation: Testing the trained model on unseen images to measure performance.
Visualization: Displaying some test images along with the model's predictions to understand its performance visually.
By running this script, you will see how well the neural network can classify handwritten digits, providing a practical introduction to machine learning with neural networks.

###
        
