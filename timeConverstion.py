def timeConversion(s):
    s1 = s[-2:]
    h = int(s[:2])  # Convert to integer
    mint = s[3:5]
    sec = s[6:8]

    def whatTime(h):
        if h == 12 and s1 == 'AM':
            return '00' +':'+ mint +':'+ sec
        elif s1 == 'AM':
            return s[:-2]
        elif h == 12 and s1 == 'PM':
            return s[:-2]
        else:
            return (str(h + 12) + ':' + mint + ':' + sec)

    return (whatTime(h))
