from datetime import datetime

with open('diary.txt') as f:
    blocks = f.read().split('\n\n')
    blocks = {datetime.strptime(lines[0], '%d.%m.%Y; %H:%M'): lines[1:] for lines in
              [block.split('\n') for block in blocks]}

    print('\n\n'.join(
        datetime.strftime(dt, '%d.%m.%Y; %H:%M') + '\n' + '\n'.join(lines) for dt, lines in sorted(blocks.items())),
          sep='\n')
