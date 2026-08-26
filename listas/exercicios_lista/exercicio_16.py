def criar_ranking(pontuacoes):
    return sorted(pontuacoes, reverse=True)

pontos = [150, 420, 300, 80, 500]
print(f"\nEx 16 - Ranking (maior p/ menor): {criar_ranking(pontos)}")