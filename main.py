import re

def valid_uzbek_phone(phone_number):
    pattern = r'^\+998\d{9}$'
    return bool(re.match(pattern, phone_number))
```

```python
# Test qilish
print(valid_uzbek_phone("+998901234567"))  # True
print(valid_uzbek_phone("+99890123456"))   # False
print(valid_uzbek_phone("+998901234"))     # False
print(valid_uzbek_phone("+9989012"))       # False
print(valid_uzbek_phone("+998901"))        # False
print(valid_uzbek_phone("+9989"))          # False
print(valid_uzbek_phone("+998"))           # False
print(valid_uzbek_phone("998901234567"))   # False
print(valid_uzbek_phone("+9989012345678")) # False
