Pre-processing to convert imagenet-1k to PyTorch's [ImageFolder](https://pytorch.org/vision/stable/generated/torchvision.datasets.ImageFolder.html) arrangement

https://huggingface.co/datasets/ILSVRC/imagenet-1k

I modified it a bit to work with the following code.
Thanks so much for the following code👍

https://stackoverflow.com/a/78633633

# Setup
```git clone https://github.com/saten-private/imagenet-1k-image-folder-preprocessing.git```

# Procedure
## train
1. Create a ```train``` folder under the repository.
2. Download ```train_images_X.tar.gz``` from [here](https://huggingface.co/datasets/ILSVRC/imagenet-1k/tree/main/data).
3. Extract the images from ```train_images_X.tar.gz``` into the ```train``` folder.
4. Run ```python train_preprocessing.py```

## val
1.  Create a ```val``` folder under the repository.
2. Download ```val_images.tar.gz``` from [here](https://huggingface.co/datasets/ILSVRC/imagenet-1k/tree/main/data).
3. Extract the images from ```val_images.tar.gz``` into the ```val``` folder.
4. Run ```python val_preprocessing.py```
