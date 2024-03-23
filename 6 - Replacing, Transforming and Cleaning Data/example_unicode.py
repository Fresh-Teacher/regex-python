import re

text = "I love using emojis 😃 and mathematical symbols like π (pi)!"

emoji_pattern = r"[\U0001F600-\U0001F64F]"
emojis = re.findall(emoji_pattern, text)
print("Emojis found:", emojis)

math_symbol_pattern = r"[\u2200-\u22FF\u0370-\u03FF]"
math_symbols = re.findall(math_symbol_pattern, text)
print("Mathematical symbols found:", math_symbols)

clean_text = re.sub(r"[^\w\s]", "", text, flags=re.ASCII)
print("Cleaned text:", clean_text)
