from flask import Flask, jsonify, request
2
 
3
app = Flask(__name__)

# GET - Listar todos os alunos
80
@app.route('/alunos', methods=['GET'])
81
def listar_alunos():
82
return jsonify(alunos)
83
 
84
# GET - Buscar aluno por ID
85
@app.route('/alunos/<int:id>', methods=['GET'])
86
def buscar_aluno(id):
87
aluno = next((a for a in alunos if a['id'] == id), None)
88
 
89
if aluno:
90
return jsonify(aluno)
91
 
92
return jsonify({"erro": "Aluno não encontrado"}), 404
93
 
94
# POST - Adicionar novo aluno
95
@app.route('/alunos', methods=['POST'])
96
def adicionar_aluno():
97
novo_aluno = request.get_json()
98
 
99
novo_id = max(aluno['id'] for aluno in alunos) + 1
100
novo_aluno['id'] = novo_id
101
 
102
alunos.append(novo_aluno)
103
 
104
return jsonify({
105
"mensagem": "Aluno cadastrado com sucesso",
106
"aluno": novo_aluno
107
}), 201
108
 
109
# PUT - Atualizar aluno
110
@app.route('/alunos/<int:id>', methods=['PUT'])
111
def atualizar_aluno(id):
112
aluno = next((a for a in alunos if a['id'] == id), None)
113
 
114
if not aluno:
115
return jsonify({"erro": "Aluno não encontrado"}), 404
116
 
117
dados = request.get_json()
118
 
119
aluno['nome'] = dados.get('nome', aluno['nome'])
120
aluno['email'] = dados.get('email', aluno['email'])
121
aluno['curso'] = dados.get('curso', aluno['curso'])
122
aluno['periodo'] = dados.get('periodo', aluno['periodo'])
123
 
124
return jsonify({
125
"mensagem": "Aluno atualizado com sucesso",
126
"aluno": aluno
127
})
128
 
129
# DELETE - Remover aluno
130
@app.route('/alunos/<int:id>', methods=['DELETE'])
131
def remover_aluno(id):
132
aluno = next((a for a in alunos if a['id'] == id), None)
133
 
134
if not aluno:
135
return jsonify({"erro": "Aluno não encontrado"}), 404
136
 
137
alunos.remove(aluno)
138
 
139
return jsonify({
140
"mensagem": "Aluno removido com sucesso"
141
})
142
 
143
# Executar aplicação
144
if __name__ == '__main__':
145
app.run(debug=True)
