import os
import random
import string

def generate_random_text(size):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=size))

def create_file(filename, size):
    print("Generated Random Text File")
    with open(filename, 'w') as f:
        f.write(generate_random_text(size))
    return


create_file('random_data.txt', 1024)



