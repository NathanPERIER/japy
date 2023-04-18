
from enum import Enum

class Diacritic(Enum) :
    NONE       = 0
    DAKUTEN    = 1
    HANDAKUTEN = 2

VOWEL_LENGTHENER = 'ー'


class Kana :
    
    def __init__(self, char: str, romaji: str, consonant: str = None, diacritic = Diacritic.NONE) :
        self.char      = char
        self.romaji    = romaji
        self.vowel     = romaji[-1]
        self.consonant = consonant
        self.diacritic = diacritic

    def has_diacritic(self) -> bool :
        return self.diacritic != Diacritic.NONE

    def __str__(self) :
        return f"{self.char} ({self.romaji})"


