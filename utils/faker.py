from faker import Faker


fake = Faker()

def get_login_faker(num_casos=5):

    lista = [] 
    usuarios_validos = ["standard_user", "performance_glitch_user"]
    
    password_valido = "secret_sauce"

    for _ in range(num_casos):
        
        if fake.boolean(chance_of_getting_true=70):
            username = fake.random.choice(usuarios_validos)
            password = password_valido
            login_booleano = True
        else:
            username = fake.user_name()
            password = fake.password(length=12)
            login_booleano = False

        lista.append((username, password, login_booleano))

    return lista


