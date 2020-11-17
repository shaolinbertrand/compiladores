def AutomatoM(sentença):
    m = [[9,9,1,9,1,9],[2,9,9,3,9,3],[9,9,4,9,4,9],[6,5,9,6,9,6],[9,9,7,9,8,9]]
    pilha = []
    pilha.append('$') #colocando o simbolo delimitador na pilha
    pilha.append('E') #colocando o simbolo setencial na pilha
    prod=[]
    sentença = sentença + '$'
    print(sentença)
    i = ''
    for i in sentença:
        print("analisando o elemeto ",i," da sentença")
        if i == '+':
            c=0
        elif i == '*':
            c=1
        elif i == '(':
            c=2
        elif i == ')':
            c=3
        elif i == 'v':
            c=4
        elif i == '$':
            c=5
        else:
            return 0
        while(1):
            t = len(pilha) - 1
            t = pilha[t]
            print ("o topo da pilha é: ",t)
            if t == 'E':
                l = 0
            elif t == 'F':
                l=1
            elif t == 'M':
                print("adicionando 2 na linha")
                l=2
            elif t == 'N':
                l=3
            elif t == 'P':
                l=4
            else:
                return 0
            Nprod = m[l][c]
            print("A produção é ",Nprod)
            print("linha: ",l,"\ncoluna: ",c)
            if Nprod == 1:
                prod = 'FM'
            elif Nprod == 2:
                prod = 'FM+'
            elif Nprod == 3:
                prod = "&"
            elif Nprod == 4:
                prod = 'NP'
            elif Nprod == 5:
                prod = 'NP*'
            elif Nprod == 6:
                prod = "&"
            elif Nprod == 7:
                prod = ')E('
            elif Nprod == 8:
                prod = 'v'
            else:
                return 0
            if prod[0] == "&":
                pilha.pop()
            else:
                pilha.pop()
                for j in prod:
                    pilha.append(j)
            t = len(pilha) - 1
            t = pilha[t]
            print("o topo da pilha 2 é: ",t)
            print("o valor de i é: ",i)
            if(t == i): #verificando se há igualdade no topo da pilha e o caractere em analise
                if t == '$': #reconhecimento da sentença
                    return 1
                else: #mudança de estado do automato
                    pilha.pop()
                    print("mudando o estado do automato")
                    break
sentença = input('|------>Digite a sentença para reconhecimento: ')
res = AutomatoM(sentença)
if(res == 1):
    print("-----> O automato reconheceu a sentença")
else:
    print("|----> O automato Não reconheceu a sentença")