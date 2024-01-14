#!/usr/bin/env python3

print('Download a list of songs from to_download.txt file (d) or a single link (s), [d/s]?')
action = input()

match action:
    case 'd':
        import list
    case 's':
        import link
    case _:
        quit()
