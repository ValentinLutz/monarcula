default_colors = {
    'bg0': '232628',
    'bg_caret': '2d3032',
    'bg1': '3c3f41',
    'fg1': '838e8f',
    'fg0': 'fdf9f3',
    'red': 'f92672',
    'magenta': 'fd5ff0',
    'violet': 'ae81ff',
    'blue': '6593ef',
    'cyan': '66d9ef',
    'green': 'a6e22e',
    'yellow': 'e6db71',
    'orange': 'fd971f',
}

soft_colors = {
    'red': 'eb6288',
    'magenta': 'eb8ae4',
    'violet': 'ab9df2',
    'blue': '77a4e8',
    'cyan': '78dce8',
    'green': 'a9dc76',
    'yellow': 'f4d966',
    'orange': 'ee9867',
}

island_background = {
    'bg0': '1e1f22',
    'bg_caret': '26282e',
}

dark_background = {
    'bg0': '2b2d30',
    'bg_caret': '35373a',
}


def create_theme(theme_name: str, colors: dict):
    with open('src/main/resources/META-INF/Monarcula.xml', 'r') as file:
        theme = file.read()

    theme = theme.replace('name="Monarcula"', f'name="{theme_name}"')

    for color_name, new_color in colors.items():
        old_color = default_colors.get(color_name)
        if old_color:
            print(f'{color_name}: {old_color} -> {new_color}')
            theme = theme.replace(old_color.lower(), new_color.lower())

    with open(f'src/main/resources/META-INF/{theme_name}.xml', 'w') as file:
        file.write(theme)

    print(f'Created {theme_name}.xml\n')


def create_theme_json(theme_name: str):
    json_content = f'''{{
  "name": "{theme_name.replace("Monarcula", "Monarcula ").replace("Soft", " Soft").replace("Island", " Island").replace("Dark", " Dark").replace("  ", " ").strip()}",
  "dark": true,
  "author": "Valentin Lutz",
  "editorScheme": "/META-INF/{theme_name}.xml",
  "ui": {{
  }}
}}
'''
    with open(f'src/main/resources/META-INF/{theme_name}.theme.json', 'w') as file:
        file.write(json_content)

    print(f'Created {theme_name}.theme.json')


print('=== Generating Soft variant ===')
create_theme('MonarculaSoft', soft_colors)
create_theme_json('MonarculaSoft')

print('\n=== Generating Island variants ===')
create_theme('MonarculaIsland', island_background)
create_theme_json('MonarculaIsland')

island_soft_colors = {**island_background, **soft_colors}
create_theme('MonarculaIslandSoft', island_soft_colors)
create_theme_json('MonarculaIslandSoft')

print('\n=== Generating Dark variants ===')
create_theme('MonarculaDark', dark_background)
create_theme_json('MonarculaDark')

dark_soft_colors = {**dark_background, **soft_colors}
create_theme('MonarculaDarkSoft', dark_soft_colors)
create_theme_json('MonarculaDarkSoft')

print('\n=== All themes generated ===')
