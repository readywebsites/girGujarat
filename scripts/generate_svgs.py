import os

svg_dir = 'D:/hussain/assets/svg'
os.makedirs(svg_dir, exist_ok=True)

icons = {
    'icon-temple.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v3"/><path d="M12 5l-4 7h8l-4-7z"/><path d="M4 12v9h16v-9"/><path d="M9 21v-5a3 3 0 0 1 6 0v5"/><line x1="2" y1="21" x2="22" y2="21"/><path d="M6 12h12"/></svg>''',
    'icon-lion.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="4" r="2"/><circle cx="18" cy="8" r="2"/><circle cx="20" cy="16" r="2"/><path d="M9 10a5 5 0 0 1 5 5v3a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2v-3a5 5 0 0 1 5-5z"/><circle cx="4" cy="12" r="2"/><circle cx="6" cy="6" r="2"/></svg>''',
    'icon-coastal.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12c2.5 0 2.5-2 5-2s2.5 2 5 2 2.5-2 5-2 2.5 2 5 2"/><path d="M2 16c2.5 0 2.5-2 5-2s2.5 2 5 2 2.5-2 5-2 2.5 2 5 2"/><path d="M2 20c2.5 0 2.5-2 5-2s2.5 2 5 2 2.5-2 5-2 2.5 2 5 2"/><path d="M17 4a5 5 0 0 0-5 5v3"/><path d="M12 4c2 0 4 2 4 4"/><path d="M9 5c1 0 3 1 3 3"/></svg>''',
    'icon-roadtrip.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="5" width="20" height="14" rx="2"/><circle cx="7" cy="15" r="2"/><circle cx="17" cy="15" r="2"/><path d="M2 10h20"/><path d="M6 5l2-3h8l2 3"/></svg>''',
    'icon-pickup.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2a7 7 0 0 0-7 7c0 5.25 7 13 7 13s7-7.75 7-13a7 7 0 0 0-7-7z"/><circle cx="12" cy="9" r="2.5"/><path d="M3 21h18"/></svg>''',
    'icon-actravel.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 16H9m10 0h3v-3.34a2 2 0 0 0-.6-1.42L18 8h-4.5"/><path d="M2 12.66V16h2"/><circle cx="6.5" cy="16.5" r="2.5"/><circle cx="16.5" cy="16.5" r="2.5"/><path d="M2 10l3-5h8l3 5"/><line x1="8" y1="2" x2="8" y2="4"/><line x1="12" y1="2" x2="12" y2="4"/></svg>''',
    'icon-hotel.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 4v16"/><path d="M2 8h18a2 2 0 0 1 2 2v10"/><path d="M2 17h20"/><path d="M6 8v9"/><circle cx="6" cy="11" r="1.5"/></svg>''',
    'icon-meal.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 2v20"/><path d="M21 15V2a5 5 0 0 0-5 5v8h5zm0 0v7"/><path d="M4 2v6a3 3 0 0 0 6 0V2"/><path d="M7 8v14"/></svg>''',
    'icon-sightseeing.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/></svg>''',
    'icon-safari.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="6" width="20" height="12" rx="2"/><path d="M6 12h.01"/><path d="M10 12h.01"/><path d="M14 12h.01"/><path d="M18 12h.01"/><path d="M2 10a2 2 0 0 0 0 4"/><path d="M22 10a2 2 0 0 1 0 4"/></svg>''',
    'icon-shield.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><polyline points="9 12 11 14 15 10"/></svg>''',
    'icon-calendar.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/><polyline points="9 15 11 17 15 13"/></svg>''',
    'icon-heart.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>''',
    'icon-whatsapp.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/></svg>''',
    'icon-call.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>''',
    'brand-logo.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 54" fill="none">
  <g transform="translate(6, 4)">
    <circle cx="23" cy="23" r="22" stroke="url(#goldBorder)" stroke-width="1.5" fill="#061F17"/>
    <!-- Sacred Rising Sun & Mountain peaks -->
    <path d="M23 7 A16 16 0 0 1 39 23 L7 23 A16 16 0 0 1 23 7 Z" fill="url(#sunGlow)" opacity="0.3"/>
    <circle cx="23" cy="18" r="4.5" fill="url(#goldSun)"/>
    <path d="M12 31 L19 20 L24 27 L28 20 L34 31 Z" stroke="url(#goldFill)" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
  </g>
  <text x="60" y="24" font-family="'Cinzel', 'Playfair Display', serif" font-size="14.5" font-weight="700" letter-spacing="2" fill="#FFFFFF">TRAVEL FIRST</text>
  <text x="61" y="38" font-family="'Plus Jakarta Sans', sans-serif" font-size="8" font-weight="700" letter-spacing="3.5" fill="#D4AF37">HOLIDAYS</text>
  <defs>
    <linearGradient id="goldFill" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#FDE047"/>
      <stop offset="100%" stop-color="#B45309"/>
    </linearGradient>
    <linearGradient id="goldBorder" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#F59E0B"/>
      <stop offset="100%" stop-color="#78350F"/>
    </linearGradient>
    <linearGradient id="goldSun" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#FFFBEB"/>
      <stop offset="100%" stop-color="#D97706"/>
    </linearGradient>
    <radialGradient id="sunGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#F59E0B" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#F59E0B" stop-opacity="0"/>
    </radialGradient>
  </defs>
</svg>'''
}

for name, content in icons.items():
    p = os.path.join(svg_dir, name)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(content.strip())
print(f"Successfully generated {len(icons)} SVGs in {svg_dir}")

