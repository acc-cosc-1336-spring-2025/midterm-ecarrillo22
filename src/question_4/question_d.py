#write functions here, don't add input('') statements here!
def is_prime(num):
        
    for i in range(2, num):
        if num % i == 0:
            return False
        else:
            return True