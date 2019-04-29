
import os , shutil
import os.path as path

os.mkdir('Train')
os.chdir('Train')
os.mkdir('train')
os.chdir('..')
train_file_dir= os.chdir('Train/train') 
train_file=os.getcwd() 
os.chdir('..')
n_train=15000
#N_train=random.sample(range(0,len(dir_class_0)-1),n_train)
#os.chdir('img_align_celeba')
list=os.listdir()
for i in range(0,len(list)):
  if path.exists(list[i]):
     nuevo=list[i].replace(".jpg","0")
     if int(nuevo) <= 1627700   :
           shutil.copy(list[i],train_file) 
   
os.chdir('..')
os.mkdir('Test')
os.chdir('Test')
os.mkdir('trest')
os.chdir('..')
test_file_dir= os.chdir('Test/test') 
test_file=os.getcwd() 
os.chdir('..')
#n_train=15000
#N_train=random.sample(range(0,len(dir_class_0)-1),n_train)
os.chdir('img_align_celeba')
list=os.listdir()
for i in range(0,len(list)):
  if path.exists(list[i]):
     nuevo=list[i].replace(".jpg","0")
     if int(nuevo) >= 1826380 :
           shutil.copy(list[i],test_file) 
   
os.chdir('..')
      
  
import matplotlib.pyplot  as plt

import os , shutil
import os.path as path
train_file_dir= os.chdir('Train/train') 
list=os.listdir()

plt.subplot(4,4,1)
plt.imshow(list[34])
plt.subplot(4,4,2)
plt.imshow(list[234])
plt.subplot(4,4,3)
plt.imshow(list[3340])
plt.subplot(4,4,4)
plt.imshow(list[4321])
plt.subplot(4,4,5)
plt.imshow(list[5421])
plt.subplot(4,4,6)
plt.imshow(list[49816])
plt.subplot(4,4,7)
plt.imshow(list[1953])
plt.subplot(4,4,8)
plt.imshow(list[1532])
plt.subplot(4,4,9)
plt.imshow(list[98261])
plt.subplot(4,4,10)
plt.imshow(list[42512])
plt.subplot(4,4,11)
plt.imshow(list[98362])
plt.subplot(4,4,12)
plt.imshow(list[87251])
plt.subplot(4,4,13)
plt.imshow(list[12415])
plt.subplot(4,4,14)
plt.imshow(list[98261])
plt.subplot(4,4,15)
plt.imshow(list[124972])
plt.subplot(4,4,16)
plt.imshow(list[872154])

