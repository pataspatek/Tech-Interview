# Time complexity: O(n)
# Space complexity: O(n)

def encrypt(string, key):
    encrypted_message = ""
    alphabet_size = 26

    # Calculate the effective key
    effective_key = key % alphabet_size

    # If the effective key is 0, input won't get encrypted
    if effective_key == 0:
        return string

    for letter in string:
        new_letter = ord(letter) + effective_key

        # Wrap around to the beginning of the alphabet
        if new_letter > 122:
            new_letter -= alphabet_size

        encrypted_message = encrypted_message + chr(new_letter)

    return encrypted_message


def decrypt(string, key):
    encrypted_message = ""
    alphabet_size = 26

    # Calculate the effective key
    effective_key = key % alphabet_size

    # If the effective key is 0, input won't get encrypted
    if effective_key == 0:
        return string

    for letter in string:
        new_letter = ord(letter) - effective_key

        # Wrap around to the beginning of the alphabet
        if new_letter < 97:
            new_letter += alphabet_size

        encrypted_message = encrypted_message + chr(new_letter)

    return encrypted_message


def test_caesar():
    # Test encryption
    assert encrypt("hello", 3) == "khoor"
    assert encrypt("attackatdawn", 7) == "haahjrhakhdu"
    assert encrypt("test", 20) == "nymn"
    assert encrypt("python", 13) == "clguba"
    assert encrypt("abc", 0) == "abc"

    # Test decryption
    assert decrypt("khoor", 3) == "hello"
    assert decrypt("haahjrhakhdu", 7) == "attackatdawn"
    assert decrypt("nymn", 20) == "test"
    assert decrypt("clguba", 13) == "python"
    assert decrypt("abc", 0) == "abc"


test_caesar()