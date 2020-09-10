# flask packages
from flask import jsonify, Response, request
from flask_restful import Resource

# mongo-engine models
from backend.src.model.Question import Question


class QuestionApi(Resource):
    @staticmethod
    def get() -> Response:
        output = Question.objects()
        return jsonify({'result': output})

    @staticmethod
    def post() -> Response:
        data = request.get_json()
        post_question = Question(**data)
        # agregar validacion
        post_question.save()
        return jsonify({'result': post_question})

