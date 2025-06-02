import json

def load_vocabulary():
    with open("data/vocabulary.txt", "r", encoding="utf-8") as f:
        vocab = [line.strip() for line in f]
    return vocab
