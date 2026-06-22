import numpy as np

from fos import factor_of_safety


def run_monte_carlo(n=10000):

    c = np.random.normal(25, 5, n)

    phi = np.random.normal(35, 3, n)

    gamma = np.random.normal(20, 1, n)

    fos_results = []

    for i in range(n):

        fos = factor_of_safety(
            c[i],
            phi[i],
            gamma[i],
            z=5,
            beta=30
        )

        fos_results.append(fos)

    return np.array(fos_results)


if __name__ == "__main__":

    fos_values = run_monte_carlo()

    print("Mean FoS =", np.mean(fos_values))

    print("Std Dev =", np.std(fos_values))
