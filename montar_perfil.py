def montar_perfil(**dados):
    print(type(dados))
    return dados

p = montar_perfil(nome="Ana", curso="ADS")
print(p["nome"])
