#!/usr/bin/python3

import sys
import random
from collections import deque

from katakana.kana import builder

# 💮🔰


if __name__ == '__main__' :
    total = 0
    success = 0
    miss = 0
    buffer_size = 10
    buffer = deque()
    table = builder.build_table()
    kana_list = list(table.kana)
    print('🎌 どうも (dōmo)\n') # 🇯🇵
    try :
        while True :
            kana = kana_list.pop(random.randrange(len(kana_list)))
            guess = input(f"{kana.char} ")
            if guess == kana.romaji :
                print(f"✅ \033[1;32m{kana.char} {guess}\033[0m")
                success += 1
            else :
                if table.has_romaji(guess) :
                    chars = "/".join(table.get_chars(guess))
                    print(f"❌ \033[1;31m{chars} {guess}\033[0m -> \033[1;34m{kana.char} {kana.romaji}\033[0m")
                else :
                    print(f"❌ \033[1;31m{guess}\033[0m -> \033[1;34m{kana.char} {kana.romaji}\033[0m")
                miss += 1
            total += 1
            buffer.append(kana)
            if len(buffer) > buffer_size :
                kana_list.append(buffer.popleft())
            print('')
    except KeyboardInterrupt :
        pass
    except EOFError :
        pass
    print('')
    if total > 0 :
        message = f"attempts: {total}, success: {success}, miss: {miss}"
        accuracy = 100 * success / total
        print(f"{'=' * (len(message) + 2)}\n {message}\n accuracy: {accuracy:.2f}%\n{'=' * (len(message) + 2)}")
