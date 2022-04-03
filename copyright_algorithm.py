# cosine similarity measure ->

import math

s1 = "the sun rises in the east"
s1_splits = s1.split()

s2 = "the sun in the sky is bright"
s2_splits = s2.split()

T = set()

for x in s1_splits:
    T.add(x)
for x in s2_splits:
    T.add(x)
print(T)

Vs1 = []
for x in T:
    c = 0
    for y in s1_splits:
        if x == y:
            c = c+1
    Vs1.append(c)

print(Vs1)

Vs2 = []
for x in T:
    c = 0
    for y in s2_splits:
        if x == y:
            c = c+1
    Vs2.append(c)

print(Vs2)

vector_size = len(Vs1)

dot_product = 0
for i in range(0, vector_size):
    dot_product = dot_product + Vs1[i]*Vs2[i]

cross_product_vector = []
for i in range(0, vector_size):
    product = 0
    for j in range(0, vector_size):
        product = product + Vs1[i]*Vs2[j]
    cross_product_vector.append(product)

cross_product = 0
for product in cross_product_vector:
    cross_product = cross_product + product**2
cross_product = math.sqrt(cross_product)


cosine = (dot_product/cross_product)*100

print(f"{cosine}% similarity!")












