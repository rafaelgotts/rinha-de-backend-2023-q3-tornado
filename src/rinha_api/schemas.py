from marshmallow import Schema, fields, pre_load


class InputErrorValidation(Exception):
    pass


class PessoaSchema(Schema):
    apelido = fields.Str(required=True)
    nome = fields.Str(required=True)
    nascimento = fields.Date(required=True, allow_none=True)
    stack = fields.List(fields.Str(), required=True, allow_none=True)

    @pre_load
    def process_null(self, data, **kwargs):
        if data.get('apelido') is None or data.get('nome') is None:
            raise InputErrorValidation('Field may not be null.')
