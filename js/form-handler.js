/**
 * ==============================================================================
 * TRAVEL FIRST HOLIDAYS — DJANGO REST FRAMEWORK (DRF) DATABASE HANDLER
 * ==============================================================================
 * Connects directly to the real Django backend with SQLite persistence:
 * - Endpoints: POST /api/bookings/ and POST /api/inquiries/
 * - CSRF Security: Automatically obtains and passes X-CSRFToken with credentials
 * - Duplicate submission prevention (button lock, inputs lock, spinner)
 * - DRF Serializer HTTP 400 validation error mapping
 * - Real database persistence confirmation (no mock / no localStorage fallback)
 * ==============================================================================
 */

// Configuration for Django REST Framework Backend
const DRF_CONFIG = {
  // Configurable base URL. Default is relative '/api' when served via Django on port 8000,
  // or window.DRF_API_BASE_URL if configured for cross-origin local development.
  baseUrl: window.DRF_API_BASE_URL || '/api',
  endpoints: {
    booking: '/bookings/',
    inquiry: '/inquiries/',
    csrf: '/csrf/'
  },
  timeoutMs: 10000 // 10 second timeout for database operations
};

document.addEventListener('DOMContentLoaded', () => {
  ensureCsrfCookie();
  initBookingForm();
  initInquiryForm();
});

/**
 * Reads Django's CSRF token from document.cookie
 */
function getDjangoCsrfToken() {
  const cookieName = 'csrftoken=';
  const decodedCookie = decodeURIComponent(document.cookie);
  const cookieArray = decodedCookie.split(';');

  for (let i = 0; i < cookieArray.length; i++) {
    let cookie = cookieArray[i].trim();
    if (cookie.indexOf(cookieName) === 0) {
      return cookie.substring(cookieName.length, cookie.length);
    }
  }
  return null;
}

/**
 * Ensures CSRF cookie is obtained on page load from the Django backend
 */
async function ensureCsrfCookie() {
  if (!getDjangoCsrfToken()) {
    try {
      await fetch(`${DRF_CONFIG.baseUrl}${DRF_CONFIG.endpoints.csrf}`, {
        method: 'GET',
        credentials: 'include'
      });
    } catch (e) {
      // Backend may not be started yet; handler handles network failure during submit
    }
  }
}

/* ==========================================================================
   VALIDATION HELPERS
   ========================================================================== */

function validateFullName(name) {
  if (!name || !name.trim()) {
    return 'Full name is required.';
  }
  if (name.trim().length < 2) {
    return 'Full name must be at least 2 characters.';
  }
  return null;
}

function validatePhoneNumber(phone) {
  if (!phone || !phone.trim()) {
    return 'Phone number is required.';
  }
  const cleanPhone = phone.replace(/[\s\-\(\)]/g, '');
  const phonePattern = /^(\+91|0)?[6-9]\d{9}$|^(\+)?[1-9]\d{9,14}$/;
  if (!phonePattern.test(cleanPhone)) {
    return 'Please enter a valid 10-digit mobile number (e.g. 9876543210).';
  }
  return null;
}

function validateEmailAddress(email) {
  if (!email || !email.trim()) {
    return 'Email address is required.';
  }
  const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
  if (!emailPattern.test(email.trim())) {
    return 'Please enter a valid email address (e.g. name@example.com).';
  }
  return null;
}

function validateTravelDate(dateStr) {
  if (!dateStr) {
    return 'Please select your preferred travel date.';
  }
  const selected = new Date(dateStr);
  const today = new Date();
  today.setHours(0, 0, 0, 0);

  if (isNaN(selected.getTime())) {
    return 'Please enter a valid date format.';
  }
  if (selected < today) {
    return 'Travel date cannot be in the past.';
  }
  return null;
}

function validateTravelersCount(count) {
  const num = parseInt(count, 10);
  if (isNaN(num) || num < 1) {
    return 'At least 1 traveler is required.';
  }
  if (num > 50) {
    return 'For groups larger than 50, please contact us for custom charter buses.';
  }
  return null;
}

function setFieldError(fieldInput, errorContainer, errorMsg) {
  if (!fieldInput || !errorContainer) return;
  if (errorMsg) {
    fieldInput.classList.add('has-error');
    errorContainer.textContent = errorMsg;
    errorContainer.style.display = 'block';
  } else {
    fieldInput.classList.remove('has-error');
    errorContainer.textContent = '';
    errorContainer.style.display = 'none';
  }
}

function clearFormErrors(form) {
  form.querySelectorAll('.has-error').forEach(input => input.classList.remove('has-error'));
  form.querySelectorAll('.field-error-msg').forEach(el => {
    el.textContent = '';
    el.style.display = 'none';
  });
}

function displayFormStatus(statusContainer, type, title, message, details = null) {
  if (!statusContainer) return;
  statusContainer.className = `form-status-alert status-${type}`;
  statusContainer.style.display = 'block';

  let icon = '';
  if (type === 'loading') {
    icon = '<span class="status-spinner" aria-hidden="true"></span>';
  } else if (type === 'success') {
    icon = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>';
  } else if (type === 'error') {
    icon = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>';
  }

  let html = `
    <div class="status-header">
      ${icon}
      <span>${title}</span>
    </div>
    <div class="status-body">${message}</div>
  `;

  if (details) {
    html += `<div class="status-details"><code>${details}</code></div>`;
  }

  statusContainer.innerHTML = html;
}

function toggleSubmissionLock(form, isSubmitting, loadingText = 'Submitting...') {
  const submitBtn = form.querySelector('button[type="submit"]');
  const btnLabel = submitBtn ? submitBtn.querySelector('.btn-label-text') : null;
  const formElements = form.querySelectorAll('input, select, textarea, button');

  if (isSubmitting) {
    form.dataset.submitting = 'true';
    if (submitBtn) {
      submitBtn.disabled = true;
      submitBtn.classList.add('is-loading');
    }
    if (btnLabel) {
      if (!submitBtn.dataset.originalLabel) {
        submitBtn.dataset.originalLabel = btnLabel.textContent;
      }
      btnLabel.textContent = loadingText;
    }
    formElements.forEach(el => {
      if (el !== submitBtn) el.disabled = true;
    });
  } else {
    delete form.dataset.submitting;
    if (submitBtn) {
      submitBtn.disabled = false;
      submitBtn.classList.remove('is-loading');
    }
    if (btnLabel && submitBtn.dataset.originalLabel) {
      btnLabel.textContent = submitBtn.dataset.originalLabel;
    }
    formElements.forEach(el => {
      el.disabled = false;
    });
  }
}

/**
 * Sends form payload to Django REST Framework via Fetch API
 */
async function postToDjangoApi(endpointPath, payload) {
  const targetUrl = `${DRF_CONFIG.baseUrl}${endpointPath}`;
  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), DRF_CONFIG.timeoutMs);

  const headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
  };

  const csrfToken = getDjangoCsrfToken();
  if (csrfToken) {
    headers['X-CSRFToken'] = csrfToken;
  }

  try {
    const response = await fetch(targetUrl, {
      method: 'POST',
      headers: headers,
      credentials: 'include', // Ensures cookies (session, csrf) are passed securely
      body: JSON.stringify(payload),
      signal: controller.signal
    });

    clearTimeout(timeoutId);

    let data = null;
    const contentType = response.headers.get('content-type');
    if (contentType && contentType.includes('application/json')) {
      data = await response.json();
    } else {
      const text = await response.text();
      data = { detail: text };
    }

    return {
      success: response.ok,
      status: response.status,
      statusText: response.statusText,
      data: data,
      url: targetUrl
    };
  } catch (err) {
    clearTimeout(timeoutId);
    return {
      success: false,
      status: 0,
      statusText: err.name === 'AbortError' ? 'Request Timeout' : 'Network Failure',
      error: err,
      url: targetUrl
    };
  }
}

/* ==========================================================================
   1. BOOKING RESERVATION FORM CONTROLLER
   ========================================================================== */
function initBookingForm() {
  const form = document.getElementById('bookingForm');
  if (!form) return;

  const statusAlert = document.getElementById('bookingFormStatus');
  const inputName = document.getElementById('bookingFullName');
  const inputPhone = document.getElementById('bookingPhone');
  const inputEmail = document.getElementById('bookingEmail');
  const inputDate = document.getElementById('bookingDateInput');
  const inputTravelers = document.getElementById('bookingTravelersInput');
  const inputNotes = document.getElementById('bookingNotes');
  const inputTotalPrice = document.getElementById('bookingTotalPriceInput');

  // Real-time live error clearing on input
  [inputName, inputPhone, inputEmail, inputDate].forEach(input => {
    if (input) {
      input.addEventListener('input', () => {
        const errContainer = document.getElementById(`error-${input.id}`);
        setFieldError(input, errContainer, null);
      });
    }
  });

  form.addEventListener('submit', async (e) => {
    e.preventDefault();

    if (form.dataset.submitting === 'true') {
      return;
    }

    clearFormErrors(form);

    // Client-side validations
    const nameErr = validateFullName(inputName ? inputName.value : '');
    const phoneErr = validatePhoneNumber(inputPhone ? inputPhone.value : '');
    const emailErr = validateEmailAddress(inputEmail ? inputEmail.value : '');
    const dateErr = validateTravelDate(inputDate ? inputDate.value : '');
    const travelersErr = validateTravelersCount(inputTravelers ? inputTravelers.value : 2);

    let hasErrors = false;
    let firstErrorField = null;

    if (nameErr) {
      setFieldError(inputName, document.getElementById('error-bookingFullName'), nameErr);
      hasErrors = true;
      firstErrorField = firstErrorField || inputName;
    }
    if (phoneErr) {
      setFieldError(inputPhone, document.getElementById('error-bookingPhone'), phoneErr);
      hasErrors = true;
      firstErrorField = firstErrorField || inputPhone;
    }
    if (emailErr) {
      setFieldError(inputEmail, document.getElementById('error-bookingEmail'), emailErr);
      hasErrors = true;
      firstErrorField = firstErrorField || inputEmail;
    }
    if (dateErr) {
      setFieldError(inputDate, document.getElementById('error-bookingDateInput'), dateErr);
      hasErrors = true;
      firstErrorField = firstErrorField || inputDate;
    }
    if (travelersErr) {
      setFieldError(inputTravelers, document.getElementById('error-bookingTravelersInput'), travelersErr);
      hasErrors = true;
    }

    if (hasErrors) {
      if (firstErrorField) firstErrorField.focus();
      return;
    }

    const vehicleChoice = form.querySelector('input[name="vehicleChoice"]:checked')?.value || 'bus';
    const hotelChoice = form.querySelector('input[name="hotelChoice"]:checked')?.value || 'standard';

    const bookingPayload = {
      full_name: inputName.value.trim(),
      phone: inputPhone.value.trim(),
      email: inputEmail.value.trim(),
      travel_date: inputDate.value,
      travelers_count: parseInt(inputTravelers ? inputTravelers.value : '2', 10),
      vehicle_choice: vehicleChoice,
      hotel_category: hotelChoice,
      total_price: parseInt(inputTotalPrice ? inputTotalPrice.value : '19998', 10),
      special_requests: inputNotes ? inputNotes.value.trim() : ''
    };

    toggleSubmissionLock(form, true, 'Saving to Database...');
    displayFormStatus(
      statusAlert,
      'loading',
      'Connecting to Django REST API...',
      'Validating and saving your booking reservation into the database.'
    );

    const response = await postToDjangoApi(DRF_CONFIG.endpoints.booking, bookingPayload);

    toggleSubmissionLock(form, false);

    if (response.success) {
      // Verified real database insertion
      const recordId = response.data?.id || response.data?.database_record_id || 'OK';
      displayFormStatus(
        statusAlert,
        'success',
        'Reservation Stored in Database!',
        `Thank you, <strong>${escapeHtml(bookingPayload.full_name)}</strong>! Your booking record has been successfully committed to the database (<strong>Database ID #${recordId}</strong>).<br>` +
        `• Travel Date: <strong>${bookingPayload.travel_date}</strong><br>` +
        `• Travelers: <strong>${bookingPayload.travelers_count} Guest(s)</strong><br>` +
        `• Persistence: <strong>SQLite (backend/db.sqlite3)</strong><br>` +
        `Our Saurashtra tour executive will contact you at <strong>${escapeHtml(bookingPayload.phone)}</strong> with your confirmation voucher.`
      );
      form.reset();
      if (typeof window.recalcBookingDrawerPrice === 'function') {
        window.recalcBookingDrawerPrice();
      }
    } else if (response.status === 400 && response.data && typeof response.data === 'object') {
      let errorSummary = [];
      for (const [field, fieldErrors] of Object.entries(response.data)) {
        const fieldMsg = Array.isArray(fieldErrors) ? fieldErrors.join(' ') : fieldErrors;
        errorSummary.push(`• ${field}: ${fieldMsg}`);

        if (field === 'full_name' && inputName) setFieldError(inputName, document.getElementById('error-bookingFullName'), fieldMsg);
        if (field === 'phone' && inputPhone) setFieldError(inputPhone, document.getElementById('error-bookingPhone'), fieldMsg);
        if (field === 'email' && inputEmail) setFieldError(inputEmail, document.getElementById('error-bookingEmail'), fieldMsg);
        if (field === 'travel_date' && inputDate) setFieldError(inputDate, document.getElementById('error-bookingDateInput'), fieldMsg);
      }

      displayFormStatus(
        statusAlert,
        'error',
        'Django Validation Error (HTTP 400)',
        'The Django backend serializer rejected one or more fields. Please review the highlighted fields above.',
        errorSummary.join('\n')
      );
    } else {
      const isMissingServer = response.status === 0 || response.status === 404 || response.status === 405 || response.status === 501;
      displayFormStatus(
        statusAlert,
        'error',
        isMissingServer ? `Backend Server Unavailable (${response.status ? 'HTTP ' + response.status : 'Connection Error'})` : `Server Error (HTTP ${response.status})`,
        `<strong>Form data was NOT saved.</strong><br>` +
        `Target Endpoint: <code>POST ${response.url}</code><br>` +
        (isMissingServer
          ? `<strong>What is missing:</strong> The Django REST Framework backend server is not running on port 8000 or the route <code>${DRF_CONFIG.endpoints.booking}</code> was not reachable.<br>` +
            `<em>Notice: As per security and architecture rules, data is never faked into localStorage. Please start the Django backend server with: <code>python backend/manage.py runserver 8000</code>.</em>`
          : `The backend returned an unexpected response. Please inspect Django server terminal logs.`),
        response.statusText || (response.error ? response.error.message : null)
      );
    }
  });
}

/* ==========================================================================
   2. QUICK INQUIRY / CALLBACK FORM CONTROLLER
   ========================================================================== */
function initInquiryForm() {
  const form = document.getElementById('inquiryForm');
  if (!form) return;

  const statusAlert = document.getElementById('inquiryFormStatus');
  const inputName = document.getElementById('inquiryFullName');
  const inputPhone = document.getElementById('inquiryPhone');
  const inputEmail = document.getElementById('inquiryEmail');
  const selectDest = document.getElementById('inquiryDestination');
  const inputMsg = document.getElementById('inquiryMessage');

  [inputName, inputPhone, inputEmail].forEach(input => {
    if (input) {
      input.addEventListener('input', () => {
        const errContainer = document.getElementById(`error-${input.id}`);
        setFieldError(input, errContainer, null);
      });
    }
  });

  form.addEventListener('submit', async (e) => {
    e.preventDefault();

    if (form.dataset.submitting === 'true') {
      return;
    }

    clearFormErrors(form);

    const nameErr = validateFullName(inputName ? inputName.value : '');
    const phoneErr = validatePhoneNumber(inputPhone ? inputPhone.value : '');
    const emailErr = validateEmailAddress(inputEmail ? inputEmail.value : '');

    let hasErrors = false;
    let firstError = null;

    if (nameErr) {
      setFieldError(inputName, document.getElementById('error-inquiryFullName'), nameErr);
      hasErrors = true;
      firstError = firstError || inputName;
    }
    if (phoneErr) {
      setFieldError(inputPhone, document.getElementById('error-inquiryPhone'), phoneErr);
      hasErrors = true;
      firstError = firstError || inputPhone;
    }
    if (emailErr) {
      setFieldError(inputEmail, document.getElementById('error-inquiryEmail'), emailErr);
      hasErrors = true;
      firstError = firstError || inputEmail;
    }

    if (hasErrors) {
      if (firstError) firstError.focus();
      return;
    }

    const inquiryPayload = {
      full_name: inputName.value.trim(),
      phone: inputPhone.value.trim(),
      email: inputEmail.value.trim(),
      destination: selectDest ? selectDest.value : 'General Gujarat Tour',
      message: inputMsg ? inputMsg.value.trim() : ''
    };

    toggleSubmissionLock(form, true, 'Saving Inquiry...');
    displayFormStatus(
      statusAlert,
      'loading',
      'Connecting to Django REST API...',
      'Submitting your callback inquiry to the backend database.'
    );

    const response = await postToDjangoApi(DRF_CONFIG.endpoints.inquiry, inquiryPayload);

    toggleSubmissionLock(form, false);

    if (response.success) {
      const recordId = response.data?.id || response.data?.database_record_id || 'OK';
      displayFormStatus(
        statusAlert,
        'success',
        'Inquiry Stored in Database!',
        `Thank you, <strong>${escapeHtml(inquiryPayload.full_name)}</strong>! Your inquiry regarding <strong>${escapeHtml(inquiryPayload.destination)}</strong> has been recorded in the database (<strong>Database ID #${recordId}</strong>).<br>` +
        `• Persistence: <strong>SQLite (backend/db.sqlite3)</strong><br>` +
        `Our senior travel consultant will call you at <strong>${escapeHtml(inquiryPayload.phone)}</strong> shortly.`
      );
      form.reset();
    } else if (response.status === 400 && response.data && typeof response.data === 'object') {
      let errorSummary = [];
      for (const [field, fieldErrors] of Object.entries(response.data)) {
        const fieldMsg = Array.isArray(fieldErrors) ? fieldErrors.join(' ') : fieldErrors;
        errorSummary.push(`• ${field}: ${fieldMsg}`);
        if (field === 'full_name' && inputName) setFieldError(inputName, document.getElementById('error-inquiryFullName'), fieldMsg);
        if (field === 'phone' && inputPhone) setFieldError(inputPhone, document.getElementById('error-inquiryPhone'), fieldMsg);
        if (field === 'email' && inputEmail) setFieldError(inputEmail, document.getElementById('error-inquiryEmail'), fieldMsg);
      }

      displayFormStatus(
        statusAlert,
        'error',
        'Django Validation Error (HTTP 400)',
        'The backend API rejected one or more fields. Please review the highlighted fields above.',
        errorSummary.join('\n')
      );
    } else {
      const isMissingServer = response.status === 0 || response.status === 404 || response.status === 405 || response.status === 501;
      displayFormStatus(
        statusAlert,
        'error',
        isMissingServer ? `Backend Server Unavailable (${response.status ? 'HTTP ' + response.status : 'Connection Error'})` : `Server Error (HTTP ${response.status})`,
        `<strong>Form data was NOT saved.</strong><br>` +
        `Target Endpoint: <code>POST ${response.url}</code><br>` +
        (isMissingServer
          ? `<strong>What is missing:</strong> The Django REST Framework backend server is not running on port 8000 or the route <code>${DRF_CONFIG.endpoints.inquiry}</code> was not reachable.<br>` +
            `<em>Notice: As per security and architecture rules, data is not saved to localStorage. Please start the Django backend server with: <code>python backend/manage.py runserver 8000</code>.</em>`
          : `The backend returned an error. Please check your Django server terminal.`),
        response.statusText || (response.error ? response.error.message : null)
      );
    }
  });
}

function escapeHtml(str) {
  if (!str) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}
