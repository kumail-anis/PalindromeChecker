# https://docs.python.org/3/library/unittest.html
import unittest
from Palindrome import isPalindrome


class TestPalindrome(unittest.TestCase):

    # phrases taken from https://www.grammarly.com/blog/16-surprisingly-funny-palindromes/ and http://www.word-buff.com/single-word-palindromes.html

    def test_for_mirror(self):
        # simple palindromes that are mirrored strings
        print('\033[1m' + '\033[4m' + "result for def test_for_mirror")
        print("")
        assert isPalindrome('AAA') is True
        assert isPalindrome('A') is True
        assert isPalindrome('AMANAPLANACANALPANAMA') is True
        assert isPalindrome('MADAM') is True
        assert isPalindrome('noon') is True
        assert isPalindrome('SERES') is True
        assert isPalindrome('racecar') is True
        print("")

    def test_for_mixed_casing(self):
        # palindromes with mixed leter casing
        print('\033[1m' + '\033[4m' + "result for test_for_mixing_casing")
        print("")
        assert isPalindrome('cCcC') is True
        assert isPalindrome('SiRiS') is True
        assert isPalindrome('MaDaM') is True
        assert isPalindrome('roTor') is True
        print("")

    def test_with_whitespace(self):
        # palindromes with whitespace
        print('\033[1m' + '\033[4m' + "result for test_with_whitespace")
        print("")
        assert isPalindrome('mad am') is True
        assert isPalindrome('rot or') is True
        assert isPalindrome('race fast safe car') is True
        print("")

    def test_with_whitespace_and_mixed_casing(self):
        # palindromes with whitespace and mixed letter casing
        print('\033[1m' + '\033[4m' + "result for test_with_whitespace_and_mixed_casing")
        print("")
        assert isPalindrome('mad Am') is True
        assert isPalindrome('roT Or') is True
        assert isPalindrome('Race Fast Safe Car') is True
        print("")

    def test_with_whitespace_and_punctuation(self):
        # palindromes with whitespace and punctuation
        print('\033[1m' + '\033[4m' + "result for test_with_whitespace_and_punctuation")
        print("")
        assert isPalindrome('mad am!') is True
        assert isPalindrome('rot or!!') is True
        assert isPalindrome('race fast, safe car.') is True
        print("")

    def test_with_mixed_casing_and_punctuation(self):
        # palindromes with whitespace, punctuation and mixed letter casing
        print('\033[1m' + '\033[4m' + "result for test_with_mixed_casing_and_punctuation")
        print("")
        assert isPalindrome('Race fast, safe car.') is True
        assert isPalindrome('SHAHS, SUsus Stets u STETS SUSUS SHAHS?') is True
        assert isPalindrome("Go hang a salami, I'm a lasagna hog.") is True
        assert isPalindrome('Ed, I saw Harpo Marx ram Oprah W. aside.') is True
        print("")

        #negative testing
    def test_with_non_palindrome(self):
        print('\033[1m' + '\033[4m' + "result for test_with_non_palindrome")
        print("")
        assert isPalindrome('Th!is') is False
        assert isPalindrome('I@S') is False
        assert isPalindrome('Tes#ting') is False
        assert isPalindrome('Fal$e') is False
        assert isPalindrome('Resu^&*(lts!') is False
        print("")

if __name__ == '__main__':
    unittest.main()
