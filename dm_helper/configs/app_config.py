def add_config_section_to_app(app, config_section):
    for key, value in config_section.items():
        app.config[key] = value
