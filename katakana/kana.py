
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
    ('ヲ', 'wo', SpecificUsageTag.RARE),
    ('ウィ', 'wi', SpecificUsageTag.FOREIGN_TRANSCRIPTION),
    ('ウェ', 'we', SpecificUsageTag.FOREIGN_TRANSCRIPTION),
    ('ウォ', 'wo', SpecificUsageTag.FOREIGN_TRANSCRIPTION)
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

builder.add_group('f', [
    ('ファ', 'fa', SpecificUsageTag.FOREIGN_TRANSCRIPTION),
    ('フィ', 'fi', SpecificUsageTag.FOREIGN_TRANSCRIPTION),
    ('フェ', 'fe', SpecificUsageTag.FOREIGN_TRANSCRIPTION),
    ('フォ', 'fo', SpecificUsageTag.FOREIGN_TRANSCRIPTION)
])

builder.add_group('v', [
    ('ヴァ', 'va', SpecificUsageTag.FOREIGN_TRANSCRIPTION),
    ('ヴィ', 'vi', SpecificUsageTag.FOREIGN_TRANSCRIPTION),
    ('ヴ',   'vu', ['ウ', Diacritic.DAKUTEN], SpecificUsageTag.FOREIGN_TRANSCRIPTION),
    ('ヴェ', 've', SpecificUsageTag.FOREIGN_TRANSCRIPTION),
    ('ヴォ', 'vo', SpecificUsageTag.FOREIGN_TRANSCRIPTION)
])
