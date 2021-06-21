print('[유니코드] :', chr(0xB098), hex(0xB098))
print('0xB0 : ', bin(0xB0))
print('0x98 : ', bin(0x98))
print()
 
utf8byte1 = 0b11100000
utf8byte2 = 0b10000000
utf8byte3 = 0b10000000
 
print('[UTF-8 binary format]')
print('1st Byte:', bin(utf8byte1), end=', ')
print('2nd Byte:', bin(utf8byte2), end=', ')
print('3rd Byte:', bin(utf8byte3))
print('1st Byte: 0b1110XXXX, 2nd Byte: 0b10XXXXXX, 3rd Byte: 0b10XXXXXX')
 
 
h1 = 0xB0 >> 4
print('h1:', bin(h1)[2:].zfill(4))
 
h2 = 0xB0 << 2
h2 = h2 & 0b0000111100
print('h2:', bin(h2)[2:].zfill(4))
 
h3 = 0x98 >> 6
print('h3:', bin(h3)[2:].zfill(2))
 
h4 = 0x98 & 0b00111111
print('h4:', bin(h4)[2:].zfill(6))
print()
 
c1 = bin(utf8byte1 | h1)
c2 = bin(utf8byte2 | h2 | h3)
c3 = bin(utf8byte3 | h4)
 
print('[바이트 3개]')
print(c1)
print(c2)
print(c3)
print()
 
print('[UTF-8 인코딩 완료]')
print(hex(int(c1, 2)), end=' ')
print(hex(int(c2, 2)), end=' ')
print(hex(int(c3, 2)))
 
test1 = "나".encode("UTF-8")
print(test1)