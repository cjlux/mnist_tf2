import matplotlib.pyplot as plt

def plot(history):
    # Plot training & validation accuracy values, giving an argument 'history' 
    # of type 'tensorflow.python.keras.callbacks.History':
    
    plt.figure(figsize=(15,5))
    ax1 = plt.subplot(1,2,1)
    if history.history.get('accuracy'):
        ax1.plot(history.history['accuracy'], 'o-',label='Train')
    if history.history.get('val_accuracy'):
        ax1.plot(history.history['val_accuracy'], 'o-', label='Test')
    ax1.set_title('Model accuracy')
    ax1.set_ylabel('Accuracy')
    ax1.set_xlabel('Epoch') 
    ax1.grid()
    ax1.legend(loc='best')
    
    # Plot training & validation loss values
    ax2 = plt.subplot(1,2,2)
    if history.history.get('loss'):
        ax2.plot(history.history['loss'], 'o-', label='Train')
    if history.history.get('val_loss'):
        ax2.plot(history.history['val_loss'], 'o-',  label='Test')
    ax2.set_title('Model loss')
    ax2.set_ylabel('Loss')
    ax2.set_xlabel('Epoch')
    ax2.legend(loc='best')
    ax2.grid()
    plt.show()

import sklearn
from sklearn.metrics import confusion_matrix    
import seaborn as sns

def plot_cm(labels, predictions, p=0.5):
      cm = confusion_matrix(labels, predictions > p)
      plt.figure(figsize=(5,5))
      sns.heatmap(cm, annot=True, fmt="d")
      plt.title('Confusion matrix @{:.2f}'.format(p))
      plt.ylabel('Actual label')
      plt.xlabel('Predicted label')

      print('Legitimate Transactions Detected (True Negatives): ', cm[0][0])
      print('Legitimate Transactions Incorrectly Detected (False Positives): ', cm[0][1])
      print('Fraudulent Transactions Missed (False Negatives): ', cm[1][0])
      print('Fraudulent Transactions Detected (True Positives): ', cm[1][1])
      print('Total Fraudulent Transactions: ', np.sum(cm[1]))
