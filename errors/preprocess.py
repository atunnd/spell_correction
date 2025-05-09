import re
from langdetect import detect

def sentence_clean(sentence):

    # Thay tất cả cụm \n (kể cả nhiều cái liên tiếp) bằng dấu chấm và khoảng trắng
    clean_text = re.sub(r'\n+', '. ', sentence)

    # Loại bỏ dấu chấm dư (nếu có)
    clean_text = re.sub(r'\.\s*\.', '.', clean_text)

    # Bỏ khoảng trắng đầu cuối và chuẩn hóa
    clean_text = clean_text.strip()

    # Xoá dấu chấm dư (". .", "..", v.v.)
    text = re.sub(r'\.\s*\.+', '.', clean_text)

    # Xoá dấu chấm đứng trước hoặc sau khoảng trắng thừa
    text = re.sub(r'\s*\.\s*', '. ', text)

    # Xoá khoảng trắng thừa
    text = re.sub(r'\s{2,}', ' ', text)

    # Strip khoảng trắng đầu cuối
    text = text.strip()

    return text

def is_english(text):
    try:
        return detect(text) == 'en'
    except:
        return False  
    
def is_only_numbers_and_special_chars(text):
    text = text.strip()
    return bool(text) and not re.search(r'[a-zA-ZÀ-ỹ]', text)

def is_vietnamese(text):
    try:
        return detect(text) == 'vi'
    except:
        return False
    
def check_vietnamese(sentence):
    words = sentence.split()
    for word in words:
        if not is_vietnamese(word):
            return False
    return True