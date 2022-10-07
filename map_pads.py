import ast
import json
import argparse

'''
Usage `python map_pads.py --config before.beatstep --map chromatic3.json --out output.beatstep`
'''

parser=argparse.ArgumentParser(
    description='''This script allows quick editing of note mappings for pads 1-16 using a mapping file.''',
    epilog="""....""")
parser.add_argument('--config', required=True, type=str, help='This is the .beatstep file exported from control centre.')
parser.add_argument('--map', type=str, default='chromatic3.json', help='json file that has pad 1-16 mapping to notes in C2 format')
parser.add_argument('--out', type=str, default='output.beatstep', help='merged .beatstep file name')
args=parser.parse_args()

config_file = args.config
map_file = args.map
out_file = args.out

## C1 => 36, C2 => 48
note_base = 36

## 1 => 112, 16 => 127, 0 => 111
pad_base = 111

## # => +1 , b => -1
notes = [ 'C', '', 'D', '', 'E', 'F', '', 'G', '', 'A', '', 'B' ]

def read_file(file_name):
    with open(file_name) as f:
        return ast.literal_eval(f.read())

def note_parse(note):
    sharp = note.count('#')
    flat = note.count('b')
    accent =  sharp - flat
    note = note.replace('#', '').replace('b', '')
    octave = int(note[-1])
    note = note[0]
    note_number = notes.index(note) + note_base + accent + (octave - 1) * 12
    return note_number

def map_pad(pad):
    pad_number = int(pad)
    if pad_number < 1 or pad_number > 16:
        raise Exception('Pad number must be in range [1-16]')
    return str(pad_number + pad_base) + "_3"


def parse_map(map):
    return [ [ map_pad(pair[0]), note_parse(pair[1]) ] for pair in map.items()]

config_data = read_file(config_file)
mapping_data = read_file(map_file)
device_data = parse_map(mapping_data)

config_data.update(device_data)
with open(out_file, 'w') as f:
    json.dump(config_data, f, indent=4)

