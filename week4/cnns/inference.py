import torch
from torchvision import transforms, datasets
import torch.nn.functional as F
from tqdm import tqdm
import matplotlib.pyplot as plt
from mnist_no_noise import Net

transform=transforms.Compose([
	transforms.ToTensor(),
	transforms.Normalize((0.1307,), (0.3081,))
	])
dataset2 = datasets.MNIST('../data', train=False,
					transform=transform)
test_loader = torch.utils.data.DataLoader(dataset2, batch_size=16, shuffle=False)

with torch.inference_mode():
	for i in tqdm(range(8)):
		print(i)
		net = Net()
		net.load_state_dict(torch.load("mnist_cnn_small.pt"))
		net.conv1.weight[i] = torch.Tensor([[0,0,0],
											[0,0,0],
											[0,0,0]])
		net.eval()

		loss = 0
		for batch_idx, (x, y) in enumerate(test_loader):
			y_hat = net(x)
			loss += F.nll_loss(y_hat, y)
		loss /= len(test_loader)

		print(loss)

net = Net()
net.load_state_dict(torch.load("mnist_cnn_small.pt"))
x = dataset2[0][0]
plt.imshow(x[0], cmap='gray')
plt.savefig("test.png")

input = torch.unsqueeze(x, dim=0)
kernel = torch.unsqueeze(net.conv1.weight[1], dim=0)
x1 = F.conv2d(input, kernel, stride=3)
plt.clf()
plt.imshow(x1[0][0], cmap='gray')
plt.savefig("conv3.png")