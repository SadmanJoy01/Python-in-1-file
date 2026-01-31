"""
PYTHON CHEAT SHEET (Most Important Methods)
=========================================
Focused on real-world usage, interviews, automation, data, backend.
"""

# =============================
# BASIC BUILT-IN FUNCTIONS
# =============================
print()             # output
input()             # user input
len()               # length of object
type()              # check data type
range()             # generate sequence
enumerate()         # index + value
zip()               # combine iterables
sorted()            # sort iterable
sum()               # sum values
min(), max()        # min / max
abs()               # absolute value
round()             # rounding
help()              # documentation


# =============================
# STRING METHODS
# =============================
s = " Hello World "

s.lower()
s.upper()
s.title()
s.strip()
s.replace("World", "Python")
s.split(" ")
" ".join(["Hello", "Python"])
s.startswith("H")
s.endswith("d")
s.find("World")
s.count("o")
s.isdigit()
s.isalpha()


# =============================
# LIST METHODS
# =============================
lst = [1, 2, 3]

lst.append(4)
lst.extend([5, 6])
lst.insert(0, 0)
lst.remove(3)
lst.pop()
lst.index(2)
lst.count(2)
lst.sort()
lst.reverse()
lst.copy()
lst.clear()


# =============================
# TUPLE (IMMUTABLE)
# =============================
t = (1, 2, 3)
t.count(2)
t.index(3)


# =============================
# SET METHODS
# =============================
st = {1, 2, 3}

st.add(4)
st.remove(2)
st.discard(10)
st.union({5, 6})
st.intersection({1, 4})
st.difference({3})
st.clear()


# =============================
# DICTIONARY METHODS
# =============================
d = {"a": 1, "b": 2}

d.keys()
d.values()
d.items()
d.get("a")
d.update({"c": 3})
d.pop("b")
d.popitem()
d.clear()


# =============================
# CONDITIONALS & LOOPS
# =============================
if True:
    pass

for i in range(5):
    pass

while False:
    break

continue


# =============================
# FUNCTIONS
# =============================
def func(a, b=0):
    return a + b

lambda x: x * 2


# =============================
# EXCEPTION HANDLING
# =============================
try:
    x = int("10")
except ValueError:
    print("Error")
finally:
    print("Done")


# =============================
# FILE HANDLING
# =============================
with open("file.txt", "r") as f:
    f.read()

with open("file.txt", "w") as f:
    f.write("Hello")


# =============================
# OS & SYSTEM (AUTOMATION)
# =============================
import os
import sys
from pathlib import Path

os.getcwd()
os.listdir()
os.mkdir("test")
os.remove("file.txt")

Path("data").exists()
Path("data/file.txt").read_text()
Path("data/file.txt").write_text("Hello")

sys.argv
sys.exit()


# =============================
# DATE & TIME
# =============================
from datetime import datetime, timedelta

now = datetime.now()
now.date()
now.time()
now.strftime("%Y-%m-%d")

now + timedelta(days=1)


# =============================
# JSON (API & DATA)
# =============================
import json

json.dumps({"a": 1})
json.loads('{"a": 1}')

with open("data.json", "r") as f:
    json.load(f)

with open("data.json", "w") as f:
    json.dump({"a": 1}, f)


# =============================
# REQUESTS (API)
# =============================
import requests

r = requests.get("https://api.example.com")
r.status_code
r.json()
r.text


# =============================
# COMPREHENSIONS (VERY IMPORTANT)
# =============================
[x * 2 for x in range(5)]
{x: x * 2 for x in range(5)}
{x for x in range(5) if x % 2 == 0}


# =============================
# USEFUL MODULES TO REMEMBER
# =============================
# math, random, statistics
# itertools, functools
# pandas, numpy (data)
# streamlit (apps)
# fastapi, flask, django (backend)
