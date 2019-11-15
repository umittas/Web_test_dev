#CONSTANTS
#Url, kullanıcı adı, şifre ve diğer input bilgileri bu sayfadan değiştirilir.
import inspect
URL         = "https://am1.solvay.com:1443/auth/console"
USERNAME    = "Amadmin"
PASSWORD    = "Password123"

URL2        = "https://am2.solvay.com:1443/auth/console"
USERNAME2    = "Amadmin"
PASSWORD2    = "Password123"

def whoami():
    return inspect.stack()[1][3]