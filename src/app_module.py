from nest.core import PyNestFactory, Module
from src.config import config
from src.app_controller import AppController
from src.app_service import AppService
from src.coin.coin_module import CoinModule


@Module(imports=[CoinModule], controllers=[AppController], providers=[AppService])
class AppModule:
    pass


app = PyNestFactory.create(
    AppModule,
    description="This is my Async PyNest app.",
    title="PyNest Application",
    version="1.0.0",
    debug=True,
)

http_server = app.get_server()


@http_server.on_event("startup")
async def startup():
    await config.create_all()
