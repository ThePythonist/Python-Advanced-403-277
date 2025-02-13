import hashlib

content = "ali"
hash_object = hashlib.md5(content.encode('utf-8'))
hex_dig = hash_object.hexdigest()

print(f"Hashed String: {hex_dig}")
