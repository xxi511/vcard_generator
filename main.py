from myrandom import randomVcard

def write(file_name: str, vcard: str):
    f = open(file_name, "w")
    f.write(vcard)
    f.close()

if __name__ == '__main__':
    total_vcard = 250
    phone_digit = 10
    family_name_digit = 5
    name_digit = 5

    vcard = []
    for _ in range(total_vcard):
        vcard.append(randomVcard(phone_digit, family_name_digit, name_digit))
    write('randomVcard.vcf', "".join(vcard))