default_colors = {
    'bg0': '232628',
    'bg1': '3C3F41',
    'bg2': 'TBD',
    'bg3': 'TBD',
    'fg3': 'TBD',
    'fg2': 'TBD',
    'fg1': '838E8F',
    'fg0': 'FDF9F3',
    'red': 'F92672',
    'magenta': 'FD5FF0',
    'violet': 'AE81FF',
    'blue': '6593EF',
    'cyan': '66D9EF',
    'green': 'A6E22E',
    'yellow': 'E6DB71',
    'orange': 'FD971F',
}


def create_theme(theme_name: str, colors: dict):
    with open('src/main/resources/META-INF/Monarcula.xml', 'r') as file:
        theme = file.read()

    theme = theme.replace("Monarcula", theme_name)

    for color_name, new_color in colors.items():
        print(default_colors.get(color_name).lower() + " " + new_color.lower())
        theme = theme.replace(default_colors.get(color_name).lower(), new_color.lower())

    with open('src/main/resources/META-INF/' + theme_name + ".xml", 'w') as file:
        file.write(theme)


create_theme(
    'MonarculaSoft', {
        'bg0': '232628',
        'bg1': '3C3F41',
        'bg2': 'TBD',
        'bg3': 'TBD',
        'fg3': 'TBD',
        'fg2': 'TBD',
        'fg1': '838E8F',
        'fg0': 'FDF9F3',
        'red': 'EB6288',
        'magenta': 'EB8AE4',
        'violet': 'AB9DF2',
        'blue': '77A4E8',
        'cyan': '78DCE8',
        'green': 'A9DC76',
        'yellow': 'F4D966',
        'orange': 'EE9867',
    })
