
# name = input("Write your full name ")
# age = int(input("Write your age "))


# print(name , age)
# print("Hello World")
# for i in range (0,6,1):
#     if i == 0 or i== 6 :
#         print("*")
#     elif i == 1 or i == 5 :
#         print("**")
#     elif i == 2 or i == 3 :
#         print("***")
#     else :
#         print("****")
# for i in range(0, 101,5):
    
#     print(i)
#     if i  == 25 :
#         print("1/4 of the way there")
#     if i  == 50 :
#         print("1/2 of the way there")
#     if i  == 75 :
#         print("3/4 of the way there")
#     if i  == 100 :
#         print("loading complete")
# stars = ""
# for i in range(0, 5, 1):
#     for j in range(0, i, 1):
#         stars += "*"
#         print(stars)

# name = input("What is your name? ")
# r_name = name[::-1]
# print("Your name reversed is : " + r_name)
# import random
# num = random.randint(0,99)
# # print(num)
# import  random
# high_score = 0
# def dicegame():
#     global high_score
#     while True:
#           print("\n\n++++++++++++++++++++++++++++++++++++++")
#           print(f"\nCurrent High Score:{high_score}\n")
#           print("1) Roll Dice\n2) Leave Game")
#           option = int(input("Enter your choice : "))
#           if option == 2 :
#            print("Goodbye!")
#            break
       
#           elif  option == 1:
#            a = random.randint(1,6)
#            b = random.randint(1,6)
#            total = a + b
#            print("\nYou roll a...",a)
#            print("You roll a...",b)
#            print(f"\nYou have rolled a total of: {total}")
#            if total > high_score:
#                         high_score=total
#                         print("\nNew high score!")
#           else:
#             print("    ///You have to choose between 1 or 2///    \n")
        
      
# dicegame()


#   Students  |  Grades  |  Letters
# ------------|----------|----------
#   George    |  46      |  F
#   Michell   |  80      |  B
#   Josh      |  12      |  F
#   Chloe     |  68      |  D
#   Stanley   |  99      |  A
#   Annie     |  100     |  A+


# gradeToTest = 0

# if gradeToTest == 100:
#     print("A+")
# elif gradeToTest >= 90:
#     print("A")
# elif gradeToTest >= 80:
#     print("B")
# elif gradeToTest >= 70:
#     print("C")
# elif gradeToTest >= 50:
#     print("D")
# else :
#   print("F")



# x = 0

# while x != 10:
#     x = x + 1
    
#     if x < 5:
#         print(x)
#     elif x == 6:
#       print(x)
#       continue
#     elif x >= 5 and x <= 8:
#         print("x is bigger then or equal to 5, and less then or equal to 8, but not 6. It is:", x)
#     else:
#         print("x is bigger than 8. It is:", x)




# priceIsRight = 15

# if priceIsRight <5:
#     print("Price is too low!")
# elif priceIsRight >=5 and priceIsRight <=9:
#         print("Price is almost there!")
# elif priceIsRight == 10:
#             print("Price is exactly that!")
# else :
#             print("Price is too high!")



# Turn this line into a comment

cities = ["Seattle", "Tacoma", "Bellevue"]

a = int(1)
print(type(a))

b = float(10)
print(type(b))

c = str("Python")
print(type(c))

d = a+b
print(d)







