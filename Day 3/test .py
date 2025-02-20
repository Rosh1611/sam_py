def fibonnaci_sequence(term_pos):
    if(term_pos<3):
        return term_pos  
    x1=1
    x2=2
    while(term_pos>2):
        x3=x1+x2
        x1=x2
        x2=x3
        term_pos-=1
    return x3

def prime_series(term_pos):
    def check_prime(number):
        for fact in range(2,number):
            if(number%fact==0):
                return False
        return True
    prev_prime=2
    while True:
        if term_pos==1:
            return prev_prime
        number=prev_prime+1
        if check_prime(number)==True:
            term_pos-=1
        
        number+=1
print("The Series : 1 2 2 3 3 5 5 7 8 11 13 13...")
term_position=int(input("Enter The Position Of The Term You Wish To Find Out : "))
if(term_position%2==0):
    term=prime_series(term_position//2)
else:
    term=fibonnaci_sequence((term_position//2)+1)
print(f"The Term At Position {term_position} Is {term}")
#1 2 2 3 3 5 5 7 8 11 13 13 21 17 34 19 55 23 89 29
#2 3 5 7 11 13 17 19 23 29
