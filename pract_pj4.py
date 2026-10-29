import random as R

number_list=  list(range(1,191))

letters_list = [
    'A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 
    'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 
    'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z'
]

symbols_list = [
    '!', '#', '$', '(', ')', '*', '+', ',', '-', '.', '/', ':', 
    ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '{', '|', '}', 
    '~'
]

def func_random_passworld(*,n:list,l:list,s:list) -> str:
    return   f'{R.choice(l)}{R.choice(s)}{R.choice(l)}{R.choice(l)}{R.choice(n)}{R.choice(s)}{R.choice(n)}{R.choice(n)}{R.choice(l)}{R.choice(s)}{R.choice(l)}{R.choice(s)}{R.choice(l)}{R.choice(n)}{R.choice(l)}'
passworld = func_random_passworld(n=number_list,l=letters_list,s=symbols_list)
print(passworld)
