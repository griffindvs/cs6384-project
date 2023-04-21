import torch
import numpy as np
import torch.nn as nn
from torch.utils.tensorboard import SummaryWriter
from torch.utils.data import DataLoader
from timeit import default_timer as timer
from sklearn.metrics import precision_recall_fscore_support

'''
Utility functions used in `leaf_classification.ipynb` for training and testing
'''

def train(dataloader: DataLoader, 
          model: nn.Module, 
          loss_fn: nn.BCEWithLogitsLoss, 
          optimizer: torch.optim.Optimizer, 
          device: str, 
          epoch: int,
          writer: SummaryWriter):
    
    '''
    Trains a binary classification model and logs loss to TensorBoard
    '''

    size = len(dataloader.dataset)
    num_batches = len(dataloader)
    total_loss, correct = 0, 0
    model.train()
    for batch, (X, y) in enumerate(dataloader):
        X, y = X.to(device), y.to(device)

        # Compute prediction error
        pred = model(X).squeeze()
        loss = loss_fn(pred, y.float())
        total_loss += loss
        
        class_pred = (pred >= 0).int()
        correct += (class_pred == y).sum().item()

        # Backpropagation
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if batch % 100 == 0:
            loss, current = loss.item(), (batch + 1) * len(X)
            print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")

    total_loss /= num_batches
    correct /= size
    
    writer.add_scalar('Loss/train', total_loss, epoch)
    writer.add_scalar('Accuracy/train', correct, epoch)

    return model

def test(dataloader: DataLoader, 
          model: nn.Module, 
          loss_fn: nn.BCEWithLogitsLoss,
          device: str, 
          epoch: int,
          writer: SummaryWriter):
    
    '''
    Evaluates a binary classification model on these metrics and logs to TensorBoard:
    - Loss
    - Accuracy
    - F1
    - Precision
    - Recall
    '''

    size = len(dataloader.dataset)
    num_batches = len(dataloader)
    model.eval()
    test_loss, correct = 0, 0
    y_true = []
    y_pred = []
    with torch.no_grad():
        for X, y in dataloader:
            X, y = X.to(device), y.to(device)
            pred = model(X).squeeze()
            test_loss += loss_fn(pred, y.float()).item()

            class_pred = (pred >= 0).int()
            correct += (class_pred == y).sum().item()
            y_true.append(y)
            y_pred.append(pred)

    test_loss /= num_batches
    correct /= size

    np_y_true = torch.cat(y_true).cpu().numpy()
    np_y_pred = (torch.cat(y_pred).cpu().numpy() >= 0).astype(int)
    
    precision, recall, f1, _ = precision_recall_fscore_support(np_y_true, np_y_pred, average='binary')

    writer.add_scalar('Loss/val', test_loss, epoch)
    writer.add_scalar('Accuracy/val', correct, epoch)
    writer.add_scalar('Precision/val', precision, epoch)
    writer.add_scalar('Recall/val', recall, epoch)
    writer.add_scalar('f1/val', f1, epoch)

    print(f"Test Error: \n Accuracy: {(100*correct):>0.1f}%, Avg loss: {test_loss:>8f} ")
    print(f" Precision: {precision:>8f}, Recall: {recall:>8f}, f1: {f1:>8f} \n")

def inference(dataloader: DataLoader, 
              model: nn.Module, 
              loss_fn: nn.BCEWithLogitsLoss, 
              device: str):
    
    '''
    Evaluates a binary classification model on these metrics (WITHOUT logging to TensorBoard):
    - Loss
    - Accuracy
    - F1
    - Precision
    - Recall
    '''

    size = len(dataloader.dataset)
    num_batches = len(dataloader)
    model.to(device)
    model.eval()
    test_loss, correct = 0, 0
    y_true = []
    y_pred = []
    exec_times = []
    with torch.no_grad():
        for X, y in dataloader:
            start_time = timer()
            X, y = X.to(device), y.to(device)
            pred = model(X).squeeze(1)
            end_time = timer()
            test_loss += loss_fn(pred, y.float()).item()

            class_pred = (pred >= 0).int()
            correct += (class_pred == y).sum().item()
            y_true.append(y)
            y_pred.append(pred)
            exec_times.append(end_time - start_time)

    test_loss /= num_batches
    correct /= size

    np_y_true = torch.cat(y_true).cpu().numpy()
    np_y_pred = (torch.cat(y_pred).cpu().numpy() >= 0).astype(int)
    
    precision, recall, f1, _ = precision_recall_fscore_support(np_y_true, np_y_pred, average='binary')
    avg_exec_time = np.mean(exec_times)

    print(f"Test Error: \n Accuracy: {(100*correct):>0.3f}%, Avg loss: {test_loss:>8f} ")
    print(f" Precision: {precision:>8f}, Recall: {recall:>8f}, f1: {f1:>8f} Exec Time: {avg_exec_time:>8f}\n")