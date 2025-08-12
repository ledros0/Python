# coding: utf-8 
import Conversor 

escolha = input("O que voce quer converter? \n1 - Metros \n2 - Pes\n\n");

if(escolha == "1"):
    metros = input("Digite a quantidade de metros\n");
    metrosConvertidos = Conversor.ConverteMetros(float(metros));
    print(f"Os {metros} metros viraram {metrosConvertidos:.2f} pes!");
    
elif(escolha == "2"):
    pes = input("Digite a quantidade de pes\n");
    pesConvertidos = Conversor.ConvertePes(float(pes));
    print(f"Os {pes} pes viraram {pesConvertidos:.2f} metros!");

