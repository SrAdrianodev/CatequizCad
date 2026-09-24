import flet as ft
import json

def main(page: ft.Page):
    texto = ft.Text("🕊️ Meus Catequizandos", size=30, color="white")

    page.title = "CatequizApp"
    page.bgcolor = "blue"
    page.window.width = 600
    page.window.height = 500

    campo = ft.TextField(
        label = "Nome",
        hint_text= "Digite o nome do aluno",
        width= 418
    )

    lista_visivel = False
    editar_nome = False
    indice_editar = 0

    nomes = []
    arquivo = "alunos.json"

    def salvar():
        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump(nomes, f, ensure_ascii=False, indent=4)

    lista_nomes = ft.Text()

    def cadastrar(e):
        nonlocal editar_nome

        nome = campo.value

        if nome:
            nomes.append(nome)
            salvar()

            if lista_visivel:
                lista_nomes.value = "\n".join(nomes)

        editar_nome = False
        campo.label = "Nome"
        campo.value = ""

    def mostrar(e):
        nonlocal lista_visivel
        lista_visivel = not lista_visivel
        botao_mostrar.content = "Ocultar" if lista_visivel else "Mostrar"
        lista_nomes.value = "\n".join(nomes) if lista_visivel else ""

    def deletar(e):
        if nomes:
            nomes.pop()
            salvar()
            
            if lista_visivel:
                lista_nomes.value = "\n".join(nomes)

    def editar(e):
        nonlocal editar_nome
        nonlocal indice_editar

        if not editar_nome:
            editar_nome = True
            campo.label = "Novo nome para: " + nomes[indice_editar]
            campo.value = ""
        else:
            if nomes and campo.value:
                nomes[indice_editar] = campo.value
                salvar()

                if lista_visivel:
                    lista_nomes.value = "\n".join(nomes)

            indice_editar = indice_editar + 1

            if indice_editar >= len(nomes):
                indice_editar = 0

                if lista_visivel:
                    lista_nomes.value = "\n".join(nomes)

            editar_nome = False
            campo.label = "Nome"
            campo.value = ""

    botao_cadastrar = ft.Button(
        content= "Cadastrar",
        on_click= cadastrar
    )

    botao_mostrar = ft.Button(
        content= "Mostrar",
        on_click= mostrar
    )

    botao_deletar = ft.Button(
        content= "Deletar",
        on_click= deletar
    )

    botao_editar = ft.Button(
        content= "Editar",
        on_click= editar
    )

    page.add(
        ft.Column([
             texto,
             campo
        ])
    )

    page.add(
        ft.Row([
            botao_cadastrar,
            botao_mostrar,
            botao_deletar,
            botao_editar
        ])
    )

    page.add(lista_nomes)

if __name__ == "__main__":
    ft.run(main)