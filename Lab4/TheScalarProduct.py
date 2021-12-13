a = [1, 2, 12, 4]
b = [2, 4, 2, 8]
if len(a) != len(b):
    raise ValueError("Dimensions of vectors must be the same")

the_scalar_product = 0

for aa, bb in zip(a, b):
    the_scalar_product += aa * bb

print("The scalar product of matrix a and b is: ")
print(the_scalar_product)
