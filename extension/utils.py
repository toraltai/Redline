from flask_sqlalchemy import SQLAlchemy
from flask_ipban import IpBan


ip_ban = IpBan(ban_seconds=200)
db=SQLAlchemy()