# flask packages
from flask import jsonify
from flask_restful import Resource

# mongo-engine models
from backend.src.Question import Question


class QuestionApi(Resource):
    def get(self):
        output = Question.objects()
        return jsonify({'result': output})
