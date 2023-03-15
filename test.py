#!/usr/bin/python3

import sys
import random

from katakana import kana, kana_reg

# 💮🔰


if __name__ == '__main__' :
    total = 0
    success = 0
    failed = 0
    kana_items = list(kana.items())
    print('🇯🇵 どうも (dōmo)\n')
    try :
        while True :
            kana_name, kana_char = random.choice(kana_items)
            guess = input(f"{kana_char} ")
            if guess == kana_name :
                print(f"✅ \033[1;32m{kana_char} {guess}\033[0m")
                success += 1
            elif guess == '?' :
                print(f"❗ \033[1;34m{kana_char} {kana_name}\033[0m")
                failed += 1
            elif guess in kana :
                print(f"❌ \033[1;31m{kana[guess]} {guess}\033[0m -> \033[1;34m{kana_char} {kana_name}\033[0m")
                failed += 1
            else :
                print(f"❌ \033[1;31m{guess}\033[0m -> \033[1;34m{kana_char} {kana_name}\033[0m")
                failed += 1
            total += 1
            print('')
    except KeyboardInterrupt :
        pass
    if total > 0 :
        message = f"attempts: {total}, success: {success}, miss: {failed}"
        accuracy = 100 * success / total
        print(f"\n{'=' * (len(message) + 2)}\n {message}\n accuracy: {accuracy:.2f}%\n{'=' * (len(message) + 2)}")


"""
if __name__ == '__main__' :
    word = input('Enter a word to be translated in katakana > ')
    chars = kana_reg.findall(word)
    if sum(len(c) for c in chars) != len(word) :
        print('Invalid word')
        sys.exit(1)
    res = []
    for char in chars :
        if char in kana :
            res.append(kana[char])
        else :
            print(f"Invalid kana {char}")
            sys.exit(1)
    print(''.join(res))
"""
