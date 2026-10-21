with open('D:/hussain/assets/svg/interactive-route-map.svg', 'r', encoding='utf-8') as f:
    svg_data = f.read()

with open('D:/hussain/index.html', 'r', encoding='utf-8') as f:
    html_data = f.read()

target = '<object data="assets/svg/interactive-route-map.svg" type="image/svg+xml" style="width: 100%; height: 100%; display: block;" id="interactiveMapObj"></object>'

if target in html_data:
    new_html = html_data.replace(target, svg_data)
    with open('D:/hussain/index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print('Inline SVG inserted successfully!')
else:
    print('Target object tag not found!')

