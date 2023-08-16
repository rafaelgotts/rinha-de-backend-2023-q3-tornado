from http import HTTPStatus

from marshmallow.exceptions import ValidationError
from tornado.web import RequestHandler

from rinha_api.schemas import InputErrorValidation, PessoaSchema


class PessoasHandler(RequestHandler):

    def prepare(self):
        self._create_model(self.request.body)

    def post(self):
        print(self.parsed_body)

    def get(self):
        pass

    def _create_model(self, body):
        try:
            self.parsed_body = PessoaSchema().loads(body)
        except ValidationError as error:
            self.set_status(
                status_code=HTTPStatus.UNPROCESSABLE_ENTITY.value,
                reason=HTTPStatus.UNPROCESSABLE_ENTITY.name
            )
            self.finish({'errors': error.messages})
        except InputErrorValidation as error:
            self.set_status(
                status_code=HTTPStatus.BAD_REQUEST.value,
                reason=HTTPStatus.BAD_REQUEST.name
            )
            self.finish({'errors': [str(error)]})
