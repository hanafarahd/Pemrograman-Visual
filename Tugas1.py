 #Hana Farahdiana 20051397073 2020MIA

kata = input ("Masukkan kata :")
kunci = int (input ("Masukkan kunci :"))
# caesar cipher
def caesar_cipher(kata,kunci):
    hasil = ""
    for i in range(len(kata)):
        if (kata[i] == " "):
            hasil += " "
        else:
            hasil += chr(ord(kata[i]) + kunci)
    return hasil
print(caesar_cipher('kata',kunci)) 