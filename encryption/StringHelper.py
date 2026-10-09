def stringTointeger(Message: str) -> int:

    MessageInt = ""
    for i in Message:
        CurrentLetter = str(ord(i)).zfill(7)

        MessageInt = MessageInt + CurrentLetter
    return int(MessageInt)


def integerToString(Message: int) -> str:
    digits = str(Message)
    digits = digits.zfill((len(digits) + 6) // 7 * 7)  # pad left to a multiple of 7

    return "".join(chr(int(digits[i : i + 7])) for i in range(0, len(digits), 7))
