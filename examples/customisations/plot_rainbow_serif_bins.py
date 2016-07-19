"""
=======================
Rainbow and Custom Bins
=======================

Invoke rainbow colour scheme and choose how many bins to use with your data.

By default, the rainbow colour scheme is used if you have many, many chains. You can
enable it before that point if you wish. You can also pick how many bins you want to
display your data with.

"""
import numpy as np
from numpy.random import normal, random, multivariate_normal
from chainconsumer import ChainConsumer


if __name__ == "__main__":
    np.random.seed(0)
    cov = 0.3 * random(size=(3, 3)) + np.identity(3)
    data = multivariate_normal(normal(size=3), 0.5 * (cov + cov.T), size=100000)
    cov = 0.3 * random(size=(3, 3)) + np.identity(3)
    data2 = multivariate_normal(normal(size=3), 0.5 * (cov + cov.T), size=100000)
    cov = 0.3 * random(size=(3, 3)) + np.identity(3)
    data3 = multivariate_normal(normal(size=3), 0.5 * (cov + cov.T), size=100000)
    cov = 0.3 * random(size=(3, 3)) + np.identity(3)
    data4 = multivariate_normal(normal(size=3), 0.5 * (cov + cov.T), size=100000)

    c = ChainConsumer()
    c.add_chain(data, name="A")
    c.add_chain(data2, name="B")
    c.add_chain(data3, name="C")
    c.add_chain(data4, name="D")
    c.configure_general(bins=150,rainbow=True)
    fig = c.plot()

    fig.set_size_inches(2.5 + fig.get_size_inches())  # Resize fig for doco. You don't need this.
