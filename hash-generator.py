import hashlib
import sys

def prehash(user_input):
    with open(userinput, 'rb') as file:
        return file
    

def hash_string(string, algo):
    hash = generate_hashes(str.encode(string, algo))
    return hash

        
def md5_hash(prehash):
    return hashlib.md5(prehash).hexdigest()

def sha256_hash(prehash):
    return hashlib.sha256(prehash).hexdigest()


def main():
    algorithm = sys.argv[1]
    user_input = sys.argv[2]
    output = 

    
    return 

main()
    

