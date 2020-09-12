# flask packages
from flask import jsonify, Response, request
from flask_restful import Resource

# mongo-engine models
from backend.src.model.Player import Player
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


class AnswerQuestionApi(Resource):
    @staticmethod
    def post(id) -> Response:
        data = request.get_json()['data']
        question = Question.objects.get(id=id)
        post_answer = question.options.get(_id=data['id'])
        if post_answer.correct:
            player = Player.objects.first()
            player.update(points=player.points + 1)
        return jsonify({'result': post_answer.correct})
