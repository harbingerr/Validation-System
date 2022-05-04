# -*- coding: utf-8 -*-

# import modulov 
from flask import Flask
from flask_restful import Api
from datetime import timedelta

# import objektov typu Resource sluziacich na spracovanie ziadosti
from validsysattacker import (SystemInit,
                              FlagValidation,
                              FlagValidation2)


# Inicializacia Flask aplikacie a JWT tokenizacie (Nastavenie tajneho kluca, povolenie blacklistu, nastavenie kontroly tokenov, nastavenie expiracie access tokenu)
app = Flask(__name__)

api = Api(app)



# pridanie zdrojov z externych suborov a nastavenie ciest(routes)
api.add_resource(SystemInit,'/attacker')
api.add_resource(FlagValidation,'/attacker/validate')
api.add_resource(FlagValidation2,'/attacker/validate2')

# spustenie aplikacie s povolenim vsetkych komunikacii na port 4999, nastavenie paralelneho spracovania ziadosti
if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0', port=4999, threaded= True)
    
