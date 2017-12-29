from website import app
import website.config as config


if __name__ == '__main__':
    app.secret_key = config.APP_SECRET_KEY
    app.debug = config.app_debug
    app.run(host=config.app_run_host, port=config.app_run_port)