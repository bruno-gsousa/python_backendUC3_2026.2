def calcular_dano(ataque, defesa):
    dano = ataque - defesa
    if dano <= 0:
        dano = 0
    return dano


def atacar(atacante, defensor):
    dano = calcular_dano(atacante["ataque"], defensor["defesa"])
    defensor["vida"] -= dano

    if defensor["vida"] <= 0:
        defensor["vida"] = 0

    print(
        f'{atacante["nome"]} atacou '
        f'{defensor["nome"]} causando {dano} de dano'
    )
    print(
        f'vida de {defensor["nome"]}: '
        f'{defensor["vida"]}'
    )


def jogar_batalha():
    jogador = {
        "nome": "Thor",
        "vida": 100,
        "ataque": 25,
        "defesa": 10
    }

    inimigo = {
        "nome": "Slime",
        "vida": 80,
        "ataque": 25,
        "defesa": 10
    }

    print("====Batalha====")
    while jogador["vida"] > 0 and inimigo["vida"] > 0:
        print("\n ---Turno do Jogador--")
        atacar(jogador, inimigo)
        if inimigo["vida"] <= 0:
            print("\n 🏆 você venceu!!")
            break

        print("\n ---Turno do Inimigo--")
        atacar(inimigo, jogador)
        if jogador["vida"] <= 0:
            print("\n 🦠 você perdeu!!")
            break


while True:
    jogar_batalha()
    resposta = input("\nDeseja jogar novamente? (s/n): ").strip().lower()

    if resposta != "s":
        print("Obrigado por jogar!")
        break