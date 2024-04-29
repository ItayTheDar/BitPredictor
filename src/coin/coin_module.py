from nest.core import Module
from .coin_controller import CoinController
from .coin_service import CoinService


@Module(controllers=[CoinController], providers=[CoinService], imports=[])
class CoinModule:
    pass
