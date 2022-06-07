# Ask for No. of Atoms
No_H = int(input('Enter number of Hydrogen Atoms: '))
No_C = int(input('Enter number of Carbon Atoms: '))
No_O = int(input('Enter number of Oxygen Atoms: '))

#Printing Molecular Weight
print('Molecular weight of compound is:', (No_H * 1.00794) + (No_C * 12.0107) + (No_O * 15.9994), 'grams/mole')
