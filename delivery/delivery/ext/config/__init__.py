def init_app(app):
    app.config["SECRET_KEY"] = "engelsink666"
    app.config["ENV"] = "development"
    app.config["DEBUG"] = True

    if app.debug:
        app.config["DEBUG_TB_TEMPLATE_EDITOR_ENABLED"] = True
        app.config["DEBUG_TB_PROFILER_ENABLED"] = True