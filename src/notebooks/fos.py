import numpy as np

def factor_of_safety(c, phi, gamma, z, beta):
    """
    Infinite Slope Model

    Parameters
    ----------
    c : cohesion (kPa)
    phi : friction angle (degrees)
    gamma : unit weight (kN/m3)
    z : failure depth (m)
    beta : slope angle (degrees)

    Returns
    -------
    Factor of Safety
    """

    phi = np.radians(phi)
    beta = np.radians(beta)

    numerator = (
        c +
        gamma * z *
        (np.cos(beta)**2) *
        np.tan(phi)
    )

    denominator = (
        gamma * z *
        np.sin(beta) *
        np.cos(beta)
    )

    return numerator / denominator


if __name__ == "__main__":

    fos = factor_of_safety(
        c=25,
        phi=35,
        gamma=20,
        z=5,
        beta=30
    )

    print("Factor of Safety =", round(fos,3))
