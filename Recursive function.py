def f(n):
    if n <=2:
        result = n
    else:
        result = f(n-2) + f(n-3)
    return result

s=input("Ingrese el numero que quiere ver ")
print(f(int(s)))


#Quiero declarar una variable que multiplique por 2 la función.

Multi=f(int(s))*2
print(Multi)