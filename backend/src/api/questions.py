# flask packages
from flask import jsonify, Response, request
from flask_restful import Resource, abort
from mongoengine import ValidationError
# mongo-engine models
from backend.src.model.Player import Player
from backend.src.model.Question import Question
from backend.src.model.Room import Room


class QuestionApi(Resource):
    @staticmethod
    def get() -> Response:
        output = Question.objects()
        return jsonify({'result': output})

    @staticmethod
    def post() -> Response:
        data = request.get_json()
        post_question = Question(**data)
        try:
            post_question.save()
        except ValidationError as e:
            raise abort(400, message=e.message)
        return jsonify({'result': post_question})


class AnswerQuestionApi(Resource):
    @staticmethod
    def post(id) -> Response:
        data = request.get_json()['data']
        print("RESPONDIENDO PREGUNTA", flush=True)
        print(data, flush=True)
        player_id = data['nick']
        question_option_id = data['id']
        question = Question.objects.get(id=id)
        a_room = Room.objects.get(name=data['room_name'])
        a_round = Room.objects.getRoundForAQuestion(data['room_name'], id)
        post_answer = question.options.get(_id=data['id'])
        first_correct_answer = not Room.objects.roundHasAnyCorrectAnswer(a_round)
        if post_answer.correct:
            points_to_add = 1
            if first_correct_answer:
                points_to_add += 1
            player = Player.objects.get(nick=data['nick'])
            player.update(points=player.points + points_to_add)
        a_round.answers.create(player_id=player_id, question_option_id=question_option_id, first=first_correct_answer)
        Room.objects(name=data['room_name'], rounds__id=a_round.id).update(set__rounds__S=a_round)
        a_room.save()
        a_room.reload()
        return jsonify({'result': post_answer.correct})
