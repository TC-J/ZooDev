from platformdirs import PlatformDirs
import tempfile
from pathlib import Path
import getpass
import socket
import platform
from plumbum import local


class Platform:
    def __init__(
        self,
        base: Path | str,
	):
		self.user = getpass.getuser()
		self.hostname = socket.gethostname()
        self.os = platform.system()
		self.arch = platform.architecture()
        self.base = Path(base)
        self.temp_dir = Path(tempfile.gettempdir())
		self.user_dirs = PlatformDirs("Zoo", self.user)
    	self.network = {
			"devs": [],
        	"addrs": [],
        	"routes": []
		}
    

class Zoo:
	def __init__(
        self,
        base = "."
    ):        
		self.base = Platform(base)        

	def _get_binaries(self):
        pass
		
