nomes = "ANA CLARA NOGUEIRA DE ARAÚJO;ANA LAURA FARIA SANTOS;ANA LAURA FERNANDES DA SILVA;BETÂNIA AMÂNCIO PEREIRA;BRENO ESTORARI DA SILVA;EDUARDO BELLO GALEGO;EDUARDO HENRIQUE DO CARMO;ERIKA DE BRITTO CÔNSOLO;FERNANDA GARCIA FLORIANO;GIUSEPPE FRANCESCO STRACERI IANES BAGGIO;GUSTAVO MEDEIROS DE BARROS;GUSTAVO PEREIRA GARCIA;JOAO PEDRO BILLO LUCIANO;JOAO VICTOR SALOTI ALVES;KAUA DANTAS MARTINS;KEVIN RENAN NOGUEIRA DA SILVEIRA;LAIS CUNHA THEODORO DA SILVA;LAVINIA DAL BELLO E SOUZA;LUiS OTAVIO FLORENCIO BARBOSA;LUIS OTAVIO MORAIS DE SOUZA;LUIZA HELENA TARDELLI MARCULLI ESPINDOLA;MARIA CAROLINA SILVA GARCIA;MARIA CLARA SANTOS MANETA;MARIA FERNANDA GRESPAN BENFEITO;MARIA FERNANDA TOBIAS CHAGAS;MATHEUS CARVALHO FELISBERTO;MURILO ANTONIO BARION;NICOLY GOMES SERRANO;OCTAVIO AUGUSTO ANDREAZZI CHAVES;PEDRO VINICIUS VIEIRA VASCONCELLOS;RAFAEL CREMASCO;RAFAEL LOPES PIRES;RAQUEL MOREIRA FERNANDES CUSTODIO;RENAN HENRIQUE TEIXEIRA;SABRYNA SATORRES BATISTINI;SOPHIA RUEDA GONÇALVES DA RITA;TAYNARA DE MELLO SIQUEIRA;TIFANI SCHIAVON MISSURA;VIToRIA CIPRIANO DE JESUS;WESLEY RICARDO SILVA PEREIRA"
notas = "9.33;8.76;6.11;1.09;2.76;2.97;9.04;3.62;3.37;1.76;8.14;2.48;3.27;9.16;9.01;1.55;2.98;3.41;8.45;5.79;0.54;2.01;6.78;1.09;4.75;0.09;7.62;0.53;8.95;6.93;1.04;2.87;7.85;6.65;6.96;9.72;9.42;0.44;6.78;7.54"
faltas = "23;5;14;5;29;20;19;2;23;5;18;27;6;8;28;29;5;7;7;19;6;14;4;21;25;25;17;23;21;13;1;19;27;21;26;27;7;19;5;21"

vetorNomes = nomes.split(";")
vetorNotas = notas.split(";")
vetorFaltas = faltas.split(";")

for i in range(len(vetorNomes)):
        print("Nome:"+vetorNomes[i],
              "\nNotas:"+vetorNotas[i],
              "\nFaltas:"+vetorFaltas[i])

print("\n---APROVADOS---\n")
totalaprovados = 0;
for i in range(len(vetorNomes)):
        if (float(vetorNotas[i]) >= 6.0 and float(vetorFaltas[i]) <= 20.0):
                totalaprovados = totalaprovados+1;
                print("\n---APROVADO---")
                print(vetorNomes[i],
                      "\nNota:" + vetorNotas[i])
print("\nTotal de aprovados:",totalaprovados)

print("\n---Reprovados por Falta---\n")
totalreprovados = 0;
for i in range(len(vetorNomes)):
        if(float(vetorFaltas[i]) > 20.0):
                totalreprovados = totalreprovados+1
                print(vetorNomes[i],
                      "\nFaltas:"+vetorFaltas[i])
print("\nTotal de reprovados por falta:", totalreprovados)

print("\n---SILVAS---\n")
for i in range(len(vetorNomes)):
        Sobrenome = vetorNomes[i].split()
        #Sobrenome.find("SILVA")
        if(Sobrenome[-1] == "SILVA"):
                print(vetorNomes[i])

        #if(Sobrenome[i].rfind("SILVA")):
         #   print(vetorNomes[i])



print("\n---Nome e Sobrenome---\n")
for i in range(len(vetorNomes)):
        aluno = vetorNomes[i].split()
        nome = aluno[0].lower()
        sobrenome = aluno[-1].lower()
        print(nome.capitalize(), sobrenome.capitalize())


print("\n---Nomes Completos---\n")
for i in range(len(vetorNomes)):
    nomecompleto = vetorNomes[i]
    nomes = nomecompleto.split()

    if(len(nomes) < 3):
        print(nomecompleto)
    else:
        qtde = len(nomes)
        nome1 = nomes[0]
        nome2 = ""
        nome3 = nomes[qtde - 1]
        for j in range(1, qtde-1):
           nome2 += nomes[j][0] + "."

        print(nome1, nome2, nome3)






