# proper-noun-replacer

固有名詞を伏せ字に変換するプログラム。

メールの返信をChatGPT等に考えてもらう際、企業名や個人名を伏せ字に変換して欲しいときに使う。

## Example

```shell
$ python main.py "こんにちは鈴木さん。abc株式会社の田中です。"
# こんにちは**さん。**株式会社の**です。
```
