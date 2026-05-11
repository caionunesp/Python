from flask import Flask 

app = Flask(__name__)

@app.route('/')
def ola_mundo():
    return 'Decorators em Python servem para modificar ou estender o comportamento de funções, métodos ou classes sem alterar o seu código-fonte original. Eles funcionam como "embalagens" (wrappers) que permitem adicionar funcionalidades extras antes ou depois da execução da função original de forma limpa e reutilizável.\nPrincipais usos e benefícios:\nAdicionar Comportamentos: Inserir lógica como logging, medição de tempo de execução, ou cache de resultados (memoização).\nControle de Acesso: Verificar permissões de usuário antes de executar uma função, comum em frameworks web como Flask.\nReutilização de Código: Aplicar a mesma lógica em múltiplas funções sem repetição.Sintaxe Limpa: Utilizam a sintaxe @nome_do_decorator acima da função, facilitando a leitura.Exemplos Comuns:@staticmethod e @classmethod: Modificam métodos de classe.@property: Transforma métodos em atributos (getters/setters).@app.route(): Define rotas em frameworks web'

if __name__ == '__main__':
    app.run(debug=True)