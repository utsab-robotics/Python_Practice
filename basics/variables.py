import sys

print("===== PYTHON DATA TYPES & SIZES =====\n")

# ---------------- Integers ----------------
a = 10
print("Integer:", a, "| Type:", type(a), "| Size:", sys.getsizeof(a), "bytes")

# ---------------- Float ----------------
b = 10.5
print("Float:", b, "| Type:", type(b), "| Size:", sys.getsizeof(b), "bytes")

# ---------------- String ----------------
c = "Hello Python"
print("String:", c, "| Type:", type(c), "| Size:", sys.getsizeof(c), "bytes")

# ---------------- Boolean ----------------
d = True
print("Boolean:", d, "| Type:", type(d), "| Size:", sys.getsizeof(d), "bytes")

# ---------------- List ----------------
e = [1, 2, 3, 4, 5]
print("List:", e, "| Type:", type(e), "| Size:", sys.getsizeof(e), "bytes")

# ---------------- Tuple ----------------
f = (1, 2, 3, 4, 5)
print("Tuple:", f, "| Type:", type(f), "| Size:", sys.getsizeof(f), "bytes")

# ---------------- Set ----------------
g = {1, 2, 3, 4, 5}
print("Set:", g, "| Type:", type(g), "| Size:", sys.getsizeof(g), "bytes")

# ---------------- Dictionary ----------------
h = {"name": "Utsav", "age": 25}
print("Dictionary:", h, "| Type:", type(h), "| Size:", sys.getsizeof(h), "bytes")

# ---------------- Complex Number ----------------
i = 3 + 4j
print("Complex:", i, "| Type:", type(i), "| Size:", sys.getsizeof(i), "bytes")

print("\n===== END =====")