conceito_final = input("")
valido = ["A", "B", "C", "D", "F", "O"]
if conceito_final not in valido:
    print("Conceito invalido!")
else:
    match conceito_final:
        case "O":
            print("REPROVADO POR FREQUENCIA")
        case "F":
            print("REPROVADO POR DESEMPENHO")
        case _:
            print("APROVADO")