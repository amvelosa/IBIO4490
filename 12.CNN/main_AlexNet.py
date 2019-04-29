#!/home/afromero/anaconda3/bin/ipython
import pdb
import torch
import torchvision
from torchvision import transforms
import matplotlib.pyplot  as plt
import torch.nn.functional as F
import numpy as np
import os 

class AlexNet(torch.nn.Module):

    def __init__(self, num_classes=1000):
        super(AlexNet, self).__init__()
        self.features = torch.nn.Sequential(
            torch.nn.Conv2d(3, 64, kernel_size=11, stride=4, padding=2),
            torch.nn.ReLU(inplace=True),
            torch.nn.MaxPool2d(kernel_size=3, stride=2),
            torch.nn.Conv2d(64, 192, kernel_size=5, padding=2),
            torch.nn.ReLU(inplace=True),
            torch.nn.MaxPool2d(kernel_size=3, stride=2),
            torch.nn.Conv2d(192, 384, kernel_size=3, padding=1),
            torch.nn.ReLU(inplace=True),
            torch.nn.Conv2d(384, 256, kernel_size=3, padding=1),
            torch.nn.ReLU(inplace=True),
            torch.nn.Conv2d(256, 256, kernel_size=3, padding=1),
            torch.nn.ReLU(inplace=True),
            torch.nn.MaxPool2d(kernel_size=3, stride=2),
        )
        self.avgpool = torch.nn.AdaptiveAvgPool2d((6, 6))
        self.classifier = torch.nn.Sequential(
            torch.nn.Dropout(),
            torch.nn.Linear(256 * 6 * 6, 4096),
            torch.nn.ReLU(inplace=True),
            torch.nn.Dropout(),
            torch.nn.Linear(4096, 4096),
            torch.nn.ReLU(inplace=True),
            torch.nn.Linear(4096, num_classes),
        )

    def forward(self, x):
        x = self.features(x)
        x = self.avgpool(x)
        x = x.view(x.size(0), 256 * 6 * 6)
        x = self.classifier(x)
        return x

tranform=transforms.Compose([
transforms.CenterCrop(112),
#transforms.Grayscale(num_output_channels=1),
transforms.ToTensor()

])         
    
#image_data = torchvision.datasets.ImageFolder('Train')

#trainset = torch.utils.data.DataLoader(image_data,batch_size=2,shuffle=True)

#image_data = torchvision.datasets.ImageFolder('Test')
#testset = torch.utils.data.DataLoader(image_data,batch_size=2,shuffle=True)


train=torchvision.datasets.MNIST(root='./data',train=True,download=True,transform=tranform)
trainset=torch.utils.data.DataLoader(train,batch_size=4,shuffle=False)

test=torchvision.datasets.MNIST(root='./data',train=False,download=True,transform=tranform)
testset=torch.utils.data.DataLoader(train,batch_size=4,shuffle=False)

net = AlexNet()
for parameter in net.parameters():
  print(str(parameter.data.numpy().shape)+'\n')
funcionPerdida = torch.nn.CrossEntropyLoss()
optimizador = torch.optim.SGD(net.parameters(),lr=0.001,momentum=0.9)

def trainModel(epocas):
  net.train()
  for epoca in range(epocas):
    perdidas =[]
    cperdida = 0 
    for i,batch in enumerate(trainset,0):
      data,salida = batch
      prediccion = net(data)
      perdida =   costFunction(prediccion,salida)
      cperdida += perdida.item()  
      optimizador.zero_grad()
      perdida.backward()
      optimizador.step()
      if i%100 ==0:
         perdidas.append(perdida.item())                                    
      if i%1000 ==0:
          print('[%d %d] perdida:%.4f'% (epoca+1,i+1, cperdida/1000))
          cperdida =0
    exactitud()
    plt.plot(perdidadas,label='epocas'+str(epocas))
    plt.legend(loc=1,mode='expanded',shadow=True,ncol=2) 
  plt.show() 

def exactitud():
  net.eval()
  golpesCorrectos=0
  total=0
  exactitud=0
  for batches in testset:
    data,salida=batches
    prediccion=net(data)
    _,prediccion=torch.max(prediccion.data,1)
    total += salida.size(0)
    golpesCorrectos += (prediccion==salida).sum().item()
    exactitud = (golpesCorrectos/total)*100
  print('Exactitud =' + str(exactitud))
  
if __name__ == '__main__':
  trainModel(2) 
  

