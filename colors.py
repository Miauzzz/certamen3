#Clase con colores
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CURSIVE = '\033[3m'
    BGGREEN = '\033[102m'
    BGRED = '\033[101m'
    BGBLUE = '\033[104m'
    BGYELLOW = '\033[103m'
    BGCYAN = '\033[106m'
    BGPINK= '\033[105m'
    BGWHITE = '\033[107m'
    BGBLACK = '\033[100m'


print(bcolors.BGBLACK+"Hola mundo"+bcolors.ENDC+" Hola mundo")