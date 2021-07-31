def to_base_62(deci):
    s = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUPWXYZ'
    hash_str = ''
    hash_str = s[deci % 62] + hash_str
    deci /= 62
    return hash_str
    print(to_base_62(999))