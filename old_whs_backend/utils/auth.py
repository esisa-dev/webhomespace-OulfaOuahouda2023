import pam

def authenticate(username, password):
    # Créez une instance de la classe PAM
    p = pam.pam()

    # Vérifiez que les valeurs de username et password ne sont pas None
    if username is None or password is None:
        return False

    return p.authenticate(username, password)
