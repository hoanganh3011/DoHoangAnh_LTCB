# 1
s = "hello world"
print(len(s))

# 2
s = "google.com"
print(s.count("g"), s.count("o"), s.count("l"), s.count("e"), s.count("."), s.count("c"), s.count("m"))

# 3
s = "w3resource"
print(s[:2] + s[-2:])

# 4
s = "restart"
print(s[0] + s[1:].replace(s[0], "$"))

# 5
a, b = "abc", "xyz"
print(b[:2] + a[2:] + " " + a[:2] + b[2:])

# 6
s = "abc"
print(s + "ing")

# 7
s = "The lyrics is not that poor!"
print(s.replace("not that poor", "good"))

# 8
words = ["Exercises", "are", "fun"]
longest = max(words, key=len)
print(longest, len(longest))

# 9
s = "python"
n = 2
print(s[:n] + s[n+1:])

# 10
s = "python"
print(s[-1] + s[1:-1] + s[0])

# 11
s = "abcdef"
print(s[::2])

# 12
s = "this is a test this"
print(len(s.split()))

# 13
s = "Hello"
print(s.upper(), s.lower())

# 14
s = "red, white, black, red, green, black"
print(",".join(sorted(set(s.split(", ")))))

# 15
tag, word = "i", "Python"
print(f"<{tag}>{word}</{tag}>")

# 16
s = "[[]]"
print(s[:2] + "Python" + s[2:])

# 17
s = "Python"
print(s[-2:]*4)

# 18
s = "python"
print(s[:3])

# 19
s = "https://www.w3resource.com/python"
print(s.rsplit("/",1)[0])

# 20
s = "abcd"
print(s[::-1])

# 21
s = "PyTHon"
print(s.upper())

# 22
s = "python"
print("".join(sorted(s)))

# 23
s = "Hello\nWorld"
print(s.replace("\n",""))

# 24
s = "Python"
print(s.startswith("Py"))

# 25
s = "abcxyz"
abc = "abcdefghijklmnopqrstuvwxyz"
print("".join([abc[(abc.index(c)+3)%26] for c in s]))

# 26
s = "Hello Python"
print(s.center(50))

# 27
s = "   hello   "
print(s.strip())

# 28
s = "line1\nline2"
print(s.replace("\n", "\n>>> "))

# 29
s = "hello"
print("   " + s)

# 30
n = 3.14159
print(round(n,2))

# 31
print(f"{n:+.2f}")

# 32
print(int(n))

# 33
print(str(7).zfill(5))

# 34
print(str(7).ljust(5,"*"))

# 35
n = 1000000
print(f"{n:,}")

# 36
x = 0.85
print(f"{x:.0%}")

# 37
s = "hi"
print(s.ljust(10), s.rjust(10), s.center(10))

# 38
s = "banana"
print(s.count("na"))

# 39
s = "python"
print(s[::-1])

# 40
s = "I love Python"
print(" ".join(s.split()[::-1]))

# 41
s = "hello world"
print(s.replace("l",""))

# 42
s = "thequickbrownfoxjumpsoverthelazydog"
print(s.count("o"), s.count("e"), s.count("u"))

# 43
s = "w3resource"
print(s.index("r"))

# 44
import string
s = "thequickbrownfoxjumpsoverthelazydog"
print(set(string.ascii_lowercase).issubset(set(s)))

# 45
s = "The quick brown fox"
print(s.split())

# 46
s = "HELLO"
print(s.lower())

# 47
s = "32.054,23"
print(s.replace(".", "#").replace(",", ".").replace("#", ","))

# 48
s = "hello world"
print(sum(s.count(v) for v in "aeiou"))

# 49
s = "a-b-c-d"
print(s.rsplit("-",1))

# 50
s = "Python Exercises"
print(s.replace(" ",""))

