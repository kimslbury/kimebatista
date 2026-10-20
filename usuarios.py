def validar_email(email):
    if email.count("@") != 1:
        return False
    usuario, dominio = email.split("@")
    return bool(usuario) and "." in dominio
