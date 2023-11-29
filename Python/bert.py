
from transformers import BertTokenizer

# 对于英文
english_tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
english_text = "Natural language processing is fascinating."
english_tokens = english_tokenizer.tokenize(english_text)
print(english_tokens)

# 对于中文
chinese_tokenizer = BertTokenizer.from_pretrained("bert-base-chinese")
chinese_text = "自然语言处理非常有趣。"
chinese_tokens = chinese_tokenizer.tokenize(chinese_text)
print(chinese_tokens)
