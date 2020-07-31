import os.path
import matplotlib.pyplot as plt
# import datetime

continuar = True
fimArqDesp, fimArqVenda = False, False

dataDes = []
codCat  = []
descCat = []
valor   = []
dataVen = []
venda   = []
despCat1, despCat2, despCat3, despCat4, despTot, vendaTot = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
numDesp, numVenda = 0, 0

if os.path.isfile("despesas.csv"):
    arqDesp = open("despesas.csv","r")
    
    while fimArqDesp == False:
        linha = arqDesp.readline()
        if linha == "":
            fimArqDesp = True  
            break    
        
        dataDesArq,codCatArq,descCatArq,valorArq = linha.split(";")           
        if int(codCatArq) == 1:
            despCat1 += float(valorArq)
        elif int(codCatArq) == 2:
            despCat2 += float(valorArq)
        elif int(codCatArq) == 3:
            despCat3 += float(valorArq)
        elif int(codCatArq) == 4:
            despCat4 += float(valorArq)
           
        despTot += float(valorArq)
        numDesp += 1  
        dataDes.append(dataDesArq) 
        codCat.append(int(codCatArq)) 
        descCat.append(descCatArq) 
        valor.append(float(valorArq)) 
    arqDesp.close()
    
if os.path.isfile("vendas.csv"): 
    arqVenda = open("vendas.csv","r")
    
    while fimArqVenda == False:
        linha = arqVenda.readline()
        if linha == "":
            fimArqVenda = True  
            break  
               
        dataVenArq,vendaArq = linha.split(";") 
        vendaTot += float(vendaArq)
        numVenda += 1
        dataVen.append(dataVenArq) 
        venda.append(float(vendaArq))         
    arqVenda.close()


while continuar:
    print("0 - Sair ")
    print("1 - Cadastrar custos/despesas")
    print("2 - Cadastrar vendas")
    print("3 - Consultar custos/despesas")
    print("4 - Consultar vendas")
    print("5 - Gerar gráficos com custos/despesas")
    print("6 - Gerar gráficos com resultado")
    opcao = int(input("Selecione uma opção: "))

    if opcao == 0:
        sair = input("Deseja sair? S-sim N-não ")
        print("")
        if sair == "S" or sair == "s":
            continuar = False
            
            if numDesp > 0:
                arqDesp = open("despesas.csv","w")
                for i in range (0,numDesp):                  
                    arqDesp.write(dataDes[i] + ";" + str(codCat[i]) + ";" + descCat[i] + ";" + str(valor[i]) + "\n")
                arqDesp.close()  
                
            if numVenda > 0:
                arqVenda = open("vendas.csv","w")
                for i in range (0,numVenda):                  
                    arqVenda.write(dataVen[i] + ";" + str(venda[i]) + "\n")
                arqVenda.close()
                
        
    elif opcao == 1:
        codCat.append(int(input("Selecione a categoria: 1-Matéria-prima 2-Aluguel 3-Salário 4-Outra "))) 
        valor.append(float(input("Informe o valor: "))) 
        dataDes.append(input("Informe a data no seguinte padrão:  DD/MM/YYYY "))
        # dia, mes, ano = map(int, dataDes.split('/'))
        # date1 = datetime.date(dia, mes, ano)  
        # print(date1)
        if codCat[numDesp] == 1:
           descCat.append("Matéria-prima")     
           despCat1 += valor[numDesp]          
        elif codCat[numDesp] == 2:
            descCat.append("Aluguel      ")
            despCat2 += valor[numDesp]           
        elif codCat[numDesp] == 3:
            descCat.append("Salário      ")
            despCat3 += valor[numDesp]          
        elif codCat[numDesp] == 4:
            descCat.append("Outra        ") 
            despCat4 += valor[numDesp]
            
        despTot += valor[numDesp]                     
        numDesp += 1        
        print("Custo/despesa cadastrada com sucesso!")
        print("")
        
        
    elif opcao == 2:
        venda.append(float(input("Informe o valor da venda: ")))
        dataVen.append(input("Informe a data no seguinte padrão:  DD/MM/YYYY "))
        vendaTot += venda[numVenda] 
        numVenda += 1      
        print("Venda cadastrada com sucesso!")
        print("")
        
        
    elif opcao == 3:
        print("")
        print("____________________________________")
        print("DATA       |CATEGORIA      |VALOR   ")
        print("___________|_______________|________")
        for i in range (0,numDesp):             
            print(dataDes[i],"|",descCat[i],"|",round(valor[i],2))
        print("___________|_______________|________")
        print("TOTAL                      ",round(despTot,2))
        print("")
        
        
    elif opcao == 4:
        print("")
        print("____________________")
        print("DATA       |VALOR   ")
        print("___________|________")
        for i in range (0,numVenda): 
            print(dataVen[i],"|",round(venda[i],2))
        print("___________|________")
        print("TOTAL      ",round(vendaTot,2))
        print("")
            
        
    elif opcao == 5:
        categorias = ['Matéria-prima', 'Aluguel', 'Salário', 'Outra']
        despesas   = [despCat1, despCat2, despCat3, despCat4]
        porcDesp   = [((despCat1*100)/despTot),((despCat2*100)/despTot),((despCat3*100)/despTot),((despCat4*100)/despTot)]
        cores      = ['blue', 'green', 'yellow', 'red']
     
        plt.title('Custos por categoria (R$)')
        plt.pie(despesas, labels=categorias, colors=cores, autopct=lambda p: 'R$ {:1.2f}'.format(p * despTot /100), 
                shadow=True, startangle=90)        
        plt.axis('equal')
        plt.show()
        print("Custo total: R$",round(despTot,2))
        print("")
        print("")
        
        plt.title('Custos por categoria (%)')
        plt.pie(porcDesp, labels=categorias, colors=cores, autopct=lambda p: '{:1.2f}%'.format(p), 
                shadow=True, startangle=90)        
        plt.axis('equal')
        plt.show()
        print("")
        print("")

    elif opcao == 6:
        resultado = vendaTot - despTot
        porcResul = (resultado / (vendaTot + despTot)) * 100
        porcVenda = (vendaTot / (vendaTot + despTot)) * 100
        porcDesp  = (despTot / (vendaTot + despTot)) * 100
        
        x = ["Resultado", "Vendas", "Custos"]
        y = [resultado, vendaTot, despTot]
        plt.barh(x,y)
        plt.xlabel('Valor (R$)')
        plt.title('Demonstração de resultados (R$)')
        plt.show()   
        print("Total de custos: R$",round(despTot,2))
        print("Total de vendas: R$",round(vendaTot,2))
        print("Resultado final: R$",round(resultado,2))
        print("")
        print("")
        
        x = ["Resultado", "Vendas", "Custos"]
        y = [porcResul, porcVenda, porcDesp]
        plt.barh(x,y)
        plt.xlabel('Porcentagem (%)')
        plt.title('Demonstração de resultados (%)')
        plt.show()   
        print("Total de custos: ",round(porcDesp,2),"%")
        print("Total de vendas: ",round(porcVenda,2),"%")
        print("Resultado final: ",round(porcResul,2),"%")
        print("")
        print("")
        
        