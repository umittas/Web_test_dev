#CONSTANTS
#Url, kullanıcı adı, şifre ve diğer input bilgileri bu sayfadan değiştirilir.
import inspect
URL         = "https://opensource-demo.orangehrmlive.com/"
USERNAME    = "Admin"
PASSWORD    = "admin123"

URL2        = "https://opensource-demo.orangehrmlive.com/"
USERNAME2   = "Admin"
PASSWORD2   = "admin123"

def whoami():
    return inspect.stack()[1][3]