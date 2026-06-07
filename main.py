import utils
import crud

def mostra_menu():
    print("\n--------------------------------")
    print("     POSTO CERRADO NORDESTE     ")
    print("--------------------------------")
    print("1) Cadastrar Cliente")
    print("2) Listar Clientes")
    print("3) Abastecer Veiculo")
    print("4) Ver Historico de Vendas")
    print("5) Alterar Abastecimento")
    print("6) Deletar Registro")
    print("7) Relatorio Financeiro")
    print("0) Fechar Sistema")
    print("--------------------------------")

def main():
    status = "rodando"
    while status == "rodando":
        mostra_menu()
        opcao_menu = utils.ler_numero_inteiro("Escolha o numero da opcao: ")

        if opcao_menu == 1:
            crud.cadastrar_cliente()
        elif opcao_menu == 2:
            crud.listar_clientes()
        elif opcao_menu == 3:
            crud.registrar_abastecimento()
        elif opcao_menu == 4:
            crud.listar_abastecimentos()
        elif opcao_menu == 5:
            crud.atualizar_abastecimento()
        elif opcao_menu == 6:
            crud.deletar_abastecimento()
        elif opcao_menu == 7:
            crud.gerar_relatorio_resumido()
        elif opcao_menu == 0:
            print("\nEncerrando o programa...")
            status = "parado"
        else:
            print("Essa opcao nao existe no menu.")

if __name__ == "__main__":
    main()