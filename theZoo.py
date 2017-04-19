#! / Usr / bin / env python
'''
     # Malware DB - a mais incrível base de dados gratuita de malware no ar
     # Copyright (C) 2014, Yuval Nativ, Lahad Ludar, 5Fingers

     # Este programa é software livre: você pode redistribuí-lo e / ou modificar
     # De acordo com os termos da Licença Pública Geral GNU publicada por
     # A Free Software Foundation, quer a versão 3 da Licença, ou
     # (À sua escolha) qualquer versão posterior.

     # Este programa é distribuído na esperança de que ele será útil,
     # Mas SEM QUALQUER GARANTIA; Sem a garantia implícita de
     # COMERCIABILIDADE OU ADEQUAÇÃO A UM PROPÓSITO ESPECÍFICO. Veja o
     # GNU General Public License para mais detalhes.

     # Você deve ter recebido uma cópia da GNU General Public License
     # Juntamente com este programa. Caso contrário, consulte <http://www.gnu.org/licenses/>.
'''
import sys
import os
from optparse import OptionParser
from imports.update_handler import Updater
from imports import manysearches
from imports import muchmuchstrings
from imports.eula_handler import EULA
from imports.globals import vars
from imports.terminal_handler import Controller
from imports import db_handler

__version__ = "0.6.0 Moat"
__codename__ = "Moat"
__appname__ = "theZoo"
__authors__ = ["Yuval Nativ", "Shahak Shalev", "Lahad Ludar", "5Fingers"]
__licensev__ = "GPL v3.0"
__maintainer = "Yuval Nativ & Shahak Shalev"
__status__ = "Beta"


def main():

    # Muitas importações :)
    updateHandler = Updater
    eulaHandler = EULA()
    bannerHandler = muchmuchstrings.banners()
    db = db_handler.DBHandler()
    terminalHandler = Controller()

    def filter_array(array, colum, value):
        ret_array = [row for row in array if value in row[colum]]
        return ret_array

    def getArgvs():
        parser = OptionParser()
        parser = OptionParser()
        parser.add_option("-f", "--filter", dest="mal_filter", default=[],
                          help="Filter the malwares.", action="append")
        parser.add_option("-u", "--update", dest="update_bol", default=0,
                          help="Updates the DB of theZoo.", action="store_true")
        parser.add_option("-v", "--version", dest="ver_bol", default=0,
                          help="Shows version and licensing information.", action="store_true")
        parser.add_option("-w", "--license", dest="license_bol", default=0,
                          help="Prints the GPLv3 license information.", action="store_true")
        (options, args) = parser.parse_args()
        return options

    # Aqui realmente começa Main ()
    arguments = getArgvs()

    # Verificando o Contrato EULA
    a = eulaHandler.check_eula_file()
    if a == 0:
        eulaHandler.prompt_eula()

    # Get arguments

    # Verificar se o flag de atualização está ativado
    if arguments.update_bol == 1:
        a = Updater()
        with open('conf/db.ver', 'r') as f:
            a.update_db(f.readline())
        sys.exit(1)

    # Verifique se o sinalizador de versão está ativado
    if arguments.ver_bol == 1:
        print(vars.maldb_banner)
        sys.exit(1)

    # Verifique se o sinalizador de licença está ativado
    if arguments.license_bol == 1:
        bannerHandler.print_license()
        sys.exit(1)

    if len(arguments.mal_filter) > 0:
        manySearch = manysearches.MuchSearch()
        print(vars.maldb_banner)
        manySearch.sort(arguments.mal_filter)
        sys.exit(1)

    #Inicie a execução normal. Nenhum argumento dado.
    os.system('cls' if os.name == 'nt' else 'clear')
    print(vars.maldb_banner)
    while 1:
        terminalHandler.MainMenu()
    sys.exit(1)


if __name__ == "__main__":
    main()
