def dia_semana(d: int, m: int, a: int) -> str:
    a0 = a - (14 - m)// 12
    x = a0 + a0 // 4 - a0 // 100 + a0 // 400
    m0 = m + 12 * ((14 - m) // 12) - 2
    d0 = (d + x + (31 * m0) // 12) % 7
    match d0:
        case 0:
            return "Domingo"
        case 1:
            return "Segunda"
        case 2:
            return "Terça"
        case 3:
            return "Quarta"
        case 4:
            return "Quinta"
        case 5:
            return "Sexta"
        case 6:
            return "Sabado"