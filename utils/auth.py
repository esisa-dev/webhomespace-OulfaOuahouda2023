import spwd
import crypt

def authenticate(username, password):
    try:
        shadow_entry = spwd.getspnam(username)
    except KeyError:
        # L'utilisateur n'existe pas
        return False

    hashed_password = shadow_entry.sp_pwd
    salt = hashed_password.split('$')[2]

    encrypted_password = crypt.crypt(password, f"$6${salt}")

    if encrypted_password == hashed_password:
        return True
    else:
        return False
