import pathlib
import shutil
import random

"""
Creates an output folder that splits the data into train and test set.
For each split, there will be a "Healthy" and "Diseased" subfolder. This
allows each set to be loaded in pyTorch with ImageFolder Dataset.

The train/test split are stratified (i.e. preserves the proportions of each 
type of plants in the split)

- 'ratio' specifies the split ratio
- 'directory' is the raw data location
- 'output' is the processed data location

"""

directory = pathlib.Path('data')
output = pathlib.Path('dataset')

random.seed(0)
ratio = 0.8

def split_list(lst, ratio):
    """
    Splits a list into two sublists based on a given ratio.

    Parameters:
        lst (list): The list to split.
        ratio (float): The ratio of the first sublist to the total length of the list.

    Returns:
        A tuple of two sublists, where the first sublist contains ratio * len(lst) elements,
        and the second sublist contains (1 - ratio) * len(lst) elements.
    """
    random.shuffle(lst)  # Shuffle the list randomly
    split_index = int(ratio * len(lst))  # Calculate the split index based on the ratio
    return lst[:split_index], lst[split_index:]  # Return two sublists based on the split index



train_path = output / "train"
test_path = output / "test"
healthy_train_path = train_path / "healthy"
diseased_train_path = train_path / "diseased"
healthy_test_path = test_path / "healthy"
diseased_test_path = test_path / "diseased"

healthy_train_path.mkdir(parents=True, exist_ok=True)
diseased_train_path.mkdir(parents=True, exist_ok=True)
healthy_test_path.mkdir(parents=True, exist_ok=True)
diseased_test_path.mkdir(parents=True, exist_ok=True)

for item in directory.iterdir():
    if not item.is_dir():
        continue

    print(f"Processing folder: {item.name}")
    

    img_list = [item for item in item.iterdir()]    
    train, test = split_list(img_list, ratio)

    for img in train:
        if (img.name.startswith("healthy")):
            shutil.copy2(img, healthy_train_path / f"{item.name}-{img.name}")
        elif (img.name.startswith("diseased")):
            shutil.copy2(img, diseased_train_path / f"{item.name}-{img.name}")


    for img in test:
        if (img.name.startswith("healthy")):
            shutil.copy2(img, healthy_test_path / f"{item.name}-{img.name}")
        elif (img.name.startswith("diseased")):
            shutil.copy2(img, diseased_test_path / f"{item.name}-{img.name}")