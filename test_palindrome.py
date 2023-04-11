import unittest
from palindrome import palindromeiter
from palindrome import palindromerecu

class TestPalindrome(unittest.TestCase):
    def test1_palindrome_simple(self):
        result = palindromeiter("oso")
        self.assertEqual(result, True)

    def test2_palindrome_simple(self):
        result = palindromeiter("neuquen")
        self.assertEqual(result, True)

    def test3_palindrome_simple(self):
        result = palindromeiter("reconocer")
        self.assertEqual(result, True)

    def test1_palindrome_recu(self):
        result = palindromerecu("noakaon")
        self.assertEqual(result, True)

    def test2_palindrome_recu(self):
        result = palindromerecu("holaaloh")
        self.assertEqual(result, True)

if __name__=="__main__":
    unittest.main()