import random

chars = "abcdefghijklmnopqristuvwxyz"

def get_random_unicode(length):
    try:
        get_char = unichr
    except NameError:
        get_char = chr

    # Update this to include code point ranges to be sampled
    include_ranges = [
        ( 0x0021, 0x0021 ),
        ( 0x0023, 0x0026 ),
        ( 0x0028, 0x007E ),
        ( 0x00A1, 0x00AC ),
        ( 0x00AE, 0x00FF ),
        ( 0x0100, 0x017F ),
        ( 0x0180, 0x024F ),
        ( 0x2C60, 0x2C7F ),
        ( 0x16A0, 0x16F0 ),
        ( 0x0370, 0x0377 ),
        ( 0x037A, 0x037E ),
        ( 0x0384, 0x038A ),
        ( 0x038C, 0x038C ),
    ]

    alphabet = [
        get_char(code_point) for current_range in include_ranges
            for code_point in range(current_range[0], current_range[1] + 1)
    ]
    return ''.join(random.choice(alphabet) for i in range(length))

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

def randomVcard(randomUnicodeName: bool, phone_digit: int, family_name_digit: int, name_digit: int):
    phone = randomPhone(phone_digit)
    phone_type = randomPhoneType()
    mail = randomEmail()
    mail_type = randomMailType()
    family_name = get_random_unicode(family_name_digit) if randomUnicodeName else randomName(family_name_digit)
    name = get_random_unicode(name_digit) if randomUnicodeName else randomName(name_digit)

    return f"""BEGIN:VCARD
VERSION:4.0
PRODID;VALUE=TEXT:pm-ez-vcard 0.0.1
FN;PREF=1:{family_name} {name}
TEL;TYPE="{phone_type}, pref";PREF=1:{phone}
EMAIL;TYPE="{mail_type}";PREF=1:{mail}
END:VCARD
"""