##syntax
def function_name(parameter):
  """Docstring"""
  #function body 
  return expression


##why functions 
def even_or_odd(num): 
  """This function finds even or odd"""
  if num%2==0:
    print("the number is even")
  else:
    print("the number is odd)

##calling a function
even_or_odd(24)

## function with multiple parameter
def add(a,b):
  return a+b
result = add(2,4)
print(result)


##Default parametrs:

def great(name):
  print(f"Hello {name} Welcome to the paradise")

greet("krish")

### Variable length Arguments
## Positional and Keyword arguments

def print_numbers(*krish):
  for number in krish:
    print(number)

### Positional
print_numbers(1,2,3,4,5,6,7,8,"krish")

def print_numbers(*args):
  for number in args:
    print(number)


### keyword arguments

def print_details(**kwargs):
  for key, value in kwargs.items();
    print()




###Positional and Keyword arguments together

def print_numbers(*args, **kwargs):
    
  for val in args:
      print(f"Positional argument:{val}")
      
  for key,value in kwargs.items():
    print(f"{key}:{value}")
    
print_numbers(1,2,3,4,"krish", name = "rishi", age = 23, country = "India")
    





















  
