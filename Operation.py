#Author : Trent Minto'o


print('Entrer des valeurs ')
valeur1 = input('Entrez un entier : ') #Permet d'entrer un entier 
if valeur1.isdigit() : #Verifie qu'on a rentré un entier 
   reponse1 = int(valeur1)      #Transforme le input en un entier 
   print ('Vous avez rentré la valeur :', reponse1  )
else : 
    print('Votre entree est invalide ')
valeur2= input('Entrez un autre entier :  ') #Permet d'entrer un autre entier 
if valeur2.isdigit() : #Verifie qu'on a rentré un entier 
   reponse2 = int(valeur2)#Transforme le input en un entier 
   print ('Vous avez rentré la valeur :', reponse2  )
else : 
    print('Votre entree est invalide ')
valeur3 = input('Entrez votre nom : ') #Permet d,entrer notre nom 
print ('Vous avez entré le nom ', valeur3 ) 
#Teste une addition de nos entiers 
if  type(reponse1) == int and type(reponse2)== int :
    print(valeur3 ,' voici une addition de vos valeurs  : ' , reponse1, '+' , reponse2 , '= ', (reponse1 + reponse2) )
