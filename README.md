# 🔤 Vietnamese Spelling Error Generator

This project is a **Vietnamese spelling error simulation tool** designed to generate synthetic noisy training data for building and evaluating spelling correction models.

It introduces a variety of realistic errors—spanning **character-level**, **word-level**, and **pronunciation-level**—into clean Vietnamese sentences sourced from the [VTSNLP Vietnamese Curated Dataset](https://huggingface.co/datasets/VTSNLP/vietnamese_curated_dataset).

---

## 🚀 Features

- ✅ Generate **character-level** errors: insertion, omission, substitution, diacritic changes, near-key typos, transpositions.
- ✅ Generate **word-level** errors: omission, insertion, substitution, teencode, OCR noise, duplication, title/lower-case, and abbreviation mistakes.
- ✅ Generate **pronunciation-level** errors using Vietnamese phonetic variations.
- ✅ Automatic **domain-based sampling** from the VTSNLP dataset (e.g., News, Science, Books).
- ✅ Clean sentence filtering using `langdetect` and `underthesea`.
- ✅ Outputs a structured training CSV file for downstream NLP tasks.

---

## 📦 Requirements

Install the necessary Python packages:

```bash
pip install -r requirements.txt
