from platformdirs import PlatformDirs
import tempfile
from pathlib import Path
import getpass
import socket
import platform
from plumbum import local
from typing import Protocol, List, Any
import ctypes
from ctypes import (
    c_void_p,
    c_ulonglong,
    c_longlong,
	c_ssize_t, 
	c_size_t, 
	c_ushort, 
	c_ubyte,
    c_char_p,
    POINTER,
    Structure
)

class PackedWord(Structure):
    _pack_ = 1 # forces smallest alignment possible: 1 byte
    _fields_ = [("value", c_ushort)]

type unpadded_uword_ptr = POINTER(OddlyAlignedWord)
type padded_uword_ptr = POI


# a computer hardware architecture memory reference.
type HWArchMemRef = c_uintptr
type HWArchValReg = c_ssize_t | c_size_t

# four letter hexcode
type VID = c_ushort_t
type VendorID = VID
# four letter hexcode
type PID = c_ushort_t
type ProductID = PID
# just needs to be unique for the product and company IDs
# so if two serial numbers match for different companies
# or different products - that is okay with serial numbers.
type SID = Any
type SerialNumber = SID
# 16 bytes exactly (128 bits) must be unique even with
# different VIDs or PIDs - no where in the world should
# this number be repeated by another item/device.
type UUID = c_ubyte * 16
type UniversallyUniqueID = UUID
# ^ principally the exact same concept (Microsoft calls UUIDs GUIDs, roughly in principal)
type GUID = c_ubyte * 16
type GloballyUniqueID = GUID
# unique only onboard our (largely private) system; could be a name as the id like "tyler".
type DID = c_void_p | POINTER(c_ubyte) | c_char_p 
type SystemDeviceID = DID
    

class HardwareDevice(Protocol):
    @property
    def vendor_id(self) -> VID:
        ...
    
    
    @id.setter
	def vendor_id(self, fresh_vid: VID) -> StatusCode:
        ...
    

	@property
    def system_device_id(self) -> str | None:
        ...
    
	@system_device_id.setter
	def system_device_id(self, new_id: str|):

        

class HardwareSystem(Protocol):
    @property
    def abi_(self) -> str:
        ...
    
	@app_binary_iface.setter
    def app_binary_iface(self, architecture: str):
        ...
    
	@property
    def devices(self) -> List[str]:
        ...

class Platform(Protocol):
    def get_userid(self) -> str:
        ...
    
	def get_hostid(self) -> str:
        ...
    
	def get_archid(self):
        ...

class Platform:
    def __init__(
        self,
        base: Path | str,
	):
		self.user = getpass.getuser()
		self.hostname = socket.gethostname()
        self.os = platform.system()
		self.arch = platform.architecture()
        self.temp_dir = Path(tempfile.gettempdir())
		self.user_dirs = PlatformDirs("Zoo", self.user)
    	self.network = {
			"devs": [],
        	"addrs": [],
        	"routes": []
		}