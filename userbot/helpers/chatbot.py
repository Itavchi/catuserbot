try:
    import randomstuff
except ModuleNotFoundError:
    from .utils.extdl import install_pip
    install_pip(randomstuff.py)
    
from ..Config import Config

rs_client = randomstuff.AsyncClient(api_key=Config.RANDOM_STUFF_API_KEY, version="4")
