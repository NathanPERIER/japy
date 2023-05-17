
from enum import Enum
from typing import Final, Optional

VOWEL_LENGTHENER = 'ー'

class Diacritic(Enum) :
    DAKUTEN    = 1
    HANDAKUTEN = 2

class SpecificUsageTag(Enum) :
    NONE                  = 0
    DEPRECATED            = 1
    RARE                  = 2
    FOREIGN_TRANSCRIPTION = 3


class KanaVoicing :

    def __init__(self, consonant: str, diacritic: Diacritic) :
        assert len(consonant) == 1
        self.consonant: Final[str]       = consonant
        self.diacritic: Final[Diacritic] = diacritic


class Kana :
    
    def __init__(self, char: str, romaji: str, consonant: Optional[str], voicing: Optional[KanaVoicing], usage: SpecificUsageTag) :
        assert len(char) in [1, 2]
        assert consonant is None or len(consonant) == 1
        self.char:      Final[str]           = char
        self.romaji:    Final[str]           = romaji
        self.consonant: Final[Optional[str]] = consonant
        self.voicing: Final[Optional[KanaVoicing]] = voicing
        self.usage:   Final[SpecificUsageTag]      = usage

    def is_voiced(self) -> bool :
        return self.voicing is not None
    
    def is_sokuon(self) -> bool :
        return len(self.char) == 2

    def __str__(self) :
        return f"{self.char} ({self.romaji})"


