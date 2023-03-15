
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

iteration_mark = 'ヽ'
iteration_mark_voiced = 'ヾ'

sokuon = 'ッ'

vowel_lenghtener = 'ー'


# https://www.kaggle.com/code/gpreda/japanese-world-of-words/input ?


import re

kana_reg = re.compile('[^aiueo]?[^aiueo][aiueo]|[aiueon]')

