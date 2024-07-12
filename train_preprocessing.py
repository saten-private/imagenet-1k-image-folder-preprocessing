# The following code is used as a reference.
# https://stackoverflow.com/a/78633633

import os
import shutil

train_images = os.listdir('train/')
for image in train_images:
    split = image.split('_')
    cls_name = split[0]

    if not os.path.exists('train/' + cls_name):
        #print('creating dir: ', 'train/' + cls_name)
        os.makedirs('train/' + cls_name, exist_ok=True)

    src = 'train/' + image
    destination = 'train/' + cls_name + '/'
    #print('moving')
    #print(src)
    #print(destination)
    
    shutil.move(src, destination)