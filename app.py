'''
플라스크에서의 요청 처리
from flask import Flask, request

app = Flask(__name__)

@app.route('/query')
def query_example():
    language = request.args.get('language')
    return f'Requested language: {language}'
'''


'''
플라스크에서의 응답 처리
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/json')
def json_example():
    return jsonify({"message": "Hello, World!"})
'''


'''
상태 코드와 헤더 설정
from flask import Flask, make_response, render_template, Response, \
    send_from_directory, Blueprint

# app = Flask(__name__)
app = Flask(__name__, static_url_path='/img', static_folder='static/img')

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/response')
def response_example():
    # 응답 객체를 생성합니다. "Hello with header"는 응답 바디이며,
    # 200은 HTTP 상태 코드 입니다.
    resp = make_response("Hello with header", 200)
    # 'Custom-Header'라는 이름의 사용자 정의 헤더를 설정하고,
    # 'custom-value' 값을 지정합니다.
    resp.headers['Custom-Header'] = 'custom-value'
    # resp.content_length = 18
    # resp.headers['Content-Length'] = '16'
    # 설정한 헤더와 함께 응답 객체를 반환합니다.
    return resp


@app.route('/responsr')
def response_wrong_example():
    resp = make_response("Not Found", 404)
    return resp


@app.route('/direct')
def direct_response():
    headers = {'X-Example': 'DirectHeader'}
    return make_response('Direct Response', 200, headers)


@app.route('/custom')
def custom_response():
    response = make_response('Custom Response', 202)
    response.headers['X-Example'] = 'CustomHeader'
    return response


@app.route('/hello/<name>')
def hello_name(name):
    return render_template('hello.html', name=name)


@app.route('/hello')
def hello_world():
    return render_template('hello.html')


@app.route('/fruits')
def show_fruits():
    # 여기에 테스트할 과일 목록을 넣습니다.
    fruits = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']
    return render_template('fruits_list.html', fruits=fruits)


@app.route('/messages')
def show_messages():
    return render_template('messages.html')


@app.route('/about')
def about_page():
    return render_template('about.html')


@app.route('/image')
def get_image():
    return send_from_directory(app.static_folder, 'MobileNetV3.jpg')


@app.route('/img/<path:filename>')
def custom_static(filename):
    return send_from_directory('static/img', filename)
'''


'''
Buleprint
from flask import Blueprint, Flask
from auth.views import auth_blueprint
from main.views import main_blueprint

app = Flask(__name__)

app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(main_blueprint, url_prefix='/')

@app.route('/welcome')
def welcome():
    return '환영합니다! 이것은 블루프린트를 사용하지 않는 직접적인 라우트입니다.'
'''

from flask import Flask, session, abort

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/set_session')
def set_session():
    session['username'] = 'John'
    return '세션에 사용자 이름이 설정되었습니다!'

@app.route('/get_session')
def get_session():
    username = session.get('username')
    if username:
        return f'사용자 이름: {username}'
    else:
        return '사용자 이름이 세션에 설정되지 않았습니다.'
    
@app.route('/protected')
def protected():
    if 'username' not in session:
        abort(403)
        return '이 페이지는 로그인한 사용자만 볼 수 있습니다!'
    else:
        return '로그인된 페이지입니다!'