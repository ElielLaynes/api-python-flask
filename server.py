from flask import Flask, request, Response

app = Flask(__name__)

funcionarios = [
                    {'nome': 'Mariana', 'cargo': 'Gerente', 'salario': 10000},
                    {'nome': 'Eliel', 'cargo': 'Gerente', 'salario': 8000},
                    {'nome': 'Paola', 'cargo': 'Desenvolvedor', 'salario': 10000}
                ]

usuarios = [
            {'nome_usuario': 'Eliel', 'senha': '1234'}
            ]

def valida_usuario(nome_usuario, senha):
    for usuario in usuarios:
        if (usuario['nome_usuario'] == nome_usuario) and (usuario['senha'] == senha):
            return True
    return False


@app.route('/')
def home():
    return '''<h1>Olá. Bem-vindo(a) a API de Funcionários =D</h1>
    <p>Nessa APi você Pode Acessar dados de Nome, Cargo e Salario de 3 funcionários fictícios.</p>
'''


@app.route('/funcionarios')
def get_funcionarios():
    return {'funcionarios': funcionarios}


@app.route('/funcionarios/<cargo>')
def get_funcionarios_cargo(cargo):
    saida_funcionarios = []
    for func in funcionarios:
        if cargo == func['cargo'].lower():
            saida_funcionarios.append(func)
    return {'funcioarios': saida_funcionarios}


@app.route('/funcionarios/<info>/<valor>')
def get_funcinarios_info(info, valor):
    saida_funcionarios = []
    for func in funcionarios:
        if info in func.keys():
            valor_funcionario = func[info]

            if type(valor_funcionario) == str:
                if valor == valor_funcionario.lower():
                    saida_funcionarios.append(func)

            if type(valor_funcionario) == int:
                if int(valor) == valor_funcionario:
                    saida_funcionarios.append(func)
    return {'funcionarios': saida_funcionarios}


@app.route('/informacoes', methods=['POST'])
def get_funcinarios_post():

    nome_usuario = request.form['nome_usuario']
    senha = request.form['senha']

    if not valida_usuario(nome_usuario, senha):
        # 401 HTTP Não Autotizado
        return Response('Login Não Autorizado', status=401)

    info = request.form['info']
    valor = request.form['valor']

    saida_funcionarios = []
    for func in funcionarios:
        if info in func.keys():
            valor_funcionario = func[info]

            if type(valor_funcionario) == str:
                if valor == valor_funcionario.lower():
                    saida_funcionarios.append(func)

            if type(valor_funcionario) == int:
                if int(valor) == valor_funcionario:
                    saida_funcionarios.append(func)
    return {'funcionarios': saida_funcionarios}


if __name__ == '__main__':
    app.run(debug=False)
