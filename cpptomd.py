#! /usr/bin/env python3
#
# Author:  James R. Small
# Last Modified:  12-13-2020-02
# Version:  1.21
#
# To do/bugs:
# * The replace needs to be a little more particular and if the "character" is
#   already an encoded entity, not replace it again...
#   Example:  "&amp;" becomes "&amp;amp;"
# * Add support to automate adding/customizing this:
#   <div style="height: 500px; width: 99%; border: 1px solid #ccc; overflow: auto;">
# * Add support to toggle wrapping on/off (default to on for now):
#   <code class="language-*" style="white-space: pre-wrap;">
#
# Note:  Formatting according to this Champlain KB on Canvas:
#        https://clt.champlain.edu/knowledgebase/code-snippets/
#

import os
import sys

# DEFAUL_SRCTYPE = 'cpp'
DEFAUL_SRCTYPE = 'clike'
# Was using cpp for C++ which seemed to work well - make sure clike works well too:
VALIDSRC = {'ASP.NET': 'aspnet', 'Bash': 'bash', '(*) C/C++': 'clike', 'CSS': 'css',
            'Git': 'git', 'Haskell': 'haskell', 'HTML/XML/Markup': 'markup',
            'Java': 'java', 'JavaScript': 'javascript', 'Latex': 'latex',
            'Objective-C': 'objectivec', 'PHP': 'php', 'Python': 'python',
            'Scala': 'scala', 'SCSS': 'scss', 'SQL': 'sql'}
# ENTITIES = {'<', '>', '&', '"', "'"}
# Looks like single/double quotes are OK without translation
# ENTITIES = {'<': '&lt;', '>': '&gt;', '&': '&amp;'}
# Need to do '&' first - depends on Ordered dict in v3.7+
ENTITIES = {'&': '&amp;', '<': '&lt;', '>': '&gt;'}

def main(argv):
    numbered = False
    srctype = DEFAUL_SRCTYPE

    # Primitive - should use argparse...
    if len(argv) == 3:
        if argv[2] == 'numbered':
            numbered = True
        elif argv[2] in VALIDSRC.values():
            srctype = argv[2]
        else:
            usage(argv)
    elif len(argv) == 4:
        if argv[2] == 'numbered':
            numbered = True
        elif argv[2] in VALIDSRC.values():
            srctype = argv[2]
        else:
            usage(argv)

        if argv[3] == 'numbered':
            numbered = True
        elif argv[3] in VALIDSRC.values():
            srctype = argv[3]
        else:
            usage(argv)
  
    pre_start = '<pre'
    if numbered:
        pre_start += ' class="line-numbers">'
    else:
        pre_start += '>'
    pre_end = '</pre>'
    code_start = f'<code class="language-{srctype}" style="white-space: pre-wrap;">'
    code_end = '</code>'


    with open(argv[1]) as infile:
        print(f'{pre_start}{code_start}', end='')
        # print(f'<pre><code class="{srctype} language-{srctype}">', end='')
        for line in infile:
            for k, v in ENTITIES.items():
                line = line.replace(k, v)
            print(line, end='')
        print(f'{code_end}{pre_end}')

def usage(argv):
    cmd = os.path.basename(argv[0])
    print(f'Usage:  {cmd} <input-file> [<type>] [numbered]')
    print('\tSupported types [(*) = default] include:')
    [print(f'\t* {k:>15}:  {VALIDSRC[k]}') for k in VALIDSRC]
    print('\tnumbered = Use line numbers')
    print(f'\nExample:  {cmd} program.sh bash numbered > program.md\n')

    sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 4:
        usage(sys.argv)

    main(sys.argv)
