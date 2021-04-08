import time
import sys

def get_firstUnit():
    while True:
        A = input("Gib die Einheit ein, die du umrechnen willst: ")
        try:
            A = str(A)
            return A

        except ValueError:
            print("Das ist keine gültige Einheit!")


def get_unit():
    while True:
        E = input("Gib die Einheit ein, IN die du umgerechnet haben willst: ")
        try:
            E = str(E)
            return E

        except ValueError:
            print("Das ist keine gültige Einheit!")


def get_number():
    while True:
        C = input("Gib die gewünschte Zahl ein: ")
        try:
            C = float(C)
            return C

        except ValueError:
            print("Das ist keine gültige Angabe für eine Temperatur!")


n = get_firstUnit()
m = get_unit()


if __name__ == "__main__":
    
    #Temperatur
    if n == "Celsius":
        if m == "Kelvin":
            T = get_number()
            print("Das sind " + str(T + 273.15) + "° Kelvin.")

        if m == "Fahrenheit":
            T = get_number()
            print("Das sind " + str(T * 1.8 + 32) + "° Fahrenheit.")


    if n == "Kelvin":
        if m == "Celsius":
            T = get_number()
            print("Das sind " + str(T - 273.15) + "° Celsius.")

        if m == "Fahrenheit":
            T = get_number()
            print("Das sind " + str(T - 273.15 * 1.8 + 32) + "° Fahrenheit.")

    
    if n == "Fahrenheit":
        if m == "Celsius":
            T = get_number()
            print("Das sind " + str(T / 1.8 - 32) + "° Celsius.")

        if m == "Kelvin":
            T = get_number()
            print("Das sind " + str(T + 273.15 / 1.8 - 32) + "° Fahrenheit")

    #Strecke

    if n == "Meter":
        if m == "Kilometer":
            S = get_number()
            print("Das sind " + str(S / 1000) + " Kilometer.")

        if m == "Dezimeter":
            S = get_number()
            print("Das sind " + str(S * 10) + " Dezimeter.")

        if m == "Zentimeter":
            S = get_number()
            print("Das sind " + str(S * 100) + " Zentimeter.")

        if m == "Millimeter":
            S = get_number()
            print("Das sind " + str(S * 1000) + " Milimeter.")


    if n == "Kilometer":
        if m == "Meter":
            S = get_number()
            print("Das sind " + str(S * 1000) + " Meter.")

        if m == "Dezimeter":
            S = get_number()
            print("Das sind " + str(S * 100) + " Dezimeter.")

        if m == "Zentimeter":
            S = get_number()
            print("Das sind " + str(S * 1000) + " Zentimeter.")

        if m == "Millimeter":
            S = get_number()
            print("Das sind " + str(S * 1000000) + " Milimeter.")


    if n == "Dezimeter":
        if m == "Kilometer":
            S = get_number()
            print("Das sind " + str(S / 10000) + " Kilometer.")

        if m == "Meter":
            S = get_number()
            print("Das sind " + str(S / 10) + " Dezimeter.")

        if m == "Zentimeter":
            S = get_number()
            print("Das sind " + str(S * 10) + " Zentimeter.")

        if m == "Millimeter":
            S = get_number()
            print("Das sind " + str(S * 100) + " Milimeter.")


    if n == "Zentimeter":
        if m == "Kilometer":
            S = get_number()
            print("Das sind " + str(S / 100000) + " Kilometer.")

        if m == "Dezimeter":
            S = get_number()
            print("Das sind " + str(S / 10) + " Dezimeter.")

        if m == "Meter":
            S = get_number()
            print("Das sind " + str(S / 100) + " Meter.")

        if m == "Millimeter":
            S = get_number()
            print("Das sind " + str(S * 10) + " Milimeter.")


    if n == "Millimeter":
        if m == "Kilometer":
            S = get_number()
            print("Das sind " + str(S / 1000000) + " Kilometer.")

        if m == "Dezimeter":
            S = get_number()
            print("Das sind " + str(S / 100) + " Dezimeter.")

        if m == "Zentimeter":
            S = get_number()
            print("Das sind " + str(S / 10) + " Zentimeter.")

        if m == "Meter":
            S = get_number()
            print("Das sind " + str(S / 1000) + " Milimeter.")


time.sleep(5)