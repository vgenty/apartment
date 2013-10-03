import sys

def who_ows_who(vic,doug) :
    split = (sum(vic)+sum(doug))/2
    print ''
    payme = ''
    if sum(vic) > split : 
        payme = "Doug ows Vic $ %f" % (-1*(sum(doug)-split))       
    if sum(doug) > split : 
        payme = "Vic ows Doug $ %f" % (-1*(sum(vic)-split))

    return payme

def main():
    print "Who ows who? Hit 0 to move on to the next person."
    vic=[]
    doug=[]
    temp= 1  

    while temp > 0:
        temp = float(raw_input("Vic spent: "))
        vic.append(temp)
                  
    temp=1
    while temp > 0:
        temp=float(raw_input("Doug spent: "))
        doug.append(temp)

    print who_ows_who(vic,doug)

if __name__ == '__main__':
    main()
