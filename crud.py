import dados
import utils

def cadastrar_cliente():
    print("\n--- CADASTRO DE CLIENTES ---")
    nome_cli = input("Nome do cliente: ").strip()
    if nome_cli == "":
        print("Nao pode deixar o nome vazio")
        return

    cpf_cli = input("CPF (so numeros): ").strip()
    if utils.valida_cpf(cpf_cli) == False:
        return

    id_novo = utils.gera_id_cliente(nome_cli, cpf_cli)
    
    dic_cliente = {
        "id": id_novo,
        "nome": nome_cli,
        "cpf": cpf_cli
    }
    
    dados.clientes.append(dic_cliente)
    dados.cpfs_existentes.add(cpf_cli)
    print("Cliente salvo e ID gerado foi:", id_novo)

def listar_clientes():
    print("\n=== TODOS OS CLIENTES ===")
    gerador_cli = utils.pegador(dados.clientes)
    existe = False
    for c in gerador_cli:
        existe = True
        print("ID: " + c['id'] + " | Nome: " + c['nome'] + " | CPF: " + c['cpf'])
    if existe == False:
        print("Nao encontrado")

def registrar_abastecimento():
    print("\n--- NOVO ABASTECIMENTO ---")
    if len(dados.clientes) == 0:
        print("Erro: Cadastre um cliente antes")
        return

    busca_id = input("Digite o ID do cliente: ").strip().upper()
    
    filtro = [item for item in dados.clientes if item["id"] == busca_id]
    
    if len(filtro) == 0:
        print("Cliente nao encontrado")
        return

    print("\nCombustiveis:")
    cont = 0
    for cb in dados.combustiveis:
        print(str(cont) + " - " + cb[0] + " (R$ " + str(cb[1]) + ")")
        cont = cont + 1
        
    opcao = utils.ler_numero_inteiro("Escolha o numero: ")
    if opcao < 0 or opcao >= len(dados.combustiveis):
        print("Opcao invalida")
        return

    comb_escolhido = dados.combustiveis[opcao]
    nome_comb = comb_escolhido[0]
    preco_comb = comb_escolhido[1]
    
    litros_comb = utils.ler_numero_quebrado("Quantidade de litros: ")
    if litros_comb < 2.0:
        print("Obrigatorio abastecer mais de 2 litros")
        return

    total_pagar = litros_comb * preco_comb
    id_venda = len(dados.vendas) + 1
    
    dic_venda = {
        "id": id_venda,
        "id_cliente": busca_id,
        "combustivel": nome_comb,
        "litros": litros_comb,
        "total": total_pagar
    }
    
    dados.vendas.append(dic_venda)
    print("Abastecimento numero " + str(id_venda) + " concluido Total: R$ " + str(round(total_pagar, 2)))

def listar_abastecimentos():
    print("\n=== LISTA DE VENDAS ===")
    if len(dados.vendas) == 0:
        print("Nenhuma venda registrada")
        return
    for v in dados.vendas:
        print("ID da venda: " + str(v['id']) + " | Cliente: " + v['id_cliente'] + " | Tipo: " + v['combustivel'] + " | Litros: " + str(v['litros']) + " | Total: R$ " + str(v['total']))

def atualizar_abastecimento():
    print("\n--- EDITAR VENDA ---")
    id_procurado = utils.ler_numero_inteiro("Qual o ID do abastecimento? ")
    
    alvo = None
    for v in dados.vendas:
        if v["id"] == id_procurado:
            alvo = v
            break
            
    if alvo == None:
        print("esse ID nao existe")
        return

    print("Abastecimento atual tem " + str(alvo['litros']) + " litros de " + alvo['combustivel'])
    novos_litros = utils.ler_numero_quebrado("Digite a nova quantidade de litros: ")
    if novos_litros < 2.0:
        print("Erro: Obrigatorio abastecer mais de 2 litros")
        return

    preco_atual = 0.0
    for c in dados.combustiveis:
        if c[0] == alvo["combustivel"]:
            preco_atual = c[1]
            break

    alvo["litros"] = novos_litros
    alvo["total"] = novos_litros * preco_atual
    print("Novo total: R$ " + str(round(alvo["total"], 2)))

def deletar_abastecimento():
    print("\n--- EXCLUIR ABASTECIMENTO ---")
    id_procurado = utils.ler_numero_inteiro("ID para deletar: ")
    
    achou = None
    for v in dados.vendas:
        if v["id"] == id_procurado:
            achou = v
            break
            
    if achou == None:
        print("nao encontrado")
        return

    certeza = input("Quer mesmo apagar o registro " + str(id_procurado) + "? (s/n): ").strip().lower()
    if certeza == "s":
        dados.vendas.remove(achou)
        print("Exckuido com sucesso")
    else:
        print("Cancelado")

def gerar_relatorio_resumido():
    print("\n=== RELATORIO DE VENDAS ===")
    resumo_comb = {c[0]: {"litros_total": 0.0, "grana_total": 0.0} for c in dados.combustiveis}
    
    for v in dados.vendas:
        nome = v["combustivel"]
        if nome in resumo_comb:
            resumo_comb[nome]["litros_total"] += v["litros"]
            resumo_comb[nome]["grana_total"] += v["total"]

    for k, info in resumo_comb.items():
        print("Tipo: " + k + " | Litros: " + str(info["litros_total"]) + " | Faturado: R$ " + str(info["grana_total"]))
    
    caixa = sum(aux["grana_total"] for aux in resumo_comb.values())
    print("----------------------------------------")
    print("FATURAMENTO DO POSTO EM TERESINA: R$ " + str(round(caixa, 2)))