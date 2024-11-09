import time
import random
goodansw = 0
RED = '\033[31m'
BLUE = '\033[34m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
RESET = '\033[0m'
print(f"{YELLOW}Quiz de culture G")
presse = input(f"{YELLOW}Appuyez sur [x] pour commencer\n")
while presse.lower() != 'x':
    presse = input(f"{YELLOW}Appuyez sur [x] pour commencer\n")

questions_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

while questions_list:
    randomquestion = random.choice(questions_list)

    if randomquestion == 1:
        print(f"{BLUE}La capitale de Chypre est ?")
        print(f"[a] {RESET}Nicosie")
        print(f"{BLUE}[b] {RESET}La Valette")
        print(f"{BLUE}[c] {RESET}Dublin")
        if input().lower() == "a":
            print(f"{GREEN}Réponse correcte")
            print(f"{YELLOW}La capital de Chypre est bien Nicosie")
            goodansw += 1
        else:
            print(f"{RED}Réponse erronée")
            print(f"{YELLOW}La capital de Chypre est Nicosie")
        questions_list.remove(randomquestion)

    elif randomquestion == 2:
        print(f"{BLUE}Quel type de fleur n'est pas rose ?")
        print(f"[a] {RESET}Pivoine")
        print(f"{BLUE}[b] {RESET}Cœur de Marie")
        print(f"{BLUE}[c] {RESET}Jasmin")
        if input().lower() == "c":  
            print(f"{GREEN}Réponse correcte")
            print(f"{YELLOW}La bonne réponse est bien le jasmin(fleur de couleur blanc)")
            goodansw += 1
        else:
            print(f"{RED}Réponse erronée")
            print(f"{YELLOW}La bonne réponse est le jasmin(fleur de couleur blanc)")
        questions_list.remove(randomquestion)

    elif randomquestion == 3:
        print(f"{BLUE}Lequel de ces tableaux n'a pas été réalisé pas Van Gogh ?")
        print(f"[a] {RESET}Le Café de nuit")
        print(f"{BLUE}[b] {RESET}Le Jardin des délices")
        print(f"{BLUE}[c] {RESET}La Nuit étoilée")
        if input().lower() == "b":
            print(f"{GREEN}Réponse correcte")
            print(f"{YELLOW}La bonne réponse est bien le Jardin des délices de Hieronimus Bosh ")
            goodansw += 1
        else:
            print(f"{RED}Réponse erronée")
            print(f"{YELLOW}La bonne réponse est le Jardin des délices de Hieronimus Bosh ")
        questions_list.remove(randomquestion)

    elif randomquestion == 4:
        print(f"{BLUE}Quel mots est mal orthographié ?")
        print(f"[a] {RESET}Subtilité")
        print(f"{BLUE}[b] {RESET}Inéluctable")
        print(f"{BLUE}[c] {RESET}Consciense")
        if input().lower() == "c":
            print(f"{GREEN}Réponse correcte")
            print(f"{YELLOW}Consciense est effectivement mal orthographié vrai orthographie: Conscience")
            goodansw += 1
        else:
            print(f"{RED}Réponse erronée")
            print(f"{YELLOW}Consciense est mal orthographié vrai orthographie: Conscience")
        questions_list.remove(randomquestion)

    elif randomquestion == 5:
        print(f"{BLUE}Sin(270)= ?")
        print(f"[a] {RESET}-1")
        print(f"{BLUE}[b] {RESET}1")
        print(f"{BLUE}[c] {RESET}0")
        if input().lower() == "a":
            print(f"{GREEN}Réponse correcte")
            print(f"{YELLOW}Sin(270) = -1")
            goodansw += 1
        else:
            print(f"{RED}Réponse erronée")
            print(f"{YELLOW}Sin(270) = -1")
        questions_list.remove(randomquestion)

    elif randomquestion == 6:
        print(f"{BLUE}Qui a inventé le concept de la gravité universelle ?")
        print(f"[a] {RESET}Johannes Kepler")
        print(f"{BLUE}[b] {RESET}Isaac Newton")
        print(f"{BLUE}[c] {RESET}Albert Einstein{RESET}")
    
        if input().lower() == "b":
            print(f"{GREEN}Réponse correcte")
            print(f"{YELLOW}La bonne réponse est bien Isaac Newton")
            goodansw += 1
        else:
            print(f"{RED}Réponse erronée")
            print(f"{YELLOW}La bonne réponse est Isaac Newton")
        questions_list.remove(randomquestion) 

    if randomquestion == 7:
        print(f"{BLUE}En quelle année a eu lieu le premier atterrissage sur la Lune ?")
        print(f"[a]{RESET} 1959")
        print(f"{BLUE}[b]{RESET} 1969")
        print(f"{BLUE}[c]{RESET} 1979")
    
        if input().lower() == "b":
            print(f"{GREEN}Réponse correcte")
            print(f"{YELLOW}La bonne réponse est bien 1969, réalisée par la mission Apollo 11")
            goodansw += 1
        else:
            print(f"{RED}Réponse erronée")
            print(f"{YELLOW}La bonne réponse est 1969, réalisée par la mission Apollo 11")
        questions_list.remove(randomquestion)        

    if randomquestion == 8:
        print(f"{BLUE}Qui a écrit 'Les Misérables' ?")
        print(f"[a]{RESET} Émile Zola")
        print(f"{BLUE}[b]{RESET} Victor Hugo")
        print(f"{BLUE}[c]{RESET} Gustave Flaubert")
    
        if input().lower() == "b":
            print(f"{GREEN}Réponse correcte")
            print(f"{YELLOW}La bonne réponse est bien Victor Hugo")
            goodansw += 1
        else:
            print(f"{RED}Réponse erronée")
            print(f"{YELLOW}La bonne réponse est Victor Hugo")
        questions_list.remove(randomquestion)    

    if randomquestion == 9:
        print(f"{BLUE}Quel est le plus grand océan du monde ?")
        print(f"[a]{RESET} Océan Atlantique")
        print(f"{BLUE}[b]{RESET} Océan Pacifique")
        print(f"{BLUE}[c]{RESET} Océan Indien")
    
        if input().lower() == "b":
            print(f"{GREEN}Réponse correcte")
            print(f"{YELLOW}La bonne réponse est bien Océan Pacifique")
            goodansw += 1
        else:
            print(f"{RED}Réponse erronée")
            print(f"{YELLOW}La bonne réponse est Océan Pacifique")
        questions_list.remove(randomquestion)

    if randomquestion == 10:
        print(f"{BLUE}Quel est le plus grand désert du monde ?")
        print(f"[a]{RESET} Le Sahara")
        print(f"{BLUE}[b]{RESET} Le désert de Gobi")
        print(f"{BLUE}[c]{RESET} L'Antarctique")
    
        if input().lower() == "c":
            print(f"{GREEN}Réponse correcte")
            print(f"{YELLOW}La bonne réponse est bien l'Antarctique")
            goodansw += 1
        else:
            print(f"{RED}Réponse erronée")
            print(f"{YELLOW}La bonne réponse est l'Antarctique")    
        questions_list.remove(randomquestion)

    if randomquestion == 11:
        print(f"{BLUE}Qui a remporté l'Euro 2008 de football ?")
        print(f"[a]{RESET} Espagne")
        print(f"{BLUE}[b]{RESET} Allemagne")
        print(f"{BLUE}[c]{RESET} Italie")
    
        if input().lower() == "a":
            print(f"{GREEN}Réponse correcte")
            print(f"{YELLOW}La bonne réponse est bien l'Espagne")
            goodansw += 1
        else:
            print(f"{RED}Réponse erronée")
            print(f"{YELLOW}La bonne réponse est l'Espagne")
        questions_list.remove(randomquestion)    

    if randomquestion == 12:
        print(f"{BLUE}Quel empire a été dirigé par le Sultan Mehmed II, qui a conquis Constantinople en 1453 ?")
        print(f"[a]{RESET} Empire ottoman")
        print(f"{BLUE}[b]{RESET} Empire byzantin")
        print(f"{BLUE}[c]{RESET} Empire mongol")
    
        if input().lower() == "a":
            print(f"{GREEN}Réponse correcte")
            print(f"{YELLOW}La bonne réponse est bien l'Empire ottoman")
            goodansw += 1
        else:
            print(f"{RED}Réponse erronée")
            print(f"{YELLOW}La bonne réponse est l'Empire ottoman")
        questions_list.remove(randomquestion)    

    if randomquestion == 13:
        print(f"{BLUE}Qui a inventé le téléphone ?")
        print(f"[a]{RESET} Alexander Graham Bell")
        print(f"{BLUE}[b]{RESET} Thomas Edison")
        print(f"{BLUE}[c]{RESET} Nikola Tesla")
    
        if input().lower() == "a":
            print(f"{GREEN}Réponse correcte")
            print(f"{YELLOW}La bonne réponse est bien Alexander Graham Bell")
            goodansw += 1
        else:
            print(f"{RED}Réponse erronée")
            print(f"{YELLOW}La bonne réponse est Alexander Graham Bell")
        questions_list.remove(randomquestion)    

    if randomquestion == 14:
        print(f"{BLUE}Quel la VRAI équipe de milan ?")
        print(f"[a]{RESET} Inter Milano")
        print(f"{BLUE}[b]{RESET} Milan")
    
        if input().lower() == "a":
            print(f"{GREEN}Réponse correcte")
            print(f"{YELLOW}La bonne réponse est evidemment l'Inter Milano")
            goodansw += 1
        else:
            print(f"{RED}Réponse erronée")
            print(f"{YELLOW}Casse toidu quiz")
        questions_list.remove(randomquestion)

    if randomquestion == 15:
        print(f"{BLUE}Quel est le seul circuit à avoir été utilisé pour toutes les éditions du Championnat du Monde de Formule 1 depuis sa création ?")
        print(f"[a]{RESET} Circuit de Monaco")
        print(f"{BLUE}[b]{RESET} Circuit de Silverstone")
        print(f"{BLUE}[c]{RESET} Circuit de Monza")
    
        if input().lower() == "b":
            print(f"{GREEN}Réponse correcte")
            print(f"{YELLOW}La bonne réponse est bien Circuit de Silverstone")
            goodansw += 1
        else:
            print(f"{RED}Réponse erronée")
            print(f"{YELLOW}La bonne réponse est le Circuit de Silverstone")
        questions_list.remove(randomquestion)

    if randomquestion == 16:
        print(f"{BLUE}Qui a été le premier président des États-Unis ?")
        print(f"[a]{RESET} Abraham Lincoln")
        print(f"{BLUE}[b]{RESET} John Adams")
        print(f"{BLUE}[c]{RESET} George Washington")
        print(f"{BLUE}[d]{RESET} Franklin D. Roosevelt")
        print(f"{BLUE}[e]{RESET} Theodore Roosevelt")
    
        if input().lower() == "c":
            print(f"{GREEN}Réponse correcte")
            print(f"{YELLOW}La bonne réponse est bien George Washington élue en 1789")
            goodansw += 1
        else:
            print(f"{RED}Réponse erronée")
            print(f"{YELLOW}La bonne réponse est George Washington élue en 1789")
        questions_list.remove(randomquestion)

    if randomquestion == 17:
        print(f"{BLUE}Trouve l'intrus parmi ces éléments :")
        print(f"[a]{RESET} Tigre")
        print(f"{BLUE}[b]{RESET} Lion")
        print(f"{BLUE}[c]{RESET} Leopard")
        print(f"{BLUE}[d]{RESET} Cheetah")
        print(f"{BLUE}[e]{RESET} Panda")
    
        if input().lower() == "e":
            print(f"{GREEN}Réponse correcte")
            print(f"{YELLOW}La bonne réponse est bien Panda car il est herbivore")
            goodansw += 1
        else:
            print(f"{RED}Réponse erronée")
            print(f"{YELLOW}La bonne réponse est Panda car il est herbivore")
        questions_list.remove(randomquestion)

    if randomquestion == 18:
        print(f"{BLUE}Quel est le synonyme de 'astonished' en anglais ?")
        print(f"[a]{RESET} Surprised")
        print(f"{BLUE}[b]{RESET} Angry")
        print(f"{BLUE}[c]{RESET} Tired")
    
        if input().lower() == "a":
            print(f"{GREEN}Réponse correcte")
            print(f"{YELLOW}La bonne réponse est bien surprised(surpris)")
            goodansw += 1
        else:
            print(f"{RED}Réponse erronée")
            print(f"{YELLOW}La bonne réponse est Surprised(surpris)")
        questions_list.remove(randomquestion)

    if randomquestion == 19:
        print(f"{BLUE}Quel pays a comme capital New Delhi ?")
        if input() == "Inde" or "inde" or "INDE":
            print(f"{GREEN}Réponse correcte")
            print(f"{YELLOW}La bonne réponse est bien l'Inde")
            goodansw += 1
        else:
            print(f"{RED}Réponse erronée")
            print(f"{YELLOW}La bonne réponse est l'Inde")
        questions_list.remove(randomquestion)

    if randomquestion == 20:
        print(f"{BLUE}Quel est la formule chimique du phosphate ?")
        if input() == "PO4":
            print(f"{GREEN}Réponse correcte")
            print(f"{YELLOW}La formule chimique tu méthane est PO4")
            goodansw += 1
        else:
            print(f"{RED}Réponse erronée")
            print(f"{YELLOW}La formule chimique tu méthane est PO4")
        questions_list.remove(randomquestion)


    time.sleep(3)

print(f"{GREEN}FINISH")
print(f"{BLUE}Score: {RED}{goodansw}{BLUE}/20")
if goodansw <= 9:
    print(f"{RED}bien essayé")
elif 10 <= goodansw <= 15:
    print(f"{YELLOW}Bien joué")
elif 15 <= goodansw <= 19:
    print(f"{RESET}excellent")
elif goodansw == 20:
    print(f"{GREEN}Parfait")