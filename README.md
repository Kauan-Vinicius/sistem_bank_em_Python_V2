# Desafio de projeto: Otimizando sistemma bancário com Python

## Objetivos gerais

Utilizar a primeira versão do projeto com as operações de depósito, saque e visualizar extrato. E, adicionar mais algumas funções:
- Criar usuário (cliente)
- Criar conta corrente
- Listar as contas que o usuário possui

  ### Operação de criar usuário:
  O programa deve armazenar os usuários em uma lista, um usuário é composto por: nome, data de nascimento, cpf e endereço.
  O endereço é uma string com o formato: logradouro, nro - bairro - cidade/sigla estado.
  Deve ser armazenado somente os números do CPF. Não podemos cadastrar 2 usuários com o mesmo CPF.

  #### Exemplo abaixo:

  ![Alt text](./Criar usuário (cliente).png "Operação de criar usuário:")

  ### Operação de criar conta corrente:
  O programa deve armazenar contas em uma lista, uma conta é composta por: agência, número da conta e usuário.
  O número da conta é sequencial, iniciando em 1. O número da agência é fixo: "0001".
  O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.

  
  
