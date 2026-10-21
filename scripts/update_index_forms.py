import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update plan-banner-section to include the Quick Inquiry Card Form
old_plan_section = """    <section class="plan-banner-section">
      <img src="assets/crops/footer_banner.png" alt="Somnath Sunset Temple" class="plan-bg-img" onerror="this.src='assets/images/temple_sunset_retina.jpg'">
      <div class="plan-box-content">
        <span class="section-kicker">WHY TRAVEL FIRST HOLIDAYS</span>
        <h2 style="font-size: clamp(28px, 4vw, 42px); font-weight: 800; color: #FFFFFF; margin-bottom: 12px;">Let's Plan Your Gujarat Holiday</h2>
        <p style="font-size: 15px; color: rgba(255, 255, 255, 0.9); margin-bottom: 28px; line-height: 1.6;">
          Reach out to our Saurashtra travel experts for customized group bookings, senior pilgrim care, and memorable travel experiences.
        </p>

        <div class="plan-actions-row">
          <a href="https://wa.me/919876543210?text=Hi%20Travel%20First%20Holidays!%20Please%20help%20me%20plan%20my%20Gujarat%20Tour%20Package." class="btn-hero-primary" style="padding: 14px 34px;" target="_blank" rel="noopener">
            <img src="assets/svg/icon-whatsapp.svg" alt="WhatsApp" width="20" height="20">
            <span>Enquire on WhatsApp</span>
          </a>
          <a href="tel:+919876543210" class="btn-hero-secondary" style="padding: 13px 30px;">
            <img src="assets/svg/icon-call.svg" alt="Call Us" width="18" height="18" style="color:var(--gold-300);">
            <span>Call Us</span>
          </a>
        </div>
      </div>
    </section>"""

new_plan_section = """    <section class="plan-banner-section" id="sectionInquiry">
      <img src="assets/crops/footer_banner.png" alt="Somnath Sunset Temple" class="plan-bg-img" onerror="this.src='assets/images/temple_sunset_retina.jpg'">
      <div class="container">
        <div class="plan-inquiry-container">
          <div class="plan-box-content">
            <span class="section-kicker">WHY TRAVEL FIRST HOLIDAYS</span>
            <h2 style="font-size: clamp(28px, 4vw, 42px); font-weight: 800; color: #FFFFFF; margin-bottom: 12px;">Let's Plan Your Gujarat Holiday</h2>
            <p style="font-size: 15px; color: rgba(255, 255, 255, 0.9); margin-bottom: 24px; line-height: 1.6;">
              Reach out to our Saurashtra travel experts for customized group bookings, senior pilgrim care, and memorable travel experiences.
            </p>

            <div class="plan-actions-row" style="justify-content: flex-start; margin-bottom: 20px;">
              <a href="https://wa.me/919876543210?text=Hi%20Travel%20First%20Holidays!%20Please%20help%20me%20plan%20my%20Gujarat%20Tour%20Package." class="btn-hero-primary" style="padding: 12px 28px;" target="_blank" rel="noopener">
                <img src="assets/svg/icon-whatsapp.svg" alt="WhatsApp" width="18" height="18">
                <span>Enquire on WhatsApp</span>
              </a>
              <a href="tel:+919876543210" class="btn-hero-secondary" style="padding: 11px 24px;">
                <img src="assets/svg/icon-call.svg" alt="Call Us" width="16" height="16" style="color:var(--gold-300);">
                <span>Call Us Directly</span>
              </a>
            </div>

            <div style="font-size: 12px; color: #94A3B8; display: flex; align-items: center; gap: 8px;">
              <span style="color: var(--gold-400);">★ 4.9/5 Rating</span>
              <span>•</span>
              <span>5,000+ Happy Pilgrims &amp; Travelers</span>
            </div>
          </div>

          <!-- Quick Callback & Inquiry Form Card -->
          <div class="plan-inquiry-card">
            <div style="margin-bottom: 16px;">
              <span style="font-size: 10px; font-weight: 800; color: var(--gold-400); letter-spacing: 1.5px; text-transform: uppercase;">EXPERT CONSULTATION</span>
              <h3 style="font-size: 20px; font-weight: 700; color: #FFFFFF; margin-top: 2px;">Request a Custom Tour Plan</h3>
              <p style="font-size: 12px; color: #94A3B8; margin-top: 4px;">Get custom dates, family discounts, and private vehicle quotes.</p>
            </div>

            <form id="inquiryForm" class="inquiry-card-form" novalidate>
              <div class="form-field-group">
                <label for="inquiryFullName" class="form-field-label">Full Name <span class="required-mark">*</span></label>
                <input type="text" id="inquiryFullName" name="full_name" class="form-control-input" placeholder="e.g. Priya Sharma" autocomplete="name" required>
                <div class="field-error-msg" id="error-inquiryFullName"></div>
              </div>

              <div class="form-row-2col">
                <div class="form-field-group">
                  <label for="inquiryPhone" class="form-field-label">Phone Number <span class="required-mark">*</span></label>
                  <input type="tel" id="inquiryPhone" name="phone" class="form-control-input" placeholder="e.g. 9876543210" autocomplete="tel" required>
                  <div class="field-error-msg" id="error-inquiryPhone"></div>
                </div>

                <div class="form-field-group">
                  <label for="inquiryEmail" class="form-field-label">Email Address <span class="required-mark">*</span></label>
                  <input type="email" id="inquiryEmail" name="email" class="form-control-input" placeholder="e.g. priya@example.com" autocomplete="email" required>
                  <div class="field-error-msg" id="error-inquiryEmail"></div>
                </div>
              </div>

              <div class="form-field-group">
                <label for="inquiryDestination" class="form-field-label">Tour Package / Destination <span class="optional-label">(Select)</span></label>
                <select id="inquiryDestination" name="destination" class="form-control-select">
                  <option value="Gujarat Signature Tour (4D/3N: Dwarka, Somnath, Gir)">Gujarat Signature Tour (4D/3N: Dwarka, Somnath, Gir)</option>
                  <option value="Dwarka &amp; Somnath Sacred Darshan (3D/2N)">Dwarka &amp; Somnath Sacred Darshan (3D/2N)</option>
                  <option value="Sasan Gir Asiatic Lion Wildlife Safari (2D/1N)">Sasan Gir Asiatic Lion Wildlife Safari (2D/1N)</option>
                  <option value="Customized Family Pilgrimage &amp; Private Cab Tour">Customized Family Pilgrimage &amp; Private Cab Tour</option>
                </select>
              </div>

              <div class="form-field-group">
                <label for="inquiryMessage" class="form-field-label">Your Travel Notes / Requirements <span class="optional-label">(Optional)</span></label>
                <textarea id="inquiryMessage" name="message" class="form-control-textarea" rows="2" placeholder="e.g. Traveling with 4 adults and 2 children in November"></textarea>
              </div>

              <div id="inquiryFormStatus" class="form-status-alert" role="alert" aria-live="polite"></div>

              <button type="submit" id="btnSubmitInquiry" class="btn-hero-primary btn-submit-action" style="width: 100%; justify-content: center; padding: 13px;">
                <span class="btn-label-text">Request Tour Callback</span>
                <span class="btn-loading-spinner" aria-hidden="true"></span>
              </button>
            </form>
          </div>
        </div>
      </div>
    </section>"""

# Normalize CRLF/LF for replacement
html_normalized = html.replace('\r\n', '\n')
old_plan_normalized = old_plan_section.replace('\r\n', '\n')
new_plan_normalized = new_plan_section.replace('\r\n', '\n')

if old_plan_normalized in html_normalized:
    html_normalized = html_normalized.replace(old_plan_normalized, new_plan_normalized)
    print("Plan section updated successfully!")
else:
    print("WARNING: Old plan section not matched!")

# 2. Update bookingDrawerModal content to be a full form
old_booking_modal_content = """      <div style="display: flex; flex-direction: column; gap: 16px;">
        <!-- Travel Date -->
        <div>
          <label for="bookingDateInput" style="display: block; font-size: 11px; font-weight: 700; color: #52635B; margin-bottom: 6px;">SELECT TRAVEL DATE</label>
          <input type="date" id="bookingDateInput" style="width: 100%; padding: 10px 14px; border: 1.5px solid #CBD5E1; border-radius: 10px; font-family: inherit; font-size: 13px; font-weight: 600; color: #1E293B;">
        </div>

        <!-- Travelers Counter -->
        <div>
          <label style="display: block; font-size: 11px; font-weight: 700; color: #52635B; margin-bottom: 6px;">NUMBER OF TRAVELERS</label>
          <div style="display: flex; align-items: center; justify-content: space-between; background: #F8FAFC; border: 1px solid #E2E8F0; padding: 8px 14px; border-radius: 12px;">
            <span style="font-size: 13px; font-weight: 600; color: #1E293B;">Seats / Guests (12+ years)</span>
            <div style="display: flex; align-items: center; gap: 12px;">
              <button id="calcMinusTravelers" style="width: 32px; height: 32px; border-radius: 50%; background: #E2E8F0; font-size: 18px; font-weight: 700; color: #1E293B; display: flex; align-items: center; justify-content: center;">-</button>
              <span id="calcTravelersCount" style="font-size: 16px; font-weight: 800; min-width: 24px; text-align: center; color: #0F172A;">2</span>
              <button id="calcPlusTravelers" style="width: 32px; height: 32px; border-radius: 50%; background: var(--gold-400); font-size: 18px; font-weight: 700; color: #1A1202; display: flex; align-items: center; justify-content: center;">+</button>
            </div>
          </div>
        </div>

        <!-- Travel Mode Selection (Group Bus vs Private Cab Option) -->
        <div>
          <label style="display: block; font-size: 11px; font-weight: 700; color: #52635B; margin-bottom: 6px;">TRAVEL MODE &amp; VEHICLE</label>
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
            <label style="display: flex; flex-direction: column; padding: 12px; border: 2px solid var(--gold-400); background: #FFFDF7; border-radius: 12px; cursor: pointer;">
              <div style="display: flex; align-items: center; gap: 6px; margin-bottom: 4px;">
                <input type="radio" name="vehicleChoice" value="bus" checked>
                <span style="font-size: 12px; font-weight: 800; color: #1E293B;">Group AC Bus</span>
              </div>
              <span style="font-size: 10px; color: #047857; font-weight: 700;">Standard • ₹9,999/person</span>
              <span style="font-size: 9px; color: #64748B; margin-top: 2px;">2x2 Pushback AC Coach</span>
            </label>

            <label style="display: flex; flex-direction: column; padding: 12px; border: 1.5px solid #CBD5E1; border-radius: 12px; cursor: pointer;">
              <div style="display: flex; align-items: center; gap: 6px; margin-bottom: 4px;">
                <input type="radio" name="vehicleChoice" value="private">
                <span style="font-size: 12px; font-weight: 800; color: #1E293B;">Private AC Cab</span>
              </div>
              <span style="font-size: 10px; color: #B45309; font-weight: 700;">Innova / Sedan Upgrade</span>
              <span style="font-size: 9px; color: #64748B; margin-top: 2px;">Custom quote on WhatsApp</span>
            </label>
          </div>
        </div>

        <!-- Hotel Category -->
        <div>
          <label style="display: block; font-size: 11px; font-weight: 700; color: #52635B; margin-bottom: 6px;">HOTEL CATEGORY</label>
          <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 8px;">
            <label style="display: flex; align-items: center; gap: 8px; padding: 10px 12px; border: 1.5px solid #E2E8F0; border-radius: 10px; cursor: pointer;">
              <input type="radio" name="hotelChoice" value="standard" checked>
              <div>
                <p style="font-size: 11.5px; font-weight: 700; color: #1E293B;">Deluxe 3★ AC</p>
                <p style="font-size: 9px; color: #64748B;">Included in Base Fare</p>
              </div>
            </label>
            <label style="display: flex; align-items: center; gap: 8px; padding: 10px 12px; border: 1.5px solid var(--gold-400); background: #FFFDF7; border-radius: 10px; cursor: pointer;">
              <input type="radio" name="hotelChoice" value="heritage">
              <div>
                <p style="font-size: 11.5px; font-weight: 700; color: #1E293B;">Luxury Heritage 4★</p>
                <p style="font-size: 9px; color: #B45309;">Pool &amp; Campfire Resort</p>
              </div>
            </label>
          </div>
        </div>

        <!-- Price Summary & CTAs -->
        <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 14px; padding: 14px;">
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
            <span style="font-size: 11px; font-weight: 600; color: #64748B;">Estimated Total (All Taxes Incl.):</span>
            <span id="calcTotalPrice" style="font-size: 22px; font-weight: 800; color: #14533D;">₹19,998/-</span>
          </div>
          <p style="font-size: 9.5px; color: #10B981; font-weight: 600;">✓ Includes Sasan Gir Safari Pass, AC Travel, 3N Stay &amp; Meals</p>
        </div>

        <a id="btnConfirmWhatsApp" href="#" class="btn-hero-primary" style="width: 100%; justify-content: center; padding: 14px;" target="_blank" rel="noopener">
          <img src="assets/svg/icon-whatsapp.svg" alt="WhatsApp" width="20" height="20">
          <span>Confirm &amp; Book on WhatsApp</span>
        </a>
      </div>"""

new_booking_modal_content = """      <form id="bookingForm" class="booking-form" novalidate>
        <!-- Contact Details -->
        <div class="form-field-group">
          <label for="bookingFullName" class="form-field-label">Full Name <span class="required-mark">*</span></label>
          <input type="text" id="bookingFullName" name="full_name" class="form-control-input" placeholder="e.g. Ramesh Patel" autocomplete="name" required>
          <div class="field-error-msg" id="error-bookingFullName"></div>
        </div>

        <div class="form-row-2col">
          <div class="form-field-group">
            <label for="bookingPhone" class="form-field-label">Phone Number <span class="required-mark">*</span></label>
            <input type="tel" id="bookingPhone" name="phone" class="form-control-input" placeholder="e.g. 9876543210" autocomplete="tel" required>
            <div class="field-error-msg" id="error-bookingPhone"></div>
          </div>
          <div class="form-field-group">
            <label for="bookingEmail" class="form-field-label">Email Address <span class="required-mark">*</span></label>
            <input type="email" id="bookingEmail" name="email" class="form-control-input" placeholder="e.g. ramesh@example.com" autocomplete="email" required>
            <div class="field-error-msg" id="error-bookingEmail"></div>
          </div>
        </div>

        <!-- Travel Date -->
        <div class="form-field-group">
          <label for="bookingDateInput" class="form-field-label">Select Travel Date <span class="required-mark">*</span></label>
          <input type="date" id="bookingDateInput" name="travel_date" class="form-control-input" required>
          <div class="field-error-msg" id="error-bookingDateInput"></div>
        </div>

        <!-- Travelers Counter -->
        <div class="form-field-group">
          <label class="form-field-label">Number of Travelers <span class="required-mark">*</span></label>
          <div style="display: flex; align-items: center; justify-content: space-between; background: #F8FAFC; border: 1.5px solid #CBD5E1; padding: 8px 14px; border-radius: 10px;">
            <span style="font-size: 13px; font-weight: 600; color: #1E293B;">Seats / Guests (12+ years)</span>
            <div style="display: flex; align-items: center; gap: 12px;">
              <button type="button" id="calcMinusTravelers" style="width: 32px; height: 32px; border-radius: 50%; background: #E2E8F0; font-size: 18px; font-weight: 700; color: #1E293B; display: flex; align-items: center; justify-content: center; border: none; cursor: pointer;">-</button>
              <span id="calcTravelersCount" style="font-size: 16px; font-weight: 800; min-width: 24px; text-align: center; color: #0F172A;">2</span>
              <button type="button" id="calcPlusTravelers" style="width: 32px; height: 32px; border-radius: 50%; background: var(--gold-400); font-size: 18px; font-weight: 700; color: #1A1202; display: flex; align-items: center; justify-content: center; border: none; cursor: pointer;">+</button>
            </div>
          </div>
          <input type="hidden" id="bookingTravelersInput" name="travelers_count" value="2">
          <div class="field-error-msg" id="error-bookingTravelersInput"></div>
        </div>

        <!-- Travel Mode Selection (Group Bus vs Private Cab Option) -->
        <div class="form-field-group">
          <label class="form-field-label">Travel Mode &amp; Vehicle</label>
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
            <label style="display: flex; flex-direction: column; padding: 12px; border: 2px solid var(--gold-400); background: #FFFDF7; border-radius: 12px; cursor: pointer;">
              <div style="display: flex; align-items: center; gap: 6px; margin-bottom: 4px;">
                <input type="radio" name="vehicleChoice" value="bus" checked>
                <span style="font-size: 12px; font-weight: 800; color: #1E293B;">Group AC Bus</span>
              </div>
              <span style="font-size: 10px; color: #047857; font-weight: 700;">Standard • ₹9,999/person</span>
              <span style="font-size: 9px; color: #64748B; margin-top: 2px;">2x2 Pushback AC Coach</span>
            </label>

            <label style="display: flex; flex-direction: column; padding: 12px; border: 1.5px solid #CBD5E1; border-radius: 12px; cursor: pointer;">
              <div style="display: flex; align-items: center; gap: 6px; margin-bottom: 4px;">
                <input type="radio" name="vehicleChoice" value="private">
                <span style="font-size: 12px; font-weight: 800; color: #1E293B;">Private AC Cab</span>
              </div>
              <span style="font-size: 10px; color: #B45309; font-weight: 700;">Innova / Sedan Upgrade</span>
              <span style="font-size: 9px; color: #64748B; margin-top: 2px;">Custom quote on WhatsApp</span>
            </label>
          </div>
        </div>

        <!-- Hotel Category -->
        <div class="form-field-group">
          <label class="form-field-label">Hotel Category</label>
          <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 8px;">
            <label style="display: flex; align-items: center; gap: 8px; padding: 10px 12px; border: 1.5px solid #E2E8F0; border-radius: 10px; cursor: pointer;">
              <input type="radio" name="hotelChoice" value="standard" checked>
              <div>
                <p style="font-size: 11.5px; font-weight: 700; color: #1E293B; margin: 0;">Deluxe 3★ AC</p>
                <p style="font-size: 9px; color: #64748B; margin: 2px 0 0;">Included in Base Fare</p>
              </div>
            </label>
            <label style="display: flex; align-items: center; gap: 8px; padding: 10px 12px; border: 1.5px solid var(--gold-400); background: #FFFDF7; border-radius: 10px; cursor: pointer;">
              <input type="radio" name="hotelChoice" value="heritage">
              <div>
                <p style="font-size: 11.5px; font-weight: 700; color: #1E293B; margin: 0;">Luxury Heritage 4★</p>
                <p style="font-size: 9px; color: #B45309; margin: 2px 0 0;">Pool &amp; Campfire Resort</p>
              </div>
            </label>
          </div>
        </div>

        <!-- Special Requests / Notes -->
        <div class="form-field-group">
          <label for="bookingNotes" class="form-field-label">Pickup Point / Special Requests <span class="optional-label">(Optional)</span></label>
          <textarea id="bookingNotes" name="special_requests" class="form-control-textarea" rows="2" placeholder="e.g. Pickup at Ahmedabad station, vegetarian/Jain meal preference, senior assistance"></textarea>
        </div>

        <!-- Price Summary -->
        <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 14px; padding: 14px;">
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
            <span style="font-size: 11px; font-weight: 600; color: #64748B;">Estimated Total (All Taxes Incl.):</span>
            <span id="calcTotalPrice" style="font-size: 22px; font-weight: 800; color: #14533D;">₹19,998/-</span>
          </div>
          <p style="font-size: 9.5px; color: #10B981; font-weight: 600; margin: 0;">✓ Includes Sasan Gir Safari Pass, AC Travel, 3N Stay &amp; Meals</p>
        </div>
        <input type="hidden" id="bookingTotalPriceInput" name="total_price" value="19998">

        <!-- Status Message Container -->
        <div id="bookingFormStatus" class="form-status-alert" role="alert" aria-live="polite"></div>

        <!-- Submit Button -->
        <button type="submit" id="btnSubmitBooking" class="btn-hero-primary btn-submit-action" style="width: 100%; justify-content: center; padding: 14px;">
          <span class="btn-label-text">Submit Booking Request</span>
          <span class="btn-loading-spinner" aria-hidden="true"></span>
        </button>

        <!-- Preserved WhatsApp Alternative -->
        <div class="form-or-divider"><span>OR INSTANT CHAT</span></div>
        <a id="btnConfirmWhatsApp" href="#" class="btn-whatsapp-secondary" style="width: 100%; justify-content: center; padding: 11px;" target="_blank" rel="noopener">
          <img src="assets/svg/icon-whatsapp.svg" alt="WhatsApp" width="18" height="18">
          <span>Book Directly via WhatsApp</span>
        </a>
      </form>"""

old_booking_normalized = old_booking_modal_content.replace('\r\n', '\n')
new_booking_normalized = new_booking_modal_content.replace('\r\n', '\n')

if old_booking_normalized in html_normalized:
    html_normalized = html_normalized.replace(old_booking_normalized, new_booking_normalized)
    print("Booking modal form updated successfully!")
else:
    print("WARNING: Old booking modal content not matched!")

# Save back with original CRLF
with open('index.html', 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(html_normalized)

print("index.html write completed successfully.")

