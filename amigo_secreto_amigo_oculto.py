# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/

#  DESCRIÇÃO
# ===========
# um código para um amigo secreto/oculto! Os sites de amigo secreto disponíveis,
# além de horríveis, muitas vezes não cuidam para que não haja pessoas que se
# peguem cruzado, o que quebra a roda e a diversão. Este código garante que o
# círculo será completo, ou seja, só haverá uma roda, ninguém se pegará cruzado
# :D

# Sugestões para melhorias são bem-vindas!
# (https://github.com/arthur-pandolfo/standalones)

from numpy.random import shuffle
# !!! https://pypi.org/project/yagmail/ - usa por tua conta e risco!
import yagmail 

# !!! preenche aqui com os participantes e seus respectivos e-mails
data = {"pessoa1":"email1@example.com",
        "pessoa2":"email2@example.com",
        # etc.
        }

# !!! substitui estes pelos dados do e-mail que enviará os resultados do sorteio
# aos usuários. Os e-mails enviados ficarão disponíveis na seção "Enviados" 
# deste e-mail, então cuidado para não leres!
# !!! O GMAIL BLOQUEIA O ACESSO PELO PYTHON A NÃO SER QUE O ACESSO À CONTA POR
# APPS MENOS SEGURO ESTEJA ATIVADO (NAS CONFIGURAÇÕES DE SEGURANÇA DO GOOGLE).
# USA POR TUA CONTA E RISCO (sugere-se criar uma conta nova do gmail)
email_user = "email.do.gmail@gmail.com"
email_password = "senha.email"

# !!! observações para serem enviadas juntas no corpo do e-mail (sugestão abaixo)
email_obs = "\nValor máximo no entorno de R$ 150,00\nSugestões no grupo da família"

### CÓDIGO
yag = yagmail.SMTP( 
    user=email_user,
    password=email_password)

participants = list(data.keys())
num_participants = len(participants)

# embaralhando participantes
shuffle(participants)
pairs = [pair for pair in zip(participants[:-1],participants[1:])] + \
    [(participants[-1],participants[0])]

count = (i+1 for i in range(len(data)))
for giver,taker in pairs:

    # HINT: podes adicionar mais texto ao e-mail para evitar que os nomes tirados
    # apareçam no preview do e-mail!
    contents = ["Olá, %s" %giver,
                "Teu amigo secreto é: %s" %taker,
                "Observações: %s" %email_obs]

    yag.send(data[giver], 'Amigo secreto #1', contents)
    
    print("E-mail #%d de %d enviado!" %(next(count),num_participants))

print("Tudo certo!")

# Salvando backup - NÃO LEIA SE FOR O OFICIAL
with open("SPOILER.txt",'w') as f:
    f.write("Pegou,pegado")
    for pair in pairs:
        f.write(','.join(pair))
print("SPOILER.txt criado. CONTÉM A LISTA DOS AMIGOS SECRETOS, NÃO O LEIAS!")