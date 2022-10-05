# Import dependencies.
import random
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision.transforms import ToTensor
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

lossFunction = nn.NLLLoss()
output = torch.tensor([[1.1, 0.888, 13.11111]])
softmax = nn.Softmax(dim=0)
output2 = softmax(output)
print("output2",output2)
output3=torch.log(output2)
print("output3",output3)
target = torch.tensor([1])
# loss = lossFunction(output, target)
# loss = lossFunction(output, target)
# loss = lossFunction(output, target)
# loss = lossFunction(output, target)
# loss = lossFunction(output, target)
loss = lossFunction(output, target)
print("loss",loss)
