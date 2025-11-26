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

answer = input("Qual é a capital da França? ").strip().lower()
if answer == "paris":
    print("Correto! Paris é a capital da França.")
else:
    print("Incorreto. A resposta correta é Paris.")

