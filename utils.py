import json 
import os
from bs4 import BeautifulSoup



def push_entry(tool:dict, collection:'pymongo.collection.Collection', log:dict):
    '''Push tool to collection.

    tool: dictionary. Must have at least an '@id' key.
    collection: collection where the tool will be pushed.
    log : {'errors':[], 'n_ok':0, 'n_err':0, 'n_total':len(insts)}
    '''
    # date objects cause trouble and are prescindable
    if 'about' in tool.keys():
            tool['about'].pop('date', None)

    log['names'].append(tool['name'])
    
    try:
        updateResult = collection.update_many({'@id':tool['@id']}, { '$set': tool }, upsert=True)
    except Exception as e:
        log['errors'].append({'file':tool,'error':e})
        print(f"❌ An exception occurred while processing {tool['name']}: {e}")
        return(log)
    else:
        log['n_ok'] += 1
    finally:
        return(log)


def save_entry(tool, output_file, log):
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
                print('Saving to file: ' + output_file)
                data = json.load(outfile)
                data.append(tool)
                # Sets file's current position at offset.
                outfile.seek(0)
                json.dump(data, outfile)

    except Exception as e:
        log['errors'].append({'file':tool['name'],'error':e})
        return(log)

    else:
        log['n_ok'] += 1
    finally:
        return(log)

def connect_db():
    '''Connect to MongoDB and return the database and collection objects.

    '''
    from pymongo import MongoClient
    ALAMBIQUE = os.getenv('ALAMBIQUE', 'alambique')
    HOST = os.getenv('HOST', 'localhost')
    PORT = os.getenv('PORT', 27017)
    DB = os.getenv('DB', 'observatory')
    
    client = MongoClient(HOST, int(PORT))
    alambique = client[DB][ALAMBIQUE]

    return alambique

def print_progress(log):
    # Keeping track of progress
    print(f"{len(log['names'])} recipes processes --- {log['n_ok']} parsed and loaded sucessfully --- {len(log['errors'])} raised an exception", end="\r", flush=True)
    return

def print_final_report(log):
    print(f"\n----- Importation finished -----\nNumber of packages in Bioconda {log['n_ok']}")
    print('Exceptions:')
    if len(log['errors']) != 0:
        for e in log['errors']:
            print(f"File {e['file']} raised the exception {e['error']}")  
    else:
        print('--- No exceptions were raised ---')
    
    return

