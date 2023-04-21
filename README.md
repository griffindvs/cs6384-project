# Detecting Plant Diseases in Browser Using Efficient Deep Learning
>We examine the comparative performance of EfficientNet and MobileNet, two lightweight image classification neural networks, and AlexNet, a large-scale image classification network in detecting disease on the leaves of plants of 21 species. Both the predictive performance of the models as well as their computational efficiency are tested in multiple environments. To determine the ability of each of these models to be used away from computers with high computational resources, the models will be run in browsers on mobile devices.

This repository applies transfer learning on pre-trained classification models (from the [PyTorch pretrained model hub](https://pytorch.org/hub/)) to detect if an image of a plant leaf is healthy or diseased. The main notebook `leaf_classification.ipynb` trains and test various models, and exports the final models as ONNX files. `./plant-disease-web` contains the web app that runs the models using the [ONNX Runtime for Web](https://onnxruntime.ai/docs/tutorials/web/).

## Python Model-Training Setup
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
- While training, metrics on the validation set can be monitored in real-time using TensorBoard. The dashboard can be accessed by running:
    ```
    tensorboard --logdir=runs
    ```
    and visiting `localhost:6006`

## Web Application
The application used here is a modified version of the ONNX Runtime Web [Image Classifier Template](https://onnxruntime.ai/docs/tutorials/web/classify-images-nextjs-github-template.html).

### Environment and Dependencies Requirements
- Node == 16.x

### Getting Started
- Move exported ONNX model files to the deployment directory: `./plant-disease-web/model`
    - Supported models without additional configuration are:
        - `efficientnet-b4-40.onnx`
        - `mobilenetv3-20.onnx`
        - `mobilenetv3-s-20.onnx`
        - `resnet18-20.onnx`
        - `resnet50-95.onnx`
- Switch to the web application directory: `./plant-disease-web`
- Install dependencies by running:
    ```
    npm install
    ```
- Run the [Next.js](https://nextjs.org/) server:
    ```
    npm run dev
    ```
- Access the development server at `localhost:3000`
- Build the application for production:
    ```
    npm run buld
    ```

## Additional Scripts
- `data_merge.py`: parses the original datasets and creates a merged directory `./data` with a subdirectory for each type of plant. Images are labeled as `healthy-i.jpg` or `diseased-i.jpg`
- `create_train_test.py`: creates a new directory `./dataset` given `./data` with train/test split and a subdirectory for `healthy` and `diseased` images so its compatible `torchvision.datasets.ImageFolder`
- `utils.py`: contains training and test functions called by `leaf_classification.ipynb` to create a binary classifier