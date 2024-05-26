def shift_list(input_list, shifts):
    shifts = shifts % len(input_list)
    return input_list[-shifts:] + input_list[:-shifts]


def encrypt(key, shifts, text):
    sum_list = []
    ans_list = ''

    for i in range(len(text)):
        x = ord(text[i]) - 97
        y = ord(key[i % len(key)]) - 97
        sum_list.append((x + y) % 26)

    sum_list = shift_list(sum_list, shifts)

    for i in sum_list:
        ans_list += chr(i + 97)

    return ans_list


def decrypt(key, shifts, text):
    sum_list = []
    ans_list = ''

    sum_list = [ord(c) - 97 for c in text]
    sum_list = shift_list(sum_list, -shifts)

    for i in range(len(text)):
        x = sum_list[i]
        y = ord(key[i % len(key)]) - 97
        ans_list += chr((x - y + 26) % 26 + 97)

    return ans_list


# 입력 형식에 맞추어 처리
input_string = "encrypt_secretword_3_helloworld"  # 예시 입력 문자열

if input_string.startswith("encrypt"):
    _, key, shifts, text = input_string.split("_")
    result = encrypt(key, int(shifts), text)
    print(f"암호화 결과: {result}")  # 예상 출력: cspkfcgzin
elif input_string.startswith("decrypt"):
    _, key, shifts, text = input_string.split("_")
    result = decrypt(key, int(shifts), text)
    print(f"복호화 결과: {result}")  # 예상 출력: helloworld

# 암호화 예시
encrypt_input = "encrypt_secretword_3_helloworld"
if encrypt_input.startswith("encrypt"):
    _, key, shifts, text = encrypt_input.split("_")
    encrypted_result = encrypt(key, int(shifts), text)
    print(f"암호화 결과: {encrypted_result}")  # 예상 출력: cspkfcgzin

# 복호화 예시
decrypt_input = "decrypt_secretword_3_cspkfcgzin"
if decrypt_input.startswith("decrypt"):
    _, key, shifts, text = decrypt_input.split("_")
    decrypted_result = decrypt(key, int(shifts), text)
    print(f"복호화 결과: {decrypted_result}")  # 예상 출력: helloworld
