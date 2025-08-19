# coding: utf-8 
import Conversor 

escolha = input("O que voce quer converter? \n1 - Metros \n2 - Pes\n3 - Jardas\n");

if(escolha == "1"):
    metros = input("Digite a quantidade de metros\n");
    escolha2 = input("Para o que voce quer converter?\n1 - Pes\n2 - Jardas\n")

    if(escolha2 == "1"):
       metrosConvertidos = Conversor.ConverteMetrosParaPes(float(metros));
       print(f"Os {metros} metros viraram {metrosConvertidos:.2f} pes!");

    elif(escolha2 == "2"):
        metrosConvertidos = Conversor.ConverteMetrosParaJardas(float(metros));
        print(f"Os {metros} metros viraram {metrosConvertidos:.2f} jardas!");
    

elif(escolha == "2"):
    pes = input("Digite a quantidade de pes\n");
    escolha2 = input("Para o que voce quer converter?\n1 - Metros\n2 - Jardas\n");

    if(escolha2 == "1"):
      pesConvertidos = Conversor.ConvertePesParaMetros(float(pes));
      print(f"Os {pes} pes viraram {pesConvertidos:.2f} metros!");

    elif(escolha2 == "2"):
      pesConvertidos = Conversor.ConvertePesParaJardas(float(pes));
      print(f"Os {pes} pes viraram {pesConvertidos:.2f} jardas!");

elif(escolha == "3"):
    jardas = input("Digite a quantidade de jardas\n");
    escolha2 = input("Para o que voce quer converter?\n1 - Metros\n2 - Pes\n");

    if(escolha2 == "1"):
      pesConvertidos = Conversor.ConverteJardaParaMetros(float(jardas));
      print(f"As {jardas} pes viraram {pesConvertidos:.2f} metros!");

    elif(escolha2 == "2"):
      pesConvertidos = Conversor.ConverteJardasParaPes(float(jardas));
      print(f"As {jardas} pes viraram {pesConvertidos:.2f} pes!");
