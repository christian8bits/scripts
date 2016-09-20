#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
versao 1
OBS1: Caso tenha algum acento no endereço absoluto de alguma musica, 
ou em qualquer musica da playlist, não irá funcionar.
OBS2: por enquanto o script só move os arquivos para a home do usuario.
OBS3: script deve ser rodado na pasta do arquivo playlist (.pls) 
OBS4: se o diretorio de destino já existir, o script usara o existente 
e deve sobreescrever caso algum arquivo de nome igual exista.
"""
import os
#Apaga a tela
os.system("clear")
print("Arquivos .pls no diretorio atual:")
os.system("ls *.pls")

nomePlay = raw_input("nome da playlist? \n(Omitir extensão .pls) : ")
os.system("mkdir $HOME/"+nomePlay)

arquivo = open(nomePlay+".pls","r")
for linha in arquivo:
	if linha.startswith("File"):
		listaMusicas = linha.split("=file://")
		musica = "\""+listaMusicas[1]+"\""
		musica = musica.replace("%20", " ")
		musica = musica.replace("%5B", "[")
		musica = musica.replace("%5D", "]")
		musica = musica.replace("\n", "")
		os.system("cp "+musica+" $HOME/"+nomePlay)
		print("OK "+musica)
