# -*- coding : utf-8 -*-
val_1 = 10
val_2 = 20
val_3 = 10
print(id(val_1))
print(id(val_3))
print(id(val_2))
val_3 = 30
print(id(val_3))

print("-" * 20)

abcde = "abcde"
abcde_en = abcde.encode("utf-8")
print(abcde_en)
print(type(abcde_en))

abcde_by = bytes(abcde, encoding = "utf-8")
print(abcde_by)
print((type(abcde_by)))
print("参照先↓")
print(id(abcde_en))
print(id(abcde_by))

print("-" * 20)

b_abc = b"abcde"
b_abc_by = bytes(b_abc)
print(b_abc)
print(b_abc_by)
print("-"*10)
print(type(b_abc))
print(type(b_abc_by))
print("-"*10)
print(id(b_abc))
print(id(b_abc_by))

print(list(b_abc))
#for i in b_abc:
#   print(i)

print("-"*20)

abcde = "abcde"
abcde_en = abcde.encode("utf-8")
print(abcde_en)
print(type(abcde_en))
print("-"*10)
abcde_byary = bytearray(abcde, encoding = "utf-8")
print(abcde_byary)
print(type(abcde_byary))
print("-"*10)
print(id(abcde_en))
print(id(abcde_byary))
print("-"*20)

b_abcde = b"abcde"
b_abcde_byary = bytearray(b_abcde)
print(b_abcde_byary)
print(type(b_abcde_byary))
print("-"*10)
print(id(b_abcde))
print(id(b_abcde_byary))
print(list(b_abcde_byary))
print("-"*10)
b_abcde_byary[0] = 98
print(list(b_abcde_byary))
print(b_abcde_byary)
print("-"*20)

mrv = memoryview(b"abcde")
print(list(mrv))
print(mrv[2])
print(chr(mrv[2]))
print("-"*20)

mrv = memoryview(bytearray(b"abcde"))
print(mrv[2])
print(chr(mrv[2]))
mv[2] = old("d")
print(mv[2])
print("-"*20)

# chr関数 = Unicodeを文字列に変換
# ord関数 = 文字列をUnicodeに変換

#【バイナリ】
#バイナリ (binary) とは、本来は二進法のこと
#情報技術においては、コンピュータが直接的に処理するために２進数で表現されるデータ（バイナリデータ）のことを指して用いられる。

#【ビットとバイト】
# ビット  : 0と1を用いたバイナリ表記
# 1ビット : 0と1 × 1組み  2パターンを表現 (2の1乗=2)
# 4ビット : 0と1 × 4組み  16パターンを表現（2の4乗＝16）
# 8ビット : 0と1 × 8組み  256パターンを表現（2の8乗＝256）

# 1バイト = 8ビット
# 256は16×16なので『16進数表記×16進数表記』を用い表記できる

#『コンピューターで文字を扱う際の流れ』
# https://wa3.i-3-i.info/word11422.html
# ①文字 => ②文字に割り当てた番号 => ③実際にコンピュータが扱う数字
# 主に2段階に別れている
# ① => ② = 符号化文字集合
# ② => ③ = 文字符号化方式

#【符号化文字集合】
# ASCII   ：英語圏などで使われ（7ビットを用い最大128文字を表現）
# Unicorde：世界中の文字を扱う。(UTF-16)と読み替え使用する場合あり

#『文字符号化方式』
# UTF-7、UTF-8、UTF-16、UTF-32
# Base64

#『(あ)と(a)の、エンコードとデコード』
# Unicorde = あ=12354、a=97
# 2進数     = あ=0b11000001000010、a=0b1100001
# 16進数    = あ=0x3042、a=0x61
# UTF-8    = あ=b'\xe3\x81\x82'、a=b'a'
# base64   = あ=＃b'44GC'、a=＃b'YQ=='
