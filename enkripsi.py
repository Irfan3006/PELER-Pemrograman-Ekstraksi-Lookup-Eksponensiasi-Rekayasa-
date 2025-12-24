# enkripsi script
mapping = {
    "A": "da778688000ji",
    "B": "ic7575729344jktk",
    "C": "c7668682048dr",
    "D": "hi7940149875ah",
    "E": "ng7833173256ja",
    "F": "an7495014493jb",
    "G": "go8108486729rgrpkt",
    "H": "ll7880599000spj",
    "I": "io7988005999bf",
    "J": "va7940149875jg",
    "K": "in8132727331ab",
    "L": "sp7506509912jm",
    "M": "ab7809531904cm",
    "N": "im8096384512ar",
    "O": "ml7952095936xl",
    "P": "on7868724669gvr",
    "Q": "rp20178205738913mr",
    "R": "by7940149875ym",
    "S": "ft8169178744cl",
    "T": "pt8144865728ah",
    "U": "da7988005999dm",
    "V": "v8230172859am",
    "W": "ly8181353375wc",
    "X": "ry8036054027mk",
    "Y": "ck7952095936dhm",
    "Z": "ig8193540096ak",
    "0": "ar8120601000mh",
    "1": "ct8157016197jw",
    "2": "ue8169178744ey",
    "3": "te8193540096rh",
    "4": "er8132727331yk",
    "5": "ne8120601000ja",
    "6": "ry8072216216jr",
    "7": "ap8132727331mojt",
    "8": "xt8193540096gr",
    "9": "id8217949832rc",
}

def encrypt(text):
    text = text.upper()
    ciphertext = ""
    for ch in text:
        if ch in mapping:
            ciphertext += mapping[ch]

    reverse = "".join(reversed(ciphertext))
    return reverse

if __name__ == "__main__":
    plaintext = input("Masukkan teks: ")
    hasil = encrypt(plaintext)
    print("Ciphertext:", hasil)
