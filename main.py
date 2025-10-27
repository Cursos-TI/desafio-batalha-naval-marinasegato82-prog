

# Tamanho do tabuleiro (5x5)
TAMANHO = 5
NUM_NAVIOS = 3  # quantidade de navios

def criar_tabuleiro():
    return [["~" for _ in range(TAMANHO)] for _ in range(TAMANHO)]

def posicionar_navios(tabuleiro):
    navios = []
    while len(navios) < NUM_NAVIOS:
        linha = random.randint(0, TAMANHO - 1)
        coluna = random.randint(0, TAMANHO - 1)
        if (linha, coluna) not in navios:
            navios.append((linha, coluna))
    return navios

def mostrar_tabuleiro(tabuleiro):
    print("   0 1 2 3 4")
    print("  -----------")
    for i, linha in enumerate(tabuleiro):
        print(f"{i}| " + " ".join(linha))

def jogar():
    print("=== BATALHA NAVAL ===")
    print("Tente encontrar os navios do computador!\n")

    tabuleiro = criar_tabuleiro()
    navios = posicionar_navios(tabuleiro)

    acertos = 0
    tentativas = 0
    limite = 10

    while tentativas < limite and acertos < NUM_NAVIOS:
        mostrar_tabuleiro(tabuleiro)
        print(f"\nTentativa {tentativas + 1} de {limite}")
        print(f"Acertos: {acertos}/{NUM_NAVIOS}\n")

        entrada = input("Digite linha e coluna (ex: 2 3) ou 'sair': ").strip()
        if entrada.lower() == "sair":
            print("Jogo encerrado.")
            return

        try:
            lin, col = map(int, entrada.split())
        except:
            print("Entrada inválida! Use o formato: 2 3\n")
            continue

        if lin < 0 or lin >= TAMANHO or col < 0 or col >= TAMANHO:
            print("Coordenada fora do tabuleiro!\n")
            continue

        if tabuleiro[lin][col] in ("X", "O"):
            print("Você já atirou aqui!\n")
            continue

        tentativas += 1

        if (lin, col) in navios:
            print("💥 ACERTOU um navio!")
            tabuleiro[lin][col] = "X"
            acertos += 1
        else:
            print("🌊 Água...")
            tabuleiro[lin][col] = "O"

    mostrar_tabuleiro(tabuleiro)
    print("\n=== FIM DE JOGO ===")
    if acertos == NUM_NAVIOS:
        print(f"Parabéns! Você afundou todos os {NUM_NAVIOS} navios! 🚢🔥")
    else:
        print(f"Você acertou {acertos}/{NUM_NAVIOS} navios.")
        print("Posições corretas eram:")
        for (l, c) in navios:
            print(f"- Navio em ({l}, {c})")

if _name_ == "_main_":
    jogar()