from flask import Flask, jsonify, request
import database

app = Flask(__name__)


# GET - Listar todos os alunos
@app.route("/alunos", methods=["GET"])
def listar_alunos():
    return jsonify(database.listar_todos_alunos())


# GET - Buscar aluno por ID
@app.route("/alunos/<int:id>", methods=["GET"])
def buscar_aluno(id):
    aluno = database.buscar_aluno_por_id(id)
    if aluno:
        return jsonify(aluno)
    return jsonify({"erro": "Aluno não encontrado"}), 404


# POST - Adicionar novo aluno
@app.route("/alunos", methods=["POST"])
def adicionar_aluno():
    dados = request.get_json()

    if (
        not dados
        or "nome" not in dados
        or "email" not in dados
        or "curso" not in dados
        or "periodo" not in dados
    ):
        return jsonify({"erro": "Dados incompletos"}), 400

    novo_aluno = database.inserir_aluno(dados)

    return (
        jsonify(
            {"mensagem": "Aluno cadastrado com sucesso", "aluno": novo_aluno}
        ),
        201,
    )


# PUT - Atualizar aluno
@app.route("/alunos/<int:id>", methods=["PUT"])
def atualizar_aluno(id):
    dados = request.get_json() or {}
    aluno_atualizado = database.atualizar_aluno_db(id, dados)

    if not aluno_atualizado:
        return jsonify({"erro": "Aluno não encontrado"}), 404

    return jsonify(
        {"mensagem": "Aluno atualizado com sucesso", "aluno": aluno_atualizado}
    )


# DELETE - Remover aluno
@app.route("/alunos/<int:id>", methods=["DELETE"])
def remover_aluno(id):
    removido = database.deletar_aluno_db(id)

    if not removido:
        return jsonify({"erro": "Aluno não encontrado"}), 404

    return jsonify({"mensagem": "Aluno removido com sucesso"})


# Executar aplicação
if __name__ == "__main__":
    app.run(debug=True)