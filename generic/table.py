
from typing import Sequence

from generic.kana import Kana

class KanaTable :
    
    def __init__(self, kana: Sequence[Kana]) :
        self.romaji = {}
        self.kana = kana
        for k in kana :
            if k.romaji not in self.romaji :
                self.romaji[k.romaji] = [k]
            else :
                self.romaji[k.romaji].append(k)

    def has_romaji(self, romaji: str) -> bool :
        return romaji in self.romaji

    def get_chars(self, romaji: str) -> "list[str]" :
        return [k.char for k in self.romaji[romaji]]

