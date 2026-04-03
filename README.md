import random
import string

def generate_username(length):
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

# عدد اليوزرات
count = 20

print("=== Generated Usernames ===")

for _ in range(count):
    length = random.choice([3, 4])  # 3 أو 4 أحرف
    username = generate_username(length)
    print(username)
