# Detecting Plant Diseases in Browser Using Efficient Deep Learning
>We examine the comparative performance of EfficientNet and MobileNet, two lightweight image classification neural networks, and AlexNet, a large-scale image classification network in detecting disease on the leaves of plants of 21 species. Both the predictive performance of the models as well as their computational efficiency are tested in multiple environments. To determine the ability of each of these models to be used away from computers with high computational resources, the models will be run in browsers on mobile devices.

This repository applies transfer learning on pre-trained classification models to detect if an image of a plant leaf is healthy or diseased. The main notebook `leaf_classification.ipynb` trains and test various models, and exports the final models as ONNX files. `./plant-diseased-web` contains the web app that runs the models using the ONNX runtime. 

## Setup
### Environment and Dependencies Requirements
- Python == 3.10
- PyTorch == 2.0.0
- TensorBoard == 2.10.0
- scikit-learn == 1.2.1
### Getting Started
- Install PyTorch for your system following https://pytorch.org/
- Install other dependencies manually or by running:
    ```
    pip install -r requirements.txt
    ```
- Create train and test dataset by creating two directories for train and test set, each with two subdirectories for diseased and and healthy images (the name of the files does not matter):
    ```
    train
    |-- diseased
    |   |-- diseased-0.jpg
    |   |-- dieased-1.jpg
    |   ...
    |-- healthy
    |   |-- healthy-0.jpg
    |   |-- healthy-1.jpg
    |   ...

    test
    |-- diseased
    |   |-- diseased-0.jpg
    |   |-- dieased-1.jpg
    |   ...
    |-- healthy
    |   |-- healthy-0.jpg
    |   |-- healthy-1.jpg
    |   ...
    ```
- Train and test models following `leaf_classification.ipynb`! During training, these directories will be created:
    - `./models`: stores checkpointed model outputs
    - `./runs`: TensorBoard outputs
- While training, metrics on the validation set can be monitored in real-time using TensoBoard. The dashboard can be accessed by running:
    ```
    tensorboard --logdir=runs
    ```
    and visiting `localhost:6006`

## Additional Scripts
- `data_merge.py`: parses the original datasets and creates a merged directory `./data` with a subdirectory for each type of plant. Images are labeled as `healthy-i.jpg` or `diseased-i.jpg`
- `create_train_test.py`: creates a new directory `./dataset` given `./data` with train/test split and a subdirectory for `healthy` and `diseased` images so its compatible `torchvision.datasets.ImageFolder`
- `utils.py`: contains training and test functions called by `leaf_classification.ipynb` to create a binary classifier