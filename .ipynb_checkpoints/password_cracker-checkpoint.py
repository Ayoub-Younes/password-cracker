import hashlib

salts = open("known-salts.txt").read().split()
passwords = open("top-10000-passwords.txt").read().split()
def crack_sha1_hash(hash, use_salts = False):

    password = ''
    
    if use_salts:
        for ps in passwords:
            for x in salts:
                pass_salt = x+ps
                if hashlib.sha1(pass_salt.encode()).hexdigest() == hash:
                    password =  ps
            for x in salts:
                pass_salt = ps+x
                if hashlib.sha1(pass_salt.encode()).hexdigest() == hash:
                    password =  ps
    else:
        for ps in passwords:
            if hashlib.sha1(ps.encode()).hexdigest() == hash:
                password =  ps

    if password:
        return password
    else:
        return "PASSWORD NOT IN DATABASE" 

hash = '03810a46a2c1a0eae58d9332f01c32bdcec9a01a'
print(crack_sha1_hash(hash, use_salts = True))

def hash_password(password):
    # Hash the new password using SHA-1
    hashed_password = hashlib.sha1(password.encode()).hexdigest()
    
  # Check if the password already exists in the top-10000-passwords.txt file
    with open("top-10000-passwords.txt", "r") as f:
        existing_passwords = f.read().splitlines()
    
    if password in existing_passwords:
        # If the password already exists, inform the user
        print(f"The password '{password}' already exists in the database.")
        print(f"Hashed password: {hashed_password}")
    else:
        # Append the new password to the top-10000-passwords.txt file
        with open("top-10000-passwords.txt", "a") as f:
            f.write(password + "\n")
        
        # Inform the user of the new hashed password
        print(f"Your password '{password}' has been hashed: {hashed_password}")


hash_password('Younes')