# The following code is used as a reference.
# https://stackoverflow.com/a/78633633

import os
import shutil

val_images = os.listdir('val/')
for image in val_images:
   temp_split = image.split('.')
   split = temp_split[0].split('_')
   cls_name = split[3]

   if not os.path.exists('val/' + cls_name):
       print('creating dir: ', 'val/' + cls_name)
       os.makedirs('val/' + cls_name, exist_ok=True)

   src = 'val/' + image
   destination = 'val/' + cls_name + '/'
   print('moving')
   print(src)
   print(destination)
   
   shutil.move(src, destination)