import requests

print('->' * 20, 'Método GET', '->' * 20)

resposta = requests.get("http://127.0.0.1:5000/funcionarios/salario/10000")
mensagem = resposta.json()
print(mensagem)
print('- ' * 50)
print(mensagem['funcionarios'])


print('->' * 20, 'Método POST', '->' * 20)

infos = {'info': 'nome', 'valor': 'mariana'}

resposta = requests.post("http://127.0.0.1:5000/informacoes", data=infos)
if resposta.status_code == 200:
    mensagem = resposta.json()
    print(mensagem['funcionarios'])
else:
    print(resposta.status_code)


print('->' * 20, 'Método POST Com Autenticação', '->' * 20)

infos = {'nome_usuario': 'Eliel', 'senha': '1234', 'info': 'salario', 'valor': 10000}

resposta = requests.post("http://127.0.0.1:5000/informacoes", data=infos)
if resposta.status_code == 200:
    mensagem = resposta.json()
    print(mensagem['funcionarios'])
else:
    print(resposta.status_code)
