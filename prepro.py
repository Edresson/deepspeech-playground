import os
import json
import argparse
from pydub import AudioSegment
from hyperparams import Hyperparams as hp
from datasets.pt.PETRUS.g2p.g2p import G2PTranscriber
def match_target_amplitude(sound, target_dBFS):
    change_in_dBFS = target_dBFS - sound.dBFS
    return sound.apply_gain(change_in_dBFS)

def prepro(desc_file):
    """
    removes noise and normalizes audio volume
    """
    keys =[]
    durations =[]
    labels = []
    with open(desc_file) as json_line_file:
                for json_line in json_line_file:7
                    
                    try:
                        spec = json.loads(json_line)

                        if hp.phoneme:  
                            if hp.language='pt':   
                                keys.append(spec['key'])
                                durations.append(spec['duration'])
                                words = spec['text'].strip().lower().split(' ')
                                transcrito = [] 
                                for word in words:
                                    # Initialize g2p transcriber
                                    g2p = G2PTranscriber(word, algorithm='silva')
                                    # Write file
                                    #print(g2p.transcriber())
                                    transcrito.append(g2p.transcriber())
                                labels.append(" ".join(transcrito))
                            
                        os.system("sox "+spec['key']+" -r 48k "+spec['key'])
                        os.system("sox "+spec['key']+" --bits 16 --encoding signed-integer --endian little INPUT.raw")
                        os.system("./rnnoise/examples/rnnoise_demo INPUT.raw  out.raw")
                        os.system("sox  -e signed-integer -b 16 -r 48000  out.raw "+spec['key'])
                        sound = AudioSegment.from_file(spec['key'], "wav")
                        normalized_sound = match_target_amplitude(sound, -20.0)
                        normalized_sound.export(spec['key'], format="wav")

                        if hp.phoneme:
                            with open(output_file, 'w') as out_file:
                                for i in range(len(keys)):
                                    line = json.dumps({'key': keys[i], 'duration': durations[i],
                                                    'text': labels[i]},ensure_ascii=False)
                                    out_file.write(line + '\n')

                    except Exception as e:
                        print(e)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('train_desc_json', type=str,default=None)
    parser.add_argument('test_desc_json', type=str,default=None)
    args = parser.parse_args()
    if args.train_desc_json is not None:
        prepro(args.train_desc_json)
    if args.test_desc_json is not None:
        prepro(args.test_desc_json)
