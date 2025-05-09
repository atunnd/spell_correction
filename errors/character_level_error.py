import random
import re
import unicodedata
from .dictionary import tone_dict, tone_dict_vni, NEAR_KEYS

def telex_error(word):
    for i, char in enumerate(word):
        if char in tone_dict:
            base_char, telex_key = tone_dict[char]
            if not telex_key:
                return word  
            word = word.replace(char, base_char, 1) + telex_key
    return word  

def vni_error(word):
    for i, char in enumerate(word):
        if char in tone_dict:
            base_char, vni_key = tone_dict_vni[char]
            if not vni_key:
                return word 
            word = word.replace(char, base_char, 1) + vni_key
    return word  

# TH1: Từ bị thừa kí tự
def letter_insertion(word):
    pos = random.randint(0, len(word))
    char = random.choice('abcdefghijklmnopqrstuvwxyz')
    temp_word =  word[:pos] + char + word[pos:]
    choice = random.choice(['telex', 'vni'])
    if choice == 'telex':
        return telex_error(temp_word)
    return vni_error(temp_word)

# TH2: Từ bị thiếu kí tự
def letter_omission(word):
    if len(word) <= 1:
        return word
    pos = random.randint(0, len(word)-1)
    temp_word =  word[:pos] + word[pos+1:]
    choice = random.choice(['telex', 'vni'])
    if choice == 'telex':
        return telex_error(temp_word)
    return vni_error(temp_word)


# TH3: Từ có kí tự bị thay thế bằng kí tự khác
def letter_substitution(word):
    if not word:
        return word
    pos = random.randint(0, len(word)-1)
    char = random.choice('abcdefghijklmnopqrstuvwxyz')
    temp_word = word[:pos] + char + word[pos+1:] 
    choice = random.choice(['telex', 'vni'])
    if choice == 'telex':
        return telex_error(temp_word)
    return vni_error(temp_word)

# TH4: Từ có kí tự bị thay thế bằng kí tự khác trên bàn phím
def near_key(word):
    if not word:
        return word
    pos = random.randint(0, len(word)-1)
    char = word[pos].lower()
    near = NEAR_KEYS.get(char)
    if near:
        new_char = random.choice(near)
        word =  word[:pos] + new_char + word[pos+1:]
    choice = random.choice(['telex', 'vni'])
    if choice == 'telex':
        return telex_error(word)
    return vni_error(word)

# TH5: Từ có kí tự đổi vị trí
def letter_transposition(word):
    if len(word) < 2:
        return word
    pos = random.randint(0, len(word) - 2)
    chars = list(word)
    chars[pos], chars[pos+1] = chars[pos+1], chars[pos]
    temp_word =  ''.join(chars)
    choice = random.choice(['telex', 'vni'])
    if choice == 'telex':
        return telex_error(temp_word)
    return vni_error(temp_word)

# TH6: Từ bị mất dấu thanh
def diacritic_omission(word):
    return ''.join(
        c for c in unicodedata.normalize('NFD', word)
        if unicodedata.category(c) != 'Mn'
    )

# TH7: Từ có dấu thanh bị đổi sang dấu thanh khác
def diacritic_substitution(word):
    TONE_MAP = {
        'á': 'ả', 'à': 'ã', 'ả': 'ạ', 'ạ': 'á', 'ã': 'à',
        'é': 'ẻ', 'è': 'ẽ', 'ẻ': 'ẹ', 'ẹ': 'é', 'ẽ': 'è',
        'ó': 'ỏ', 'ò': 'õ', 'ỏ': 'ọ', 'ọ': 'ó', 'õ': 'ò',
        'í': 'ỉ', 'ì': 'ĩ', 'ỉ': 'ị', 'ị': 'í', 'ĩ': 'ì',
        'ú': 'ủ', 'ù': 'ũ', 'ủ': 'ụ', 'ụ': 'ú', 'ũ': 'ù',
        'ý': 'ỷ', 'ỳ': 'ỹ', 'ỷ': 'ỵ', 'ỵ': 'ý', 'ỹ': 'ỳ'
    }
    return ''.join([TONE_MAP.get(c, c) for c in word])

def create_character_level(sentence, error_idx, error_type):
    error_word = error_type(sentence[error_idx])
    sentence[error_idx] = error_word
    return " ".join(sentence)
