import torch
print(torch.cuda.is_available())


# create a 0D tensor (scalar) from a Python integer  
tensor0d = torch.tensor(1)
print(tensor0d.dtype)


dff
# create a 1D tensor (vector) from a Python list
tensor1d = torch.tensor([1, 2, 3])
# print(tensor1d)


# # create a 2D tensor from a nested Python list
# tensor2d = torch.tensor([[1, 2], [3, 4]])

# # create a 3D tensor from a nested Python list
# tensor3d = torch.tensor([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])


# tensor1d = torch.tensor([1, 2, 3])  
# # print(tensor1d.dtype)

# floatvec = torch.tensor([1.0, 2.0, 3.0])
# # print(floatvec.dtype)

floatvec = tensor1d.to(torch.float32)  # convert into  64-bit integer tensor into a 32-bit float tensor:
print(floatvec.dtype)

dfff

# import torch.nn.functional as F
# import torch
# y = torch.tensor([1.0])  # true label
# x1 = torch.tensor([1.1]) # input feature
# w1 = torch.tensor([2.2]) # weight parameter
# b = torch.tensor([0.0])  # bias unit

# z = x1 * w1 + b          # net input
# a = torch.sigmoid(z)     # activation & output

# loss = F.binary_cross_entropy(a, y)
# print(loss)




import torch.nn.functional as F
from torch.autograd import grad

y = torch.tensor([1.0])
x1 = torch.tensor([1.1])
w1 = torch.tensor([2.2], requires_grad=True)
b = torch.tensor([0.0], requires_grad=True)

z = x1 * w1 + b
a = torch.sigmoid(z)

loss = F.binary_cross_entropy(a, y)

grad_L_w1 = grad(loss, w1, retain_graph=True)
grad_L_b = grad(loss, b, retain_graph=True)


# print(grad_L_w1)
print(grad_L_b)

loss.backward()

# print(w1.grad)
# print(b.grad)




######### Neural Network Module ###############

class NeuralNetwork(torch.nn.Module):
    def __init__(self, num_inputs, num_outputs):
        super().__init__()

        self.layers = torch.nn.Sequential(

            # 1st hidden layer
            torch.nn.Linear(num_inputs, 30),
            torch.nn.ReLU(),

            # 2nd hidden layer
            torch.nn.Linear(30, 20),
            torch.nn.ReLU(),

            # output layer
            torch.nn.Linear(20, num_outputs),
        )

    def forward(self, x):
        logits = self.layers(x)
        return logits
    

model = NeuralNetwork(50, 3)

print(model)


num_params = sum(
    p.numel() for p in model.parameters() if p.requires_grad)

print("Total number of trainable model parameters:", num_params)



print(model.layers[0].weight)
print(model.layers[0].weight.shape)

print(model.layers[0].bias)



## Manual seeding of small numbers for initialization of neural network
torch.manual_seed(123)

model = NeuralNetwork(50, 3)
print(model.layers[0].weight)


### Model initialization

torch.manual_seed(123)

X = torch.rand((1, 50))
out = model(X)
print(out)



X_train = torch.tensor([
    [-1.2, 3.1],
    [-0.9, 2.9],
    [-0.5, 2.6],
    [2.3, -1.1],
    [2.7, -1.5]
])



y_train = torch.tensor([0, 0, 0, 1, 1])


X_test = torch.tensor([
    [-0.8, 2.8],
    [2.6, -1.6],
])


y_test = torch.tensor([0, 1])


from torch.utils.data import Dataset


class ToyDataset(Dataset):
    def __init__(self, X, y):
        self.features = X
        self.labels = y

    def __getitem__(self, index):
        one_x = self.features[index]
        one_y = self.labels[index]
        return one_x, one_y

    def __len__(self):
        return self.labels.shape[0]

train_ds = ToyDataset(X_train, y_train)
test_ds = ToyDataset(X_test, y_test)

len(train_ds)


from torch.utils.data import DataLoader

torch.manual_seed(123)

train_loader = DataLoader(
    dataset=train_ds,
    batch_size=2,
    shuffle=True,
    num_workers=0,
    drop_last=True
)

test_ds = ToyDataset(X_test, y_test)

test_loader = DataLoader(
    dataset=test_ds,
    batch_size=2,
    shuffle=False,
    num_workers=0
)

for idx, (x, y) in enumerate(train_loader):
    print(f"Batch {idx+1}:", x, y)




import torch.nn.functional as F


torch.manual_seed(123)
model = NeuralNetwork(num_inputs=2, num_outputs=2)
optimizer = torch.optim.SGD(model.parameters(), lr=0.5)

num_epochs = 3

for epoch in range(num_epochs):

    model.train()
    for batch_idx, (features, labels) in enumerate(train_loader):

        logits = model(features)

        loss = F.cross_entropy(logits, labels) # Loss function

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        ### LOGGING
        print(f"Epoch: {epoch+1:03d}/{num_epochs:03d}"
              f" | Batch {batch_idx:03d}/{len(train_loader):03d}"
              f" | Train/Val Loss: {loss:.2f}")

    
    model.eval()

    with torch.no_grad():
        outputs = model(X_train)

    print(outputs)


torch.set_printoptions(sci_mode=False)
probas = torch.softmax(outputs, dim=1)
print(probas)


predictions = torch.argmax(probas, dim=1)
print(predictions)


# Note that it is unnecessary to compute softmax probabilities to obtain the class labels.
#  We could also apply the argmax function to the logits (outputs) directly:

predictions = torch.argmax(outputs, dim=1)
print(predictions)

predictions == y_train
torch.sum(predictions == y_train)


# However, to generalize the computation of the prediction accuracy, let’s implement a compute_accuracy function as shown in the following code.

def compute_accuracy(model, dataloader):

    model = model.eval()
    correct = 0.0
    total_examples = 0

    for idx, (features, labels) in enumerate(dataloader):

        with torch.no_grad():
            logits = model(features)

        predictions = torch.argmax(logits, dim=1)
        compare = labels == predictions
        correct += torch.sum(compare)
        total_examples += len(compare)

    return (correct / total_examples).item()


compute_accuracy(model, train_loader)
compute_accuracy(model, test_loader)

# Here’s the recommended way how we can save and load models in PyTorch:

torch.save(model.state_dict(), "model.pth")
# Once we saved the model, we can restore it from disk as follows:

model = NeuralNetwork(2, 2) # needs to match the original model exactly
model.load_state_dict(torch.load("model.pth", weights_only=True))



# 9 Optimizing training performance with GPUs 

print(torch.cuda.is_available())

# Now, suppose we have two tensors that we can add as follows – this computation will be carried out on the CPU by default:

tensor_1 = torch.tensor([1., 2., 3.])
tensor_2 = torch.tensor([4., 5., 6.])

print(tensor_1 + tensor_2)

# We can now use the .to() method to transfer these tensors onto a GPU and perform the addition there:

tensor_1 = tensor_1.to("cuda")
tensor_2 = tensor_2.to("cuda")

print(tensor_1 + tensor_2)

# 9.2 Single-GPU training 
torch.manual_seed(123)
model = NeuralNetwork(num_inputs=2, num_outputs=2)

# New: Define a device variable that defaults to a GPU.
device = torch.device("cuda")

# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# New: Transfer the model onto the GPU.
model.to(device)

optimizer = torch.optim.SGD(model.parameters(), lr=0.5)

num_epochs = 3

for epoch in range(num_epochs):

    model.train()
    for batch_idx, (features, labels) in enumerate(train_loader):

        # New: Transfer the data onto the GPU.
        features, labels = features.to(device), labels.to(device)    #C
        logits = model(features)
        loss = F.cross_entropy(logits, labels) # Loss function

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        ### LOGGING
        print(f"Epoch: {epoch+1:03d}/{num_epochs:03d}"
              f" | Batch {batch_idx:03d}/{len(train_loader):03d}"
              f" | Train/Val Loss: {loss:.2f}")

    model.eval()
    # Optional model evaluation


# First, we will import a few additional submodules, classes, and functions for distributed training PyTorch as shown in code below.

import platform
from torch.utils.data.distributed import DistributedSampler
from torch.nn.parallel import DistributedDataParallel as DDP
from torch.distributed import init_process_group, destroy_process_group



if rank == 0: # only print in the first process
    print("Test accuracy: ", accuracy)