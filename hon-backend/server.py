# -*- coding: utf-8 -*-

from flask import render_template, request, redirect

from app import app
from hon.api.accounts import register_account_resource
from hon.api.user import register_user_resource

register_user_resource()
register_account_resource()


@app.route('/')
def index():
    return render_template('index.html')


@app.before_request
def before_request():
    path = request.path
    if path != '/' and path.endswith('/'):
        return redirect(path[:-1])


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin',
                         app.config['ALLOWED_DOMAIN'])
    response.headers.add('Access-Control-Max-Age', 0)
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET, POST, PUT, DELETE')
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)
