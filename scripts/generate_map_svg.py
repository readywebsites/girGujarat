import os

svg_path = 'D:/hussain/assets/svg/interactive-route-map.svg'

svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 480" width="100%" height="100%" fill="none" class="gujarat-interactive-map">
  <defs>
    <!-- Background Gradients -->
    <linearGradient id="mapBgGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#08291F" stop-opacity="0.95"/>
      <stop offset="50%" stop-color="#041B14" stop-opacity="0.98"/>
      <stop offset="100%" stop-color="#03140F" stop-opacity="1"/>
    </linearGradient>

    <!-- Landmass Gradient -->
    <linearGradient id="landGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F4232" stop-opacity="0.7"/>
      <stop offset="60%" stop-color="#0B3528" stop-opacity="0.5"/>
      <stop offset="100%" stop-color="#07261C" stop-opacity="0.3"/>
    </linearGradient>

    <!-- Route Line Glow -->
    <filter id="glowGold" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>

    <radialGradient id="pinPulse" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#F59E0B" stop-opacity="1"/>
      <stop offset="70%" stop-color="#F59E0B" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#F59E0B" stop-opacity="0"/>
    </radialGradient>
    
    <radialGradient id="ahdPulse" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#10B981" stop-opacity="1"/>
      <stop offset="70%" stop-color="#10B981" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#10B981" stop-opacity="0"/>
    </radialGradient>
  </defs>

  <!-- Deep Forest Map Background -->
  <rect width="380" height="480" fill="url(#mapBgGrad)" rx="24"/>

  <!-- Subtle Topographic Contour Grid Lines -->
  <g stroke="#134E39" stroke-width="0.8" opacity="0.3" stroke-dasharray="3 4">
    <path d="M20 60 Q180 80 360 40"/>
    <path d="M10 140 Q150 180 370 120"/>
    <path d="M30 220 Q200 240 350 200"/>
    <path d="M10 300 Q160 340 370 280"/>
    <path d="M20 380 Q180 400 360 360"/>
  </g>

  <!-- Stylized Gujarat & Saurashtra Peninsula Coastline -->
  <g class="landmass" filter="drop-shadow(0 4px 12px rgba(0,0,0,0.5))">
    <!-- Gulf of Kutch, Dwarka Headland, Saurashtra South Coast, Gulf of Khambhat -->
    <path d="M 120 40 
             C 180 35, 260 45, 340 50 
             C 360 80, 350 130, 310 160 
             C 280 180, 270 210, 260 250 
             C 255 280, 265 310, 270 340 
             C 275 390, 240 430, 200 440 
             C 150 445, 120 410, 100 370 
             C 70 310, 50 260, 40 210 
             C 32 170, 45 130, 80 120 
             C 110 110, 120 80, 120 40 Z" 
          fill="url(#landGrad)" stroke="#1D664E" stroke-width="1.8"/>
          
    <!-- Arabian Sea Coast Ripple Accents -->
    <path d="M 35 220 C 42 270, 65 320, 95 380 C 115 420, 150 455, 205 448" 
          stroke="#38BDF8" stroke-width="1.2" opacity="0.4" stroke-dasharray="2 3" fill="none"/>
  </g>

  <!-- The Tour Route Line: Ahmedabad -> Dwarka -> Somnath -> Sasan Gir -> Ahmedabad -->
  <!-- Base Route Path -->
  <path id="tourRoutePath" class="tour-route-line"
        d="M 280 95 
           C 210 110, 120 130, 75 185 
           C 55 240, 75 320, 145 405 
           C 165 415, 190 395, 210 335 
           C 235 255, 265 170, 280 95" 
        stroke="#D4AF37" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"
        stroke-dasharray="6 6" fill="none" filter="url(#glowGold)"/>

  <!-- Return Journey Shortcut Indicator (Gir to Ahmedabad) -->
  <path d="M 210 335 C 240 250, 265 170, 280 95" 
        stroke="#10B981" stroke-width="2" stroke-linecap="round" stroke-dasharray="4 4" opacity="0.75" fill="none"/>

  <!-- WAYPOINT 1: AHMEDABAD (Pickup & Drop) -->
  <g class="map-waypoint" id="wp-ahmedabad" transform="translate(280, 95)" cursor="pointer" data-day="0">
    <circle cx="0" cy="0" r="16" fill="url(#ahdPulse)" class="pulse-ring"/>
    <circle cx="0" cy="0" r="8" fill="#10B981" stroke="#FFFFFF" stroke-width="2"/>
    <circle cx="0" cy="0" r="3" fill="#FFFFFF"/>
    <!-- Label Badge -->
    <g transform="translate(12, -18)">
      <rect x="0" y="0" width="85" height="34" rx="8" fill="#06241A" stroke="#10B981" stroke-width="1" opacity="0.95"/>
      <text x="8" y="14" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" font-weight="700" fill="#FFFFFF">Ahmedabad</text>
      <text x="8" y="27" font-family="'Plus Jakarta Sans', sans-serif" font-size="8" font-weight="600" fill="#34D399">Pickup &amp; Drop</text>
    </g>
  </g>

  <!-- WAYPOINT 2: DWARKA (Day 1) -->
  <g class="map-waypoint" id="wp-dwarka" transform="translate(75, 185)" cursor="pointer" data-day="1">
    <circle cx="0" cy="0" r="18" fill="url(#pinPulse)" class="pulse-ring"/>
    <!-- Temple Crest Marker -->
    <circle cx="0" cy="0" r="11" fill="#D4AF37" stroke="#FFFBEB" stroke-width="2"/>
    <path d="M 0 -6 L 4 2 L -4 2 Z" fill="#041F16"/>
    <rect x="-3" y="2" width="6" height="4" fill="#041F16"/>
    <!-- Label Badge -->
    <g transform="translate(-75, 8)">
      <rect x="0" y="0" width="70" height="34" rx="8" fill="#06241A" stroke="#D4AF37" stroke-width="1" opacity="0.95"/>
      <text x="8" y="14" font-family="'Plus Jakarta Sans', sans-serif" font-size="10.5" font-weight="700" fill="#FFFFFF">Dwarka</text>
      <text x="8" y="27" font-family="'Plus Jakarta Sans', sans-serif" font-size="8.5" font-weight="600" fill="#FCD34D">Day 1</text>
    </g>
  </g>

  <!-- WAYPOINT 3: SOMNATH (Day 2) -->
  <g class="map-waypoint" id="wp-somnath" transform="translate(145, 405)" cursor="pointer" data-day="2">
    <circle cx="0" cy="0" r="18" fill="url(#pinPulse)" class="pulse-ring"/>
    <!-- Temple Crest Marker -->
    <circle cx="0" cy="0" r="11" fill="#D4AF37" stroke="#FFFBEB" stroke-width="2"/>
    <path d="M 0 -6 L 4 2 L -4 2 Z" fill="#041F16"/>
    <rect x="-3" y="2" width="6" height="4" fill="#041F16"/>
    <!-- Label Badge -->
    <g transform="translate(12, -22)">
      <rect x="0" y="0" width="72" height="34" rx="8" fill="#06241A" stroke="#D4AF37" stroke-width="1" opacity="0.95"/>
      <text x="8" y="14" font-family="'Plus Jakarta Sans', sans-serif" font-size="10.5" font-weight="700" fill="#FFFFFF">Somnath</text>
      <text x="8" y="27" font-family="'Plus Jakarta Sans', sans-serif" font-size="8.5" font-weight="600" fill="#FCD34D">Day 2</text>
    </g>
  </g>

  <!-- WAYPOINT 4: SASAN GIR (Day 3 & 4) -->
  <g class="map-waypoint" id="wp-gir" transform="translate(210, 335)" cursor="pointer" data-day="3">
    <circle cx="0" cy="0" r="20" fill="url(#pinPulse)" class="pulse-ring"/>
    <!-- Wildlife Paw / Lion Emblem -->
    <circle cx="0" cy="0" r="12" fill="#F59E0B" stroke="#FFFBEB" stroke-width="2"/>
    <circle cx="-3" cy="-4" r="1.5" fill="#041F16"/>
    <circle cx="3" cy="-4" r="1.5" fill="#041F16"/>
    <circle cx="0" cy="0" r="2.5" fill="#041F16"/>
    <circle cx="-4" cy="2" r="1.2" fill="#041F16"/>
    <circle cx="4" cy="2" r="1.2" fill="#041F16"/>
    <!-- Label Badge -->
    <g transform="translate(-78, -32)">
      <rect x="0" y="0" width="74" height="34" rx="8" fill="#06241A" stroke="#F59E0B" stroke-width="1" opacity="0.95"/>
      <text x="8" y="14" font-family="'Plus Jakarta Sans', sans-serif" font-size="10.5" font-weight="700" fill="#FFFFFF">Sasan Gir</text>
      <text x="8" y="27" font-family="'Plus Jakarta Sans', sans-serif" font-size="8.5" font-weight="600" fill="#FCD34D">Day 3 &amp; 4</text>
    </g>
  </g>

  <!-- Animated Tour Vehicle that traverses route -->
  <g id="animatedTourCar" transform="translate(280, 95)">
    <g transform="translate(-14, -14)">
      <!-- Mini Yellow AC Tour Taxi / Safari SUV -->
      <rect x="2" y="5" width="24" height="15" rx="4" fill="#F59E0B" stroke="#FFFFFF" stroke-width="1.5" filter="drop-shadow(0 2px 4px rgba(0,0,0,0.4))"/>
      <rect x="6" y="8" width="6" height="5" rx="1" fill="#0E2E23"/>
      <rect x="15" y="8" width="8" height="5" rx="1" fill="#0E2E23"/>
      <circle cx="7" cy="20" r="2.5" fill="#1E293B"/>
      <circle cx="21" cy="20" r="2.5" fill="#1E293B"/>
      <circle cx="26" cy="11" r="1.5" fill="#EF4444"/> <!-- Tail light -->
      <circle cx="2" cy="11" r="1.5" fill="#FEF08A"/> <!-- Head light -->
    </g>
  </g>

  <!-- Distance / Legend Card at Bottom Left -->
  <g transform="translate(18, 435)">
    <rect x="0" y="0" width="135" height="30" rx="8" fill="#051C14" stroke="#1D664E" stroke-width="1" opacity="0.9"/>
    <circle cx="12" cy="15" r="4" fill="#D4AF37"/>
    <text x="24" y="19" font-family="'Plus Jakarta Sans', sans-serif" font-size="9" font-weight="600" fill="#E2E8F0">Total Route: ~1,100 km</text>
  </g>
</svg>'''

with open(svg_path, 'w', encoding='utf-8') as f:
    f.write(svg_content.strip())

print(f"Generated interactive route map at {svg_path}")

