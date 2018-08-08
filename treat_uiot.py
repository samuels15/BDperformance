import json
import csv
from datetime import datetime
import time

def importing(file):
    with open(file + ".json") as json_data:
        d = json.load(json_data)
        return d["docs"]

def filtering(registers):       # funcao feita para filtragem dos dados em data
    try:
        i=0;
        max = len(registers);
        while (i<max):
            doc = registers[i];
            # Formatando os tempos de epoch pra mm/dd/aa HH:MM:SS
            doc["clientTimef"] = datetime.fromtimestamp(doc["clientTime"]).\
                strftime('%Y-%m-%d %H:%M:%S')
            doc["serverTimef"] = datetime.fromtimestamp(doc["serverTime"]).\
                strftime('%Y-%m-%d %H:%M:%S')

            # Retirando os registros que tem mais de um parametro
            # E tratando os registros que so tem um parametro
            if ((len(doc["parameters"])==1) and (len(doc["values"])==1)):
                mac = 'undefined'
                param = doc["parameters"][0]
                value = doc["values"][0]
                try:        # tratando valores nao numericos
                    value = float(value);
                except ValueError:
                    value = 0;
                commaindex = param.rfind(':')
                if commaindex >=0:
                    mac = param[:commaindex].upper()
                    param = param[commaindex+1:].lower()
                doc['parameters'] = param;
                doc['mac'] = mac;
                doc['values'] = str(value);     # str() evita erros futuros.
                try:
                    del doc['clientId']
                    del doc['serviceId']
                    del doc['tags']
                    #del doc['serverTime']
                    #del doc['clientTime']
                except:
                    # print('Inexistent tag');
                    pass;
                registers[i]=doc;
            else:
                # print ("Removendo parametro...");
                # print (doc['clientTimef'] + '\t' + str(len(doc['values'])));
                registers.remove(doc)
                i-=1;
                max-=1;
            i+=1;
        # Testando tamanhos das listas dos valores:
        with open('data/uiotf.json', 'w') as outfile:
            outfile.write(json.dumps(registers, sort_keys=True, indent=4))
        # Exportando json para csv:

        with open('data/uiot.csv', 'wb') as outfile:
            # outfile.write("clientTimef;parameters;serverTime;clientTime;mac;values;serverTimef");
            for item in registers:
                w = csv.DictWriter(outfile, item.keys(), delimiter=';', quotechar='"');
                w.writerow(item);

        return registers

    except:
        print("Erro na filtragem")

# reg_dict = filtering(importing('../data500'))
filtering (importing('data/uiot'));
