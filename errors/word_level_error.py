import random
from pyvi import ViTokenizer
import random

# TH1. Word insertion: chèn một từ ngẫu nhiên
def word_insertion(sentence):
    words = sentence.split()
    index = random.randint(0, len(words))
    insert_word = random.choice(words)
    words.insert(index, insert_word)
    return ' '.join(words)

# TH2. Word omission: xóa một từ bất kỳ
def word_omission(sentence):
    words = sentence.split()
    if len(words) <= 1:
        return sentence
    index = random.randint(0, len(words) - 1)
    del words[index]
    return ' '.join(words)

# TH3. Word omission compound: bỏ một từ trong từ ghép (ví dụ "lập trình")
def word_omission_compound(sentence):
    segmented = ViTokenizer.tokenize(sentence)
    words = segmented.split()
    res = []
    compound_words = [w for w in words if '_' in w]
    if compound_words:
        for c_words in compound_words:
            target = c_words
            parts = target.split('_')
            if len(parts) >= 2:
                remove_part = random.choice(parts)
                res.append(sentence.replace(remove_part, '', 1).replace('  ', ' '))
            return res[0]
    return ''

# TH4. Word substitution: thay một từ bằng từ khác
def word_substitution(sentence):
    words = sentence.split()
    index = random.randint(0, len(words) - 1)
    sub_word = random.choice(words)
    words[index] = sub_word
    return ' '.join(words)

# TH5. Teencode: thay thế 1 từ bằng dạng teencode
def load_teencode_reverse_dict(filepath):
    teencode_dict = {}
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            if '\t' in line:
                teencode, standard = line.strip().split('\t')
                teencode_dict.setdefault(standard.lower(), teencode)
    return teencode_dict

def convert_to_teencode(sentence):
    reverse_dict = load_teencode_reverse_dict('dictionary/teencode.txt')
    words = sentence.split()
    new_words = [
        reverse_dict.get(word.lower(), word) for word in words
    ]
    return ' '.join(new_words)

reverse_dict = load_teencode_reverse_dict('dictionary/teencode.txt')

# TH6. OCR error: mô phỏng lỗi nhận diện ký tự
def load_ocr_error_dict(filepath):
    ocr_dict = {}
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split('\t')
            if len(parts) >= 4:
                correct = parts[1].strip()  
                error = parts[3].strip()    
                if len(correct) == 1:  
                    ocr_dict.setdefault(correct, set()).add(error)
                else:  
                    ocr_dict.setdefault(correct, set()).add(error)
    return ocr_dict

# Hàm để thay thế văn bản với các lỗi OCR
def ocr_error(text, error_prob=0.3):
    ocr_dict = load_ocr_error_dict('dictionary/vie.unicharambigs.txt')
    result = []
    i = 0  # Vị trí trong văn bản

    make_error = False
    
    while i < len(text):
        for length in range(min(5, len(text) - i), 0, -1):  
            substring = text[i:i+length]
            if substring in ocr_dict and random.random() < error_prob and not make_error:
                result.append(random.choice(list(ocr_dict[substring])))  
                i += length  
                make_error = True
                break
            else:
                result.append(text[i])
            i += 1
    
    return ''.join(result)

# TH7. Word transposition: đổi chỗ 2 từ gần nhau
def word_transposition(sentence):
    words = sentence.split()
    if len(words) < 2:
        return sentence
    index = random.randint(0, len(words) - 2)
    words[index], words[index + 1] = words[index + 1], words[index]
    return ' '.join(words)

# TH8. Split word: chèn khoảng trắng làm tách từ
def split_word(sentence):
    words = sentence.split()
    index = random.randint(0, len(words) - 1)
    word = words[index]
    if len(word) > 2:
        split_index = random.randint(1, len(word) - 1)
        first_split = word[:split_index]
        second_split = word[split_index:]
        words[index:index+1]=[first_split, second_split]
    return ' '.join(words)

# TH9. Merge word: nối 2 từ làm một
def merge_word(sentence):
    words = sentence.split()
    if len(words) < 2:
        return sentence
    index = random.randint(0, len(words) - 2)
    merged = words[index] + words[index + 1]
    temp = [merged]
    words[index:index + 2] = temp
    return ' '.join(words)

# TH10. Duplication word: lặp lại một từ
def duplication_word(sentence):
    words = sentence.split()
    index = random.randint(0, len(words) - 1)
    words.insert(index, words[index])
    return ' '.join(words)

# TH11. Title case: viết hoa 1 từ không đúng
def title_case_error(sentence):
    words = sentence.split()
    index = random.randint(0, len(words) - 1)
    words[index] = words[index].capitalize()
    return ' '.join(words)

# TH12. Lower case: viết thường 1 từ đang viết hoa
def lower_case_error(sentence):
    words = sentence.split()
    
    for i in range(len(words)):
        if words[i].istitle() or words[i].upper(): 
            words[i] = words[i].lower() 
    
    return ' '.join(words)

# TH13. Abbr name: viết tắt bị viết thường
def load_short_dict(filepath):
    short_dict = {}
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split(',')
            if len(parts) == 2:
                abbreviation = parts[0].strip()
                full_name = parts[1].strip()
                short_dict[abbreviation] = full_name
    return short_dict

def abbr_name_error(sentence):
    words = sentence.split()  
    short_dict = load_short_dict('dictionary/short_dict.txt')
    for i in range(len(words)):
        abbr = words[i].strip()  
        if abbr.upper() in short_dict: 
            words[i] = short_dict[abbr.upper()] 
        
        if words[i].istitle() or words[i].upper():  
            words[i] = words[i].lower() 
    return ' '.join(words)
