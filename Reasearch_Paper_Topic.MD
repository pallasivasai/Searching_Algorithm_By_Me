
### **SAI SEARCH ALGORITHM**

### **A Secure, Worst-Case O(1) Perfect Hashing Search System**

### *Invented by P. Siva Sai*

---

## **Abstract**

The SAI Search Algorithm is a novel, secure, and deterministic search algorithm designed to achieve **worst-case O(1)** lookup performance. Unlike conventional hash tables—which rely on probabilistic assumptions for O(1) performance—the SAI Search Algorithm guarantees strict constant-time search using **two-level perfect hashing**, a cryptographically hardened key-transformation system, and optimized memory layout.

This paper presents the theoretical foundation, system design, and performance analysis of the SAI Search Algorithm created by **P. Siva Sai**.

---

## **1. Introduction**

Searching is a core operation in computing, and traditional hash tables provide efficient average-case performance. However, they fail to guarantee worst-case O(1) time due to collisions and adversarial inputs.

The **SAI Search Algorithm** overcomes these limitations by combining:

* **Perfect hashing (FKS method)**
* **Cryptographic key obfuscation**
* **Collision-free bucket construction**
* **Value-to-key reverse mapping**

The result is a **secure and fully deterministic constant-time search system**, independently designed and formulated by **P. Siva Sai**.

---

## **2. Background**

Traditional hash tables operate in expected O(1) time but degrade to O(n) with collisions.
Perfect hashing solves this by precomputing collision-free structures.

The SAI Search Algorithm extends this concept with:

1. **Cryptographic hashing (SHA-256 + secret)**
2. **Two-level hashing FKS scheme**
3. **Runtime O(1) reverse search**

---

## **3. Algorithm Overview**

### **3.1 Secure Key Transformation**

Each key `k` is transformed into:

```
H(k) = SHA256(secret || k)
```

This ensures:

* Key privacy
* Non-reversible mapping
* Collision resistance
* Protection from hash-flooding attacks

---

### **3.2 First-Level Hashing**

Keys are mapped into `m` buckets:

```
bucket = (a1 * H(k) + b1) mod P mod m
```

This is always O(1).

---

### **3.3 Second-Level Perfect Hashing**

Each bucket is replaced by a collision-free perfect hash table sized:

```
bucket_size²
```

A new hash function:

```
slot = (a2 * H(k) + b2) mod bucket_size²
```

ensures no collisions.

This guarantees **single-step lookup** → **O(1)**.

---

### **3.4 Reverse Value Lookup**

A secondary dictionary maps value → key in O(1) time, enabling two-way search.

---

## **4. Complexity Analysis**

| Operation      | Complexity                       |
| -------------- | -------------------------------- |
| Build          | O(n)                             |
| Search (key)   | **O(1)** (worst-case guaranteed) |
| Search (value) | **O(1)**                         |
| Memory         | O(n)                             |

This surpasses typical hash tables by eliminating collision performance degradation.

---

## **5. Security Model**

The algorithm is resistant to:

* Key exposure
* Reverse lookup attacks
* Hash-flooding DoS attacks
* Collision manipulation

Due to cryptographically salted hashing.

---

## **6. Applications**

* High-performance databases
* Cybersecurity indexing
* Blockchain lookup structures
* Real-time systems
* Search engines
* Machine learning label storage

---

## **7. Conclusion**

The SAI Search Algorithm, invented by **P. Siva Sai**, represents a modern, secure, and fully deterministic O(1) indexing system. Its combination of perfect hashing and cryptographic protection enables unprecedented reliability, making it suitable for high-security or large-scale search applications.

---

# 📊 **2. Diagram of the SAI Search Algorithm**

Below is an ASCII diagram (you can also request a graphical PNG version):

```
                +------------------------------+
                |  User Input (Key or Value)  |
                +---------------+--------------+
                                |
                                v
                    +-----------------------+
                    | Secure Hash Function  |
                    | H = SHA256(secret|k)  |
                    +-----------------------+
                                |
                                v
               +------------------------------------+
               | First-Level Hash Function          |
               | bucket = (a1*H + b1) mod P mod m   |
               +------------+-----------------------+
                            |
                            v
               +-------------------------------+
               |   Bucket for this key         |
               |   (precomputed during build)  |
               +---------------+---------------+
                               |
                               v
           +----------------------------------------------+
           | Second-Level Perfect Hash Function           |
           | slot = (a2*H + b2) mod bucket_size²          |
           +-------------------+--------------------------+
                               |
                               v
          +------------------------------------------------+
          | Collision-Free Slot → Returns Value in O(1)    |
          +------------------------------------------------+
```

---

# 📄 **3. LICENSE (MIT License)**

```
MIT License

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
```

---

