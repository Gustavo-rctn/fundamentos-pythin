# Operador or

def posso_comprar():
    TEM_CARTAO = False
    tem_dinheiro = bool(input("Vcoê tem dinheiro para comprar?"))
    autorizado = tem_dinheiro or TEM_CARTAO
    print(f"Vou comprar um MC-Donalds hoje? {autorizado}")
    
posso_comprar()