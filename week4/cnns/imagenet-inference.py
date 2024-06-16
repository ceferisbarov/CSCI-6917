## TODO: Is there a particular convolutional filter
## that is the most important for all/most samples?
import torch
from torchvision import transforms, datasets
from imagenet import Net
import torch.nn.functional as F
from tqdm import tqdm
import copy
import matplotlib.pyplot as plt
from datasets import load_dataset
import numpy as np

dataset = load_dataset("zh-plus/tiny-imagenet")
dataset2 = dataset["valid"]
dataset2 = dataset2.filter(lambda x: np.array(x["image"]).shape == (64, 64, 3))
dataset2 = dataset2.filter(lambda x: x["label"] in range(2))
dataset2 = dataset2.with_format("torch", columns = ["image", "label"])
test_loader = torch.utils.data.DataLoader(dataset2)

with torch.inference_mode():
#     for i in tqdm(range(8)):
#         print(i)
#         net = Net()
#         net.load_state_dict(torch.load("imagenet_cnn_small.pt"))
#         net.conv1.weight[i] = torch.Tensor([[0,0,0],
#                                             [0,0,0],
#                                             [0,0,0]])
#         net.eval()

#         loss = 0
#         # for batch_idx, sample in enumerate(test_loader):
#         sample = dataset2[10]
#         x = sample["image"].float()
#         x = torch.unsqueeze(x, dim=0)
#         y = sample["label"].long()
#         y = torch.unsqueeze(y, dim=0)

#         y_hat = net(x)
#         loss += F.nll_loss(y_hat, y)
#         # loss /= len(test_loader)

#         print(loss)

    net = Net()
    net.load_state_dict(torch.load("imagenet_cnn_small.pt"))
    net.eval()
    num = 10
    x = dataset2[num]["image"]
    plt.imshow(torch.permute(x, (1,2,0)))
    plt.savefig(f"test_{num}.png")

    input = torch.unsqueeze(x, dim=0)
    kernel = torch.unsqueeze(net.conv1.weight[4], dim=0)
    print(input.shape)
    print(kernel.shape)
    x1 = F.conv2d(input.float(), kernel, stride=3)
    plt.clf()
    plt.imshow(x1[0][0], cmap='gray')
    plt.savefig(f"conv4_{num}.png")
