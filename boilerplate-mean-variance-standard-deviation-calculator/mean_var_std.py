import numpy as np

def calculate(list):
    if len(list) != 9 :
        raise ValueError("List must contain nine numbers.")
    arr = np.array(list)
    arr = arr.reshape(3, 3)
    calculations = {}
    calculations['mean'] = [np.mean(arr, axis=0).tolist(), np.mean(arr, axis=1).tolist(), np.mean(arr).tolist()]
    calculations['variance'] = [np.var(arr, axis=0).tolist(), np.var(arr, axis=1).tolist(), np.var(arr).tolist()]
    calculations['standard deviation'] = [np.std(arr, axis=0).tolist(), np.std(arr, axis=1).tolist(), np.std(arr).tolist()]
    calculations['max'] = [np.max(arr, axis=0).tolist(), np.max(arr, axis=1).tolist(), np.max(arr).tolist()]
    calculations['min'] = [np.min(arr, axis=0).tolist(), np.min(arr, axis=1).tolist(), np.min(arr).tolist()]
    calculations['sum'] = [np.sum(arr, axis=0).tolist(), np.sum(arr, axis=1).tolist(), np.sum(arr).tolist()]
    return calculations