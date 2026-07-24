import cmath, math, sys

pi = math.pi

E = 220

while True:
    try:
        frequency = int(input("Enter the frequency: "))
        if frequency == 0:
            print("Please enter another value, frequency cannot be zero in AC circuits!!")
            continue

        break

    except ValueError:
        print("Please enter a number")
    


class Resistor():

    def __init__(self, value=0):    
        self.mag = value

    def impedance(self, frequency):

        return self.mag + 0j
    
class Capacitor():

    def __init__(self, value=0):  
        self.mag = value


    def impedance(self, frequency):
        omega = 2 * pi * frequency


        return 0 - (1 / (omega * self.mag)) * 1j
    
    
class Inductor():

    def __init__(self, value=0):   
        self.mag = value

    def impedance(self, frequency):
        omega = 2 * pi * frequency

        return 0 + (omega * self.mag) * 1j
    
def series(resistors, capacitors, inductors, frequency):
    total = 0

    for r in resistors:
        total+= Resistor.impedance(r, frequency)
    for c in capacitors:
        total += Capacitor.impedance(c, frequency)
    for l in inductors:
        total += Inductor.impedance(l, frequency)
    
    return total

def parallel(resistors, capacitors, inductors, frequency):
    invert = 0

    for r in resistors:
        invert += 1/Resistor.impedance(r, frequency)
    for c in capacitors:
        invert += 1/Capacitor.impedance(c, frequency)
    for l in inductors:
        invert += 1/Inductor.impedance(l, frequency)

    return 1/invert


resistors=[]
capacitors=[]
inductors=[]

while True:
    print('''What do you want to enter?:
    1. Capacitance
    2. Resistance
    3. Inductance
    4. Quit''')
    try:
        x=int(input())

    except ValueError:
        print("Please enter a number!")
        continue

    if x == 1:
        try:
            capacitance = float(input("What is the capacitance? "))
            if capacitance !=0:
                capacitors.append(Capacitor(capacitance))
            else:
                print("If value is 0, component doesn't exist -- skipping.", end='\n')

        except ValueError:
            print("Please enter a number!")
            continue

    elif x == 2:
        try:
            resistance = int(input("What is the resistance? "))
            if resistance !=0:
                resistors.append(Resistor(resistance))
            else:
                print("If value is 0, component doesn't exist -- skipping.", end='\n')

        except ValueError:
            print("Please enter a number!")     
            continue   

    elif x == 3:
        try:
            inductance = float(input("What is the inductance? "))
            if inductance != 0:
                inductors.append(Inductor(inductance))
            else:
                print("If value is 0, component doesn't exist -- skipping.", end='\n')

        except ValueError:
            print("Please enter a number!")
            continue

    elif x == 4:
        break

    else:
        print("Please enter one of the given options!")

if not (resistors or capacitors or inductors):
    print("No Components added -- exiting")
    sys.exit()

while True:
    circuit = input("series or parallel?: ").lower()

    if circuit == 'series':
        Z_total = series(resistors, capacitors, inductors, frequency)
        break
    elif circuit == 'parallel':
        Z_total = parallel(resistors, capacitors, inductors, frequency)
        break

    else:
        print("Kindly check your spelling and enter again!", end='\n')

I = E/Z_total
I_mag = abs(I)
I_phase = cmath.phase(I)

Z_mag = abs(Z_total)
Z_phase = cmath.phase(Z_total)

while True:
    print('''What would you like to know?:
    1. Current
    2. Phase of Current
    3. Total Impedance
    4. Phase of Total Impedance
    5. Quit''')

    try:
        y=int(input())

    except ValueError:
        print("Please enter a number!")
        continue

    if y==1:
        print(round(I_mag, 3), end='\n')

    elif y==2:
        print(I_phase, end='\n')

    elif y==3:
        print(round(Z_mag, 3), end='\n')

    elif y==4:
        print(Z_phase, end='\n')

    elif y==5:
        break

    else:
        print("Please enter one of the given options!")