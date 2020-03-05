def secondelement(matrix):
    return matrix[1]

def main():
    new_mtrix=[['Apple',20,56],['Mango',1,45],['Orange',40,34],['banana',2,67]]
    new_mtrix.sort(key=secondelement)
    print(new_mtrix)
main()