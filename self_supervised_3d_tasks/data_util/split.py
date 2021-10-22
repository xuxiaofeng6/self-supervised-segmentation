import os
import glob
import random
import shutil

def pathExist(path):
    if not os.path.exists(path):
        os.makedirs(path)
    return path

raw_dir = '/media/tiger/Disk0/xxu/raw/Task08_HepaticVessel/images_resized_128_bbox_labeled/'
train_dir = os.path.join(raw_dir,'train')
train_label_dir = os.path.join(raw_dir,'train_labels')
test_dir = os.path.join(raw_dir,'test')
test_label_dir = os.path.join(raw_dir,'test_labels')
pathExist(train_dir)
pathExist(train_label_dir)
pathExist(test_dir)
pathExist(test_label_dir)

label_list = glob.glob(raw_dir+'*label.npy')
#print(label_list)
random.shuffle(label_list)
#print(label_list)

train_list = label_list[:int(0.8*len(label_list))]
test_list = label_list[int(0.8*len(label_list)):]

# print(train_list)
# print(test_list)

for i in range(len(train_list)):
    train_label = train_list[i]
    shutil.move(train_label,train_label_dir)
    shutil.move(train_label.replace('_label.npy','.npy'), train_dir)

for i in range(len(test_list)):
    test_label = test_list[i]
    shutil.move(test_label,test_label_dir)
    shutil.move(test_label.replace('_label.npy','.npy'), test_dir)