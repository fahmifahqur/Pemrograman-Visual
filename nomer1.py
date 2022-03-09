abjad = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
         'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

kata = input("Masukkan Kata = ")
modulus = ""
kunci = int(input("Masukkan Kunci = "))

for x in range(len(kata)):
    huruf = abjad.index(kata[x])+kunci
    modulus = modulus+abjad[huruf % 26]
for y in ""+modulus:
    print(y)