/**
 * ITINERARY & DESTINATION DATA
 */
const GUJARAT_TOUR_DATA = {
  packageTitle: "Dwarka – Somnath – Sasan Gir Signature Tour",
  duration: "3 Nights / 4 Days",
  basePrice: 9999,
  contactPhone: "+91 98765 43210",
  whatsappNumber: "919876543210",
  
  destinations: [
    {
      id: "dwarka",
      name: "Dwarka",
      tagline: "Dwarkadhish Temple & Bet Dwarka",
      heroImg: "assets/crops/dest_dwarka.png",
      retinaImg: "assets/images/dwarka_retina.jpg",
      description: "The ancient golden kingdom of Lord Krishna standing proudly on the western tip of Saurashtra by the Arabian Sea.",
      significance: "One of the Char Dham pilgrimage sites and one of the seven Sapta Puri sacred cities.",
      timings: "Morning: 6:30 AM – 1:00 PM | Evening: 5:00 PM – 9:30 PM",
      highlights: [
        "Dwarkadhish Temple (Jagat Mandir) with 52-yard sacred flag",
        "Bet Dwarka Island ferry boat crossing",
        "Nageshwar Jyotirling (one of 12 sacred Jyotirlingas)",
        "Gomti Ghat and holy ocean dip"
      ]
    },
    {
      id: "somnath",
      name: "Somnath",
      tagline: "Somnath Temple & Triveni Sangam",
      heroImg: "assets/crops/dest_somnath.png",
      retinaImg: "assets/images/somnath_retina.jpg",
      description: "The timeless First Jyotirling standing majestically on the shore of the roaring Arabian Sea, an eternal symbol of spiritual resilience.",
      significance: "The foremost among the 12 sacred Jyotirlingas of Lord Shiva.",
      timings: "Morning: 6:00 AM – 10:00 PM | Sound & Light Show: 8:00 PM",
      highlights: [
        "First sacred Jyotirling shrine by the ocean",
        "Triveni Sangam confluence of three holy rivers",
        "Spectacular Ocean-front Sunset Aarti",
        "Evening 3D Projection Sound & Light Show"
      ]
    },
    {
      id: "gir",
      name: "Sasan Gir",
      tagline: "Wildlife Safari & Nature Experience",
      heroImg: "assets/crops/dest_gir.png",
      retinaImg: "assets/images/gir_safari_retina.jpg",
      description: "The sole global sanctuary of the majestic Asiatic Lion, featuring teak forest canopy, rich avian life, and royal safari thrills.",
      significance: "Only natural habitat of the Asiatic Lion (Panthera leo persica) on Earth.",
      timings: "Morning Safari: 6:00 AM – 9:00 AM | Evening Safari: 3:00 PM – 6:00 PM",
      highlights: [
        "Open 4x4 Gypsy Wildlife Safari inside Gir National Park",
        "Guaranteed spotting of Asiatic Lions, Leopards, and Chital",
        "Authentic Kathiyawadi dining and campfire under the stars",
        "Siddi Dhamal tribal dance performance"
      ]
    },
    {
      id: "nageshwar",
      name: "Nageshwar",
      tagline: "Nageshwar Jyotirling & Other Sacred Sites",
      heroImg: "assets/crops/dest_nageshwar.png",
      retinaImg: "assets/crops/dest_nageshwar.png",
      description: "One of the sacred 12 Jyotirlinga shrines featuring a colossal 82-foot Lord Shiva statue visible for miles across the plains.",
      significance: "Guards against poisons and negative planetary energies according to Shiva Purana.",
      timings: "6:00 AM – 9:00 PM Daily",
      highlights: [
        "Giant 82-foot seated Lord Shiva idol",
        "Ancient underground sanctum sanctorum",
        "Spiritual peace and milk Abhishekam darshan"
      ]
    }
  ],

  itinerary: [
    {
      day: 1,
      route: "Ahmedabad → Dwarka",
      distance: "440 km | 8.5 Hours",
      thumb: "assets/crops/day1_thumb.png",
      title: "Ahmedabad Pickup & Journey to Holy Dwarka",
      summary: "Pickup from Ahmedabad, Dwarkadhish Temple Evening Aarti",
      schedule: [
        { time: "07:00 AM", event: "Personal AC vehicle pickup from Ahmedabad Airport / Railway Station / Hotel" },
        { time: "01:00 PM", event: "En-route lunch break at Rajkot highway restaurant" },
        { time: "04:30 PM", event: "Arrival in sacred Dwarka & check-in at luxury hotel" },
        { time: "06:30 PM", event: "Evening Darshan and divine Sandhya Aarti at Dwarkadhish Temple" },
        { time: "08:30 PM", event: "Stroll along Gomti Ghat, local market exploration & authentic Kathiyawadi dinner" }
      ]
    },
    {
      day: 2,
      route: "Dwarka → Somnath",
      distance: "235 km | 5 Hours",
      thumb: "assets/crops/day2_thumb.png",
      title: "Bet Dwarka Ferry, Nageshwar Jyotirling & Somnath Light Show",
      summary: "Nageshwar Jyotirling, Porbandar Kirti Mandir & Triveni Sangam",
      schedule: [
        { time: "06:30 AM", event: "Early breakfast followed by scenic ferry boat ride to Bet Dwarka Island" },
        { time: "09:30 AM", event: "Darshan at Nageshwar Jyotirling & Rukmini Devi Temple" },
        { time: "01:00 PM", event: "Coastal drive via Porbandar with visit to Mahatma Gandhi's birthplace (Kirti Mandir)" },
        { time: "05:00 PM", event: "Arrival at Somnath, check-in and refresh" },
        { time: "06:45 PM", event: "Mesmerizing Sunset Aarti inside the oceanfront Somnath Temple" },
        { time: "08:00 PM", event: "Witness the iconic Sound and Light 3D Projection show on temple stones" }
      ]
    },
    {
      day: 3,
      route: "Somnath → Sasan Gir",
      distance: "50 km | 1.5 Hours",
      thumb: "assets/crops/day3_thumb.png",
      title: "Triveni Sangam Snan & Royal Arrival in Sasan Gir Jungle",
      summary: "Check-in & Relax, Evening at Leisure with Campfire",
      schedule: [
        { time: "07:00 AM", event: "Holy morning visit to Triveni Sangam (confluence of three sacred rivers) & Bhalka Tirth" },
        { time: "10:30 AM", event: "Scenic countryside drive to Sasan Gir through lush mango orchards" },
        { time: "12:30 PM", event: "Check-in at luxury forest resort, welcome drink & grand buffet lunch" },
        { time: "04:00 PM", event: "Nature trail walk, swimming pool leisure & bird watching in resort gardens" },
        { time: "07:30 PM", event: "Evening bonfire and traditional Siddi Dhamal folk tribal dance performance" }
      ]
    },
    {
      day: 4,
      route: "Gir Safari & Return to Ahmedabad",
      distance: "380 km | 7.5 Hours",
      thumb: "assets/crops/day4_thumb.png",
      title: "Morning Open-Top Gypsy Lion Safari & Departure",
      summary: "Morning Safari, Drop to Ahmedabad Airport / Station",
      schedule: [
        { time: "06:00 AM", event: "Exciting 3-hour open 4x4 Gypsy Safari into Gir National Park with certified forest tracker" },
        { time: "09:30 AM", event: "Return to resort for hearty hot breakfast, shower and checkout" },
        { time: "11:00 AM", event: "Commence return journey to Ahmedabad via Junagadh" },
        { time: "07:30 PM", event: "Drop-off at Ahmedabad Airport or Railway Station with lifetime memories" }
      ]
    }
  ]
};

