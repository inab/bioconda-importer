import json 
import os
import logging
from bs4 import BeautifulSoup



def push_entry(tool:dict, collection:'pymongo.collection.Collection', logger):

    '''Push tool to collection.

    tool: dictionary. Must have at least an '@id' key.
    collection: collection where the tool will be pushed.
    log : {'errors':[], 'n_ok':0, 'n_err':0, 'n_total':len(insts)}
    '''
    # date objects cause trouble and are prescindable
    if 'about' in tool.keys():
            tool['about'].pop('date', None)
    
    try:
        updateResult = collection.update_many({'@id':tool['@id']}, { '$set': tool }, upsert=True)
    except Exception as e:
        logger.warning(f"error with {tool['name']} - pushing_to_db")
        logger.warning(e)
    else:
        logger.info(f"pushed_to_db_ok - {tool['name']}")
    finally:
        return

def save_entry(tool, output_file):
    '''Save tool to file.

    tool: dictionary. Must have at least an '@id' key.
    output_file: file where the tool will be saved.
    log : {'errors':[], 'n_ok':0, 'n_err':0, 'n_total':len(insts)}
    '''
    # date objects cause trouble and are prescindable

    if 'about' in tool.keys():
            tool['about'].pop('date', None)
    try:
        if os.path.isfile(output_file) is False:
            with open(output_file, 'w') as f:
                json.dump([tool], f)
        else:
            with open(output_file, 'r+') as outfile:
                logging.info('Saving to file: ' + output_file)
                data = json.load(outfile)
                data.append(tool)
                # Sets file's current position at offset.
                outfile.seek(0)
                json.dump(data, outfile)

    except Exception as e:
        logging.warning(f"error with {tool['name']} - saving_to_file")
        logging.warning(e)
        return

    else:
        logging.info(f"pushed_to_db_ok - {tool['name']}")
    finally:
        return

def connect_db():
    '''Connect to MongoDB and return the database and collection objects.

    '''
    from pymongo import MongoClient
    
    # variables come from .env file
    mongoHost = os.getenv('HOST', default='localhost')
    mongoPort = os.getenv('PORT', default='27017')
    mongoUser = os.getenv('USER')
    mongoPass = os.getenv('PWD')
    mongoAuthSrc = os.getenv('AUTH_SRC', default='admin')
    mongoDb = os.getenv('DB', default='oeb-research-software')
    mongoAlambique = os.getenv('ALAMBIQUE', default='alambique')

    # Connect to MongoDB
    mongoClient = MongoClient(
        host=mongoHost,
        port=int(mongoPort),
        username=mongoUser,
        password=mongoPass,
        authSource=mongoAuthSrc,
    )
    db = mongoClient[mongoDb]
    alambique = db[mongoAlambique]

    return alambique
    
    client = MongoClient(HOST, int(PORT))
    alambique = client[DB][ALAMBIQUE]

    return alambique

