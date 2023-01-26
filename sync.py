import os as os
from datetime import datetime

timestamp = datetime.today()
cmd = "git add . && git commit -m \"{}\" && git push".format(timestamp)
os.system(cmd)
