#!/usr/bin/env python3
"""
Monarcula Theme Generator

Generates all theme variants from a single template file.
Template uses {{placeholder}} syntax for color substitution.
"""

from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).parent.parent
TEMPLATE_PATH = BASE_DIR / '.make' / 'monarcula.template.xml'
OUTPUT_DIR = BASE_DIR / 'src' / 'main' / 'resources' / 'META-INF'

# ============================================================================
# Color Definitions
# ============================================================================

# Vibrant Monokai colors (default)
vibrant_colors = {
    'red': 'f92672',
    'magenta': 'fd5ff0',
    'violet': 'ae81ff',
    'blue': '6593ef',
    'cyan': '66d9ef',
    'green': 'a6e22e',
    'yellow': 'e6db71',
    'orange': 'fd971f',
}

# Soft/muted colors
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

# Background variants
backgrounds = {
    'darcula': {
        'bg0': '232628',
        'bg1': '2d3032',
        'bg2': '3c3f41',
        'bg3': '4e5254',
    },
    'island': {
        'bg0': '1e1f22',
        'bg1': '26282e',
        'bg2': '2e3135',
        'bg3': '3e4145',
    },
    'dark': {
        'bg0': '2b2d30',
        'bg1': '35373a',
        'bg2': '43454a',
        'bg3': '55575c',
    },
}

# Common colors (same across all themes)
common_colors = {
    'fg0': 'fdf9f3',
    'fg1': '838e8f',
    'fg2': '5c6370',
}

# ============================================================================
# Theme Definitions
# ============================================================================

# Parent theme mapping for theme.json (UI inheritance)
parent_themes = {
    'darcula': 'Darcula',
    'dark': 'Dark',
    'island': 'Islands Dark',
}

themes = [
    {
        'name': 'Monarcula',
        'file_name': 'Monarcula',
        'display_name': 'Monarcula',
        'background': 'darcula',
        'colors': 'vibrant',
    },
    {
        'name': 'Monarcula Soft',
        'file_name': 'MonarculaSoft',
        'display_name': 'Monarcula Soft',
        'background': 'darcula',
        'colors': 'soft',
    },
    {
        'name': 'Monarcula Dark',
        'file_name': 'MonarculaDark',
        'display_name': 'Monarcula Dark',
        'background': 'dark',
        'colors': 'vibrant',
    },
    {
        'name': 'Monarcula Dark Soft',
        'file_name': 'MonarculaDarkSoft',
        'display_name': 'Monarcula Dark Soft',
        'background': 'dark',
        'colors': 'soft',
    },
    {
        'name': 'Monarcula Island',
        'file_name': 'MonarculaIsland',
        'display_name': 'Monarcula Island',
        'background': 'island',
        'colors': 'vibrant',
    },
    {
        'name': 'Monarcula Island Soft',
        'file_name': 'MonarculaIslandSoft',
        'display_name': 'Monarcula Island Soft',
        'background': 'island',
        'colors': 'soft',
    },
]

# ============================================================================
# Generator Functions
# ============================================================================

def get_theme_colors(theme: dict) -> dict:
    """Build complete color dictionary for a theme."""
    colors = {}
    colors['scheme_name'] = theme['name']
    colors.update(common_colors)
    colors.update(backgrounds[theme['background']])
    if theme['colors'] == 'vibrant':
        colors.update(vibrant_colors)
    else:
        colors.update(soft_colors)
    return colors


def generate_xml(template: str, colors: dict) -> str:
    """Replace all placeholders in template with colors."""
    result = template
    for key, value in colors.items():
        result = result.replace(f'{{{{{key}}}}}', value)
    return result


def generate_theme_json(theme: dict) -> str:
    """Generate theme.json metadata file."""
    parent_theme = parent_themes[theme['background']]
    return f'''{{
  "name": "{theme['display_name']}",
  "dark": true,
  "author": "Valentin Lutz",
  "parentTheme": "{parent_theme}",
  "editorScheme": "/META-INF/{theme['file_name']}.xml",
  "ui": {{
  }}
}}
'''


def main():
    # Read template
    print(f'Reading template: {TEMPLATE_PATH}')
    template = TEMPLATE_PATH.read_text()

    # Generate each theme
    for theme in themes:
        print(f"\n=== Generating {theme['name']} ===")

        # Get colors for this theme
        colors = get_theme_colors(theme)

        # Generate XML
        xml_content = generate_xml(template, colors)
        xml_path = OUTPUT_DIR / f"{theme['file_name']}.xml"
        xml_path.write_text(xml_content)
        print(f"  Created {theme['file_name']}.xml")

        # Generate theme.json
        json_content = generate_theme_json(theme)
        json_path = OUTPUT_DIR / f"{theme['file_name']}.theme.json"
        json_path.write_text(json_content)
        print(f"  Created {theme['file_name']}.theme.json")

        # Show color summary
        bg_name = theme['background']
        color_name = theme['colors']
        print(f"  Background: {bg_name} ({backgrounds[bg_name]['bg0']})")
        print(f"  Colors: {color_name}")

    print('\n=== All themes generated ===')


if __name__ == '__main__':
    main()
