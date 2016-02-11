from project import app, conf

if __name__ == '__main__':
    app.run(host=conf.SERVER_CONF['all'], port=conf.SERVER_CONF['listen_port'], debug=conf.DEBUG)
