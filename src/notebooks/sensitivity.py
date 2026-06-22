import numpy as np

from fos import factor_of_safety


def sensitivity_analysis():

    base_fos = factor_of_safety(
        c=25,
        phi=35,
        gamma=20,
        z=5,
        beta=30
    )

    parameters = {
        "c": [20, 30],
        "phi": [32, 38],
        "gamma": [19, 21]
    }

    results = {}

    for param, values in parameters.items():

        fos_values = []

        for value in values:

            if param == "c":
                fos = factor_of_safety(
                    value, 35, 20, 5, 30
                )

            elif param == "phi":
                fos = factor_of_safety(
                    25, value, 20, 5, 30
                )

            else:
                fos = factor_of_safety(
                    25, 35, value, 5, 30
                )

            fos_values.append(fos)

        results[param] = fos_values

    return results
