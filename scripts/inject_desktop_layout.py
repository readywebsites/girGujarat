import re

# Read current index.html
with open('D:/hussain/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add css/desktop.css to head if not present
if 'css/desktop.css' not in html:
    html = html.replace(
        '<link rel="stylesheet" href="css/presentation.css">',
        '<link rel="stylesheet" href="css/presentation.css">\n  <link rel="stylesheet" href="css/desktop.css">'
    )

# 2. Replace bottom-app-nav with mobile-sticky-dual-bar
old_nav = '''          <!-- STICKY BOTTOM APP NAVIGATION -->
          <nav class="bottom-app-nav" aria-label="Bottom Navigation">
            <a href="#sectionHero" class="nav-tab-item active">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
              <span>Home</span>
            </a>

            <a href="#sectionItinerary" class="nav-tab-item">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>
              <span>Packages</span>
            </a>

            <a href="#sectionDestinations" class="nav-tab-item">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><circle cx="12" cy="12" r="10"/><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"/></svg>
              <span>Destinations</span>
            </a>

            <button class="nav-tab-item trigger-booking-modal" style="border:none; background:none;">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
              <span>Enquiry</span>
            </button>
          </nav>'''

new_mobile_nav = '''          <!-- STICKY FLOATING DUAL ACTION BAR (MOBILE) -->
          <div class="mobile-sticky-dual-bar" aria-label="Quick Booking Actions">
            <a href="https://wa.me/919876543210?text=Hello%20Travel%20First%20Holidays!%20I%20am%20interested%20in%20the%20Gujarat%20Tour%20Package." class="dual-btn-wa" target="_blank" rel="noopener">
              <img src="assets/svg/icon-whatsapp.svg" alt="WhatsApp" width="18" height="18">
              <span>WhatsApp</span>
            </a>
            <a href="tel:+919876543210" class="dual-btn-call">
              <img src="assets/svg/icon-call.svg" alt="Call Us" width="16" height="16">
              <span>Call Us</span>
            </a>
          </div>'''

if old_nav in html:
    html = html.replace(old_nav, new_mobile_nav)
    print("Replaced mobile nav with sticky dual bar!")
else:
    print("Could not find exact old_nav, using regex replace...")
    html = re.sub(r'<nav class="bottom-app-nav".*?</nav>', new_mobile_nav, html, flags=re.DOTALL)

# 3. Add Desktop Landing Page Markup right after </article> and before </div> for viewport
desktop_markup = '''
        <!-- ==========================================================================
             COMPLETE DESKTOP WEBSITE LANDING PAGE (MATCHING DESKTOP SPECIFICATION)
             ========================================================================== -->
        <div class="desktop-landing-wrapper" id="desktopLandingWrapper">

          <!-- 1. DESKTOP HEADER -->
          <header class="desktop-header-wrap">
            <div class="desktop-header-container">
              <div class="desktop-brand-logo">
                <img src="assets/svg/brand-logo.svg" alt="TRAVEL FIRST HOLIDAYS">
              </div>

              <ul class="desktop-nav-menu">
                <li><a href="#desktopHero" class="desktop-nav-link active">Home</a></li>
                <li><a href="#desktopFeatured" class="desktop-nav-link">Tour Packages</a></li>
                <li><a href="#desktopDestinations" class="desktop-nav-link">Destinations</a></li>
                <li><a href="#desktopWhyUs" class="desktop-nav-link">About Us</a></li>
                <li><a href="#desktopMoments" class="desktop-nav-link">Gallery</a></li>
                <li><a href="#desktopFooter" class="desktop-nav-link">Contact</a></li>
              </ul>

              <a href="https://wa.me/919876543210?text=Hello%20Travel%20First%20Holidays!%20I%20am%20planning%20a%20Gujarat%20Tour." class="desktop-header-cta" target="_blank" rel="noopener">
                <img src="assets/svg/icon-whatsapp.svg" alt="WhatsApp" width="18" height="18">
                <span>Enquire on WhatsApp</span>
              </a>
            </div>
          </header>

          <!-- 2. DESKTOP HERO SECTION -->
          <section class="desktop-hero-section" id="desktopHero">
            <img src="assets/crops/hero_montage.png" alt="Discover Gujarat" class="desktop-hero-bg" onerror="this.src='assets/images/hero_lion_retina.jpg'">
            <div class="desktop-hero-overlay"></div>

            <!-- Route Map Pin Indicator top right -->
            <div class="hero-route-badge-float">
              <span class="route-badge-title">Dwarka • Somnath • Sasan Gir</span>
              <div class="route-badge-stops">
                <span style="color:#D4AF37;">📍 Dwarka</span>
                <span style="color:#CBD5E1;">→</span>
                <span style="color:#D4AF37;">📍 Somnath</span>
                <span style="color:#CBD5E1;">→</span>
                <span style="color:#F59E0B;">🦁 Gir</span>
              </div>
            </div>

            <div class="desktop-hero-content">
              <span class="desktop-hero-kicker">EXPLORE • PRAY • DISCOVER • TOGETHER</span>
              <h1 class="desktop-hero-title">Discover Gujarat.</h1>
              <span class="desktop-hero-title-italic">Experience Something Extraordinary.</span>

              <!-- 3 Feature Pills -->
              <div class="desktop-hero-pills">
                <div class="desktop-pill">
                  <img src="assets/svg/icon-temple.svg" alt="Temples" class="desktop-pill-icon">
                  <span>Sacred Temples</span>
                </div>
                <div class="desktop-pill">
                  <img src="assets/svg/icon-lion.svg" alt="Wildlife" class="desktop-pill-icon">
                  <span>Wildlife Adventures</span>
                </div>
                <div class="desktop-pill">
                  <img src="assets/svg/icon-heart.svg" alt="Holidays" class="desktop-pill-icon">
                  <span>Memorable Holidays</span>
                </div>
              </div>

              <!-- Dual CTAs -->
              <div class="desktop-hero-actions">
                <button class="btn-hero-primary trigger-booking-modal">
                  <span>Explore Tour Packages</span>
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                </button>
                <button class="btn-hero-secondary trigger-booking-modal">
                  <span>Plan Your Journey</span>
                </button>
              </div>

              <!-- Floating Inclusions Strip across bottom of hero -->
              <div class="desktop-inclusions-strip">
                <div class="strip-item">
                  <div class="strip-icon"><img src="assets/svg/icon-actravel.svg" alt="Car"></div>
                  <span class="strip-text">Comfortable AC Travel</span>
                </div>
                <div class="strip-item">
                  <div class="strip-icon"><img src="assets/svg/icon-hotel.svg" alt="Hotel"></div>
                  <span class="strip-text">3 Nights Hotel Stay</span>
                </div>
                <div class="strip-item">
                  <div class="strip-icon"><img src="assets/svg/icon-meal.svg" alt="Food"></div>
                  <span class="strip-text">Breakfast + Dinner</span>
                </div>
                <div class="strip-item">
                  <div class="strip-icon"><img src="assets/svg/icon-sightseeing.svg" alt="Sightseeing"></div>
                  <span class="strip-text">All Sightseeing Included</span>
                </div>
                <div class="strip-item">
                  <div class="strip-icon"><img src="assets/svg/icon-safari.svg" alt="Safari"></div>
                  <span class="strip-text">Complimentary Safari Ticket</span>
                </div>
              </div>
            </div>
          </section>

          <!-- 3. DESKTOP FEATURED TOUR PACKAGE -->
          <section class="desktop-featured-section" id="desktopFeatured">
            <div class="desktop-featured-card">
              <div class="featured-card-left">
                <span class="featured-kicker">FEATURED TOUR PACKAGE</span>
                <h2 class="featured-title">Dwarka – Somnath – Sasan Gir</h2>
                <p class="featured-duration">3 Night / 4 Days Tour Package</p>
                <p class="featured-desc">
                  A perfect blend of spirituality, wildlife and coastal beauty — explore the best of Gujarat with comfortable travel and memorable experiences.
                </p>

                <!-- 6 Circular Inclusions Icons Row -->
                <div class="featured-icons-row">
                  <div class="featured-icon-badge">
                    <div class="featured-icon-circle"><img src="assets/svg/icon-pickup.svg" alt="Pickup"></div>
                    <span class="featured-icon-label">Pickup &amp; Drop<br><small style="color:#64748B;">Ahmedabad</small></span>
                  </div>
                  <div class="featured-icon-badge">
                    <div class="featured-icon-circle"><img src="assets/svg/icon-actravel.svg" alt="AC"></div>
                    <span class="featured-icon-label">Comfortable<br><small style="color:#64748B;">AC Travel</small></span>
                  </div>
                  <div class="featured-icon-badge">
                    <div class="featured-icon-circle"><img src="assets/svg/icon-hotel.svg" alt="Hotel"></div>
                    <span class="featured-icon-label">Hotel Stay<br><small style="color:#64748B;">3 Nights</small></span>
                  </div>
                  <div class="featured-icon-badge">
                    <div class="featured-icon-circle"><img src="assets/svg/icon-meal.svg" alt="Meals"></div>
                    <span class="featured-icon-label">Breakfast<br><small style="color:#64748B;">+ Dinner</small></span>
                  </div>
                  <div class="featured-icon-badge">
                    <div class="featured-icon-circle"><img src="assets/svg/icon-sightseeing.svg" alt="Sightseeing"></div>
                    <span class="featured-icon-label">All Sightseeing<br><small style="color:#64748B;">Included</small></span>
                  </div>
                  <div class="featured-icon-badge">
                    <div class="featured-icon-circle"><img src="assets/svg/icon-safari.svg" alt="Safari"></div>
                    <span class="featured-icon-label">Complimentary<br><small style="color:#64748B;">Safari Ticket</small></span>
                  </div>
                </div>

                <div class="featured-actions-row">
                  <button class="btn-book-package trigger-booking-modal">
                    <span>Book This Package</span>
                    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                  </button>
                  <button class="btn-view-itinerary" onclick="openDayDetailModal(1)">
                    <span>View Full Itinerary</span>
                  </button>
                </div>
              </div>

              <!-- Right Visual with Price Badge -->
              <div class="featured-card-right">
                <img src="assets/crops/package_vehicles.png" alt="Innova Crysta and Luxury Tour Bus at Temple" class="featured-right-img">
                <div class="featured-price-badge-desktop">
                  <span class="price-badge-desktop-label">Starting From</span>
                  <span class="price-badge-desktop-amount">₹9,999/-</span>
                  <span class="price-badge-desktop-sub">Per Person</span>
                </div>
              </div>
            </div>
          </section>

          <!-- 4. DESKTOP DESTINATIONS GRID (4 ACROSS) -->
          <section class="desktop-destinations-section" id="desktopDestinations">
            <div class="desktop-destinations-container">
              <div class="desktop-section-header">
                <span class="desktop-hero-kicker" style="color: var(--gold-300);">EXPLORE OUR DESTINATIONS</span>
                <h2 style="font-size: 36px; font-weight: 800; color: #FFFFFF; margin-bottom: 10px;">Icons of Gujarat, Journeys for a Lifetime.</h2>
                <p style="font-size: 14px; color: rgba(255, 255, 255, 0.78); line-height: 1.6;">
                  From sacred temples to wild forests and serene coastlines, experience the diverse beauty of Gujarat.
                </p>
              </div>

              <div class="dest-grid-4">
                <!-- Dwarka -->
                <div class="dest-grid-card trigger-dest-modal" data-dest-id="dwarka">
                  <img src="assets/crops/dest_dwarka.png" alt="Dwarka" class="dest-grid-bg" onerror="this.src='assets/images/dwarka_retina.jpg'">
                  <div class="dest-grid-overlay">
                    <div class="dest-grid-icon"><img src="assets/svg/icon-temple.svg" alt="Temple"></div>
                    <h3 class="dest-grid-title">Dwarka</h3>
                    <p class="dest-grid-sub">Dwarkadhish Temple &amp; Bet Dwarka</p>
                    <button class="btn-dest-explore">Explore →</button>
                  </div>
                </div>

                <!-- Somnath -->
                <div class="dest-grid-card trigger-dest-modal" data-dest-id="somnath">
                  <img src="assets/crops/dest_somnath.png" alt="Somnath" class="dest-grid-bg" onerror="this.src='assets/images/somnath_retina.jpg'">
                  <div class="dest-grid-overlay">
                    <div class="dest-grid-icon"><img src="assets/svg/icon-temple.svg" alt="Temple"></div>
                    <h3 class="dest-grid-title">Somnath</h3>
                    <p class="dest-grid-sub">Somnath Temple &amp; Triveni Sangam</p>
                    <button class="btn-dest-explore">Explore →</button>
                  </div>
                </div>

                <!-- Sasan Gir -->
                <div class="dest-grid-card trigger-dest-modal" data-dest-id="gir">
                  <img src="assets/crops/dest_gir.png" alt="Sasan Gir" class="dest-grid-bg" onerror="this.src='assets/images/gir_safari_retina.jpg'">
                  <div class="dest-grid-overlay">
                    <div class="dest-grid-icon"><img src="assets/svg/icon-lion.svg" alt="Lion"></div>
                    <h3 class="dest-grid-title">Sasan Gir</h3>
                    <p class="dest-grid-sub">Wildlife Safari &amp; Nature Experience</p>
                    <button class="btn-dest-explore">Explore →</button>
                  </div>
                </div>

                <!-- Nageshwar -->
                <div class="dest-grid-card trigger-dest-modal" data-dest-id="nageshwar">
                  <img src="assets/crops/dest_nageshwar.png" alt="Nageshwar" class="dest-grid-bg">
                  <div class="dest-grid-overlay">
                    <div class="dest-grid-icon"><img src="assets/svg/icon-temple.svg" alt="Temple"></div>
                    <h3 class="dest-grid-title">Nageshwar</h3>
                    <p class="dest-grid-sub">Nageshwar Jyotirling &amp; Sacred Sites</p>
                    <button class="btn-dest-explore">Explore →</button>
                  </div>
                </div>
              </div>
            </div>
          </section>

          <!-- 5. DESKTOP SASAN GIR INTO THE WILD (3-Column Split) -->
          <section class="desktop-gir-section" id="desktopGir">
            <div class="desktop-gir-container">
              <!-- Left Narrative & Lion Family -->
              <div class="gir-left-narrative">
                <div class="gir-narrative-media">
                  <img src="assets/images/lion_family_retina.jpg" alt="Asiatic Lioness and Cubs in Gir Forest" onerror="this.src='assets/crops/gir_video_thumb.png'">
                </div>
                <span class="desktop-hero-kicker" style="color: var(--gold-300);">SASAN GIR</span>
                <h2 class="gir-narrative-title">Into the Wild</h2>
                <p class="gir-narrative-desc">
                  Home to the majestic Asiatic Lion, Sasan Gir offers an unforgettable wildlife experience amidst lush forests, diverse flora and fauna, and breathtaking natural landscapes.
                </p>
                <button class="btn-hero-primary trigger-dest-modal" data-dest-id="gir" style="align-self: flex-start; padding: 12px 28px;">
                  <span>Discover Gir</span>
                  <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                </button>
              </div>

              <!-- Middle 3 Stacked Wildlife Photos -->
              <div class="gir-middle-photos">
                <div class="gir-stacked-photo">
                  <img src="assets/images/deer_retina.jpg" alt="Spotted Deer in Gir Forest" onerror="this.src='assets/crops/gir_thumb_3.png'">
                </div>
                <div class="gir-stacked-photo">
                  <img src="assets/images/peacock_retina.jpg" alt="Dancing Peacock in Sanctuary">
                </div>
                <div class="gir-stacked-photo">
                  <img src="assets/images/gir_safari_retina.jpg" alt="Open Gypsy Safari in Jungle" onerror="this.src='assets/crops/gir_thumb_2.png'">
                </div>
              </div>

              <!-- Right 4 Feature Cards -->
              <div class="gir-right-features">
                <div class="gir-feature-box">
                  <div class="gir-feature-icon"><img src="assets/svg/icon-lion.svg" alt="Lion"></div>
                  <div>
                    <h4 class="gir-feature-title">Asiatic Lions</h4>
                    <p class="gir-feature-sub">In their natural habitat</p>
                  </div>
                </div>

                <div class="gir-feature-box">
                  <div class="gir-feature-icon"><img src="assets/svg/icon-roadtrip.svg" alt="Jeep"></div>
                  <div>
                    <h4 class="gir-feature-title">Jeep Safari</h4>
                    <p class="gir-feature-sub">Forest adventure</p>
                  </div>
                </div>

                <div class="gir-feature-box">
                  <div class="gir-feature-icon"><img src="assets/svg/icon-coastal.svg" alt="Nature"></div>
                  <div>
                    <h4 class="gir-feature-title">Rich Biodiversity</h4>
                    <p class="gir-feature-sub">Flora &amp; Fauna</p>
                  </div>
                </div>

                <div class="gir-feature-box">
                  <div class="gir-feature-icon"><img src="assets/svg/icon-shield.svg" alt="Guide"></div>
                  <div>
                    <h4 class="gir-feature-title">Guided Experience</h4>
                    <p class="gir-feature-sub">Expert naturalists</p>
                  </div>
                </div>
              </div>
            </div>
          </section>

          <!-- 6. DESKTOP WHY TRAVEL FIRST HOLIDAYS (Split with Highway Bus Image) -->
          <section class="desktop-whyus-section" id="desktopWhyUs">
            <div class="desktop-whyus-container">
              <div class="whyus-left-content">
                <span class="featured-kicker">WHY TRAVEL FIRST HOLIDAYS</span>
                <h2 style="font-size: 36px; font-weight: 800; color: #121A16; margin-bottom: 6px;">Your Journey, Our Priority.</h2>
                <p style="font-size: 14px; color: var(--text-secondary-dark); line-height: 1.6;">
                  We ensure seamless coordination, luxurious private AC transport, and spiritual peace of mind for every family.
                </p>

                <div class="whyus-cards-grid">
                  <div class="whyus-card-desktop">
                    <div class="strip-icon" style="background:#FAF4EC; color:#0F382B; margin-bottom:10px;"><img src="assets/svg/icon-actravel.svg" alt="Travel"></div>
                    <h4 style="font-size:12.5px; font-weight:700; color:#1A241F;">Safe &amp; Comfortable Travel</h4>
                  </div>
                  <div class="whyus-card-desktop">
                    <div class="strip-icon" style="background:#FAF4EC; color:#0F382B; margin-bottom:10px;"><img src="assets/svg/icon-calendar.svg" alt="Itinerary"></div>
                    <h4 style="font-size:12.5px; font-weight:700; color:#1A241F;">Well-Planned Itineraries</h4>
                  </div>
                  <div class="whyus-card-desktop">
                    <div class="strip-icon" style="background:#FAF4EC; color:#0F382B; margin-bottom:10px;"><img src="assets/svg/icon-heart.svg" alt="Experience"></div>
                    <h4 style="font-size:12.5px; font-weight:700; color:#1A241F;">Memorable Experiences</h4>
                  </div>
                  <div class="whyus-card-desktop">
                    <div class="strip-icon" style="background:#FAF4EC; color:#0F382B; margin-bottom:10px;"><img src="assets/svg/icon-shield.svg" alt="Trust"></div>
                    <h4 style="font-size:12.5px; font-weight:700; color:#1A241F;">Trusted &amp; Reliable Service</h4>
                  </div>
                </div>
              </div>

              <!-- Right Media with Highway Bus & Innova -->
              <div class="whyus-right-media">
                <img src="assets/crops/package_vehicles.png" alt="Highway Travel Fleet" style="width:100%; height:100%; object-fit:cover;" onerror="this.src='assets/images/scenic_highway_bus.jpg'">
              </div>
            </div>
          </section>

          <!-- 7. DESKTOP CURATED ITINERARY (Horizontal Timeline with Connector Arrows) -->
          <section class="desktop-itinerary-section" id="desktopItinerary">
            <div class="desktop-itinerary-container">
              <div class="itinerary-top-row">
                <div>
                  <span class="desktop-hero-kicker" style="color: var(--gold-300);">4 DAYS, A LIFETIME OF MEMORIES</span>
                  <h2 style="font-size: 36px; font-weight: 800; color: #FFFFFF; margin-bottom: 6px;">Curated Itinerary</h2>
                  <p style="font-size: 14px; color: rgba(255, 255, 255, 0.78);">
                    A perfect blend of spirituality, wildlife and coastal beauty with well-planned routes and comfortable stays.
                  </p>
                </div>
                <button class="btn-hero-primary" onclick="openDayDetailModal(1)">
                  <span>View Detailed Itinerary</span>
                  <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                </button>
              </div>

              <div class="itinerary-timeline-horizontal">
                <!-- Day 1 -->
                <div class="itinerary-day-card-desktop" onclick="openDayDetailModal(1)">
                  <img src="assets/crops/day1_thumb.png" alt="Dwarka Day 1" class="day-card-media" onerror="this.src='assets/images/dwarka_retina.jpg'">
                  <div class="day-card-body">
                    <span class="day-card-kicker">Day 1</span>
                    <h3 class="day-card-title">Ahmedabad → Dwarka</h3>
                    <p class="day-card-desc">Pickup from Ahmedabad, Dwarkadhish Temple Evening Aarti</p>
                  </div>
                </div>

                <!-- Day 2 -->
                <div class="itinerary-day-card-desktop" onclick="openDayDetailModal(2)">
                  <img src="assets/crops/day2_thumb.png" alt="Somnath Day 2" class="day-card-media" onerror="this.src='assets/images/somnath_retina.jpg'">
                  <div class="day-card-body">
                    <span class="day-card-kicker">Day 2</span>
                    <h3 class="day-card-title">Dwarka → Somnath</h3>
                    <p class="day-card-desc">Nageshwar Jyotirling &amp; Triveni Sangam Confluence</p>
                  </div>
                </div>

                <!-- Day 3 -->
                <div class="itinerary-day-card-desktop" onclick="openDayDetailModal(3)">
                  <img src="assets/crops/day3_thumb.png" alt="Sasan Gir Day 3" class="day-card-media" onerror="this.src='assets/images/hero_lion_retina.jpg'">
                  <div class="day-card-body">
                    <span class="day-card-kicker">Day 3</span>
                    <h3 class="day-card-title">Somnath → Sasan Gir</h3>
                    <p class="day-card-desc">Forest Resort Check-in &amp; Relax, Evening at Leisure</p>
                  </div>
                </div>

                <!-- Day 4 -->
                <div class="itinerary-day-card-desktop" onclick="openDayDetailModal(4)">
                  <img src="assets/crops/day4_thumb.png" alt="Gir Safari Day 4" class="day-card-media" onerror="this.src='assets/images/gir_safari_retina.jpg'">
                  <div class="day-card-body">
                    <span class="day-card-kicker">Day 4</span>
                    <h3 class="day-card-title">Gir Safari &amp; Return</h3>
                    <p class="day-card-desc">Morning Open Gypsy Safari, Return Drop to Ahmedabad</p>
                  </div>
                </div>
              </div>
            </div>
          </section>

          <!-- 8. DESKTOP MOMENTS THROUGH THE LENS (5-Photo Strip) -->
          <section class="desktop-moments-section" id="desktopMoments">
            <div class="moments-container">
              <div class="desktop-section-header" style="margin-bottom: 24px;">
                <span class="desktop-hero-kicker" style="color: var(--gold-300);">THROUGH THE LENS</span>
                <h2 style="font-size: 36px; font-weight: 800; color: #FFFFFF;">Moments from Our Journeys</h2>
              </div>

              <div class="moments-photo-strip">
                <div class="moments-photo-item">
                  <img src="assets/images/hero_lion_retina.jpg" alt="Asiatic Lion Face">
                </div>
                <div class="moments-photo-item">
                  <img src="assets/crops/lens_photo_1.png" alt="Grand Temple Aarti" onerror="this.src='assets/images/temple_sunset_retina.jpg'">
                </div>
                <div class="moments-photo-item">
                  <img src="assets/crops/lens_photo_3.png" alt="Somnath Ocean Temple" onerror="this.src='assets/images/somnath_retina.jpg'">
                </div>
                <div class="moments-photo-item">
                  <img src="assets/images/lion_family_retina.jpg" alt="Lion Pride">
                </div>
                <div class="moments-photo-item">
                  <img src="assets/images/gir_safari_retina.jpg" alt="Open Jeep Safari in Gir">
                </div>
              </div>
            </div>
          </section>

          <!-- 9. DESKTOP LET'S PLAN YOUR HOLIDAY BANNER -->
          <section class="desktop-plan-banner-section">
            <img src="assets/crops/footer_banner.png" alt="Somnath Sunset Temple" class="plan-banner-bg" onerror="this.src='assets/images/temple_sunset_retina.jpg'">
            <div class="plan-banner-content">
              <span class="desktop-hero-kicker" style="color: var(--gold-300);">WHY TRAVEL FIRST HOLIDAYS</span>
              <h2 style="font-size: 38px; font-weight: 800; color: #FFFFFF; margin-bottom: 12px;">Let's Plan Your Gujarat Holiday</h2>
              <p style="font-size: 15px; color: rgba(255, 255, 255, 0.9); margin-bottom: 28px; line-height: 1.6;">
                Reach out to us for customized packages, group tours and memorable travel experiences.
              </p>

              <div style="display: flex; justify-content: center; gap: 16px;">
                <a href="https://wa.me/919876543210?text=Hi%20Travel%20First%20Holidays!%20Please%20help%20me%20plan%20my%20Gujarat%20Holiday." class="desktop-header-cta" style="padding: 14px 34px; font-size: 14.5px;" target="_blank" rel="noopener">
                  <img src="assets/svg/icon-whatsapp.svg" alt="WhatsApp" width="20" height="20">
                  <span>Enquire on WhatsApp</span>
                </a>
                <a href="tel:+919876543210" class="btn-hero-secondary" style="padding: 13px 30px; font-size: 14.5px;">
                  <img src="assets/svg/icon-call.svg" alt="Call Us" width="18" height="18" style="color:var(--gold-300);">
                  <span>Call Us</span>
                </a>
              </div>
            </div>
          </section>

          <!-- 10. DESKTOP RICH 5-COLUMN FOOTER -->
          <footer class="desktop-footer" id="desktopFooter">
            <div class="desktop-footer-container">
              <!-- Col 1: Brand & Tagline -->
              <div>
                <img src="assets/svg/brand-logo.svg" alt="Travel First Holidays" style="height: 48px; margin-bottom: 14px;">
                <p style="font-size: 12.5px; color: #94A3B8; margin-bottom: 18px; line-height: 1.5;">
                  Explore. Pray. Discover. Together.<br>
                  Gujarat's premier spiritual and wildlife tour operator.
                </p>
                <div class="footer-social-row">
                  <a href="#" class="footer-social-icon" title="Instagram">📷</a>
                  <a href="#" class="footer-social-icon" title="Facebook">📘</a>
                  <a href="#" class="footer-social-icon" title="YouTube">▶️</a>
                  <a href="#" class="footer-social-icon" title="Twitter / X">𝕏</a>
                </div>
              </div>

              <!-- Col 2: Quick Links -->
              <div>
                <h4 class="footer-col-title">Quick Links</h4>
                <ul class="footer-nav-list">
                  <li><a href="#desktopHero">Home</a></li>
                  <li><a href="#desktopFeatured">Tour Packages</a></li>
                  <li><a href="#desktopDestinations">Destinations</a></li>
                  <li><a href="#desktopWhyUs">About Us</a></li>
                  <li><a href="#desktopMoments">Gallery</a></li>
                  <li><a href="#desktopFooter">Contact</a></li>
                </ul>
              </div>

              <!-- Col 3: Top Destinations -->
              <div>
                <h4 class="footer-col-title">Top Destinations</h4>
                <ul class="footer-nav-list">
                  <li><a href="#desktopDestinations">Dwarka</a></li>
                  <li><a href="#desktopDestinations">Somnath</a></li>
                  <li><a href="#desktopGir">Sasan Gir</a></li>
                  <li><a href="#desktopDestinations">Nageshwar</a></li>
                  <li><a href="#desktopDestinations">Bet Dwarka</a></li>
                  <li><a href="#desktopDestinations">Triveni Sangam</a></li>
                </ul>
              </div>

              <!-- Col 4: Contact Us -->
              <div>
                <h4 class="footer-col-title">Contact Us</h4>
                <div class="footer-contact-item">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
                  <span>+91 98987 65123</span>
                </div>
                <div class="footer-contact-item">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
                  <span>+91 98984 56119</span>
                </div>
                <div class="footer-contact-item">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
                  <span>info@travelfirstholidays.com</span>
                </div>
                <div class="footer-contact-item">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
                  <span>Ahmedabad, Gujarat, India</span>
                </div>
              </div>

              <!-- Col 5: WhatsApp Action Card -->
              <div>
                <div class="footer-wa-card">
                  <div class="footer-wa-header">
                    <img src="assets/svg/icon-whatsapp.svg" alt="WhatsApp">
                    <div>
                      <h4 class="footer-wa-title">Plan Your Trip Today</h4>
                      <span style="font-size: 10px; color: #34D399; font-weight: 700;">Fast Response</span>
                    </div>
                  </div>
                  <p class="footer-wa-desc">
                    Get in touch for best customized packages, seasonal discounts, and special group offers.
                  </p>
                  <a href="https://wa.me/919876543210?text=Hi%20Travel%20First%20Holidays!%20Please%20share%20tour%20packages%20and%20rates." class="desktop-header-cta" style="justify-content:center; padding:10px 16px;" target="_blank" rel="noopener">
                    <span>Chat on WhatsApp</span>
                  </a>
                </div>
              </div>
            </div>

            <!-- Sub-footer Bottom Row -->
            <div class="sub-footer-row">
              <span>© 2024 Travel First Holidays. All Rights Reserved.</span>
              <div class="sub-footer-links">
                <a href="#">Privacy Policy</a>
                <a href="#">Terms &amp; Conditions</a>
                <a href="#">Cancellation Policy</a>
              </div>
              <span>Designed with ❤️ for incredible journeys</span>
            </div>
          </footer>

        </div>
        <!-- END DESKTOP WEBSITE LANDING PAGE -->
'''

# Insert desktop_markup before the closing </article> or device-screen-viewport
if '</article>' in html:
    html = html.replace('</article>', '</article>\n' + desktop_markup)
    print("Desktop markup inserted successfully!")
else:
    print("Could not find </article>!")

# 4. Add Desktop Persistent Floating Actions right before </body>
desktop_float_actions = '''
  <!-- PERSISTENT FLOATING ACTIONS (ALWAYS VISIBLE ON DESKTOP & MOBILE AT ALL SCROLL POSITIONS) -->
  <div class="desktop-floating-actions" aria-label="Always-Visible Quick Contact">
    <a href="https://wa.me/919876543210?text=Hello%20Travel%20First%20Holidays!%20I%20want%20to%20enquire%20about%20Gujarat%20Tour%20Packages." class="float-pill-wa" target="_blank" rel="noopener" title="Chat on WhatsApp">
      <img src="assets/svg/icon-whatsapp.svg" alt="WhatsApp" width="20" height="20">
      <span>WhatsApp Us</span>
    </a>
    <a href="tel:+919876543210" class="float-pill-call" title="Call Us Directly">
      <img src="assets/svg/icon-call.svg" alt="Call Us" width="16" height="16">
      <span>Call +91 98987 65123</span>
    </a>
  </div>
'''

if 'desktop-floating-actions' not in html:
    html = html.replace('</body>', desktop_float_actions + '\n</body>')
    print("Desktop floating actions added!")

with open('D:/hussain/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html successfully!")

