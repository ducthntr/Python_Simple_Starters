class EmojiCipher:
    def __init__(self):
        # Basic emoji mapping
        self.emoji_map = {
            'A': '😀', 'B': '😎', 'C': '😊', 'D': '😃', 'E': '😅',
            'F': '😂', 'G': '😇', 'H': '😉', 'I': '😋', 'J': '😌',
            'K': '😍', 'L': '😘', 'M': '😗', 'N': '😙', 'O': '😚',
            'P': '😝', 'Q': '😛', 'R': '😜', 'S': '😞', 'T': '😟',
            'U': '😤', 'V': '😢', 'W': '😭', 'X': '😦', 'Y': '😧',
            'Z': '😮', ' ': '👻'
        }
        # Reverse mapping for decryption
        self.reverse_map = {v: k for k, v in self.emoji_map.items()}

    def encrypt(self, text):
        return ''.join(self.emoji_map.get(c.upper(), c) for c in text)

    def decrypt(self, text):
        # Split
        # emojis are single characters in Python
        return ''.join(self.reverse_map.get(c, c) for c in text)

# USE

#cipher = EmojiCipher()
#message = input("What would you like to encrypt?")
#encrypted = cipher.encrypt(message)
#decrypted = cipher.decrypt(encrypted)

#print(f"Original: {message}")
#print(f"Encrypted: {encrypted}")
#print(f"Decrypted: {decrypted}")

