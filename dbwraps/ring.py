from keyring import set_password, get_password
from dataclasses import dataclass
from dill import dumps, loads

# @dead-code-ignore
class Ring:
    """Wrapper for keyring"""
    
    def __init__(self, name:str) -> None:

        self.rname = name
        self.name: str = 'philh.myftp.biz/' + dumps(name)

    def Key(self, name:str) -> 'Key':
        """Get Key in Ring by name"""

        return Key(ring=self, name=name)
    
    __getitem__ = Key

@dataclass
class Key[T]:
    """Wrapper for keyring"""
    
    ring: Ring
    name: str

    def save(self, value:T) -> None:
        """Save value to Key"""
        set_password(
            service_name = self.ring.name,
            username = dumps(self.name),
            password = dumps(value)            
        )
        
    def read(self) -> None | T:
        """Read value from key"""

        rvalue: str | None = get_password(
            service_name = self.ring.name,
            username = dumps(self.name)
        )
        
        try:
            return loads(rvalue)
        except TypeError:
            return None
        
