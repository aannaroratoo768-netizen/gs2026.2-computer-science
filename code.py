def citizen_assist_simulator():
    print("==================================================")
    print("   CITIZEN ASSIST AI - MÓDULO DE DECISÃO LÓGICA   ")
    print("==================================================")
    print("Aviso: Protótipo acadêmico (Global Solution).")
    print("Informe 1 para SIM e 0 para NÃO nas questões abaixo:\n")

    def ler_entrada(mensagem):
        while True:
            try:
                val = int(input(mensagem))
                if val in (0, 1):
                    return val
                print("⚠️ Entrada inválida! Digite apenas 0 ou 1.")
            except ValueError:
                print("⚠️ Entrada inválida! Digite apenas números inteiros (0 ou 1).")

    # Coleta de variáveis booleanas sem armazenar dados pessoais
    A = ler_entrada("1. Possui cadastro ativo no portal gov.br? (0/1): ")
    B = ler_entrada("2. A documentação obrigatória está completa? (0/1): ")
    C = ler_entrada("3. Possui direito a atendimento prioritário? (0/1): ")
    D = ler_entrada("4. Há vagas disponíveis para agendamento? (0/1): ")

    # Aplicação da Função Lógica Simplificada: S = (A + C) * B * D
    S = (A | C) & B & D

    print("\n--------------------------------------------------")
    print(f"ESTADO COMPUTADO -> Entradas: A={A}, B={B}, C={C}, D={D}")
    if S == 1:
        print("✅ [STATUS: AUTORIZADO]")
        print("Orientação: Agendamento confirmado com sucesso!")
        if C == 1:
            print("-> Direcionamento: Guichê de Atendimento Prioritário.")
        else:
            print("-> Direcionamento: Guichê de Atendimento Geral.")
    else:
        print("❌ [STATUS: NÃO AUTORIZADO]")
        print("Orientação: O agendamento não pode ser concluído.")
        if B == 0:
            print("-> Motivo provável: Documentação incompleta.")
        elif D == 0:
            print("-> Motivo provável: Sem vagas disponíveis na data.")
        else:
            print("-> Motivo provável: É necessário possuir cadastro no gov.br ou prioridade.")
    print("==================================================")

if __name__ == "__main__":
    citizen_assist_simulator()
