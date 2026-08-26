def analisar_temperaturas(temperaturas):
    qtd = len(temperaturas)
    soma = sum(temperaturas)
    media = soma / qtd
    ordenadas = sorted(temperaturas)
    return qtd, soma, media, ordenadas

temps = [25.5, 30.0, 18.2, 22.4]
qtd, soma, med, ord_t = analisar_temperaturas(temps)
print(f"\nEx 18 - Análise de Temperaturas:")
print(f"Quantidade: {qtd} | Soma: {soma} | Média: {med:.1f}°C | Ordenadas: {ord_t}")