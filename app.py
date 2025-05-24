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

'''
플라스크에서의 쿠키 사용법
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

from flask import Flask, make_response, request, abort

app = Flask(__name__)

@app.route('/set_cookie')
def set_cookie():
    resp = make_response('쿠키를 설정합니다.')
    resp.set_cookie('username', 'John', max_age=60*60*24*7)
    return resp

@app.route('/get_cookie')
def get_cookie():
    username = request.cookies.get('username', '게스트')
    return f'쿠키로부터 얻은 사용자 이름: {username}'

@app.route('/secret')
def secret():
    username = request.cookies.get('username')
    if not username:
        # 쿠키가 없다면 접근 금지 메시지 반환
        abort(403, description='접근 권한이 없습니다. 먼저 쿠키를 설정해주세요.')
    return f'환영합니다, {username}님! 비밀 페이지에 접속한 것을 환영합니다!'

@app.route('/delete_cookie')
def delete_cookie():
    resp = make_response('쿠키를 삭제합니다.')
    resp.delete_cookie('username')
    return resp
'''

'''
로깅 기본 사용법
from flask import Flask
import logging

app = Flask(__name__)
app.logger.setLevel(logging.DEBUG) # DEBUG 레벨 이상 모든 로그 기록
logging.basicConfig(filename='application.log',
                    level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

@app.route('/')
def home():
    app.logger.debug('Debug level log')
    app.logger.info('Info level log')
    app.logger.warning('Warning level log')
    app.logger.error('Error level log')
    app.logger.critical('Critical level log')
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
'''

'''
플라스크와 MySQL 연동
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:test@localhost:3306/db_name'
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    def __repr__(self):
        return '<User %r>' % self.username

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    # 데이터 생성
    new_user = User(username='john', email='john@example.com')
    db.session.add(new_user)
    db.session.commit()
    
    # 데이터 조회(Read)
    user = User.query.filter_by(username='john').first()
    
    # 데이터 업데이트(Update)
    user.email = 'john@newexample.com'
    db.session.commit()
    
    # 데이터 삭제(Delete)
    db.session.delete(user)
    db.session.commit()
    
    return 'CRUD operations completed'
'''

'''
Flask-Migrate
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:test@localhost/db_name'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    def __repr__(self):
        return '<User %r>' % self.username

migrate = Migrate(app, db)
'''

'''
Flask-Login을 사용한 인증
'''
from flask import Flask, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_required, \
    login_user, logout_user, current_user

app = Flask(__name__)

# 데이터베이스 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://funcoding:funcoding@localhost/flaskdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Flask 애플리케이션을 위한 비밀 키 설정
app.config['SECRET_KEY'] = 'mysecretkey'

db = SQLAlchemy(app) # SQLALchemy 인스턴스 생성

# LoginManager 인스턴스 생성
login_manager = LoginManager()
# Flask 애플리케이션과 LoginManager 인스턴스 연결
login_manager.init_app(app)
# 로그인 페이지의 뷰 함수 이름을 설정합니다.
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    # 각 컬럼 정의
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(128))
    
    def __repr__(self):
        return f'<User {self.username}>'

with app.app_context():
    db.create_all()

# 사용자 로드 함수에 데코레이터 적용
@login_manager.user_loader
def load_user(user_id):
    # 주어진 user_id로 사용자 조회 후 반환
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return 'Home Page'

@app.route('/protected')
@login_required
def protected():
    return f'Logged in as {current_user.username}'

@app.route('/login', method=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('protected'))
    
    # 로그인 폼 HTML 반환
    return '''
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''
    
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/create_test_user')
def create_test_user():
    test_user = User(username='testuser', email='test@example.com',
                    password='testpassword')
    db.session.add(test_user)
    db.session.commit()
    return 'Test user created'