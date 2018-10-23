"""
Use this script to create JSON-Line description files that can be used to
train deep-speech models through this library.
This works with data directories that are organized like TTS-Portuguese Corpus.
"""

import argparse
import json
import wave
import os
from utils import calc_feat_dim, spectrogram_from_file, text_to_int_sequence,text_normalize
def convert(desc_file,new_file):
    with open(new_file,'w') as file:
        with open(desc_file) as json_line_file:
            for line_num, json_line in enumerate(json_line_file):
                try:
                    
                    spec = json_line.replace('\n','').split('==')
                    if spec[0] == 'filename':
                        continue
                    speaker_path = desc_file.replace(desc_file.split('/')[-1],'')
                    audio_file = os.path.join(os.path.abspath(speaker_path), spec[0])
                    audio = wave.open(audio_file)
                    duration = float(audio.getnframes()) / audio.getframerate()
                    audio.close()
                    textlen= len(text_to_int_sequence(text_normalize(spec[1])))
                    speclen= len(spectrogram_from_file(audio_file))
                    if textlen >  speclen :
                            print('label maior que feats')
                            print('remove line: ',spec[1],textlen,speclen)
                            continue
                    if textlen < 2:
                        print('label pequeno')
                        print('remove line: ',spec[1],textlen,speclen)
                        continue

                    if len(spectrogram_from_file(audio_file)) < 5:
                        print('label pequeno')
                        print('remove line: ',spec[1],textlen,speclen)
                        continue
                    line = json.dumps({'key': audio_file, 'duration': duration,
                              'text': spec[1]},ensure_ascii=False)
                    file.write(line + '\n')
                except Exception as e:
                    # Change to (KeyError, ValueError) or
                    # (KeyError,json.decoder.JSONDecodeError), depending on
                    # json module version
                    print("Erro: ",e)
                    continue




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('desc_file', type=str,
                        help='input')
    parser.add_argument('new_file', type=str,
                        help='output')
    args = parser.parse_args()
    convert(args.desc_file,args.new_file)

