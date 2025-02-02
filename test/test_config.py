from damona.config import Config, get_damona_commands
import shutil


def test_config():
    c = Config()
    c.read()


def test_config_creation():  # this is for the local cases

    c = Config(name="damona__testing__")
    if str(c.user_config_dir).endswith("damona__testing__"):
        shutil.rmtree(str(c.user_config_dir))


def test_get_commands():
    get_damona_commands()
