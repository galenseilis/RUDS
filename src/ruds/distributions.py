import random

class HistogramDistribution:
    """
    Custom distribution class for RUDSObject.

    This class defines a custom distribution with a `sample` method used for
    resampling values according to specified probabilities.
    """

    def __init__(self, values, probabilities):
        """
        Initialize the CustomDistribution with values and probabilities.

        Args:
            values (list): List of possible values to sample from.
            probabilities (list): List of probabilities corresponding to the values.
        """
        self.values = values
        self.probabilities = probabilities

    def sample(self):
        """
        Sample a value from the distribution based on probabilities.

        Returns:
            Any: The sampled value.
        """
        return random.choices(self.values, weights=self.probabilities)[0]
