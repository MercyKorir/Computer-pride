def getVat(VAT, paymentAmount):
    vat = VAT * paymentAmount
   
    return vat 

def userInput():
    paymentAmount = int(input("Enter payment amount"))
    VAT = 0.16
    vat = getVat(VAT, paymentAmount)
    vat = str(getVat(VAT, paymentAmount))
    
    print("Ksh" +vat)
userInput()
