
from generic.kana import Kana, Diacritic, ConsonantVoicing, SpecificUsageTag
from generic.table import KanaTable

from typing import Sequence, Tuple, Union, Optional

GroupConsonant = Union[Optional[str], Tuple[str,str,Diacritic]]

GroupInitialiserList = Sequence[Union[Tuple[str,str], Tuple[str,str,SpecificUsageTag]]]


class KanaTableBuilder :

    def __init__(self) :
        self.kana = []

    def add_group(self, cons: GroupConsonant, conf: GroupInitialiserList) :
        if cons is None :
            consonant = None
            voicing   = None
        elif type(cons) == str :
            consonant = cons
            voicing   = None
        else :
            consonant = cons[0]
            voicing   = ConsonantVoicing(cons[1], cons[2])
        for c in conf :
            tag = SpecificUsageTag.NONE if len(c) == 2 else c[2]
            self.kana.append(Kana(c[0], c[1], consonant, voicing, tag))

    def build_table(self) -> KanaTable :
        return KanaTable(self.kana)

