from collections import Counter

def build_vocab(texts):
    counter = Counter()
    for text in texts:
        counter.update(text.split())
    vocab = {"<pad>": 0, "<unk>": 1, "<sos>": 2, "<eos>": 3}
    for idx, (word, _) in enumerate(counter.items(), start=4):
        vocab[word] = idx
    return vocab

def encode_text(text, vocab, max_len=120, add_tokens=False):
    tokens = text.split()
    if add_tokens:
        tokens = ['<sos>'] + tokens + ['<eos>']
    token_ids = [vocab.get(token, vocab["<unk>"]) for token in tokens]
    return token_ids[:max_len] + [vocab["<pad>"]] * (max_len - len(token_ids))