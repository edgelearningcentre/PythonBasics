
# import libraries
import torch
print(torch.__version__)
print(torch.cuda.is_available())

# # create different tensors
# # scalar
# tensor_scalar = torch.tensor(1)
# print(tensor_scalar.dtype)

# # 1D vector from a python list
# tensor1d = torch.tensor([1,2,3])
# print(tensor1d.dtype)

# # 2D vector from a nested python list
# tensor2d = torch.tensor([[1, 2], [3, 4]])
# print(tensor2d.dtype)


# # create a 3D tensor from a nested Python list
# tensor3d = torch.tensor([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# print(tensor3d.dtype)


# floatvec = torch.tensor([1.0, 2.0, 3.0])
# print(floatvec.dtype)

# floatvec = tensor1d.to(torch.float32)  # convert into  64-bit integer tensor into a 32-bit float tensor:
# print(floatvec.dtype)


# # Basic of NN 
# import torch.nn.functional as F
# from torch.autograd import grad
# import torch
# y = torch.tensor([1.0])  # true label
# x1 = torch.tensor([1.1]) # input feature
# w1 = torch.tensor([2.2],requires_grad=True) # weight parameter
# b = torch.tensor([1.0],requires_grad=True)  # bias unit

# z = x1 * w1 + b          # net input
# a = torch.sigmoid(z)     # activation & output
# print(a.min(), a.max ())
# loss = F.binary_cross_entropy(a, y)
# print(loss)
# grad_L_w1 = grad(loss, w1, retain_graph=True)
# grad_L_b = grad(loss, b, retain_graph=True)
# print(grad_L_w1)
# print(grad_L_b)

# loss.backward()

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


# print(model.layers[0].weight)
# print(model.layers[0].weight.shape)

# print(model.layers[0].bias)

## Manual seeding of small numbers for initialization of neural network
# torch.manual_seed(123)

# model = NeuralNetwork(50, 3)
# print(model.layers[0].weight)

# X = torch.rand((1, 50))
# out = model(X)
# print(out)

# Example

