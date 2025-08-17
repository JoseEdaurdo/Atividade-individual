from app import app
from flask import render_template, request, redirect, url_for
from app.models.cliente_model import ClienteModel
from app.service.cliente_service import ClienteService  
from app.models.sessao_model import SessaoModel
from app.service.sessao_service import SessaoService

cliente_service = ClienteService()
sessao_service = SessaoService()

@app.route('/')
def index():
    return redirect(url_for('list_clientes'))

@app.route('/clientes')
def list_clientes():
    clientes = cliente_service.get_all_clientes()
    return render_template('cliente/list.html', clientes=clientes)

@app.route('/clientes/novo', methods=['GET', 'POST'])
def create_cliente():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        cliente_service.create_cliente(ClienteModel(None, nome, email, telefone))
        return redirect(url_for('list_clientes'))
    return render_template('cliente/form.html')


@app.route('/clientes/editar/<int:id>', methods=['GET', 'POST'])
def update_cliente(id):
    cliente = cliente_service.get_cliente_by_id(id)
    if request.method == 'POST':
        cliente_service.update_cliente(ClienteModel(
            id,
            request.form['nome'],
            request.form['email'],
            request.form['telefone']
        ))
        return redirect(url_for('list_clientes'))
    return render_template('cliente/form.html', cliente=cliente)
            
@app.route('/clientes/excluir/<int:id>')
def delete_cliente(id):
    cliente_service.delete_cliente(id)
    return redirect(url_for('list_clientes'))

@app.route('/sessoes')
def list_sessoes():
    sessoes = sessao_service.get_all_sessoes()
    return render_template('sessao/list.html', sessoes=sessoes)

@app.route('/sessoes/novo', methods=['GET', 'POST'])
def create_sessao():
    if request.method == 'POST':
        id_cliente = request.form['id_cliente']
        data_sessao = request.form['data_sessao']
        tipo_sessao = request.form['tipo_sessao']
        local = request.form['local']
        status = request.form['status']
        sessao = SessaoModel(id=None, id_cliente=id_cliente, data_sessao=data_sessao,
                             tipo_sessao=tipo_sessao, local=local, status=status)
        sessao_service.create_sessao(sessao)
        return redirect(url_for('list_sessoes'))
    return render_template('sessao/form.html', clientes=cliente_service.get_all_clientes())

@app.route('/sessoes/editar/<int:id>', methods=['GET', 'POST'])
def update_sessao(id):
    sessao = sessao_service.get_sessao_by_id(id)
    if request.method == 'POST':
        id_cliente = request.form['id_cliente']
        data_sessao = request.form['data_sessao']
        tipo_sessao = request.form['tipo_sessao']   
        local = request.form['local']
        status = request.form['status']
        sessao_service.update_sessao(SessaoModel(
            id=id,
            id_cliente=id_cliente,
            data_sessao=data_sessao,
            tipo_sessao=tipo_sessao,
            local=local,
            status=status
        ))
        return redirect(url_for('list_sessoes'))
    return render_template('sessao/form.html', sessao=sessao, clientes=cliente_service.get_all_clientes())

@app.route('/sessoes/excluir/<int:id>')
def delete_sessao(id):
    sessao_service.delete_sessao(id)
    return redirect(url_for('list_sessoes'))


