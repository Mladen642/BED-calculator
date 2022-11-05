def BED(n,d,alfabeta):

    #racun
    BED = round(float(n*d*(1 + (d/(alfabeta)))),2)
    
    print(f'Ukupan BED iznosi {BED} Gy!')
    
if __name__ == '__main__':
    #broj frakcija  
    n = int(input('Broj frakcija: '))

    #doza po frakciji
    d = float(input('Doza po frakciji: '))
    
    alfabeta = int(input('alfa/beta: '))
    
    BED(n,d,alfabeta)