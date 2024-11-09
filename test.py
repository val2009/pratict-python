import random
print("Quiz de culture G")
presse = input("Presser [x] pour commencer\n")
questions_list = [1,2]
if presse == "x" or presse== "X" :
    for question in questions_list:
       randomquestion = random.choice(questions_list) 
       if randomquestion == 1:
            print("1ère Question")
            print("La capital de Chypre est:")
            print("[a] Nicosie")
            print("[b] La Valette")
            print("[c] Dublin")
            if input() == "a":
                print("Ta reponse est correcte")
            else:
                print("Ta reponse n'est pas correct")
            questions_list.remove(randomquestion)
       if randomquestion == 2: 
            print("1ère Question")
            print("La capital de l italie est:")
            print("[a] Nicosie")
            print("[b] La Valette")
            print("[c] Dublin") 
            if input() == "a":
                print("Ta reponse est correcte")

            else:
                print("Ta reponse n'est pas correct")        
            questions_list.remove(randomquestion)
