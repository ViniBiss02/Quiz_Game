from idlelib.configdialog import changes
coins = 5
print("\nBem -vindo ao meu programa de perguntas e respostas!\n")

while True:
    playind = input("Você quer jogar? (sim/não): ").strip().lower()
    if playind in ("sim", "s"):
        break
    if playind in ("não", "nao", "n"):
        print("Tudo bem. Até a próxima!")
        raise SystemExit
    print("Eu não entendi sua resposta. Por favor responda com 'sim' ou 'não'.")

name = input("Qual é o seu nome? ").strip()
print(f"Ótimo, {name}! Vamos começar o jogo.\n")

while True:
    answer = input("Qual é a capital da França?\n\n").strip().lower()
    print(f"chances = {coins}")
    if answer.lower() == "paris":
        print("Correto! Paris é a capital da França.\n")
        break
    elif answer.lower() != "paris" and coins > 1:
        coins -= 1
        print(f"Incorreto. Tente novamente. Você tem {coins} tentativas restantes.")
    else:
        print(f"Numero de chances = {coins}. A resposta correta é Paris.")
        raise SystemExit

while True:
    answer_1 = input("Qual é 5 + 7?\n\n").strip()
    print(f"chances = {coins}")
    if answer_1 == "12":
        print("Correto! 5 + 7 é 12.\n")
        break
    elif answer_1 != "13":
        print("Incorreto. Tente novamente.")
        coins -= 1
    else:
        print("Incorreto. A resposta correta é 12.")
        raise SystemExit

while True:
    answer_2 = input("complete a frase:\nHoje mais cedo, eu escutei mamonas _______ e fiquei feliz\n\n"
                     "(1) mortas\n"
                     "(2) assassinas\n"
                     "(3) alegres\n"
                     "(4) do rei\n").strip().lower()
    print(f"chances = {coins}")
    match answer_2:
        case "1" | "mortas":
            print("Incorreto. A resposta correta é 'assassinas'.")
            coins -= 1
            raise SystemExit
        case "2" | "assassinas":
            print("Correto! A frase completa é: Hoje mais cedo, eu escutei mamonas assassinas e fiquei feliz.\n")
            break
        case "3" | "alegres":
            print("Incorreto. A resposta correta é 'assassinas'.")
            coins -= 1
            raise SystemExit
        case "4" | "do rei":
            print("Incorreto. A resposta correta é 'assassinas'.")
            coins -= 1
            raise SystemExit
        case _:
            print("Resposta inválida. Por favor, escolha uma das opções fornecidas.")

while True:
    answer_3 = input("Qual é o maior planeta do nosso sistema solar?\n\n").strip().lower()
    print(f"chances = {coins}")
    if answer_3.lower() in ("júpiter", "jupiter"):
        print("Correto! Júpiter é o maior planeta do nosso sistema solar.\n")
        break
    else:
        print("Incorreto. A resposta correta é Júpiter.")
        raise SystemExit

print(f"Parabéns, {name}! Você respondeu todas as perguntas corretamente e venceu o jogo!\n\n")
playagain = input("Você quer jogar novamente? (sim/não): ").strip().lower()
if playagain in ("sim", "s"):
    print("\nReiniciando o jogo...\n")
    import main  # Reinicia o jogo importando o próprio arquivo
else:
    print("Obrigado por jogar! Até a próxima!")


# 19:06