from polls import blueprint


@blueprint.route('/')
def index():
    return "Hello World!"
