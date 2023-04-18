
from generic.kana import Kana, Diacritic
from generic.table import KanaTable

from typing import Sequence, Tuple, Union, Optional

GroupConsonant = Union[Optional[str], Tuple[str,str,Diacritic]]

GroupInitialiserList = Sequence[Union[Tuple[str,str], Tuple[str,str,str]]]


class KanaTableBuilder :

    def __init__(self) :
        self.kana = []

    def add_group(self, consonant: GroupConsonant, conf: GroupInitialiserList) :
        for c in conf :
            self.kana.append(Kana(c[0], c[1]))

    def build_table(self) -> KanaTable :
        return KanaTable(self.kana)

