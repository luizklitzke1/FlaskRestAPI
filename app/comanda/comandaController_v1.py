from inspect import Attribute
from turtle import st
from flask_restx import Resource, Namespace, fields, reqparse, abort, marshal_with
from flask import request

api = Namespace("Comandas", description = "CRUD dos dados de Comandas")

produtoArgumentos = {
    'id'      : fields.Integer(attribute = 'id'   ),
    'nome'    : fields.String (attribute = 'nome' ),
    'preco'   : fields.Integer(attribute = 'preco'),
}

produtoModel = api.model('ProdutoModel', produtoArgumentos)

comandaArgumentos = {
    'idUsuario'      : fields.Integer (attribute = 'idUsuario'      ),
    'nomeUsuario'    : fields.String  (attribute = 'nomeUsuario'    ),
    'telefoneUsuario': fields.Integer (attribute = 'telefoneUsuario'),
    'produtos'       : fields.List    (fields.Nested(produtoModel)  ),
}

comandaArgumentosDoc = {
    'idUsuario'      : 'Id do Usuário'      ,
    'nomeUsuario'    : 'Nome do usuário'    ,
    'telefoneUsuario': 'Telefone do usuário',
    'produtos'       : 'Produtos da comanda',
}

comandaArgumentosParser = reqparse.RequestParser()
comandaArgumentosParser.add_argument('idUsuario'      , type = fields.Integer                          , help = 'Id do Usuário'      , required = True)
comandaArgumentosParser.add_argument('nomeUsuario'    , type = fields.String                           , help = 'Nome do usuário'    , required = True)
comandaArgumentosParser.add_argument('telefoneUsuario', type = fields.Integer                          , help = 'Telefone do usuário', required = True)
comandaArgumentosParser.add_argument('produtos'       , type = fields.List(fields.Nested(produtoModel)), help = 'Produtos da comanda', required = True, action = 'append')

modeloComanda = api.model('ComandaModel', comandaArgumentos)

@api.route("")
class ComandasController(Resource):
    @api.response(200, "Busca de Comandas conclúida com sucesso")
    def get(self): #lista de Todas Comandas Cadastras
        pass

    @marshal_with(comandaArgumentos)
    @api.expect(modeloComanda, validate = True)   
    def post(self): #adiciona comanda
        pass

    @marshal_with(comandaArgumentos)
    @api.expect(modeloComanda) 
    def put(self): #atualiza comanda
        pass

@api.route("/<int:id>")
class ComandaIdController(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self, id:int): #busca comanda pelo ID
        pass

    def delete(self, id:int):
        pass