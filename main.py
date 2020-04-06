from flask import Flask, render_template, redirect, url_for, request, make_response
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api= Api(app)
app.config['SECRET_KEY']='mysecretkey'

class Dashboard(Resource):
    def __init__(self):
        pass
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('index2.html'),200,headers)

class Inbox(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('inbox.html'),200,headers)


class Registration(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('registration.html'),200,headers)


class Resume(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('resume.html'),200,headers)


class Sentimental(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('sentimental.html'),200,headers)


class Summarizer(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('summarizer.html'),200,headers)

api.add_resource(Dashboard, '/')
api.add_resource(Inbox, '/inbox')
api.add_resource(Registration, '/registration')
api.add_resource(Resume, '/resume')
api.add_resource(Sentimental, '/sentimental') #feedback
api.add_resource(Summarizer, '/summarizer')


if __name__ == "__main__":
    app.run(debug=True)
