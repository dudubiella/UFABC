mensagem = input("").split(" / ")
sos = "... --- ..."
ajuda = "com" if sos in mensagem else "sem"
print(f"Mensagem {ajuda} pedido de ajuda!")