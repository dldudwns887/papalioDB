def combine_korean(text):
    # 한글 초성, 중성, 종성 범위
    CHOSUNG_START = 0x1100
    JUNGSUNG_START = 0x1161
    JONGSUNG_START = 0x11A7
    HANGUL_START = 0xAC00

    # 초성, 중성, 종성 분리
    chosung = [chr(i) for i in range(CHOSUNG_START, CHOSUNG_START + 19)]
    jungsung = [chr(i) for i in range(JUNGSUNG_START, JUNGSUNG_START + 21)]
    jongsung = [chr(i) for i in range(JONGSUNG_START + 1, JONGSUNG_START + 28)]

    def korean_to_be_choseong(jamo):
        if 'ㄱ' <= jamo <= 'ㅎ':
            return chosung.index(jamo)
        return None

    def korean_to_be_jungseong(jamo):
        if 'ㅏ' <= jamo <= 'ㅣ':
            return jungsung.index(jamo)
        return None

    def korean_to_be_jongseong(jamo):
        if jamo == '' or jamo == ' ':
            return 0
        return jongsung.index(jamo) + 1

    result = ""
    buffer = [-1, -1, -1]  # 초성, 중성, 종성

    for char in text:
        choseong = korean_to_be_choseong(char)
        jungseong = korean_to_be_jungseong(char)
        jongseong = korean_to_be_jongseong(char)

        if choseong is not None:
            if buffer[1] == -1:
                buffer[0] = choseong
            else:
                result += chr(HANGUL_START + (buffer[0] * 588) + (buffer[1] * 28) + buffer[2])
                buffer = [choseong, -1, -1]
        elif jungseong is not None:
            buffer[1] = jungseong
        elif jongseong is not None:
            buffer[2] = jongseong

    if buffer[1] != -1:
        result += chr(HANGUL_START + (buffer[0] * 588) + (buffer[1] * 28) + buffer[2])

    return result

# 예제 문자열
example_str = "ㅇㅑㅅㅡ"
combined_str = combine_korean(example_str)
print("heel")

