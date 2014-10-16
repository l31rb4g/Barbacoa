import json


def read_config(config_file):
    with open(config_file, 'r') as f:
        content = f.read()
    if content:
        content = json.loads(content)
        return content

    return False


def send_callback(view, content):
    view.execute_script('$_BBQ.execute_callback("' + content + '")')