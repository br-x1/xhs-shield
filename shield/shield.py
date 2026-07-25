from urllib.parse         import urlparse, parse_qs
from .algorythm.xyass_aes import XyassAES
from .algorythm.sub_XXXXX import sub_XXXXX
from .algorythm.xyass_md5 import xyass_md5



class Shield:
    def __init__(self, device_id: str, main_hmac: str):
        self.a1 = 0x00000001
        self.a2 = b"xxxxxxx" # version code
        self.a3 = 0xECFAAF01 # app_id
        self.a4 = 0x04
        self.a7 = 16

        self.device_id = device_id
        self.main_hmac = main_hmac

        self.aes      = XyassAES(self.device_id)
        self.hmac_key = self.aes.encrypt_main_hmac(self.main_hmac)
    
    def parse_url(self, url: str) -> tuple[str, str]:
        parsed      = urlparse(url)
        endpoint    = "/" + (parsed.path or "").lstrip("/")
        querystring = parsed.query

        return endpoint, querystring

    def get_shield(self, url: str, headers: dict, data: str="") -> str:
        return
