# 🕊️ CatequizCad

Aplicativo desenvolvido em **Python** utilizando o framework **Flet** para realizar o cadastro e gerenciamento de catequizandos.

O projeto foi desenvolvido como atividade acadêmica de programação visual e utiliza uma interface gráfica simples para realizar operações de **CRUD (Create, Read, Update e Delete)**, com armazenamento dos dados em um arquivo **JSON**.

## 📌 Sobre o projeto

O **CatequizCad** foi desenvolvido para facilitar o cadastro e o gerenciamento de uma lista de catequizandos.

O aplicativo permite cadastrar novos nomes, visualizar os nomes cadastrados, editar informações e excluir registros.

Os dados são armazenados no arquivo `alunos.json`, utilizando o módulo `json` da linguagem Python.

## 🖥️ Interface do aplicativo

A interface possui:

- Campo para digitar o nome do catequizando;
- Botão **Cadastrar**;
- Botão **Mostrar/Ocultar**;
- Botão **Deletar**;
- Botão **Editar**;
- Área para exibição dos nomes cadastrados.

## 🔘 Funcionamento dos botões

### Cadastrar

Adiciona o nome digitado no campo à lista de catequizandos.

Após o cadastro, o nome é salvo no arquivo `alunos.json`.

### Mostrar / Ocultar

Exibe os nomes cadastrados na tela ou oculta a lista.

O mesmo botão alterna entre as opções **Mostrar** e **Ocultar**.

### Editar

### Editar

O botão **Editar** permite selecionar qual catequizando será alterado.

Ao clicar em **Editar**, o aplicativo apresenta no campo o nome que está sendo selecionado para edição. Após informar o novo nome e clicar novamente em **Editar**, a alteração é realizada.

Depois disso, o aplicativo avança para o próximo nome da lista. Dessa forma, ao utilizar o botão **Editar** novamente, é possível percorrer os catequizandos e selecionar outro nome para edição.

A seleção dos nomes é feita de forma sequencial, seguindo a ordem em que foram cadastrados. Ao chegar ao último nome, a seleção retorna para o primeiro.

Caso o botão **Cadastrar** seja pressionado durante uma edição, o aplicativo não altera o nome que estava sendo selecionado. Nesse caso, o nome digitado é tratado como um novo cadastro.

### Deletar

Remove o último nome cadastrado na lista.

Após a exclusão, os dados atualizados são novamente salvos no arquivo `alunos.json`.

## 🔄 CRUD

O aplicativo implementa as quatro operações básicas de um CRUD:

| Operação | Aplicação no CatequizCad |
|---|---|
| **Create** | Cadastrar um catequizando |
| **Read** | Mostrar os catequizandos cadastrados |
| **Update** | Editar um nome cadastrado |
| **Delete** | Deletar um catequizando |

## 🛠️ Tecnologias utilizadas

### Python

Linguagem utilizada para desenvolver a lógica do aplicativo.

### Flet

Framework utilizado para criar a **interface gráfica** do aplicativo e seus componentes, como `Text`, `TextField`, `Button`, `Row` e `Column`.

### JSON

Formato utilizado para o **armazenamento dos dados**.

O módulo `json` do Python é utilizado para transformar a lista de nomes em dados JSON e gravá-los no arquivo `alunos.json`.

## 💾 Armazenamento dos dados

Os nomes cadastrados são armazenados no arquivo:

```text
alunos.json
