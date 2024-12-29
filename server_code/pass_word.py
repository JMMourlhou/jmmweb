import anvil.secrets
import anvil.server

#Test du Mot de passe par test du pw enregistré en secret
@anvil.server.callable
def pw(pw):
        result = True
    else:
        result = False
    return result
