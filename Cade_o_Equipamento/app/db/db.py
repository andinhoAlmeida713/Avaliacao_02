from sqlmodel import create_engine, Session
from sshtunnel import SSHTunnelForwarder
from config.Config import settings
from dataclasses import dataclass
import urllib.parse

@dataclass
class Database:
    _server: SSHTunnelForwarder | None = None
    _engine = None

    def __post_init__(self):
        self.start_tunnel()

    def start_tunnel(self) -> None:
        params = self._build_ssh_params()
        
        self._server = SSHTunnelForwarder(
            params["ssh_host"],
            ssh_username=params["ssh_username"],
            ssh_password=params.get("ssh_password"),
            ssh_pkey=params.get("ssh_pkey"),
            remote_bind_address=params["remote_bind_address"]
        )
        self._server.start()
        
        encoded_password = urllib.parse.quote_plus(settings.db_password)
        url = (
            f"mysql+pymysql://{settings.db_user}:{encoded_password}"
            f"@127.0.0.1:{self._server.local_bind_port}/{settings.db_name}"
            f"?charset=utf8mb4"
        )

        self._engine = create_engine(
            url,                      
            echo=True,                
            pool_pre_ping=True,       
            pool_recycle=1800,        
            pool_size=5,              
        )

    def _build_ssh_params(self) -> dict:
        params = {
            "ssh_host": (settings.ssh_host, settings.ssh_port),
            "ssh_username": settings.ssh_user,
            "remote_bind_address": (settings.db_host, settings.db_port),
        }
        if settings.ssh_key_path:
            params["ssh_pkey"] = settings.ssh_key_path
        elif settings.ssh_password:
            params["ssh_password"] = settings.ssh_password
        else:
            raise ValueError("Defina SSH_KEY_PATH ou SSH_PASSWORD no .env")
        return params

    def stop_tunnel(self) -> None:
        if self._engine:
            self._engine.dispose()
        if self._server and self._server.is_active:
            self._server.stop()

    def get_db(self):
        with Session(self._engine) as session:
            yield session
