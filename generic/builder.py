
from generic.kana import Kana, Diacritic, KanaVoicing, SpecificUsageTag
from generic.table import KanaTable

from typing import Sequence, Tuple, Union, Optional

KanaVoicingInit = Tuple[str,Diacritic]

GroupInitialiserList = Sequence[Union[Tuple[str,str], Tuple[str,str,SpecificUsageTag], Tuple[str,str,KanaVoicingInit], Tuple[str,str,KanaVoicingInit,SpecificUsageTag]]]


class KanaTableBuilder :

    def __init__(self) :
        self.kana = []

    def add_group(self, cons: Optional[str], conf: GroupInitialiserList) :
        for c in conf :
            tag = SpecificUsageTag.NONE
            voicing = None
            if len(c) == 3 and type(c[2]) == SpecificUsageTag :
                tag = c[2]
            elif len(c) in [3, 4] :
                voicing = KanaVoicing(c[2][0], c[2][1])
            if len(c) == 4 :
                tag = c[3]
            self.kana.append(Kana(c[0], c[1], cons, voicing, tag))

    def build_table(self) -> KanaTable :
        return KanaTable(self.kana)

