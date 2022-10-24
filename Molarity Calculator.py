molecular_mass = float(input("Please enter the molecular mass of the compound(in g/mol): "))
volume_of_solution = float(input("Please enter the volume of solution you want to create (in ml): "))
molarity = float(input("Please enter the desired concentration or molarity (molar M): "))

mass =round(molarity * (volume_of_solution / 1000) * molecular_mass, 3)
print(f"\t\nSummary\nMolecular Mass: {molecular_mass}g/mol\nVolume: {volume_of_solution}ml\nConverted Volume: {volume_of_solution / 1000}L\nDesired Concentration(Molarity): {molarity}molar")
print(f"\nAmount of compound needed for the solution: {mass}g")