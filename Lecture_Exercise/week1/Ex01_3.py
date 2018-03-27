mass1 = input("Enter the mass of object 1 (kg): ")
mass2 = input("Enter the mass of object 2 (kg): ")
distance = input("Enter the distance between object 1 and object 2 (m): ")
mass1,mass2,distance=float(mass1),float(mass2),float(distance)
G=6.67384e-11
print("The force between the object 1 and object 2 is", G*mass1*mass2/(distance**2), 'N')