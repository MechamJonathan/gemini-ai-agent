

import unittest
from functions import get_files_info

class TestFunctions(unittest.TestCase):

    def test_get_files_info(self):
        get_files_info.get_files_info("calculator", ".")
        
    


if __name__ == "__main__":
    unittest.main()