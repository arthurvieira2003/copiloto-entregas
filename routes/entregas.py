from flask import Blueprint, request, jsonify
from services.entrega_service import processar_entregas

entrega_blueprint = Blueprint('entregas', __name__)

@entrega_blueprint.route('/processar', methods=['POST'])
def processar():
    data = request.get_json()
    conexoes = data.get('conexoes')
    entregas = data.get('entregas')
    resultado = processar_entregas(conexoes, entregas)
    return jsonify(resultado)
