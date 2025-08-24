# test_keywordextraction.py
"""
Tests for KeywordExtraction module.
"""

import unittest
from keywordextraction import KeywordExtraction

class TestKeywordExtraction(unittest.TestCase):
    """Test cases for KeywordExtraction class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = KeywordExtraction()
        self.assertIsInstance(instance, KeywordExtraction)
        
    def test_run_method(self):
        """Test the run method."""
        instance = KeywordExtraction()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
