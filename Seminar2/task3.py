mirror = {
    'A': 'A', 'H': 'H', 'I': 'I', 'M': 'M', 'O': 'O',
    'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X',
    'Y': 'Y', '1': '1', '8': '8',
    'E': '3', '3': 'E',
    'J': 'L', 'L': 'J',
    'S': '2', '2': 'S',
    'Z': '5', '5': 'Z',
}

s = input().strip()

is_palindrome = s == s[::-1]
is_mirrored = all(
    c in mirror and mirror[c] == s[len(s) - 1 - i]
    for i, c in enumerate(s)
)

if is_palindrome and is_mirrored:
    print(f"{s} is a mirrored palindrome.")
elif is_palindrome:
    print(f"{s} is a regular palindrome.")
elif is_mirrored:
    print(f"{s} is a mirrored string.")
else:
    print(f"{s} is not a palindrome.")
