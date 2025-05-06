import sys
import re

OJOSAMA_DICT = [
    # 関数定義
    (r'わたくしの (\w+) は ([\w:, ]+) をお受け取りになりまして', r'def \1(\2):'),
    (r'わたくし ([\w_]+) の際には ([\w:, ]+) をお受け取りになりますの', r'def \1(\2):'),

    # 非同期関数
    (r'わたくし async の (\w+) は ([\w:, ]+) をお受け取りになりまして', r'async def \1(\2):'),
    (r'await (.+?) とおっしゃってくださいませ', r'await \1'),

    # クラス定義
    (r'この子は (\w+) と申しますの', r'class \1:'),
    (r'こちらの御方 (\w+) にお仕えいたしますの', r'class \1\(object\):'),
    (r'metaclass=(\w+) といたしますわ', r'metaclass=\1'),

    # with文
    (r'お手元に (.+?) を (\w+) としてお持ちくださいまし', r'with \1 as \2:'),

    # return
    (r'お返しするのは (.+?) でしてよ', r'return \1'),

    # 条件分岐
    (r'もしや (.+?) でございましたら', r'if \1:'),
    (r'そうではなくて (.+?) でございましたら', r'elif \1:'),
    (r'それ以外でしたら', r'else:'),

    # ループ
    (r'(\w+) を (.+?) にてお回しあそばせ', r'for \1 in \2:'),
    (r'どうかお先にお進みくださいまし', r'continue'),
    (r'ご退場あそばせ', r'break'),
    (r'お静かに願いますわ', r'pass'),

    # match文
    (r'match (.+?):', r'match \1:'),
    (r'case (.+?):', r'case \1:'),

    # 出力
    (r'「(.+?)」とお申しつけくださいませ', r'print("\1")'),
    (r'(\w+) とおっしゃってくださいませ', r'print(\1)'),
    (r'「(.+?)」と (\w+) をお並べになってくださいまし', r'print("\1", \2)'),

    # import
    (r'(\w+) をお招きいたしますわ', r'import \1'),
    (r'(\w+) を (\w+) としてお招きいたしますわ', r'import \1 as \2'),
    (r'(\w+) の (\w+) をお呼び立ていたしますわ', r'from \1 import \2'),

    # raise
    (r'raise (.+?) をおっしゃってくださいませ', r'raise \1'),

    # try/except/finally
    (r'わたくしの心よりの願いとして', r'try:'),
    (r'なんということでしょう、(.+?) にございますわ', r'except \1:'),
    (r'最後に申し上げますと', r'finally:'),

    # yield
    (r'yield に (.+?) を差し上げますわ', r'yield \1'),

    # 代入（表現として自然な形の追加）
    (r'(\w+) に (.+?) を差し上げますわ', r'\1 = \2'),

    # デコレータ
    (r'@(\w+)', r'@\1'),

    # 終了
    (r'ご機嫌ようで終了なさってくださいませ', r'exit\(\)'),

    # ブロック構造終了
    (r'以上ですのよ', r''),
    (r'すべておしまいですわ', r''),
]

def translate_ojosama_to_python(source: str) -> str:
    for pattern, repl in OJOSAMA_DICT:
        source = re.sub(pattern, repl, source)
    return source

def main():
    if len(sys.argv) != 2:
        print("おいたわしや… ojopyファイルを指定していただけますか？")
        print("使い方: python ojosama.py ファイル名.ojopy")
        return
    filepath = sys.argv[1]
    try:
        with open(filepath, encoding='utf-8') as f:
            original_code = f.read()
        translated = translate_ojosama_to_python(original_code)
        exec(translated, {})
    except Exception as e:
        print("おいたわしや…実行中に問題がございましたわ：", e)

if __name__ == "__main__":
    main()
