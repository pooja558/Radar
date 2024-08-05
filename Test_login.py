from Framework_Login.Login import login
from Framework_Login.config import config
from Framework_Login.Target import Target
from Framework_Login.Scan import Scan
from Framework_Login.Dashboard import Dashboard
from Framework_Login.Admin import Admin
from LoginVars import LoginVar
#login()
config()
Target()
Scan()
Dashboard()
Admin()

# login(LoginVar.username, LoginVar.password, LoginVar.tenancy_name)