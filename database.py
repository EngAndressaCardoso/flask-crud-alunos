# Base de dados em memória
alunos = [
    {
        "id": 1,
        "nome": "João Silva",
        "email": "joao.silva@email.com",
        "curso": "Engenharia de Software",
        "periodo": "5º",
    },
    {
        "id": 2,
        "nome": "Maria Oliveira",
        "email": "maria.oliveira@email.com",
        "curso": "Ciência da Computação",
        "periodo": "3º",
    },
    {
        "id": 3,
        "nome": "Pedro Santos",
        "email": "pedro.santos@email.com",
        "curso": "Sistemas de Informação",
        "periodo": "7º",
    },
    {
        "id": 4,
        "nome": "Ana Costa",
        "email": "ana.costa@email.com",
        "curso": "Análise e Desenvolvimento de Sistemas",
        "periodo": "2º",
    },
    {
        "id": 5,
        "nome": "Lucas Pereira",
        "email": "lucas.pereira@email.com",
        "curso": "Engenharia da Computação",
        "periodo": "8º",
    },
    {
        "id": 6,
        "nome": "Juliana Rocha",
        "email": "juliana.rocha@email.com",
        "curso": "Ciência de Dados",
        "periodo": "4º",
    },
    {
        "id": 7,
        "nome": "Gabriel Martins",
        "email": "gabriel.martins@email.com",
        "curso": "Redes de Computadores",
        "periodo": "6º",
    },
    {
        "id": 8,
        "nome": "Beatriz Almeida",
        "email": "beatriz.almeida@email.com",
        "curso": "Segurança da Informação",
        "periodo": "5º",
    },
    {
        "id": 9,
        "nome": "Rafael Souza",
        "email": "rafael.souza@email.com",
        "curso": "Banco de Dados",
        "periodo": "3º",
    },
    {
        "id": 10,
        "nome": "Camila Ferreira",
        "email": "camila.ferreira@email.com",
        "curso": "Inteligência Artificial",
        "periodo": "1º",
    },
]


def listar_todos_alunos():
    return alunos


def buscar_aluno_por_id(aluno_id):
    return next((a for a in alunos if a["id"] == aluno_id), None)


def inserir_aluno(novo_aluno):
    novo_id = max((aluno["id"] for aluno in alunos), default=0) + 1
    novo_aluno["id"] = novo_id
    alunos.append(novo_aluno)
    return novo_aluno


def atualizar_aluno_db(aluno_id, dados):
    aluno = buscar_aluno_por_id(aluno_id)
    if aluno:
        aluno["nome"] = dados.get("nome", aluno["nome"])
        aluno["email"] = dados.get("email", aluno["email"])
        aluno["curso"] = dados.get("curso", aluno["curso"])
        aluno["periodo"] = dados.get("periodo", aluno["periodo"])
    return aluno


def deletar_aluno_db(aluno_id):
    aluno = buscar_aluno_por_id(aluno_id)
    if aluno:
        alunos.remove(aluno)
        return True
    return False