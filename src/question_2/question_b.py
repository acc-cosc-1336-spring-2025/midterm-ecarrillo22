#write functions here, don't add input('') statements here!

global_value = 100

def use_global():
    global global_value
    global_value = 150
    return global_value
