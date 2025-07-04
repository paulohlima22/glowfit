from flask import Flask, render_template, request, redirect, flash
import yagmail

app = Flask(__name__)
app.secret_key = 'segredo_super_secreto'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/depoimentos')
def depoimentos():
    return render_template('depoimentos.html')

@app.route('/contato', methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        mensagem = request.form['mensagem']

        # Envia e-mail
        try:
            yag = yagmail.SMTP('SEUEMAIL@gmail.com', 'SENHA-DO-APLICATIVO')
            yag.send(
                to='SEUEMAIL@gmail.com',
                subject='Nova mensagem do formulário de contato',
                contents=f'Nome: {nome}\nEmail: {email}\nMensagem:\n{mensagem}'
            )
            flash('Mensagem enviada com sucesso!')
        except Exception as e:
            flash(f'Erro ao enviar: {e}')

        return redirect('/contato')
    return render_template('contato.html')

if __name__ == '__main__':
    app.run(debug=True)
