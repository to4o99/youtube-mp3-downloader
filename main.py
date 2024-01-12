print('Download a list of song from to_download.txt file (d) or a songle link (s), [d/s]?')
action = input()

match action:
    case 'd':
        import list
    case 's':
        import link
    case _:
        quit()
