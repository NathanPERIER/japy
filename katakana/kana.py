
from typing import Mapping

from generic.kana import Diacritic, SpecificUsageTag
from generic.builder import KanaTableBuilder

small_chars: Mapping[str, str] = {
    'ャ': 'ヤ',
    'ュ': 'ユ',
    'ョ': 'ヨ',
    'ァ': 'ア',
    'ィ': 'イ',
    'ゥ': 'ウ',
    'ェ': 'エ',
    'ォ': 'オ'
}

iteration_mark = 'ヽ'
iteration_mark_voiced = 'ヾ'

sokuon = 'ッ'

vowel_lenghtener = 'ー'


builder = KanaTableBuilder()

builder.add_group(None, [
    ('ア', 'a'),
    ('イ', 'i'),
    ('ウ', 'u'),
    ('エ', 'e'),
    ('オ', 'o')
])

builder.add_group('k', [
    ('カ',   'ka'),
    ('キ',   'ki'),
    ('ク',   'ku'),
    ('ケ',   'ke'),
    ('コ',   'ko'),
    ('キャ', 'kya'),
    ('キュ', 'kyu'),
    ('キョ', 'kyo')
])

builder.add_group('s', [
    ('サ',   'sa'),
    ('シ',   'shi'),
    ('ス',   'su'),
    ('セ',   'se'),
    ('ソ',   'so'),
    ('シャ', 'sha'),
    ('シュ', 'shu'),
    ('ショ', 'sho')
])

builder.add_group('t', [
    ('タ',   'ta'),
    ('チ',   'chi'),
    ('ツ',   'tsu'),
    ('テ',   'te'),
    ('ト',   'to'),
    ('チャ', 'cha'),
    ('チュ', 'chu'),
    ('チョ', 'cho'),
    ('ティ', 'ti', SpecificUsageTag.FOREIGN_TRANSCRIPTION),
    ('トゥ', 'tu', SpecificUsageTag.FOREIGN_TRANSCRIPTION)
])

builder.add_group('n', [
    ('ナ',   'na'),
    ('ニ',   'ni'),
    ('ヌ',   'nu'),
    ('ネ',   'ne'),
    ('ノ',   'no'),
    ('ニャ', 'nya'),
    ('ニュ', 'nyu'),
    ('ニョ', 'nyo')
])

builder.add_group('h', [
    ('ハ',   'ha'),
    ('ヒ',   'hi'),
    ('フ',   'fu'),
    ('ヘ',   'he'),
    ('ホ',   'ho'),
    ('ヒャ', 'hya'),
    ('ヒュ', 'hyu'),
    ('ヒョ', 'hyo')
])

builder.add_group('m', [
    ('マ',   'ma'),
    ('ミ',   'mi'),
    ('ム',   'mu'),
    ('メ',   'me'),
    ('モ',   'mo'),
    ('ミャ', 'mya'),
    ('ミュ', 'myu'),
    ('ミョ', 'myo')
])

builder.add_group('y', [
    ('ヤ', 'ya'),
    ('ユ', 'yu'),
    ('ヨ', 'yo')
])
    
builder.add_group('r', [
    ('ラ',   'ra'),
    ('リ',   'ri'),
    ('ル',   'ru'),
    ('レ',   're'),
    ('ロ',   'ro'),
    ('リャ', 'rya'),
    ('リュ', 'ryu'),
    ('リョ', 'ryo')
])

builder.add_group('w', [
    ('ワ', 'wa'),
    ('ヰ', 'wi', SpecificUsageTag.DEPRECATED),
    ('ヱ', 'we', SpecificUsageTag.DEPRECATED),
    ('ヲ', 'wo', SpecificUsageTag.RARE)
])

builder.add_group('n', [('ン', 'n')])

builder.add_group('g', [
    ('ガ',   'ga', ['カ', Diacritic.DAKUTEN]),
    ('ギ',   'gi', ['キ', Diacritic.DAKUTEN]),
    ('グ',   'gu', ['ク', Diacritic.DAKUTEN]),
    ('ゲ',   'ge', ['ケ', Diacritic.DAKUTEN]),
    ('ゴ',   'go', ['コ', Diacritic.DAKUTEN]),
    ('ギャ', 'gya'),
    ('ギュ', 'gyu'),
    ('ギョ', 'gyo')
])

builder.add_group('z', [
    ('ザ',   'za', ['サ', Diacritic.DAKUTEN]),
    ('ジ',   'ji', ['シ', Diacritic.DAKUTEN]),
    ('ズ',   'zu', ['ス', Diacritic.DAKUTEN]),
    ('ゼ',   'ze', ['セ', Diacritic.DAKUTEN]),
    ('ゾ',   'zo', ['ソ', Diacritic.DAKUTEN]),
    ('ジャ', 'ja'),
    ('ジュ', 'ju'),
    ('ジョ', 'jo')
])

builder.add_group('d', [
    ('ダ',   'da', ['タ', Diacritic.DAKUTEN]),
    ('ヂ',   'ji', ['チ', Diacritic.DAKUTEN], SpecificUsageTag.RARE),
    ('ヅ',   'zu', ['ツ', Diacritic.DAKUTEN], SpecificUsageTag.RARE),
    ('デ',   'de', ['テ', Diacritic.DAKUTEN]),
    ('ド',   'do', ['ト', Diacritic.DAKUTEN]),
    ('ヂャ', 'ja', SpecificUsageTag.RARE),
    ('ヂュ', 'ju', SpecificUsageTag.RARE),
    ('ヂョ', 'jo', SpecificUsageTag.RARE),
    ('ディ', 'di', SpecificUsageTag.FOREIGN_TRANSCRIPTION),
    ('ドゥ', 'du', SpecificUsageTag.FOREIGN_TRANSCRIPTION)
])

builder.add_group('b', [
    ('バ',   'ba', ['ハ', Diacritic.DAKUTEN]),
    ('ビ',   'bi', ['ヒ', Diacritic.DAKUTEN]),
    ('ブ',   'bu', ['フ', Diacritic.DAKUTEN]),
    ('ベ',   'be', ['ヘ', Diacritic.DAKUTEN]),
    ('ボ',   'bo', ['ホ', Diacritic.DAKUTEN]),
    ('ビャ', 'bya'),
    ('ビュ', 'byu'),
    ('ビョ', 'byo')
])

builder.add_group('p', [
    ('パ',   'pa', ['ハ', Diacritic.HANDAKUTEN]),
    ('ピ',   'pi', ['ヒ', Diacritic.HANDAKUTEN]),
    ('プ',   'pu', ['フ', Diacritic.HANDAKUTEN]),
    ('ペ',   'pe', ['ヘ', Diacritic.HANDAKUTEN]),
    ('ポ',   'po', ['ホ', Diacritic.HANDAKUTEN]),
    ('ピャ', 'pya'),
    ('ピュ', 'pyu'),
    ('ピョ', 'pyo')
])


"""
Others (transcription of foreign sounds)

ファ fa 	フィ fi 	フェ fe 	フォ fo
ヴァ va 	ヴィ vi 	ヴ vu   	ヴェ ve 	ヴォ vo

ホゥ hu
?   ラ゜ la 	リ゜ li 	ル゜ lu 	レ゜ le 	ロ゜ lo 

"""


"""
kana = {
    'a':   'ア', 'i':   'イ', 'u':   'ウ', 'e':  'エ', 'o':  'オ',
    'ka':  'カ', 'ki':  'キ', 'ku':  'ク', 'ke': 'ケ', 'ko': 'コ', 'kya': 'キャ', 'kyu': 'キュ', 'kyo': 'キョ', # K
    'sa':  'サ', 'shi': 'シ', 'su':  'ス', 'se': 'セ', 'so': 'ソ', 'sha': 'シャ', 'shu': 'シュ', 'sho': 'ショ', # S
    'ta':  'タ', 'chi': 'チ', 'tsu': 'ツ', 'te': 'テ', 'to': 'ト', 'cha': 'チャ', 'chu': 'チュ', 'cho': 'チョ', # T
    'na':  'ナ', 'ni':  'ニ', 'nu':  'ヌ', 'ne': 'ネ', 'no': 'ノ', 'nya': 'ニャ', 'nyu': 'ニュ', 'nyo': 'ニョ', # N
    'ha':  'ハ', 'hi':  'ヒ', 'fu':  'フ', 'he': 'ヘ', 'ho': 'ホ', 'hya': 'ヒャ', 'hyu': 'ヒュ', 'hyo': 'ヒョ', # H
    'ma':  'マ', 'mi':  'ミ', 'mu':  'ム', 'me': 'メ', 'mo': 'モ', 'mya': 'ミャ', 'myu': 'ミュ', 'myo': 'ミョ', # M
    'ya':  'ヤ',              'yu':  'ユ',             'yo': 'ヨ',                                              # Y
    'ra':  'ラ', 'ri':  'リ', 'ru':  'ル', 're': 'レ', 'ro': 'ロ', 'rya': 'リャ', 'ryu': 'リュ', 'ryo': 'リョ', # R
    'wa':  'ワ',                                       'wo': 'ヲ',                                              # W
    'n':   'ン',
    'ga':  'ガ', 'gi':  'ギ', 'gu':  'グ', 'ge': 'ゲ', 'go': 'ゴ', 'gya': 'ギャ', 'gyu': 'ギュ', 'gyo': 'ギョ', # G
    'za':  'ザ', 'ji':  'ジ', 'zu':  'ズ', 'ze': 'ゼ', 'zo': 'ゾ', 'ja':  'ジャ', 'ju':  'ジュ', 'jo':  'ジョ', # Z
    'da':  'ダ', 'dji': 'ヂ', 'dzu': 'ヅ', 'de': 'デ', 'do': 'ド',                                              # D
    'ba':  'バ', 'bi':  'ビ', 'bu':  'ブ', 'be': 'ベ', 'bo': 'ボ', 'bya': 'ビャ', 'byu': 'ビュ', 'byo': 'ビョ', # B
    'pa':  'パ', 'pi':  'ピ', 'pu':  'プ', 'pe': 'ペ', 'po': 'ポ', 'pya': 'ピャ', 'pyu': 'ピュ', 'pyo': 'ピョ', # P
}

# F	ファ fa	フィ fi	 	フェ fe	フォ fo	 	 	 
# T	ツァ tsa	ティ ti	トゥ tu	 	 	 	 	 
# W	 	 	 	ウェ we	ウォ wo	 	 	 
"""

