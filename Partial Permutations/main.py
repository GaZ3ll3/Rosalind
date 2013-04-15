   
if __name__ == "__main__":
    fid = open('rosalind_pper.txt','r')
    #fout = open('out.txt','w')
    n,k = [int(x) for x in fid.readline().split()]
    #n,k = 21,7
    prod = 1
    for x in range(k):
        prod = prod*(n-x)
        if prod>1000000:
            prod = prod%1000000
    print prod
        
    
    