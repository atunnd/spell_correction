import random
import re

# Danh sách lỗi phát âm: phụ âm đầu/cuối, nguyên âm, và dấu hỏi ↔ dấu ngã
pronunciation_errors = {
    # Phụ âm đầu
    'gi': ['d', 'r'],
    'tr': ['ch'],
    'ch': ['tr'],
    'ngh': ['ng'],
    'ng': ['ngh'],
    'qu': ['u', 'h'],
    'd': ['r', 'gi'],
    'r': ['d', 'gi'],
    'n': ['l'],
    'l': ['n'],
    's': ['x'],
    'x': ['s'],
    'c': ['k', 't'],  # c vừa là đầu vừa là cuối
    'k': ['c'],
    'u': ['qu', 'h', 'uô'],
    'h': ['u', 'qu'],

    # Phụ âm cuối
    't': ['c'],
    'm': ['n'],
    'ng': ['n'],
    
    # Nguyên âm
    'ie': ['uyê'],
    'uyê': ['ie'],
    'uô': ['u'],

    # Dấu hỏi ↔ dấu ngã
    'ả': ['ã'], 'ã': ['ả'],
    'ẻ': ['ẽ'], 'ẽ': ['ẻ'],
    'ỏ': ['õ'], 'õ': ['ỏ'],
    'ỉ': ['ĩ'], 'ĩ': ['ỉ'],
    'ủ': ['ũ'], 'ũ': ['ủ'],
    'ỷ': ['ỹ'], 'ỹ': ['ỷ'],
}

# Ưu tiên thay thế chuỗi dài trước
error_keys_sorted = sorted(pronunciation_errors.keys(), key=lambda x: -len(x))

def pronunciation_error(word):
    for key in error_keys_sorted:
        if key in word:
            replacement = random.choice(pronunciation_errors[key])
            word = word.replace(key, replacement, 1)
            break  # chỉ thay 1 lỗi mỗi từ
    return word

def apply_pronunciation_error(sentence):
    words = sentence.split()
    idx_error = random.choice(range(0, len(words)))
    word_error = words[idx_error]
    words[idx_error] = pronunciation_error(word_error)
    return ' '.join(words)