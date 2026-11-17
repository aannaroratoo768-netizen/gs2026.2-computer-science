def testar_tabela_verdade():
    print("\n--- VALIDAÇÃO AUTOMATIZADA DA TABELA-VERDADE ---")
    erros = 0
    # Gabarito esperado para S = (A or C) and B and D
    gabarito = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1]
    
    i = 0
    for a in [0, 1]:
        for b in [0, 1]:
            for c in [0, 1]:
                for d in [0, 1]:
                    resultado = int((a or c) and b and d)
                    esperado = gabarito[i]
                    status = "OK" if resultado == ESPERADO else "FALHA"
                    if status == "FALHA":
                        erros += 1
                    print(f"Combinação {i:2d} (A={a}, B={b}, C={c}, D={d}) -> Esperado: {esperado} | Obtido: {resultado} [{status}]")
                    i += 1
    print(f"Validação concluída com {erros} erros encontrados.\n")

if __name__ == "__main__":
    testar_tabela_verdade()
