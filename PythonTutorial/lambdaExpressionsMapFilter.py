

def addition(a,b):
  return a+b

lambda argument : expression


add = lambda a,b: a+b
type(add)



## even numnber finder 
def even(num):
  if num%2==0:
    return True


even(24)

## even number finder with l
print(sqaure(2))

# after using map 

#map(function, iterables): It s used to apply a function over all the other iterables 
numbers = [1,2,3,4,5]
map(lambda x:x**2, numbers)



### adddition of 2 list of numbers using lampbda and map
number1 = [1,2,3]
number2 = [4,5,6]

added_numbers = list(map(lambda x,y:x+y, number1, number2))
print(added_numbers)  



## map() to conve4t a list of strings to intefgerws 
# use 3map to convert strings tointegers

str_numbers = ['1','2','3','4']

int_numbers = list(map(int, str_numbers))
print(int_numbers)



## map() to conve4t a list of strings to intefgerws 
# use 3map to convert strings tointegers

words = ['apple','banana','cherry']
upper_word = list(map(str.upper,words))
print(upper_word)


##using map on dictionaries to get items form it
def get_name(person):
    return person['name']
    
    
people = [
        {'name':'krish','age':33},
        {'name':'raghav', 'age':32}
]
    
    
print(list(map(get_name,people)))   




# filter() function in python 
def even(num):
  if num%2 == 0;
    return True

even(24)

lst = [1,2,3,4,5,6,7,8,9,10,11,12]

list(filter(even, lst))


# greate than 5  and EVEN 
numbers = [1,2,3,4,5,6,7,8,9]
even_and_greater_than_five = list(filter(lambda x:x>5 and X%2, numbers))

list(filter(age_greater_than_25, people))
