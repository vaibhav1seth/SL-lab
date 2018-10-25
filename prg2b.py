
ftclist=[]
ctflist=[]
ctklist=[]
ktclist=[]

def ftc():

    tempf=float(input("enter the temp in fahrenheit : "))
    tempc= (tempf-32)*5/9
    print("\ntemperature in celcius is "+str(tempc))
    ftctuple=(tempf,tempc)
    ftclist.append(ftctuple)

def ctf():

    	tempc=float(input("\nenter the temp in celcius: "))
        tempf= (tempc*9/5)+32
        print("\ntemperature in fahrenheit is "+str(tempf))
        ctftuple=(tempc,tempf)
        ctflist.append(ctftuple)


def ctk():

    	tempc=float(input("\nenter the temp in celcius: "))


    	tempk= tempc+273
    	print("\ntemperature in kelvin is "+str(tempk))
        ctktuple=(tempc,tempk)
        ctklist.append(ctktuple)

def ktc():

    	tempk=float(input("\nenter the temp in kelvin: "))
        tempc= tempk-273
        print("\ntemperature in celcius is "+str(tempc))
        ktctuple=(tempk,tempc)
        ktclist.append(ktctuple)

def convmethod():
    	ch='y'
    	while (ch!='N' or ch!='n'):
    	    print("TEMP-CONVERSION")
    	    print("1.fahrenheit to celcius")
    	    print("2.celcius to fahrenheit")
    	    print("3.celcius to kelvin")
    	    print("4.kelvin to celcius")
    	    ch=input("enter your choice\n")
    	    if(ch=='1'):
    	      	 ftc()
    	    elif (ch=='2'):
    	         ctf()
    	    elif(ch=='3'):
    	         ctk()
    	    elif(ch=='4'):
    	         ktc()
            else:
              	 print("invalid option entered ")

   	    ch=input("\nwish to continue more ??")
    	    if(ch=='N' or ch=='n'):
                break

convmethod()
print("\nlist of converted temperatures")

if(len(ftclist)!=0):
    print("\n list of values converted from fahrenheit to celcius is ")
    print(ftclist)
print("\n")
if(len(ctflist)!=0):
    print("\n list of values converted from celcius to fahrenheit is ")
    print(ctflist)
print("\n")
if(len(ktclist)!=0):
    print("\n list of values converted from kelvin to celcius is ")
    print(ktclist)
print("\n")
if(len(ctklist)!=0):
    print("\n list of values converted from celcius to kelvin is ")
    print(ctklist)
