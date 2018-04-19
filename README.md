# flask-blueprint-quickstart

Flask starter kit for larger apps

---

Read the accompanying blog post here https://r00m.wordpress.com/2018/04/19/directory-structure-for-a-flask-project

## How to use this

You can start by cloning the latest version:

```shell
$ git clone https://github.com/r00m/flask-blueprint-quickstart my-project
$ cd my-project
```

When that's done, install project dependencies:

```shell
$ pip install -r requirements.txt
```

Now you can start the app:

```shell
$ FLASK_APP=main.py FLASK_DEBUG=1 flask run
```

And you're ready to start developing! :sparkles:

## Project structure

```shell
$ tree
.
├── expert_disco        # global stuff like settings, utils, etc
│   ├── __init__.py     # bootstrap file. initialise your extensions here
│   └── settings.py
├── main.py             # entry point
└── requirements.txt
```

## License

MIT
