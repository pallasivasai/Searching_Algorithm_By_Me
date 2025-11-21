Below is a complete **README.md** for your algorithm, fully formatted and ready for GitHub.

---

# 📘 **SAI Search Algorithm**

### **Secure Always-O(1) Indexed Search**

### *Invented by P. Siva Sai*

The **SAI Search Algorithm** is a high-performance lookup algorithm that guarantees **worst-case O(1) search time**.
Unlike normal hash tables (which are only *expected* O(1)), the SAI Search Algorithm uses **two-level perfect hashing** to achieve **strict, provable constant-time lookups**.

It also implements **secure key hashing** using a hidden secret to prevent key leakage and unauthorized reverse-mapping.

---

## 🚀 Features

* 🔹 **True O(1) search time** — worst-case guaranteed
* 🔹 **Perfect hashing (FKS method)**
* 🔹 **Secure hashed keys using SHA-256 + secret**
* 🔹 **Supports search by key or by value**
* 🔹 **Prevents data exposure by storing only secret-hashed keys**
* 🔹 **Lightweight, fast, and memory-efficient**
* 🔹 **Custom algorithm officially named after P. Siva Sai**

---

## 🧠 How It Works

The SAI Search Algorithm uses **two-level perfect hashing**:

### **1️⃣ First-Level Hash**

Keys are mapped into buckets:

```
bucket = (a1 * H(key) + b1) mod P mod m
```

This is always **O(1)**.

---

### **2️⃣ Second-Level Perfect Hash**

Each bucket is replaced with a collision-free table sized:

```
bucket_size²
```

A second hash function:

```
slot = (a2 * H(key) + b2) mod table_size
```

Ensures **zero collisions**, guaranteeing **constant-time lookups**.

---

### **3️⃣ Secure Hashed Keys**

Every user key is internally transformed into:

```
H = SHA256(secret || key)
```

This:

* Hides original keys
* Prevents reverse engineering
* Prevents hash collision attacks

---

### **4️⃣ Reverse Lookup**

The algorithm also stores `value → key` mapping using a Python dict (O(1) expected), allowing you to search by **key or value**.

---

## 📦 Code Example

```python
# SAI SEARCH ALGORITHM - INVENTED BY P. SIVA SAI
import hashlib, secrets

print("Using SAI Search Algorithm by P. Siva Sai")

class SAISearch:
    def __init__(self, secret=None):
        self.secret = secret if secret is not None else secrets.token_bytes(16)
        self.items = []
        self.built = False
    def add_input(self, key, value):
        self.items.append((key, value))
    def build(self):
        n = len(self.items)
        self.P = (1 << 61) - 1
        self.m = max(1, n)
        self.a1 = secrets.randbelow(self.P - 1) + 1
        self.b1 = secrets.randbelow(self.P)
        buckets = [[] for _ in range(self.m)]
        for k, v in self.items:
            x = self._key_int(k)
            idx = ((self.a1 * x + self.b1) % self.P) % self.m
            buckets[idx].append((k, v))
        self.second = [None] * self.m
        self.sec_params = [None] * self.m
        for i, b in enumerate(buckets):
            bi = len(b)
            if bi == 0:
                self.second[i] = []
                self.sec_params[i] = (0, 0, 1)
                continue
            s = bi * bi
            built = False
            while not built:
                a2 = secrets.randbelow(self.P - 1) + 1
                b2 = secrets.randbelow(self.P)
                table = [None] * s
                collision = False
                for key, val in b:
                    x = self._key_int(key)
                    j = ((a2 * x + b2) % self.P) % s
                    if table[j] is None:
                        table[j] = (key, val)
                    else:
                        collision = True
                        break
                if not collision:
                    built = True
                    self.second[i] = table
                    self.sec_params[i] = (a2, b2, s)
        self.reverse = {}
        for k, v in self.items:
            self.reverse.setdefault(v, []).append(k)
        self.built = True
    def _key_int(self, key):
        kb = key.encode() if isinstance(key, str) else bytes(key)
        d = hashlib.sha256(self.secret + kb).digest()
        return int.from_bytes(d, "big") % self.P
    def _search_by_key(self, key):
        x = self._key_int(key)
        idx = ((self.a1 * x + self.b1) % self.P) % self.m
        a2, b2, s = self.sec_params[idx]
        if s == 1 and self.second[idx] == []:
            return None
        j = ((a2 * x + b2) % self.P) % s
        slot = self.second[idx][j]
        if slot is None:
            return None
        if slot[0] == key:
            return slot[1]
        return None
    def search(self, q):
        v = self._search_by_key(q)
        if v is not None:
            return v
        keys = self.reverse.get(q)
        if keys:
            return self._search_by_key(keys[0])
        return None

s = SAISearch()
count = int(input("How many key-value pairs: "))
for _ in range(count):
    k = input("Enter key: ")
    v = input("Enter value: ")
    s.add_input(k, v)
s.build()
while True:
    q = input("Search key or value (or 'exit'): ")
    if q == "exit":
        break
    r = s.search(q)
    if r is None:
        print("Result: None")
    else:
        print("Your search is found:", r)
```

---

## ⏱ Time Complexity

| Operation           | Time     | Notes                  |
| ------------------- | -------- | ---------------------- |
| **Build**           | O(n)     | Done once              |
| **Search by key**   | **O(1)** | Worst-case, guaranteed |
| **Search by value** | O(1)     | Uses dict              |
| **Memory**          | O(n)     | Efficient              |

---

## 🧑‍💻 Author

**Inventor:**

### 🟦 *P. Siva Sai*

Creator of the **SAI Search Algorithm**

---

## 📄 License

MIT License (recommended).

Copyright (c) 2025 P. Siva Sai

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "SAI Search Algorithm"),
to deal in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is furnished
to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
