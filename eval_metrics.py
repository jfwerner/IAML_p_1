from sklearn.metrics import confusion_matrix
import numpy as np

confmat = confusion_matrix(np.array([0,0,0,1,1,1]), np.array([0,1,0,1,1,1]))

print(confmat)

def evaluate(confmat):
    [[TN, FP], [FN, TP]] = confmat
    acc = (TP+TN) / (TP+TN+FP+FN) # percentage of all samples labeled correctly
    sensitivity = TP / (TP+FN) # percentage of the postives labeled correctly
    specificity = TN / (TN+FP) # percentage of the negatives labeled correctly
    precision = TP / (TP+FP)   # percentage of correctly predicted from predicted as positive
    negative_pred_value = TN / (TN+FN) # percentage of correctly predicted from predicted as negative

    return np.array([acc, sensitivity, specificity, precision, negative_pred_value])


print(evaluate(confmat))




