from flask import jsonify

from app.api.view_models.classic import ClassicCollection
from app.libs.c_blueprints import CBlueprint
from app.models.classic import Classic

api = CBlueprint('classic')


@api.route('/latest', methods=['GET'])
def get_latest():
    res = Classic().latest
    classic = ClassicCollection()
    data = classic.fill_single(res)
    print(data)
    return jsonify(data)
