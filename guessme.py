import math
import random

print("Nenn mir bitte einen Zahlenbereich Deiner Wahl.")

def number_guessing_game():
    
    # eingaben annehmen
    lower = int(input("Untere Grenze: "))
    upper = int(input("Obere Grenze: "))
    
    # gesuchte zahl definieren als random von/bis
    # berechnung anzahl der versuche mit log2:
    # binäre suche als klassischer algorithmus -> log2 ermittelt, wie oft ein wert halbiert werden kann
    # hier also log(wert=differenz der range (inkl endwert), zur basis 2)
    magicnumber = random.randint(lower, upper)
    max_attempts = math.ceil(math.log(upper - lower + 1, 2))
    
    print(f"Ich habe eine Zahl zwischen {lower} und {upper} ausgewählt.")
    print(f"Du hast {max_attempts} Versuche sie zu erraten!\n")
    
    # schleife für die versuche
    # range: +1 um tatsächliche anzahl max_attempts auszuführen, also inkl endwert
    # f-string um variablen im text einzusetzen
    for attempt in range(1, max_attempts + 1):
        guess = int(input(f"Versuch {attempt}/{max_attempts} – Gib eine Zahl ein: "))
        
        if guess < magicnumber:
            print(f"Die gesuchte Zahl ist größer als {guess}.\n")
        elif guess > magicnumber:
            print(f"Die gesuchte Zahl ist kleiner als {guess}.\n")
        else:
            print(f"Herzlichen Glückwunsch! Du hast die richtige Zahl ({magicnumber}) in {attempt} Versuchen erraten!")
            break
    else:
        print(f"Leider hast du die richtige Zahl nicht erraten. Sie lautet {magicnumber}.")

# ausführen 
number_guessing_game()