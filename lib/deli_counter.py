
katz_deli = []

def line(katz_deli):
    number = 1
    in_line = []
    if katz_deli == []:
        print('The line is currently empty.')
    else: 
        for people in katz_deli:
            print(f'The line is currently: {number}. {people}')
            number += 1
    

def take_a_number(katz_deli, name):
    katz_deli.append(name)
    print(f'Welcome, {name}. You are number {len(katz_deli)} in line.')
def now_serving(katz_deli):
    if katz_deli == []:
        print('There is nobody waiting to be served.')
    else:
        print(f'Currently servering {katz_deli[0]}')
        katz_deli.pop(0)
    

# lines off with 0 and should say the line is currently empty

now_serving(katz_deli)
take_a_number(katz_deli, 'kevin')
take_a_number(katz_deli, 'david')
now_serving(katz_deli)
now_serving(katz_deli)
take_a_number(katz_deli, 'tashi')
take_a_number(katz_deli, 'adam')
line(katz_deli)