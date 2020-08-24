import os
import requests

cwd = os.getcwd()
def download_file(url):
    #cwd = os.getcwd()
    print(cwd)
    local_filename = url.split('/')[-1]
    path=cwd+ r'/data/'+local_filename
    print("Archieve is being download at",path)
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                f.write(chunk)
    return local_filename
download_file("https://dumps.wikimedia.org/wikidatawiki/entities/latest-all.json.gz")
#os.rename(cwd+r'/data/latest-all.json.gz',cwd+'/data/wikidata.gz')
