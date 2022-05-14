# -*- coding: utf-8 -*-
"""
Created on Mon May  4 01:25:14 2020

Tento subor obsahuje zdroj(Resource) pre ziskavanie dat vo vyskumnej casti aplikacie 

Pre pracu s modulom pymongo a databazou Mongodb sme vyuzili nasledujuce stranky:
https://www.w3schools.com/python/python_mongodb_getstarted.asp
https://docs.mongodb.com/manual/reference/command/

Zaklady tvorenia API boli ziskane pomocou kurzu na adrese:
https://www.udemy.com/share/1013i4AEIbdlpWQHwB/

V pripade JWT tokenizacie sme vychadzali s prikladov a dokumentacie ku kniznici flask_jwt_extended:
https://flask-jwt-extended.readthedocs.io/en/stable/

v pripade modulu pyodbc sme vychadzali zo skusenosti s danym modulom

"""

#importovanie modulov
from flask_restful import Resource, request, reqparse
from datetime import datetime
from cryptography.fernet import Fernet
import json

class SystemInit(Resource):
    key = b'xxx'
    parser = reqparse.RequestParser()
    parser.add_argument('getscenarios', 
                        type=str,
                        required=True,
                        location='args')
    #########################################
    ## Method to load initial JSON file
    #########################################
    def get(cls):
        try:
            credentials = cls.parser.parse_args()
            key = credentials['getscenarios']
        except IOError:
            print("Wrong parameters")
        
        try:
            with open('scenarios.json', 'rb') as f:
                data = json.load(f)
            # Do something with the file
        except IOError:
            print("File not accessible")
        finally:
            f.close()

        for scenario in data["scenarios"]:
            for validation in scenario["validations"]:
                validation.pop("source")

        origokey = str.encode(key)
        s = json.dumps(data)
        res = s.encode('utf-8')
        f = Fernet(key)
        token = f.encrypt(res)
        toReturn =  { "data":""}
        toReturn['data'] = token.decode("utf-8")

        return(toReturn)

class FlagValidation2(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('output', 
                        type=str,
                        required=True,
                        location='args')
    parser.add_argument('scenario', 
                        type=int,
                        required=True,
                        location='args')
    parser.add_argument('validation',
                        type=int,
                        required=True,
                        location='args')
    
    #########################################
    ## Method to check the flag
    #########################################
    def get(cls):
        
        try:
            credentials = cls.parser.parse_args()
            output = credentials['output']
            validationId = credentials['validation']
            scenarioId = credentials['scenario']
        except IOError:
            print("Wrong parameters")
            
        try:
            with open('scenarios.json', 'r') as f:
                data = json.load(f)
        except IOError:
            print("File not accessible")
        finally:
            f.close()
        
        valid = 'False'
        changingJson = False

        for scenario in data["scenarios"]:
            if scenario["id"] == scenarioId :
                for validation in scenario["validations"]:
                    if validation["step"] == validationId:
                        output = output.strip()
                        if output == validation["output"]:
                            changingJson = True
                            print("Im HERE")
                            validation["completed"] = 'true'
                            data["score"] = data["score"] + validation["score"]
                            scenario["progress"] = scenario["progress"] + 1
                            valid = 'True'
                            
        if changingJson:                    
            try:
                with open('scenarios.json', 'w') as f:
                    json.dump(data,f)
            except IOError:
                print("File not accessible")
            finally:
                f.close() 
        
        toReturn = {'answer':valid} 
        
        return(toReturn)

class FlagValidation(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('scenario', 
                        type=int,
                        required=True,
                        location='args')
    parser.add_argument('validation',
                        type=int,
                        required=True,
                        location='args')
    parser.add_argument('flag',
                        type=str,
                        required=True,
                        location='args')
    #########################################
    ## Method to check the flag
    #########################################
    def get(cls):
        
        try:
            credentials = cls.parser.parse_args()
            scenarioId = credentials['scenario']
            validationId = credentials['validation']
            flag = credentials['flag']
            # Do something with the file
            print(flag)
        except IOError:
            print("Wrong parameters")
            
        try:
            with open('scenarios.json', 'r') as f:
                data = json.load(f)
            # Do something with the file
        except IOError:
            print("File not accessible")
        finally:
            f.close()
        
        valid = 'False'
        changingJson = False

        for scenario in data["scenarios"]:
            if scenario["id"] == scenarioId :
                for validation in scenario["validations"]:
                    if validation["step"] == validationId:
                        #check type, return success or script to run
                        if validation["type"]  == "flag":
                            if flag == validation["source"]:
                                changingJson = True
                                validation["completed"] = 'true'
                                scenario["progress"] = scenario["progress"] + 1
                                valid = 'True'
                        if validation["type"] == "internal command":
                            valid = validation["source"]
                        if validation["type"] == "none":
                            changingJson = True
                            validation["completed"] = 'true'
                            scenario["progress"] = scenario["progress"] + 1
                            valid = 'True'
        if changingJson:                    
            try:
                with open('scenarios.json', 'w') as f:
                    json.dump(data,f)
            except IOError:
                print("File not accessible")
            finally:
                f.close() 
        
        toReturn = {'answer':valid} 
        
        return(toReturn)
