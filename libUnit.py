import abc

class Temperature(abc.ABC):
    def cels_far(temp, inverse = 0):
        if inverse == 0:
            fah = (temp * 9/5) + 32
            return fah
        elif inverse == 1:
            cel = (temp - 32) * 5/9
            return cel
        else:
            print('A opção do segundo parâmentro usado não existe.\n')
            print('-> 0 de celsius para fahrenheit\n')
            print('-> 1 de fahrenheit para celsius\n')

