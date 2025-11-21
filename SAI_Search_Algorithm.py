# SAI SEARCH ALGORITHM - INVENTED BY P. SIVA SAI
import hashlib, secrets

print("Your Using SAI Search Algorithm by P. Siva Sai")

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
            k = keys[0]
            return self._search_by_key(k)
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
