
from jawa.cf import ClassFile
print("\033c\033[47;31m\ngive me a .class file ? ")
a=input().strip()
cf = ClassFile(open(a,"rb"))

print("Classe:", cf.this.name.value)

print("\nCampos")
for field in cf.fields:
    print(field.name.value, field.descriptor.value)

print("\nMétodos")
for method in cf.methods:
    print(method.name.value, method.descriptor.value)