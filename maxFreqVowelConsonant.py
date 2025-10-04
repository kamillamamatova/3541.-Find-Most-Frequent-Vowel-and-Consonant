class Solution:
    def maxFreqSum(self, s: str) -> int:
        # Frequency counter
        counter = Counter(s)

        # Finds the highest frequency of vowels
        vowel = max((counter[ch] for ch in counter if ch in "aeiou"), default = 0)

        # Finds the highest frequency of consonants
        consonant = max((counter[ch] for ch in counter if ch not in "aeiou"), default = 0)

        # Returns the sum of the highest frequencies
        return vowel + consonant
