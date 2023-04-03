from configparser import ConfigParser

# Pra poder chamar config de qualquer lugar
import os
dirname = os.path.dirname(__file__)
db_ini = os.path.join(dirname, 'db.ini')
#


def config(filename=db_ini, section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(
            'Section {0} not found in the {1} file'.format(section, filename))

    return db
