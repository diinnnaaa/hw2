# tpl = ()


# bestf = ( 'Nastya','Tori',)
# bestf2 = ('Ernat', 'Farabi' )
#2
# siblings = bestf + bestf2
# print(siblings)
#3
# print(len(siblings))
#4
# family_members = siblings + ('Nazira','askar')
# print(family_members)
#5

# lvl2
# Nastya, Ernat, *other = family_members
# print(Nastya)
# print(Ernat)
# print(other)
#1


#task 2
fruits=('Apples','Pears')
vegetables=('potato','tomato')
animal_products=('meat','milk')
food_stuff_tp=fruits + vegetables + animal_products
print(food_stuff_tp)

#task 3
food_stuff_tp=('Apples','Pears','potato','tomato','meat','milk')
food_stuff_lst=list(food_stuff_tp)
print(food_stuff_lst)

# task 5

food_stuff_lst=('Apples', 'Pears','potato', 'tomato', 'meat', 'Milk') 
print(food_stuff_lst [2:-2])


# task 6 
food_stuff_tp=('Apples', 'Pears', 'potato', 'tomato', 'meat', 'Milk')

#task 7
nordic_countries = ('Kanada', 'Finland','Iceland', 'Egipt', 'Sweden')
print('Estonia'in nordic_countries)
print('Iceland'in nordic_countries)