import os.path
currentdir = os.curdir

import sys
sys.path.append(os.path.join('src')) # add to the module search path

import codecs

filenames = []
for filename in os.listdir(os.path.join('src','vehicles')):
    if '__' not in filename and '.DS_Store' not in filename:
        filenames.append(filename)

def insert_main(filename):
    content = codecs.open(os.path.join('src','vehicles',filename),'r', encoding='utf-8').read()
    if 'def main():' in content:
        print(filename, 'already has main(), skipping')
        return
    else:
        lines = codecs.open(os.path.join('src','vehicles',filename),'r', encoding='utf-8').readlines()
        modified_lines = []
        for index, line in enumerate(lines):
            if index == 0:
                modified_lines.append(line)
            if index > 0:
                line = '    ' + line
                modified_lines.append(line)
        modified_lines.insert(1, '\n')
        modified_lines.insert(2, 'def main():')
        modified_lines.append('\n    return consist')

        file = open(os.path.join('src','vehicles',filename),'w')
        file.write(''.join(modified_lines))
        file.close


for filename in filenames:
    insert_main(filename)
