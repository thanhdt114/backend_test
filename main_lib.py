try:
    from flask import Flask, jsonify, Response
except ImportError:
    import pip
    pip.main(['install', 'flask'])
    from flask import Flask, jsonify, Response
    
try:
    from flask_cors import CORS
except ImportError:
    import pip
    pip.main(['install', 'flask_cors'])
    from flask_cors import CORS

try:
    import mysql.connector
except ImportError:
    import pip
    pip.main(['install', 'mysql-connector-python'])
    import mysql.connector

try:
    import os
except ImportError:
    import pip
    pip.main(['install', 'os'])
    import os

try:
    from dotenv import load_dotenv
except ImportError:
    import pip
    pip.main(['install', 'python-dotenv'])
    from dotenv import load_dotenv