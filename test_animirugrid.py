# test_animirugrid.py
"""
Tests for AnimiruGrid module.
"""

import unittest
from animirugrid import AnimiruGrid

class TestAnimiruGrid(unittest.TestCase):
    """Test cases for AnimiruGrid class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AnimiruGrid()
        self.assertIsInstance(instance, AnimiruGrid)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AnimiruGrid()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
