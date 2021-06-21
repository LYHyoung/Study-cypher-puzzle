import sys
import subprocess

# 1번째 지문 인코딩
string1 = "UnicOde iS a CompUtInG industRy stanDArD for ConsiStent Encoding, RepresenTation, And hanDlinG of ALL tEXT. UsinG UNIcodE, ALL HAngUl sYllAbles CAN BE ExpRessed by 16-Bit datA bEtween 0Xac00 and 0xd7aF."
ans1 = ""
cnt1 = 0

for c in string1:
    if (c >= 'A' and c <= 'Z'):
        ans1 += '1'
        cnt1 += 1
    elif (c >= 'a' and c <= 'z'):
        ans1 += '0'
        cnt1 += 1

# 2번째 지문 인코딩
string2 = "eXcluSiVe oR (XoR) IS a LOGiCaL opeRAtiOn THAt RESuLTS TruE onLY whEn iNpuTs diffER (one iS TRuE, The oThEr Is FALSE). iT Is oFTEn UsEd foR bitWiSe DyADIc OPERatIonS. (0 Xor 0) = 0, (1 Xor 1) = 0, (1 Xor 0) = 1, AnD (0 xor 1) = 1 ARe estABLisHeD."
ans2 = ""
cnt2 = 0

for c in string2:
    if (c >= 'A' and c <= 'Z'):
        ans2 += '1'
        cnt2 += 1
    elif (c >= 'a' and c <= 'z'):
        ans2 += '0'
        cnt2 += 1

t = ""

# xor 연산
for i in range(0, 160):
    a = int(ans1[i]) ^ int(ans2[i])
    t += str(a)

split = ""
for i in range(10):
    split += "0b"
    for j in range(16):
        split += t[16*i + j]
    print(chr(int(split,2)))
    split = ""