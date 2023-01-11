from keyset import KeySet, KeyObject as KO

keys = [
    KO(1, "Q"),
    KO(2, "W"),
    KO(3, "E")
]

ks = KeySet(keys)

print(ks.has_key(1))
