# AC-Circuit
Interactive Python tool that models AC circuits using complex numbers — calculates impedance, current, and phase for series/parallel combinations of L,C,R  components.

It models the working of an AC circuit. The user can add any number of resistors, capacitors or inductors, choose series or parallel connections and view the final value of impedance or current and their respective phases

Used complex numbers for the calculations of reactances since it makes the calculations much easier this way, rather than calculating using trigonometry. The imaginary part is the phase shift. 0 for resistor, +ve angle for an inductor and -ve angle for a capacitor, due to the voltage leading the current in case of inductors and lagging in case of capacitors. (Basics of AC circuits)

python AC_Generator.py
prompts guide you how to run the program throughout

**Example Run:**

```
Enter the frequency: 50
What do you want to enter?:
    1. Capacitance
    2. Resistance
    3. Inductance
    4. Quit
2
What is the resistance? 30
What do you want to enter?:
    1. Capacitance
    2. Resistance
    3. Inductance
    4. Quit
3
What is the inductance? 1
What do you want to enter?:
    1. Capacitance
    2. Resistance
    3. Inductance
    4. Quit
4
series or parallel?: series
What would you like to know?:
    1. Current
    2. Phase of Current
    3. Total Impedance
    4. Phase of Total Impedance
    5. Quit
1
0.697
What would you like to know?:
    1. Current
    2. Phase of Current
    3. Total Impedance
    4. Phase of Total Impedance
    5. Quit
2
-1.4755920468880166
What would you like to know?:
    1. Current
    2. Phase of Current
    3. Total Impedance
    4. Phase of Total Impedance
    5. Quit
3
315.588
What would you like to know?:
    1. Current
    2. Phase of Current
    3. Total Impedance
    4. Phase of Total Impedance
    5. Quit
5
```

Formulas used:
|Xc| = 1/omega*c
|Xl| = omega * c

the directions are given by + or -

Possible Future Additions:

1. Waveform/Phasor diagrams of the AC circuit (planned)
