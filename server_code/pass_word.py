import anvil.secrets
import anvil.server

#Test du Mot de passe par test du pw enregistré en secret
@anvil.server.callable
def pw(pw):
    if pw == anvil.secrets.get_secret("pass_word"):
        result = True
    else:
        result = False
    return result
