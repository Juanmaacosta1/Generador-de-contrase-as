import string
import random
longitud = int (input ("ingrese la longitud de su contraseña"))
caracteres = string.ascii_letters + string.digits + string.punctuation
contraeña = "".join(random.choice(caracteres) for i in range(longitud))
print("la contraseña generada es : " + contraeña)