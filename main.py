import sqlite3
conexao = sqlite3.connect("estoque.db")
cursor = conexao.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS estoque_itens(id INTEGER PRIMARY KEY AUTOINCREMENT, produto TEXT, categoria TEXT, unid_medid TEXT, qtd_atual REAL, qtd_minima REAL)')
conexao.commit()
itens = []
programa = True
while programa:
    print("==================== Controle de estoque iniciado! ====================")
    print("1 - Cadastrar item")
    print("2 - Ver itens")
    print("3 - Sair\n")

    opcao = input("Escolha uma opção: ")
    if opcao == '1':
        continuar = True
        while continuar:
            produto = str(input('Nome do produto: '))
            if not produto.strip():
                print('Digite um nome de produto valido!.')
                continue
            else:
                catego_cont = True
                while catego_cont:
                    categoria = str(input('Categoria: '))
                    catego_cont = False
                    if not categoria.strip():
                        print('Digite uma categoria valida!.')
                        catego_cont = True
                    

            unid_medid = str(input('Defina qual a classe de medida (KG / LT / UN ): '))
            qtd_invalida = True
            while qtd_invalida:
                try:
                    qtd_atual = float(input('Digita sua quantidade atual: '))
                    qtd_invalida = False
                    if qtd_atual < 0:
                        print('\nDigite um valor valido.\n')
                        qtd_invalida = True
                except ValueError:
                    print('\nVocê precisa digitar um numero!!')
            qtd_invalida2 = True
            while qtd_invalida2:
                try:
                    qtd_minima = float(input('Qual a quantidade minima desejada: '))
                    qtd_invalida2 = False
                    if qtd_minima < 0:
                        print('\nDigite um valor valido.\n')
                        qtd_invalida2 = True
                except ValueError:
                    print('\nVocê precisa digitar um numero!!')
            produto_cadastrado = produto, categoria, unid_medid, qtd_atual, qtd_minima
            itens.append(produto_cadastrado)
            cursor.execute("INSERT INTO estoque_itens(produto, categoria, unid_medid, qtd_atual, qtd_minima) VALUES(?, ?, ?, ?, ?)",(produto, categoria, unid_medid, qtd_atual, qtd_minima))
            conexao.commit()
            sair = input('Produto registrado com sucesso, deseja cadastrar outro item? (s/n): ')
            if sair == 's':
                continuar = True
            elif sair == 'n':
                continuar = False
            else:
                print('Resposta invalida, voltando ao menu.')
                continuar = False

    elif opcao == '2':
        cursor.execute("SELECT produto, categoria, unid_medid, qtd_atual, qtd_minima FROM estoque_itens")
        resultados = cursor.fetchall()
        if not resultados:
            print ('Nenhum Produto Encontrado!.')
        else:

            for item in resultados:
                produto, categoria, unid_medid, qtd_atual, qtd_minima = item
                print(f'Produto: {produto}\n')
                print(f'Categoria: {categoria}\n')
                print(f'Medida: {unid_medid}\n')
                print(f'Qtd. Atual: {qtd_atual}\n')
                print(f'Qtd. Minima: {qtd_minima}\n')

    elif opcao == '3':
        print('Obrigado!!\n==========================')
        programa = False
    else:
        print('Resposta invalida, digita uma das 3 opçoes(1, 2, 3)\n\n')

    


    

            
    

