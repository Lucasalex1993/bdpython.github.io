from flask import request, render_template, redirect, url_for, flash
from models import db, Usuario

def init_routes(app):

    @app.route('/')
    def index():
        usuarios = Usuario.query.all()
        return render_template('index.html', usuarios=usuarios)

    @app.route('/cadastrarUsuario', methods=['GET', 'POST'])
    def cadastrarUsuario():
        if request.method == 'POST':
            nome = request.form['nome']
            email = request.form['email']
            senha = request.form['senha']
            
            novo_usuario = Usuario(
                nome=nome, email=email, senha=senha,
            )
            db.session.add(novo_usuario)
            db.session.commit()

            flash('Usuário cadastrado com sucesso!')
            return redirect(url_for('index'))
        
        return render_template('cadastro.html')

    @app.route('/editarUsuario/<int:id>', methods=['GET', 'POST'])
    def editarUsuario(id):
        usuario = Usuario.query.get_or_404(id)
        if request.method == 'POST':
            usuario.nome = request.form['nome']
            usuario.email = request.form['email']
            usuario.senha = request.form['senha']
           
            db.session.commit()
            flash('Usuário editado com sucesso!')
            return redirect(url_for('index'))
        
        return render_template('editar.html', usuario=usuario)

    @app.route('/deletarUsuario/<int:id>', methods=['POST'])
    def deletarUsuario(id):
        usuario = Usuario.query.get_or_404(id)
        db.session.delete(usuario)
        db.session.commit()
        flash('Usuário deletado com sucesso!')
        return redirect(url_for('index'))
