def secrets():
    return {"host": "XXXX", # Insert correct values

            "port": XXXX, # Insert correct values

            "database": "XXXX", # Insert correct values

            "user": "XXXX", # Insert correct values

            "pass": "XXXX"} # Insert correct values


def elastic() :
    return {"host": "www.pg4e.com",
            "prefix" : "elasticsearch",# Insert correct values

            "port": 443, # Insert correct values

            "scheme": "https", # Insert correct values

            "user": "XXXX", # Insert correct values

            "pass": "XXXX"} # Insert correct values

def readonly():
    return {"host": "XXXX", # Insert correct values

            "port": XXXX,
            "database": "readonly",
            "user": "readonly",
            "pass": "readonly_password"}

# Return a psycopg2 connection string

def psycopg2(secrets) :
     return ('dbname='+secrets['database']+' user='+secrets['user']+
        ' password='+secrets['pass']+' host='+secrets['host']+
        ' port='+str(secrets['port']))

# Return an SQLAlchemy string

def alchemy(secrets) :
    return ('postgresql://'+secrets['user']+':'+secrets['pass']+'@'+secrets['host']+
        ':'+str(secrets['port'])+'/'+secrets['database'])
