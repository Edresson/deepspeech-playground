"""
Use this script to create JSON-Line description files that can be used to
train deep-speech models through this library.
This works with data directories that are organized like VoxForge. 
VoxForge (only portuguese brazilian audio files) dataset reader and parser

    More about the dataset: http://www.voxforge.org/
    
"""

from __future__ import absolute_import, division, print_function

import argparse
import json
import os
import wave


def main(data_directory, output_file):
    labels = []
    durations = []
    keys = []
    IGNORED_LIST = ['Marcelo-20131106-iqc',
                    'anonymous-20140619-wcy',
                    'ThiagoCastro-20131129-qpn',
                    'anonymous-20131016-uzv']

    for speaker_path in os.listdir(data_directory):

        if speaker_path in IGNORED_LIST:
                continue

        root_path = os.path.join(os.path.abspath(data_directory),speaker_path)
        
        if not os.path.isdir(os.path.join(root_path)):
                continue

        labels_file = os.path.join(root_path, 'etc', 'PROMPTS')
        if not os.path.exists(labels_file):
                labels_file = os.path.join(root_path, 'PROMPTS')

        for line in open(labels_file):
                split = line.strip().split()
                file_id = split[0].split('/')[-1]
                label = ' '.join(split[1:]).lower()
                audio_file = os.path.join(root_path, 'wav', file_id) + '.wav'
                if not os.path.exists(audio_file):
                    audio_file = os.path.join(root_path, file_id) + '.wav'
                try:
                    audio = wave.open(audio_file)
                except IOError:
                    print('File %s not found' % audio_file)
                    continue
                
                duration = float(audio.getnframes()) / audio.getframerate()
                audio.close()
                keys.append(audio_file)
                durations.append(duration)
                labels.append(label)
    with open(output_file, 'w') as out_file:
        for i in range(len(keys)):
            line = json.dumps({'key': keys[i], 'duration': durations[i],
                              'text': labels[i]},ensure_ascii=False)
            out_file.write(line + '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('data_directory', type=str,
                        help='Path to data directory')
    parser.add_argument('output_file', type=str,
                        help='Path to output file')
    args = parser.parse_args()
    main(args.data_directory, args.output_file)
