import random
import unicodedata
from unidecode import unidecode
import bogo
import re
from langdetect import detect
from errors.word_level_error import word_insertion, word_omission, word_omission_compound, word_substitution, convert_to_teencode, ocr_error, word_transposition
from errors.word_level_error import split_word, merge_word, duplication_word, title_case_error, lower_case_error, abbr_name_error
from errors.character_level_error import letter_insertion, letter_omission, letter_substitution, near_key, letter_transposition, diacritic_omission, diacritic_substitution
from errors.character_level_error import create_character_level
from errors.spell_level_error import apply_pronunciation_error
from errors.preprocess import sentence_clean, is_english, is_vietnamese, is_only_numbers_and_special_chars, check_vietnamese

import os
from underthesea import sent_tokenize
import pandas as pd
import csv
from datasets import load_dataset
import argparse


character_level_errors = {
    'letter_insertion': letter_insertion,
    'letter_omission': letter_omission,
    'letter_substitution': letter_substitution,
    'near_key': near_key,
    'letter_transposition': letter_transposition,
    'diacritic_omission': diacritic_omission,
    'diacritic_substitution': diacritic_substitution,
}

word_level_errors = {
    "word_insertion": word_insertion,
    "word_omission": word_omission,
    "word_omission_compound": word_omission_compound,
    "word_substitution": word_substitution,
    "teencode": convert_to_teencode,
    "ocr": ocr_error,
    "word_transposition": word_transposition,
    "split_word": split_word,
    "merge_word": merge_word,
    "duplication_word": duplication_word,
    "title_case": title_case_error,
    "lower_case": lower_case_error,
    "abbr_name": abbr_name_error
}

def create_error(sentence):
    words = sentence.split()
    res = []
    number_of_words_get_error = int(len(words) * 0.15)
    error_idx = random.sample(range(0, len(words)), number_of_words_get_error)
    for idx in error_idx:
        if not is_vietnamese(words[idx]):
            continue
        if random.uniform(0, 1) <= 0.8:
            error_level = random.choice([0, 1, 2])
            if error_level == 0: 
                error_type = random.choice(list(character_level_errors.keys()))
                #print(f"\nCreate errors in character level: {error_type}")
                error_function = character_level_errors[error_type]
                result = create_character_level(words, idx, error_function)
                if result != sentence:
                    res.append(result)
            elif error_level == 1:
                error_type = random.choice(list(word_level_errors.keys()))
                #print(f"\nCreate errors in word level: {error_type}")
                error_function = word_level_errors[error_type]
                result = error_function(sentence)
                if result != sentence:
                    res.append(result)
            elif error_level == 2:
                #print("\nCreate errors in spell level")
                error_function = apply_pronunciation_error
                result = error_function(sentence)
                if result != sentence:
                    res.append(result)
    return res

def load_training_data(num_samples):
    ds = load_dataset("VTSNLP/vietnamese_curated_dataset", cache_dir="../data/vtsnlp")
    df = pd.DataFrame(ds['train'][:num_samples])
    num_domains = df['domain'].value_counts().min()
    df_sampled = df.groupby('domain', group_keys=False).apply(
        lambda x: x.sample(n=min(num_samples, len(x)), random_state=42)).reset_index(drop=True)

    return df_sampled

def create_training_data(args):
    num_samples = args.num_of_samples

    df = load_training_data(num_samples)
    train_df = pd.DataFrame(columns=["id", "error_sentence", "GT_sentence"])

    for idx in range(len(df)):
        sample = df.iloc[idx, 0]
        sample = sentence_clean(sample)
        sentences = sent_tokenize(sample)
        for sentence in sentences:
            if not is_english(sentence) and not is_only_numbers_and_special_chars(sentence) and is_vietnamese(sentence):
                error_sentences = create_error(sentence)
                if error_sentences:
                    for error in error_sentences:
                        train_df.loc[len(train_df)] = [len(train_df), error, sentence]

    os.makedirs("output", exist_ok=True)
    train_df.to_csv("output/training.csv", quoting=csv.QUOTE_ALL, encoding='utf-8-sig', index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--num_of_samples", type=int, default=10, help="Number of training sample from VTSNLP")
    args = parser.parse_args()
    create_training_data(args)