import numpy as np


def probability_of_failure(fos_values):

    return np.sum(fos_values < 1.0) / len(fos_values)


def reliability_index(fos_values):

    mean_fos = np.mean(fos_values)

    std_fos = np.std(fos_values)

    beta = (mean_fos - 1.0) / std_fos

    return beta
