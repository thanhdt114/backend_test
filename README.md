# Instructions for running this project

**NOTE 1:**
Replace Python3 with Python if your computer has Python installed

**NOTE 2:**
Replace the values of variables in the .env file with values to connect to mysql on your computer

**NOTE 3:**
Create 1 database with test name if your mysql is not there 

1. Create python environment
```bash
python3 -m venv .venv
```

2. Activate python environment.\

- For linux
```bash
source .venv/bin/activate 
```
- For windowns
```bash
.venv\Scripts\activate
```
The cursor in the terminal should look like this (with .venv)
```cmd
(.venv) johnny@johnny-Inspiron-5502:/media/johnny/Data/Code/cloud_service/be_test$
```

3. Run project
```bash
python3 main.py
```

# API User Guide
1. Test api
- Link: `http://localhost:5000`
- Respone: 
```console
BE Hello
```

2. Create data api
- Link: `http://localhost:5000/api/account/create`
- Respone: 
```console
Account added
```

3. Get all data api
- Link: `http://localhost:5000/api/account/all`
- Respone: 
```console
[
  {
    "id": 1,
    "name": "Nguyen Van A"
  }
]
```

**NOTE:**
Every time you call create api, all api will have 1 more data with incremental id