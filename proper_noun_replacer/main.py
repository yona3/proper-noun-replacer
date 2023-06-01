import re
import sys

import spacy

# GiNZAモデルをロード
nlp = spacy.load("ja_ginza")

# テキストを入力
text = sys.argv[1]  # CLIで入力された値を取得

# テキストを解析
doc = nlp(text)


# 固有名詞を伏せ字に置換する関数
def mask_propn(text, doc):
    # 固有名詞のリストを作成
    propns = [token.text for token in doc if token.pos_ == "PROPN" and not token.text.startswith("\n")]
    # 伏せ字にするパターンを作成
    pattern = re.compile("|".join(propns))
    # 伏せ字に置換
    masked_text = pattern.sub("**", text)
    return masked_text


# 置換したテキストを出力
masked_text = mask_propn(text, doc)
print(masked_text)
