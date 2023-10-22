import unittest

class TestHistogramDistribution(unittest.TestCase):
    def test_sample(self):
        values = [1, 2, 3]
        probabilities = [0.2, 0.3, 0.5]
        distribution = HistogramDistribution(values, probabilities)

        sampled_value = distribution.sample()
        self.assertIn(sampled_value, values)  # Check if the sampled value is one of the possible values


class TestRUDSDescriptor(unittest.TestCase):
    def test_resampling(self):
        method = lambda x: x
        descriptor = RUDSDescriptor(method)
        instance = object()
        owner = object()
        resampled_value = descriptor.__get__(instance, owner)
        self.assertIn(resampled_value, [1, 2, 3])  # Check if the value is one of the possible values

class TestRUDSMeta(unittest.TestCase):
    def test_method_resampling(self):
        class TestClass(metaclass=RUDSMeta):
            def method(self):
                return 42

        instance = TestClass()
        resampled_value = instance.method  # Accessing the method should trigger resampling
        self.assertEqual(resampled_value, 42)  # Check if the value is the expected result

class TestRUDSObject(unittest.TestCase):
    def setUp(self):
        self.distribution = HistogramDistribution([1, 2, 3], [0.2, 0.3, 0.5])

    def test_attribute_resampling(self):
        ruds_obj = RUDSObject(self.distribution)
        resampled_value = ruds_obj.distribution.sample()  # Trigger resampling explicitly
        self.assertIn(resampled_value, [1, 2, 3])  # Check if the value is one of the possible values

if __name__ == '__main__':
    unittest.main()

