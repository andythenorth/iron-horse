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
    if not 'return consist' in content:
        print(filename, 'is not an engine, skipping')
        return
    else:
        """"
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
        """
        lines = codecs.open(os.path.join('src','vehicles',filename),'r', encoding='utf-8').readlines()
        modified_lines = []
        for line in lines:
            if 'def main():\n' in line:
                modified_lines.append('def main(roster):\n')
            elif '(id=' in line:
                splits = line.split('(')
                print(splits)
                modified_lines.append('(roster=roster,\n   '.join(splits))
            else:
                modified_lines.append(line)
        file = open(os.path.join('src','vehicles',filename),'w')
        file.write(''.join(modified_lines))
        file.close

for filename in filenames:
    insert_main(filename)
