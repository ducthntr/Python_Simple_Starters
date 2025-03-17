from emojicypher import EmojiCipher

cipher = EmojiCipher()
message = input("What should I encrypt for you?")
encrypted = cipher.encrypt(message)
decrypted = cipher.decrypt(encrypted)

print(f"Original: {message}")
print(f"Emojified: {encrypted}")
print(f"Demojified: {decrypted}")
