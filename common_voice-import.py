import argparse
import  json
def convert(desc_file,new_file):
    with open(new_file,'w') as file:
        with open(desc_file) as json_line_file:
            for line_num, json_line in enumerate(json_line_file):
                try:
                    
                    spec = json_line.replace('\n','').split(',')
                    #print(json_line,spec)
                    if spec[0] == 'filename':
                        continue
                    line = json.dumps({'key': spec[0], 'duration': float(spec[1])*10000,
                              'text': spec[2]})
                    file.write(line + '\n')
                except Exception as e:
                    # Change to (KeyError, ValueError) or
                    # (KeyError,json.decoder.JSONDecodeError), depending on
                    # json module version
                    print('Except')




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('desc_file', type=str,
                        help='input')
    parser.add_argument('new_file', type=str,
                        help='output')
    args = parser.parse_args()
    convert(desc_file,new_file)

