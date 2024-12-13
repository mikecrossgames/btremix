init python:
    redux_config = None

    def redux_conf(key_name, default = False):
        global redux_config
        if redux_config is None:
            redux_config = get_redux_config()
        if key_name in redux_config:
            return redux_config[key_name]
        return default
