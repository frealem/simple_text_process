import os
import re
from collections import Counter
from seraaaa import Sera

def parallel_and_preprocess(amharic, tigrigna):
    try:
        # ========================display parallel===================================================
        with open(amharic, "r", encoding="utf-8") as f:
            amharic_text = f.read()
        with open(tigrigna, "r", encoding="utf-8") as f:
            tigrigna_text = f.read()
        print(f'\t\t===================================question number 1 & 2==============================\t\t\n')
        print(f"Amharic version \n {amharic_text} \n Tigrigna version \n {tigrigna_text} \n")

        # ========================preprocessing and clean=============================================
        combined_language = amharic_text + tigrigna_text

        # Remove non-Amharic characters
        preprocessed_text = re.sub(
            r"[^\u1200-\u137F\u2D80-\u2DDF\u2E80-\u2EFF\u3040-\u309F\uAC00-\uD7AF]",
            "",
            combined_language,
        )

        print("preprocessed version \n" + preprocessed_text)

        # return preprocessed_text
    except FileNotFoundError:
        print("error: file not found")
        return None
    except UnicodeDecodeError:
        print("error:unicode error!")
        return None

# ===============================count unique words===============================================
def count_word_frequency(amharic, tigrigna):
    try:
        with open(amharic, "r", encoding="utf-8") as f:
            amharic_text = f.read()
        with open(tigrigna, "r", encoding="utf-8") as f:
            tigrigna_text = f.read()

        combined_text = amharic_text + tigrigna_text

        words = combined_text.split()
        word_freq = dict(Counter(words))

        print(f'\t\t=========================== question number 3=================================\t\t')
        print(f"the total word Count is:\n", word_freq)
    except FileNotFoundError:
        print("error: file not found")
        return None
    except UnicodeDecodeError:
        print("error:unicode error!")
        return None

# ===============================overlapping words==================================================
def overlappedwords(amharic, tigrigna):
    try:
        with open(amharic, "r", encoding="utf-8") as f:
            amharic_text = f.read()
        with open(tigrigna, "r", encoding="utf-8") as f:
            tigrigna_text = f.read()

        amharic_words = set(amharic_text.split())
        tigrinya_words = set(tigrigna_text.split())

        shared_words = amharic_words.intersection(tigrinya_words)
        total_words = len(amharic_words) + len(tigrinya_words)

        word_overlap = (len(shared_words)/total_words)*100
       
        print('shared words',len(shared_words))
        print('total words',total_words)
        print("The overlappedwords in percent is:", word_overlap)
    except FileNotFoundError:
        print("error: file not found")
        return None
    except UnicodeDecodeError:
        print("error:unicode error!")
        return None

# =========================G2P=================================================================
def grapheme_to_phoneme(amharic,tigrigna):
    phoneme_text_am = ''
    phoneme_text_tg=''
    with open(amharic, "r", encoding="utf-8") as f:
            amharic_text = f.read()
    with open(tigrigna, "r", encoding="utf-8") as f:
            tigrigna_text = f.read()

    amharic_words = amharic_text
    tigrinya_words = tigrigna_text
    
    if amharic_words:
     for char in amharic_words:
        if char in Sera:
            phoneme_text_am += Sera[char]
            
        else:
            phoneme_text_am += char
     
    if tigrinya_words:
        for char in tigrinya_words:
         if char in Sera:
            phoneme_text_tg += Sera[char]
         else:
            phoneme_text_tg += char
    print(f'\t\t\t===============question number 4 & 5===============\t\t')     
    print(f"amharic G2P:\t\n",phoneme_text_am)
    print(f"Tigrigna G2P:\t\n",phoneme_text_tg)
#==========================distribution analysis==================================================
    char_freq_am = dict(Counter(phoneme_text_am))
    char_freq_tg = dict(Counter(phoneme_text_tg))

    print(f'number of unique phonemes for amahric: \t\n',char_freq_am)
    print(f'number of unique phonemes for Tigrigna: \t\n',char_freq_tg)

#============================overlap analysis========================================================
    overlapped_phonemes = len(set(phoneme_text_am).intersection(set(phoneme_text_tg)))
    total_phonemes = len(phoneme_text_tg) + len(phoneme_text_am)
    percentage_phoneme_overlap = (overlapped_phonemes/total_phonemes)*100
    
    print(f'overlap phoneme percentage analysis:\n',percentage_phoneme_overlap)

#============================display the results of the project======================================

def main():
    parallel_and_preprocess("amharic.txt", "tigrigna.txt")
    # count_word_frequency("amharic.txt", "tigrigna.txt")
    # overlappedwords("amharic.txt", "tigrigna.txt")
    # grapheme_to_phoneme("amharic.txt", "tigrigna.txt")

    
if __name__ == "__main__":
    main()