from website import app
import website.config as config
from flask_session import Session

sess = Session()

if __name__ == '__main__':
    app.secret_key = config.APP_SECRET_KEY
    app.config['SESSION_TYPE'] = 'filesystem'
    sess.init_app(app)
    app.debug = config.app_debug
    app.run(host=config.app_run_host, port=config.app_run_port)