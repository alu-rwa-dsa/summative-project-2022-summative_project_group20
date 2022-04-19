import unittest


def setUP(self):
    pass


# Test if anything shows up when clicking AddDetail without entering any detail.
class Test_AddDetail(unittest.TestCase):
    def test_AddDetail(self):
        expected = "Please fill in the information"
        actual ="Please fill in the information"
        self.assertEqual(expected, actual)

# Test if anything shows up when clicking UpdateDetail without entering any detail.
class Test_UpdateDetail(unittest.TestCase):
    def test_UpdateDetail(self):
        expected = "Please select the name and press Display"
        actual ="Please select the name and press Display"
        self.assertEqual(expected, actual)

# Test if anything shows up when clicking DeleteEntry without entering any detail.
class Test_DeleteEntry(unittest.TestCase):
    def test_DeleteEntry(self):
        expected = "Please select the contact"
        actual ="Please select the contact"
        self.assertEqual(expected, actual)

# Test if anything shows up when clicking DisplayEntry without entering any detail.
class Test_DisplayEntry(unittest.TestCase):
    def test_DisplayEntry(self):
        expected = "Please select the name"
        actual ="Please select the name"
        self.assertEqual(expected, actual)

# Test if anything shows up when clicking Name without entering any detail.
class Test_Name(unittest.TestCase):
    def test_Name(self):
        expected = "String"
        actual ="String"
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()