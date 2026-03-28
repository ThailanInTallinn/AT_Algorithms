from hashtable import *

ht = HashTableChained(100)
for i in range(0, 1000):
    ht.put(i, i)

print(ht.tabela)
print(ht.__len__())
