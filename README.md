# Desafio de projeto: Otimizando sistema bancário com Python

## Objetivos gerais

Utilizar a primeira versão do [projeto](https://github.com/Kauan-Vinicius/sistema_bank_em_Python/tree/main) com as operações de depósito, saque e visualizar extrato. E, adicionar mais algumas funções:
- Criar usuário (cliente).
- Criar conta corrente.
- Listar as contas que o usuário possui.

  ### Operação de criar usuário:
  O programa deve armazenar os usuários em uma lista, um usuário é composto por: nome, data de nascimento, cpf e endereço.
  O endereço é uma string com o formato: logradouro, nro - bairro - cidade/sigla estado.
  Deve ser armazenado somente os números do CPF. Não podemos cadastrar 2 usuários com o mesmo CPF.

  #### Exemplo abaixo:

  ![Alt text](./Criar_usuário_(cliente).png "Operação de criar usuário:")

  ### Operação de criar conta corrente:
  O programa deve armazenar contas em uma lista, uma conta é composta por: agência, número da conta e usuário.
  O número da conta é sequencial, iniciando em 1. O número da agência é fixo: "0001".
  O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.

  #### Exemplo abaixo:

  ![Alt text](./Criar_conta_corrente.png "Operação de criar conta corrente:")

  #### Se por acaso tentarem criar uma conta corrente sem ter feito o cadastro de usuário a seguinte mensagem de erro aparecerá:

  ![Alt text](./Insucesso_conta_corrente.png "Operação de criar conta corrente falhou")

  ### Operação de listar contas:
  O programa lista as informações armazenadas do usuário e informa quantas contas correntes o usuário possui.

  #### Exemplo abaixo:

  ![Alt text](./Listar_contas.png "Operação de listar contas:")
  
