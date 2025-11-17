# tempwerature conversion

def convert_temperature(temp, unit):
  """This function concverts the temperature oin faharnite to celsius"""

  if unit == 'c';
    return temp*9/5 + 32    # celsius to fahrenite

  elif unit == "F":
    return (temp - 32)*5/9  # fahrenite to celsius
  
  else:
    return None    


convert_temperature(25, 'c');
convert_temperature(77, 'f');


#password strength Checker :

def is_strong_passwaord(password):
    if len(password)<8:
      return False

    if not any(char.isdigi() for char in password):
      return False

    if not any(char.islower() for char in password):
      return False

    if not any(char.isupper() for char in password):
      return False

    if not any(char in '@#$%^&*()_+' for char in password):
      return False
    return True




#total cost in a shopping cart;


def calculate_total_cost(cart):
    total_cost=0
    for item in cart:
        total_cost += item['price']*item['quantity']

    return total_cost


cart = [
  {'name':'Apple', 'price': 0.5, 'quantity':4},
  {'name':'banana', 'price':0.3, 'quantity':6},
  {'name': 'Orange','price': 0.7, 'quantity':3}
]


total_cost = calculate_total_cost(cart)  
print(total_cost)





# check if a string is a palindrome or not

def is_palindrome(s):
  s = s.lower().replace(" ","")
  return s == s[:: -1]
  
  
print(is_palindrome("A man a plan a canal Panama"))
print(is_palindrome("hello"))


# Calculate the factorial  of a nuber using recursion 
def factorial(n):
  if n==0:
    return 1

  else:
    return n * factorial(n-1)


print(factorial(6))


# Function to read a file and calculate the frequency of each woord 

def count_word_frequency(file_path):
  word_count = {}
  with open(file_path, 'r') as file:
    for line in file:
        words = line.split()   
        for word in words:
          word = word.lower().strip('.,!?;:"\'')
          word_count[word]=word_count.get(word,0)+1

  return word_count

filepath = 'sample.txt'
word_frequency = count_word_frequency(filepath)
print(word_frequency)

# Validate the email address:

def email_validation(email):
    
  if not any(char.isalpha() for char in email):
    return False

  if not any(char.isdigit() for char in email):
    return False
  
  if not any(char in '!@#$%^&*()_+' for char in email):
    return False

  return True
  
  
print(email_validation("rishijha0910@gmail.com")) 


## email validation through rdegular expression:


def is_valid_email(email):
  pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
  return re,match(patter, email) is not None

print(is_valid_email("test@example.com"))
print(is_valid_email("invalid-email"))











