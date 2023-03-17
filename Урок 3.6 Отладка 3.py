'''
Севокентий решил написать программу, которая заполняет пустой список степенями двойки
Даёшь ей, любую степень двойки, а она список от 2 до этой степени создаёт.
Он вроде бы всё сделал, но что-то идёт не так. Как это исправить?

'''

twolist = []
def make2(twonk, twolist):
    if twonk == 1:
        return twolist
    else:
        twolist.insert(0, int(twonk))
        make2(twonk/2, twolist)
        
make2(1024, twolist)
print(twolist)