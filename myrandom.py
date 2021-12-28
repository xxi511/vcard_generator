import random

chars = "abcdefghijklmnopqristuvwxyz"

def randomPhoneType():
    types = ['Phone', 'Mobile', 'Work', 'Fax', 'Other']
    return types[random.randint(0, 4)]

def randomMailType():
    types = ['Email', 'Personal', 'Work', 'Other']
    return types[random.randint(0, 3)]

def randomPhone(digit: int):
    result = []
    for _ in range(digit):
        result.append(str(random.randint(0, 9)))
    return "".join(result)

def randomEmail():
    name_digit = random.randint(3,10)
    host_digit = random.randint(1, 5)
    domain_digit = random.randint(3, 5)
    result = []
    digits = [name_digit, host_digit, domain_digit]
    appends = ['@', '.', '']
    for index in range(3):
        digit = digits[index]
        for _ in range(digit):
            charIdx = random.randint(0, len(chars) - 1)
            result.append(chars[charIdx])
        result.append(appends[index])
    return "".join(result)

def randomName(digit: int):
    result = []
    for _ in range(digit):
        charIdx = random.randint(0, len(chars)-1)
        result.append(chars[charIdx])
    return "".join(result)

def randomVcard(phone_digit: int, family_name_digit: int, name_digit: int):
    phone = randomPhone(phone_digit)
    phone_type = randomPhoneType()
    mail = randomEmail()
    mail_type = randomMailType()
    family_name = randomName(family_name_digit)
    name = randomName(name_digit)

    return f"""
    BEGIN:VCARD
    VERSION:4.0
    PRODID;VALUE=TEXT:pm-ez-vcard 0.0.1
    FN;PREF=1:{family_name} {name}
    TEL;TYPE="{phone_type}, pref";PREF=1:{phone}
    EMAIL;TYPE="{mail_type}";PREF=1:{mail}
    END:VCARD"""