'''
Read an integer number that is the code number for phone dialing. Then, print the destination according to the following table:

        DDD                          DESTINATION
        61                              BRASILIA
        71                              SALVADOR
        11                              SAO PAULO
        21                              RIO DE JANEIRO
        32                              JUIZ DE FORA
        19                              CAMPINAS
        27                              VITORIA
        31                              BELO HORIZONTE


If the input number isn’t found in the above table, the output must be:
DDD nao cadastrado
That means “DDD not found” in Portuguese language.

Input

The input consists in a unique integer number.

Output

Print the city name corresponding to the input DDD. Print DDD nao cadastrado if doesn't exist corresponding DDD to the typed number.

Input Sample	Output Sample
11                  Sao Paulo

'''
numero = int(input())

DDD = {61:'Brasilia',
        71:'Salvador',
        11:'Sao Paulo',
        21:'Rio de Janeiro',
        32:'Juiz de Fora',
        19:'Campinas',
        27:'Vitoria',
        31:'Belo Horizonte' }

if numero in DDD:
    print(DDD[numero])
else:
    print('DDD nao cadastrado')