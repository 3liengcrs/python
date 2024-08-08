# number_set = {1,2,3,4}
number_set = {1,2,3,4}
words_set = {"Alpha","Bravo","Charlie"}
abc = ""
for word in words_set:
    abc += word
print(abc)
# if "Bravo" in words_set:
#     print("Yes")
# else :
#     print("False")
words_set.add("Delta")

words_set.discard("Alpha")
words_set.discard("Delta")
words_set.discard("Bravo")
words_set.discard("Charlie")
print(type(words_set))
b ={(1, 2), (3, 4), (5, 6)}
print(type(b))
print(words_set)

