/**
 * APPLICATION LOGIC & INTERACTIVITY
 * Engineered with 10-year UI/UX expert standards
 */

document.addEventListener('DOMContentLoaded', () => {
  initPresentationModes();
  initInteractiveMap();
  initBookingCalculator();
  initModals();
  initCarousel();
  initModernWebFallbacks();
  initSpecsDrawer();
});

/* ==========================================================================
   1. PRESENTATION VIEWPORT SWITCHER (Safe No-Op in Production)
   ========================================================================== */
function initPresentationModes() {
  const stageCanvas = document.getElementById('stageCanvas');
  const viewBtns = document.querySelectorAll('.view-tab-btn');
  if (!stageCanvas || !viewBtns.length) return;

  viewBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const targetMode = btn.dataset.mode;
      viewBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      stageCanvas.className = `stage-canvas mode-${targetMode}`;
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  });
}

/* ==========================================================================
   2. INTERACTIVE ROUTE MAP CONTROLLER
   ========================================================================== */
function initInteractiveMap() {
  const playBtn = document.getElementById('btnPlayMapAnim');
  const carEl = document.getElementById('animatedTourCar');
  const routePath = document.getElementById('tourRoutePath');
  const waypoints = document.querySelectorAll('.map-waypoint');

  if (!routePath || !carEl) return;

  const pathLength = routePath.getTotalLength();
  let animFrameId = null;
  let isPlaying = false;

  // Waypoint click events
  waypoints.forEach(wp => {
    wp.addEventListener('click', (e) => {
      e.stopPropagation();
      const dayIndex = parseInt(wp.dataset.day, 10);
      highlightWaypoint(dayIndex);
    });
  });

  if (playBtn) {
    playBtn.addEventListener('click', () => {
      if (isPlaying) {
        cancelAnimationFrame(animFrameId);
        isPlaying = false;
        playBtn.innerHTML = '<span>▶</span> Simulate';
        return;
      }

      isPlaying = true;
      playBtn.innerHTML = '<span>⏸</span> Pause';
      animateCarAlongPath(0);
    });
  }

  function animateCarAlongPath(startTime) {
    const duration = 6500; // 6.5s smooth tour
    const start = performance.now();

    function step(now) {
      if (!isPlaying) return;
      const elapsed = now - start;
      const progress = Math.min(elapsed / duration, 1);
      
      const distance = progress * pathLength;
      const point = routePath.getPointAtLength(distance);

      // Check orientation angle
      const nextPoint = routePath.getPointAtLength(Math.min(distance + 2, pathLength));
      const angle = Math.atan2(nextPoint.y - point.y, nextPoint.x - point.x) * (180 / Math.PI);

      carEl.setAttribute('transform', `translate(${point.x}, ${point.y}) rotate(${angle})`);

      if (progress < 1) {
        animFrameId = requestAnimationFrame(step);
      } else {
        isPlaying = false;
        if (playBtn) playBtn.innerHTML = '<span>▶</span> Replay';
      }
    }

    animFrameId = requestAnimationFrame(step);
  }

  function highlightWaypoint(dayIndex) {
    if (dayIndex === 0) {
      alert("Ahmedabad: Tour Pickup & Drop Hub\nDistance to Dwarka: ~440 km\nComplimentary Airport/Station pickup included.");
    } else {
      openDayDetailModal(dayIndex);
    }
  }
}

/* ==========================================================================
   3. INTERACTIVE BOOKING CALCULATOR & WHATSAPP GENERATOR
   ========================================================================== */
function initBookingCalculator() {
  const basePricePerPerson = GUJARAT_TOUR_DATA.basePrice; // 9999
  let travelersCount = 2;
  let selectedVehicle = 'bus';
  let selectedHotel = 'standard';

  const countDisplay = document.getElementById('calcTravelersCount');
  const btnMinus = document.getElementById('calcMinusTravelers');
  const btnPlus = document.getElementById('calcPlusTravelers');
  const totalPriceDisplay = document.getElementById('calcTotalPrice');
  const btnConfirmWa = document.getElementById('btnConfirmWhatsApp');
  const dateInput = document.getElementById('bookingDateInput');

  // Set default date to next Friday
  if (dateInput) {
    const nextFri = new Date();
    nextFri.setDate(nextFri.getDate() + ((7 - nextFri.getDay() + 5) % 7 || 7));
    dateInput.value = nextFri.toISOString().split('T')[0];
  }

  function updatePrice() {
    const isPrivate = (selectedVehicle === 'private');
    let hotelSurcharge = selectedHotel === 'heritage' ? 2200 : 0;
    
    let perPersonTotal = basePricePerPerson + hotelSurcharge;
    let grandTotal = perPersonTotal * travelersCount;

    if (countDisplay) countDisplay.textContent = travelersCount;
    if (totalPriceDisplay) {
      if (isPrivate) {
        totalPriceDisplay.textContent = `₹${grandTotal.toLocaleString('en-IN')}/- + Cab Custom`;
      } else {
        totalPriceDisplay.textContent = `₹${grandTotal.toLocaleString('en-IN')}/-`;
      }
    }

    // Synchronize form hidden fields for DRF API submission
    const hiddenTravelers = document.getElementById('bookingTravelersInput');
    if (hiddenTravelers) hiddenTravelers.value = travelersCount;
    const hiddenTotalPrice = document.getElementById('bookingTotalPriceInput');
    if (hiddenTotalPrice) hiddenTotalPrice.value = grandTotal;

    // Update WhatsApp link
    if (btnConfirmWa) {
      const travelDate = dateInput ? dateInput.value : "Upcoming Date";
      const vehicleDesc = isPrivate 
        ? "Private AC Cab (Innova Crysta / Sedan upgrade requested)" 
        : "Group AC Luxury Coach Bus (Included in ₹9,999/- base fare)";
      const hotelDesc = selectedHotel === 'heritage' ? "Luxury Heritage 4★ Resort" : "Deluxe 3★ AC Hotel";

      const waMsg = encodeURIComponent(
        `Hello Travel First Holidays! 🌟\n\nI want to book the *Dwarka – Somnath – Sasan Gir 4D/3N Tour*.\n` +
        `• Travelers: ${travelersCount} Person(s)\n` +
        `• Travel Date: ${travelDate}\n` +
        `• Travel Mode: ${vehicleDesc}\n` +
        `• Accommodation: ${hotelDesc}\n` +
        (isPrivate 
          ? `• Base Fare: ₹${grandTotal.toLocaleString('en-IN')}/- (Please share customized private cab quote & vehicle options)\n\n` 
          : `• Estimated Total: ₹${grandTotal.toLocaleString('en-IN')}/- (All taxes & Group Bus included)\n\n`) +
        `Please confirm seat availability and send booking details!`
      );
      btnConfirmWa.href = `https://wa.me/${GUJARAT_TOUR_DATA.whatsappNumber}?text=${waMsg}`;
    }
  }

  // Expose for form resets
  window.recalcBookingDrawerPrice = () => {
    travelersCount = 2;
    selectedVehicle = 'bus';
    selectedHotel = 'standard';
    if (dateInput) {
      const nextFri = new Date();
      nextFri.setDate(nextFri.getDate() + ((7 - nextFri.getDay() + 5) % 7 || 7));
      dateInput.value = nextFri.toISOString().split('T')[0];
    }
    updatePrice();
  };

  if (btnMinus) {
    btnMinus.addEventListener('click', () => {
      if (travelersCount > 1) {
        travelersCount--;
        updatePrice();
      }
    });
  }

  if (btnPlus) {
    btnPlus.addEventListener('click', () => {
      if (travelersCount < 20) {
        travelersCount++;
        updatePrice();
      }
    });
  }

  document.querySelectorAll('input[name="vehicleChoice"]').forEach(radio => {
    radio.addEventListener('change', (e) => {
      selectedVehicle = e.target.value;
      updatePrice();
    });
  });

  document.querySelectorAll('input[name="hotelChoice"]').forEach(radio => {
    radio.addEventListener('change', (e) => {
      selectedHotel = e.target.value;
      updatePrice();
    });
  });

  if (dateInput) {
    dateInput.addEventListener('change', updatePrice);
  }

  updatePrice();
}

/* ==========================================================================
   4. MODALS & DRAWERS
   ========================================================================== */
function initModals() {
  const bookingDrawer = document.getElementById('bookingDrawerModal');
  const openBookingBtns = document.querySelectorAll('.trigger-booking-modal');
  const closeBtns = document.querySelectorAll('.modal-close-trigger');

  openBookingBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      if (bookingDrawer) bookingDrawer.classList.add('is-open');
    });
  });

  closeBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.modal-overlay').forEach(m => m.classList.remove('is-open'));
    });
  });

  // Close on backdrop click
  document.querySelectorAll('.modal-overlay').forEach(modal => {
    modal.addEventListener('click', (e) => {
      if (e.target === modal) {
        modal.classList.remove('is-open');
      }
    });
  });

  // Close on Escape key
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      document.querySelectorAll('.modal-overlay').forEach(m => m.classList.remove('is-open'));
    }
  });

  // Destination & Day detail handlers
  document.querySelectorAll('.trigger-dest-modal').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const destId = btn.dataset.destId;
      openDestDetailModal(destId);
    });
  });

  document.querySelectorAll('.timeline-step').forEach(step => {
    step.addEventListener('click', () => {
      const dayNum = parseInt(step.dataset.day, 10);
      openDayDetailModal(dayNum);
    });
  });

  // Video Teaser trigger
  const triggerVideoBtn = document.getElementById('triggerGirVideo');
  if (triggerVideoBtn) {
    triggerVideoBtn.addEventListener('click', () => {
      const videoModal = document.getElementById('videoPlayerModal');
      if (videoModal) videoModal.classList.add('is-open');
    });
  }
}

function openDayDetailModal(dayNum) {
  const dayData = GUJARAT_TOUR_DATA.itinerary.find(d => d.day === dayNum);
  if (!dayData) return;

  const modal = document.getElementById('detailDrawerModal');
  const titleEl = document.getElementById('detailDrawerTitle');
  const bodyEl = document.getElementById('detailDrawerBody');

  if (titleEl) titleEl.textContent = `Day ${dayData.day}: ${dayData.route}`;
  
  let scheduleHtml = `<div style="margin-bottom: 16px;">
    <p style="font-size: 13px; font-weight: 700; color: #14533D; margin-bottom: 4px;">${dayData.title}</p>
    <p style="font-size: 11px; color: #52635B; margin-bottom: 12px;">Distance & Time: <strong>${dayData.distance}</strong></p>
    <div style="display: flex; flex-direction: column; gap: 8px;">`;

  dayData.schedule.forEach(item => {
    scheduleHtml += `
      <div style="display: flex; gap: 10px; font-size: 11.5px; line-height: 1.4;">
        <span style="font-weight: 700; color: #B45309; min-width: 65px;">${item.time}</span>
        <span style="color: #1A241F;">${item.event}</span>
      </div>`;
  });

  scheduleHtml += `</div></div>
  <button class="btn-primary-gold trigger-booking-modal" style="width: 100%;" onclick="document.getElementById('detailDrawerModal').classList.remove('is-open'); document.getElementById('bookingDrawerModal').classList.add('is-open');">
    Book This Day / Package →
  </button>`;

  if (bodyEl) bodyEl.innerHTML = scheduleHtml;
  if (modal) modal.classList.add('is-open');
}

function openDestDetailModal(destId) {
  const dest = GUJARAT_TOUR_DATA.destinations.find(d => d.id === destId);
  if (!dest) return;

  const modal = document.getElementById('detailDrawerModal');
  const titleEl = document.getElementById('detailDrawerTitle');
  const bodyEl = document.getElementById('detailDrawerBody');

  if (titleEl) titleEl.textContent = `${dest.name} Spotlight`;

  let contentHtml = `
    <div style="margin-bottom: 16px;">
      <img src="${dest.retinaImg || dest.heroImg}" style="width: 100%; height: 180px; object-fit: cover; border-radius: 12px; margin-bottom: 12px;" alt="${dest.name}">
      <p style="font-size: 13px; font-weight: 700; color: #121A16; margin-bottom: 4px;">${dest.tagline}</p>
      <p style="font-size: 11.5px; color: #52635B; line-height: 1.5; margin-bottom: 12px;">${dest.description}</p>
      <div style="background: #FDF8EE; padding: 10px 12px; border-radius: 8px; border-left: 3px solid #D4AF37; margin-bottom: 14px;">
        <p style="font-size: 10.5px; font-weight: 700; color: #92400E; margin-bottom: 2px;">Darshan / Safari Timings</p>
        <p style="font-size: 11px; color: #1A1202;">${dest.timings}</p>
      </div>
      <h4 style="font-size: 12px; font-weight: 700; margin-bottom: 8px; color: #14533D;">Key Highlights</h4>
      <ul style="font-size: 11px; color: #2B261F; padding-left: 18px; margin-bottom: 16px; line-height: 1.6;">
        ${dest.highlights.map(h => `<li>${h}</li>`).join('')}
      </ul>
      <button class="btn-primary-gold" style="width: 100%;" onclick="document.getElementById('detailDrawerModal').classList.remove('is-open'); document.getElementById('bookingDrawerModal').classList.add('is-open');">
        Plan Visit to ${dest.name} →
      </button>
    </div>`;

  if (bodyEl) bodyEl.innerHTML = contentHtml;
  if (modal) modal.classList.add('is-open');
}

/* ==========================================================================
   5. PHOTO CAROUSEL & LIGHTBOX
   ========================================================================== */
function initCarousel() {
  const track = document.getElementById('lensTrack');
  const prevBtn = document.getElementById('lensPrevBtn');
  const nextBtn = document.getElementById('lensNextBtn');

  if (!track) return;

  if (prevBtn) {
    prevBtn.addEventListener('click', () => {
      track.scrollBy({ left: -140, behavior: 'smooth' });
    });
  }

  if (nextBtn) {
    nextBtn.addEventListener('click', () => {
      track.scrollBy({ left: 140, behavior: 'smooth' });
    });
  }

  // Lightbox click on slides
  document.querySelectorAll('.lens-slide, .gir-thumb-item').forEach(item => {
    item.addEventListener('click', () => {
      const img = item.querySelector('img');
      if (img) openLightbox(img.src, img.alt);
    });
  });
}

function openLightbox(src, alt) {
  const modal = document.getElementById('lightboxModal');
  const imgEl = document.getElementById('lightboxImg');
  const captionEl = document.getElementById('lightboxCaption');

  if (imgEl) imgEl.src = src;
  if (captionEl) captionEl.textContent = alt || 'Gujarat Travel Memories';
  if (modal) modal.classList.add('is-open');
}

/* ==========================================================================
   6. MODERN WEB GUIDANCE COMPLIANCE
   ========================================================================== */
function initModernWebFallbacks() {
  // Guidance fallback for hidden="until-found"
  if (!('onbeforematch' in HTMLElement.prototype)) {
    document.querySelectorAll('[hidden="until-found"]').forEach((el) => {
      el.removeAttribute('hidden');
    });
  }
}

/* ==========================================================================
   7. DESIGN SYSTEM SPECS DRAWER
   ========================================================================== */
function initSpecsDrawer() {
  const toggleBtn = document.getElementById('btnToggleSpecs');
  const drawerBackdrop = document.getElementById('specsDrawerBackdrop');
  const closeBtn = document.getElementById('btnCloseSpecs');

  if (toggleBtn && drawerBackdrop) {
    toggleBtn.addEventListener('click', () => {
      drawerBackdrop.classList.add('is-open');
    });
  }

  if (closeBtn && drawerBackdrop) {
    closeBtn.addEventListener('click', () => {
      drawerBackdrop.classList.remove('is-open');
    });
  }

  if (drawerBackdrop) {
    drawerBackdrop.addEventListener('click', (e) => {
      if (e.target === drawerBackdrop) {
        drawerBackdrop.classList.remove('is-open');
      }
    });
  }
}

