try:
	from config.config import __token__, __prefix__
except ImportError:
	import os
	
from config.games import __games__, __gamesTimer__	
from config.cogs import __cogs__	
from config.blacklist import __blacklist__
