#!/usr/bin/env python3
"""
Zay Supply Co. — SEO/AEO Page Generator
Generates 650+ unique, keyword-rich HTML pages for wholesale disposables.
"""

import os
import random
from datetime import datetime

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_URL = "https://zaysupply.com"
UPDATED = "April 2026"
PHONE = "(925) 255-5484"
EMAIL = "reshad@zaysupply.com"

# ── DATA ──────────────────────────────────────────────────────────────────────

EAST_BAY = [
    ("Walnut Creek", "East Bay"), ("Orinda", "East Bay"), ("Lafayette", "East Bay"),
    ("Moraga", "East Bay"), ("El Sobrante", "East Bay"), ("Oakland", "East Bay"),
    ("Berkeley", "East Bay"), ("Emeryville", "East Bay"), ("Richmond", "East Bay"),
    ("Alameda", "East Bay"), ("San Leandro", "East Bay"), ("Castro Valley", "East Bay"),
    ("Dublin", "East Bay"), ("Pleasanton", "East Bay"), ("Livermore", "East Bay"),
    ("Fremont", "East Bay"), ("Hayward", "East Bay"), ("Union City", "East Bay"),
    ("Newark", "East Bay"), ("San Ramon", "East Bay"), ("Danville", "East Bay"),
    ("Concord", "East Bay"), ("Martinez", "East Bay"), ("Brentwood", "East Bay"),
    ("Antioch", "East Bay"), ("Pittsburg", "East Bay"),
]
BAY_AREA = [
    ("San Francisco", "Bay Area"), ("San Jose", "Bay Area"), ("Santa Clara", "Bay Area"),
    ("Sunnyvale", "Bay Area"), ("Mountain View", "Bay Area"), ("Palo Alto", "Bay Area"),
    ("Redwood City", "Bay Area"), ("San Mateo", "Bay Area"), ("Foster City", "Bay Area"),
    ("Burlingame", "Bay Area"), ("South San Francisco", "Bay Area"), ("Daly City", "Bay Area"),
]
SOCAL = [
    ("Los Angeles", "Southern California"), ("Santa Monica", "Southern California"),
    ("Culver City", "Southern California"), ("Inglewood", "Southern California"),
    ("Long Beach", "Southern California"), ("Anaheim", "Southern California"),
    ("San Diego", "Southern California"),
]
NORCAL = [
    ("Sacramento", "Northern California"), ("Stockton", "Central Valley"),
    ("Fresno", "Central Valley"), ("Modesto", "Central Valley"),
    ("Bakersfield", "Central Valley"),
]
ALL_CITIES = EAST_BAY + BAY_AREA + SOCAL + NORCAL

PRODUCTS = [
    {
        "name": "Wholesale Hot Cups",
        "slug": "wholesale-hot-cups",
        "keyword": "wholesale hot cups",
        "variants": ["hot coffee cups wholesale", "paper hot cups bulk", "disposable coffee cups wholesale"],
        "sizes": "8oz, 10oz, 12oz, 16oz, and 20oz",
        "price_range": "$0.06–$0.18 per unit",
        "desc": "Insulated paper hot cups for coffee, tea, and hot drinks. Available in all standard sizes.",
        "use": "hot beverages, coffee, tea, espresso drinks",
    },
    {
        "name": "Wholesale Cold Cups",
        "slug": "wholesale-cold-cups",
        "keyword": "wholesale cold cups",
        "variants": ["plastic cold cups bulk", "iced drink cups wholesale", "clear cups wholesale"],
        "sizes": "16oz, 20oz, 24oz, and 32oz",
        "price_range": "$0.08–$0.22 per unit",
        "desc": "Crystal-clear PET cold cups for iced coffee, smoothies, and cold drinks.",
        "use": "iced beverages, cold brew, smoothies, lemonade",
    },
    {
        "name": "Wholesale Boba Cups",
        "slug": "wholesale-boba-cups",
        "keyword": "wholesale boba cups",
        "variants": ["bubble tea cups wholesale", "boba shop cups bulk", "tapioca cup wholesale"],
        "sizes": "24oz and 32oz",
        "price_range": "$0.10–$0.25 per unit",
        "desc": "Wide-mouth clear cups designed for bubble tea and boba drinks with fat straws.",
        "use": "bubble tea, boba drinks, smoothies, slushies",
    },
    {
        "name": "Wholesale Cup Lids",
        "slug": "wholesale-cup-lids",
        "keyword": "wholesale cup lids",
        "variants": ["disposable lids bulk", "hot cup lids wholesale", "dome lids wholesale"],
        "sizes": "hot cup lids, cold cup lids, and dome lids in all standard diameters",
        "price_range": "$0.03–$0.10 per unit",
        "desc": "Matching lids for hot cups, cold cups, and dome lids for whipped cream drinks.",
        "use": "all cup types — hot, cold, boba, smoothie",
    },
    {
        "name": "Wholesale Straws",
        "slug": "wholesale-straws",
        "keyword": "wholesale straws",
        "variants": ["bulk straws California", "boba straws wholesale", "paper straws bulk"],
        "sizes": "regular (7.75\"), jumbo, boba (0.4\" diameter), and eco paper straws",
        "price_range": "$0.01–$0.08 per unit",
        "desc": "Regular plastic, jumbo, fat boba straws, and eco-friendly paper straws.",
        "use": "all beverage types, boba, smoothies, fountain drinks",
    },
    {
        "name": "Wholesale Napkins",
        "slug": "wholesale-napkins",
        "keyword": "wholesale napkins",
        "variants": ["bulk napkins California", "disposable napkins wholesale", "tissue napkins bulk"],
        "sizes": "1-ply beverage, 2-ply dinner, and dispenser napkins",
        "price_range": "$0.01–$0.04 per unit",
        "desc": "1-ply and 2-ply napkins in bulk quantities for cafes, restaurants, and food service.",
        "use": "table service, counter dispensers, to-go bags",
    },
    {
        "name": "Wholesale Food Containers",
        "slug": "wholesale-food-containers",
        "keyword": "wholesale food containers",
        "variants": ["to-go containers wholesale", "clamshell containers bulk", "takeout containers California"],
        "sizes": "6\", 8\", and 9\" clamshells plus compartment containers",
        "price_range": "$0.12–$0.45 per unit",
        "desc": "Hinged clamshell and compartment containers for hot and cold to-go food.",
        "use": "takeout, meal prep, bakery, deli, food trucks",
    },
    {
        "name": "Wholesale Coffee Sleeves",
        "slug": "wholesale-coffee-sleeves",
        "keyword": "wholesale coffee sleeves",
        "variants": ["cup sleeves bulk", "hot cup sleeves wholesale", "coffee sleeve wholesale"],
        "sizes": "fits 10oz–20oz hot cups (universal fit)",
        "price_range": "$0.04–$0.12 per unit",
        "desc": "Corrugated cardboard sleeves that insulate hot cups and protect customer hands.",
        "use": "hot coffee, tea, any hot cup over 10oz",
    },
    {
        "name": "Custom Branded Cups",
        "slug": "custom-branded-cups",
        "keyword": "custom branded cups",
        "variants": ["logo cups wholesale", "branded disposable cups California", "printed cups bulk"],
        "sizes": "hot and cold cups in all standard sizes",
        "price_range": "$0.15–$0.45 per unit (with custom printing)",
        "desc": "Hot and cold cups printed with your business logo and brand colors.",
        "use": "brand marketing, customer experience, logo visibility",
    },
    {
        "name": "Custom Printed Cups",
        "slug": "custom-printed-cups",
        "keyword": "custom printed cups",
        "variants": ["printed wholesale cups", "custom cup printing California", "logo cup printing bulk"],
        "sizes": "8oz–32oz in hot and cold varieties",
        "price_range": "$0.18–$0.50 per unit",
        "desc": "Full-color custom printed cups with your brand. Low minimums, fast California turnaround.",
        "use": "brand visibility, events, seasonal promotions",
    },
    {
        "name": "Wholesale Disposable Utensils",
        "slug": "wholesale-disposable-utensils",
        "keyword": "wholesale disposable utensils",
        "variants": ["bulk utensils California", "plastic utensils wholesale", "cutlery sets wholesale"],
        "sizes": "individual forks, knives, spoons, and wrapped sets",
        "price_range": "$0.02–$0.08 per unit",
        "desc": "Individual and wrapped cutlery sets — forks, knives, teaspoons, and soup spoons.",
        "use": "dine-in, takeout, catering, food trucks",
    },
    {
        "name": "Wholesale Paper Bags",
        "slug": "wholesale-paper-bags",
        "keyword": "wholesale paper bags",
        "variants": ["kraft paper bags bulk", "takeout bags wholesale", "deli bags California"],
        "sizes": "#4, #6, #8, and #10 standard sizes",
        "price_range": "$0.05–$0.18 per unit",
        "desc": "White and natural kraft paper bags for takeout, bakeries, and retail.",
        "use": "bakery, deli, takeout, retail packaging",
    },
    {
        "name": "Wholesale Eco-Friendly Disposables",
        "slug": "wholesale-eco-friendly-disposables",
        "keyword": "wholesale eco-friendly disposables",
        "variants": ["compostable cups wholesale", "biodegradable disposables bulk", "sustainable packaging California"],
        "sizes": "cups, lids, straws, and containers in all standard sizes",
        "price_range": "$0.12–$0.35 per unit",
        "desc": "Certified compostable and biodegradable cups, straws, and containers for eco-conscious businesses.",
        "use": "zero-waste cafes, California compliance, eco branding",
    },
]

ICPS = [
    {
        "name": "Coffee Shops",
        "slug": "coffee-shops",
        "keyword": "wholesale supplies for coffee shops",
        "desc": "Hot cups, sleeves, lids, stirrers, and napkins for independent coffee shops.",
        "pain": "running out of cups mid-rush or overpaying at Restaurant Depot",
        "products": "hot cups (8–20oz), lids, sleeves, stir sticks, napkins",
    },
    {
        "name": "Cafes",
        "slug": "cafes",
        "keyword": "wholesale cafe supplies California",
        "desc": "Full cafe supply packages — hot cups, cold cups, food containers, and utensils.",
        "pain": "juggling 3 different suppliers and paying retail markup",
        "products": "hot cups, cold cups, food containers, utensils, napkins",
    },
    {
        "name": "Boba Shops",
        "slug": "boba-shops",
        "keyword": "wholesale boba shop supplies",
        "desc": "Wide-mouth boba cups, fat straws, dome lids, and to-go bags for bubble tea shops.",
        "pain": "sourcing specialty boba cups and fat straws at a fair price",
        "products": "24oz/32oz boba cups, boba straws, dome lids, paper bags",
    },
    {
        "name": "Gas Stations with Food Service",
        "slug": "gas-stations",
        "keyword": "wholesale supplies for gas stations California",
        "desc": "High-volume cups, lids, straws, and condiment supplies for gas station food service.",
        "pain": "high-volume needs with inconsistent local supplier availability",
        "products": "hot cups, cold cups, lids, straws, napkins in bulk quantities",
    },
    {
        "name": "Food Trucks",
        "slug": "food-trucks",
        "keyword": "wholesale food truck supplies California",
        "desc": "Lightweight, stackable disposables for mobile food service — cups, containers, utensils.",
        "pain": "limited storage space requiring compact, high-count case packs",
        "products": "to-go containers, cups, utensils, kraft bags, napkins",
    },
    {
        "name": "Quick Service Restaurants",
        "slug": "quick-service-restaurants",
        "keyword": "wholesale QSR supplies California",
        "desc": "Speed-of-service supplies for QSRs — beverage cups, lids, straws, and food containers.",
        "pain": "supply chain delays from national distributors cutting into service speed",
        "products": "cold cups, hot cups, lids, straws, food containers, utensils",
    },
    {
        "name": "Bakeries",
        "slug": "bakeries",
        "keyword": "wholesale bakery supplies California",
        "desc": "Kraft bags, food containers, napkins, and boxes for retail bakeries.",
        "pain": "finding food-safe packaging that looks good on the counter at fair prices",
        "products": "kraft bags, clamshell containers, tissue paper, napkins, coffee cups",
    },
    {
        "name": "Juice Bars",
        "slug": "juice-bars",
        "keyword": "wholesale juice bar supplies California",
        "desc": "Cold cups, dome lids, straws, and eco-friendly packaging for juice and smoothie bars.",
        "pain": "eco-conscious customers demanding sustainable packaging that's also affordable",
        "products": "clear cold cups, dome lids, paper straws, eco cups, kraft bags",
    },
    {
        "name": "Sandwich Shops",
        "slug": "sandwich-shops",
        "keyword": "wholesale sandwich shop supplies California",
        "desc": "Deli bags, food containers, napkins, and beverage cups for sandwich and deli shops.",
        "pain": "managing both food and drink packaging from separate suppliers",
        "products": "deli bags, to-go containers, hot cups, cold cups, napkins, utensils",
    },
    {
        "name": "Hotels and Hospitality",
        "slug": "hotels-hospitality",
        "keyword": "wholesale hospitality supplies California",
        "desc": "In-room coffee cups, lobby beverage supplies, and banquet disposables for hotels.",
        "pain": "consistent quality expectations across high guest volume",
        "products": "hot cups, cold cups, lids, napkins, wrapped utensil sets",
    },
    {
        "name": "Office Break Rooms",
        "slug": "office-break-rooms",
        "keyword": "wholesale office supplies disposables California",
        "desc": "Bulk hot cups, cold cups, stirrers, and napkins for office kitchens and break rooms.",
        "pain": "ordering through Amazon Business or Costco without business-rate pricing",
        "products": "hot cups, lids, stir sticks, cold cups, napkins, utensils",
    },
    {
        "name": "Event Catering",
        "slug": "event-catering",
        "keyword": "wholesale catering supplies California",
        "desc": "High-volume event supplies — cups, utensils, containers, and napkins for caterers.",
        "pain": "last-minute bulk needs with no local supplier offering fast turnaround",
        "products": "all disposables — cups, lids, straws, containers, utensils, napkins",
    },
]

COMPARISONS = [
    ("sysco-alternative-california", "Sysco Alternative in California", "Sysco", "Sysco's long contracts and high MOQs"),
    ("us-foods-alternative-california", "US Foods Alternative in California", "US Foods", "US Foods' national pricing without local flexibility"),
    ("restaurant-depot-alternative-california", "Restaurant Depot Alternative California", "Restaurant Depot", "Restaurant Depot's warehouse-only model"),
    ("gordon-food-service-alternative-california", "Gordon Food Service Alternative California", "Gordon Food Service", "GFS national distributor pricing"),
    ("webstaurant-store-alternative-california", "WebstaurantStore Alternative California", "WebstaurantStore", "online-only ordering with slow shipping"),
    ("costco-wholesale-alternative-business", "Costco Wholesale Alternative for Businesses", "Costco", "Costco's retail-focused approach"),
    ("amazon-business-alternative-wholesale-california", "Amazon Business Alternative for Wholesale Supplies California", "Amazon Business", "Amazon's inconsistent quality and slow B2B support"),
    ("cheap-wholesale-cups-california", "Cheap Wholesale Cups California — Best Prices", None, "overpaying for cups from retail channels"),
    ("best-wholesale-prices-cups-california", "Best Wholesale Prices on Cups in California", None, "searching for the best deal on bulk cups"),
    ("wholesale-cups-no-minimum-california", "Wholesale Cups Low Minimum Order California", None, "supplier minimums too high for small businesses"),
    ("wholesale-cups-small-business-california", "Wholesale Cups for Small Businesses in California", None, "getting wholesale pricing without large-business volume"),
    ("same-day-wholesale-delivery-bay-area", "Same-Day Wholesale Delivery Bay Area California", None, "waiting days for supply deliveries"),
    ("fast-wholesale-delivery-california", "Fast Wholesale Delivery California — Local Stock", None, "out-of-stock delays from national suppliers"),
    ("custom-cups-low-minimum-california", "Custom Logo Cups Low Minimum Order California", None, "custom cup MOQs of 10,000+ units"),
    ("low-minimum-wholesale-order-california", "Low Minimum Wholesale Order California", None, "high minimum orders blocking small operators"),
    ("save-on-wholesale-supplies-california", "Save on Wholesale Supplies California", None, "paying 15–30% above market on disposables"),
    ("cut-cafe-supply-costs-california", "How to Cut Cafe Supply Costs in California", None, "supply costs eating into thin cafe margins"),
    ("wholesale-supplier-near-me-california", "Wholesale Supplier Near Me — California", None, "finding a reliable local wholesale supplier"),
    ("wholesale-cups-bulk-discount-california", "Wholesale Cups Bulk Discount California", None, "no volume discount from current suppliers"),
    ("switch-wholesale-supplier-california", "How to Switch Wholesale Suppliers in California", None, "being locked into an underperforming supplier"),
]

HOWTOS = [
    ("how-to-cut-cafe-supply-costs", "How to Cut Cafe Supply Costs by 20% in California",
     "cafe owners paying too much for disposable supplies", "switching to a local California wholesale supplier"),
    ("how-to-choose-cup-size-cafe", "How to Choose the Right Cup Size for Your Cafe",
     "cafes unsure which cup sizes to stock", "matching cup sizes to your menu and customer preferences"),
    ("hot-cup-vs-cold-cup-wholesale", "Hot Cup vs Cold Cup: Which to Buy Wholesale for Your Business",
     "buyers confused about cup types", "choosing the right cup type reduces waste and saves money"),
    ("custom-branding-guide-cafe-cups", "Custom Branding Guide for Cafe Cups — California",
     "cafes wanting branded cups but unsure where to start", "low-minimum custom printing through a local CA supplier"),
    ("what-is-moq-minimum-order-quantity", "What Is MOQ? Minimum Order Quantity Explained for Food Businesses",
     "food business owners new to wholesale buying", "understanding MOQs helps you negotiate and plan inventory"),
    ("how-to-switch-wholesale-suppliers", "How to Switch Wholesale Suppliers Without Disrupting Your Business",
     "businesses locked into underperforming suppliers", "a smooth transition plan with a local California backup"),
    ("wholesale-vs-retail-pricing-guide", "Wholesale vs Retail Pricing: What You're Actually Paying for Cups",
     "business owners buying supplies at retail prices", "the true cost difference between wholesale and retail cups"),
    ("how-to-order-wholesale-new-cafe", "How to Order Wholesale Supplies for a New Cafe in California",
     "new cafe owners figuring out their first bulk order", "a step-by-step guide to first wholesale order"),
    ("boba-shop-supply-checklist", "Boba Shop Supply Checklist — Everything You Need to Open",
     "new boba shop owners planning their supply list", "a complete checklist from cups to boba straws to bags"),
    ("coffee-shop-opening-supply-checklist", "Coffee Shop Opening Supply Checklist California",
     "new coffee shop owners planning their supply list", "everything you need to stock before opening day"),
    ("food-truck-supply-checklist", "Food Truck Supply Checklist — Disposables and Packaging",
     "food truck operators planning their supply setup", "space-efficient supply list for mobile food service"),
    ("how-much-do-wholesale-cups-cost-california", "How Much Do Wholesale Cups Cost in California? (2026 Pricing Guide)",
     "buyers researching cup pricing before contacting suppliers", "real price ranges for every cup type in California"),
    ("eco-friendly-cup-options-cafes", "Eco-Friendly Cup Options for California Cafes (2026 Guide)",
     "cafes wanting sustainable packaging options", "compostable and biodegradable cups that meet CA regulations"),
    ("biodegradable-vs-compostable-cups", "Biodegradable vs Compostable Cups: What's the Difference?",
     "businesses confused by sustainable packaging labels", "choosing the right eco-friendly option for your business"),
    ("best-cups-for-hot-coffee-togo", "Best Cups for Hot Coffee To-Go: A Buyer's Guide",
     "cafes optimizing their hot beverage packaging", "double-wall vs single-wall cups and sleeve options"),
    ("best-cups-for-iced-drinks", "Best Cups for Iced Drinks: Cold Cup Buyer's Guide",
     "cafes optimizing their cold beverage packaging", "PET vs PP cups and which holds up best"),
    ("wholesale-supply-delivery-times-california", "Wholesale Supply Delivery Times in California — What to Expect",
     "businesses frustrated by long delivery wait times", "local CA stock means 1–3 day delivery vs 7–14 from national"),
    ("how-to-get-custom-logo-cups", "How to Get Custom Logo Cups for Your Business in California",
     "businesses wanting branded cups but unsure of the process", "low-minimum custom cup printing from a local supplier"),
    ("cup-sizing-guide-8oz-to-32oz", "Cup Sizing Guide: 8oz to 32oz — Which Size for Which Drink?",
     "buyers unsure which cup sizes match which drinks", "matching cup sizes to espresso, drip, iced, boba, and smoothie"),
    ("paper-vs-plastic-cups-cafes", "Paper vs Plastic Cups for Cafes: Which Is Better?",
     "cafes debating paper vs plastic disposables", "the environmental, cost, and customer-experience tradeoffs"),
    ("reduce-supply-chain-costs-small-business", "How Small Food Businesses Can Reduce Supply Chain Costs",
     "small food businesses overpaying for supplies", "consolidating vendors and switching to local wholesale"),
    ("wholesale-ordering-tips-cafe-owners", "10 Wholesale Ordering Tips for Cafe Owners in California",
     "cafe owners wanting to optimize their buying process", "practical tips to cut costs and avoid stockouts"),
    ("california-food-service-regulations-disposables", "California Food Service Regulations for Disposables (2026)",
     "CA food businesses navigating packaging regulations", "what's required, what's banned, and what's coming"),
    ("sustainable-packaging-options-wholesale", "Sustainable Packaging Options for California Food Businesses",
     "businesses wanting eco packaging without the premium cost", "affordable sustainable options available at wholesale"),
    ("how-to-build-supplier-relationship", "How to Build a Strong Relationship with Your Wholesale Supplier",
     "businesses wanting better service and pricing from suppliers", "relationship-driven wholesale buying for long-term savings"),
]

# ── HTML TEMPLATES ─────────────────────────────────────────────────────────────

CSS = """
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    :root {
      --navy: #0a1628; --navy-mid: #142241; --navy-soft: #1e3160;
      --gold: #c9922a; --gold-lt: #e8b050; --gold-pale: #fdf6e9;
      --white: #ffffff; --off-white: #f9f9f7;
      --gray-100: #f4f4f2; --gray-200: #e8e8e4;
      --gray-400: #a0a09a; --gray-600: #666660; --text: #1a1a18;
      --radius: 10px; --shadow: 0 2px 20px rgba(0,0,0,0.07);
      --shadow-md: 0 8px 40px rgba(0,0,0,0.10);
    }
    html { scroll-behavior: smooth; }
    body { font-family: 'Inter', sans-serif; color: var(--text); background: var(--white); line-height: 1.6; -webkit-font-smoothing: antialiased; }
    nav { position: fixed; top: 0; left: 0; right: 0; z-index: 200; height: 68px; display: flex; align-items: center; justify-content: space-between; padding: 0 6%; background: rgba(10,22,40,0.96); backdrop-filter: blur(12px); border-bottom: 1px solid rgba(255,255,255,0.06); }
    .nav-logo { font-family: 'DM Serif Display', serif; font-size: 1.35rem; color: var(--white); letter-spacing: 0.2px; text-decoration: none; }
    .nav-logo em { color: var(--gold-lt); font-style: normal; }
    .nav-links { display: flex; align-items: center; gap: 2rem; list-style: none; }
    .nav-links a { color: rgba(255,255,255,0.65); text-decoration: none; font-size: 0.875rem; font-weight: 500; transition: color .2s; }
    .nav-links a:hover { color: var(--white); }
    .nav-btn { background: var(--gold); color: var(--white) !important; padding: .5rem 1.25rem; border-radius: 6px; font-weight: 600 !important; }
    .nav-btn:hover { background: var(--gold-lt) !important; }
    .page-hero { background: var(--navy); padding: 120px 6% 80px; }
    .page-hero .eyebrow { display: inline-flex; align-items: center; gap: .5rem; font-size: .72rem; font-weight: 700; letter-spacing: 1.8px; text-transform: uppercase; color: var(--gold-lt); margin-bottom: 1.25rem; }
    .page-hero .eyebrow::before { content: ''; display: block; width: 24px; height: 1.5px; background: var(--gold); }
    .page-hero h1 { font-family: 'DM Serif Display', serif; font-size: clamp(2rem, 4vw, 3.2rem); color: var(--white); line-height: 1.15; margin-bottom: 1.25rem; max-width: 800px; }
    .page-hero h1 em { font-style: italic; color: var(--gold-lt); }
    .page-hero .subtitle { font-size: 1.05rem; color: rgba(255,255,255,0.6); line-height: 1.75; max-width: 640px; margin-bottom: 2rem; }
    .page-hero .cta-row { display: flex; gap: 1rem; flex-wrap: wrap; }
    .btn { display: inline-flex; align-items: center; gap: .5rem; font-family: 'Inter', sans-serif; font-weight: 600; font-size: .9rem; padding: .8rem 1.75rem; border-radius: 7px; text-decoration: none; transition: all .2s; cursor: pointer; border: none; }
    .btn-gold { background: var(--gold); color: var(--white); box-shadow: 0 4px 16px rgba(201,146,42,0.35); }
    .btn-gold:hover { background: var(--gold-lt); transform: translateY(-1px); }
    .btn-ghost { background: transparent; color: rgba(255,255,255,0.7); border: 1px solid rgba(255,255,255,0.2); }
    .btn-ghost:hover { border-color: rgba(255,255,255,0.5); color: var(--white); }
    .section { padding: 80px 6%; }
    .section-alt { background: var(--off-white); }
    .section-navy { background: var(--navy); color: var(--white); }
    .section h2 { font-family: 'DM Serif Display', serif; font-size: clamp(1.75rem, 3vw, 2.5rem); margin-bottom: 1rem; }
    .section-navy h2 { color: var(--white); }
    .section p { font-size: 1rem; line-height: 1.8; color: var(--gray-600); margin-bottom: 1rem; max-width: 720px; }
    .section-navy p { color: rgba(255,255,255,0.65); }
    .why-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1.5rem; margin-top: 2rem; }
    .why-card { background: var(--white); border: 1px solid var(--gray-200); border-radius: var(--radius); padding: 1.75rem; }
    .why-icon { font-size: 1.75rem; margin-bottom: .75rem; }
    .why-card h3 { font-size: 1rem; font-weight: 700; margin-bottom: .5rem; }
    .why-card p { font-size: .9rem; color: var(--gray-600); margin: 0; }
    .faq-list { margin-top: 2rem; }
    .faq-item { border-bottom: 1px solid var(--gray-200); padding: 1.5rem 0; }
    .faq-item:last-child { border-bottom: none; }
    .faq-q { font-weight: 700; font-size: 1rem; margin-bottom: .5rem; color: var(--navy); }
    .faq-a { font-size: .95rem; color: var(--gray-600); line-height: 1.75; }
    .cta-section { background: var(--navy); padding: 80px 6%; text-align: center; }
    .cta-section h2 { font-family: 'DM Serif Display', serif; color: var(--white); font-size: clamp(1.75rem, 3vw, 2.5rem); margin-bottom: 1rem; }
    .cta-section p { color: rgba(255,255,255,0.6); max-width: 560px; margin: 0 auto 2rem; }
    .form-wrap { background: var(--white); border-radius: 12px; padding: 2.5rem; max-width: 640px; margin: 0 auto; text-align: left; }
    .frow { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; }
    .fgroup { display: flex; flex-direction: column; gap: .35rem; margin-bottom: 1rem; }
    .fgroup label { font-size: .8rem; font-weight: 700; text-transform: uppercase; letter-spacing: .6px; color: var(--gray-600); }
    .fgroup input, .fgroup select, .fgroup textarea { padding: .75rem 1rem; border: 1.5px solid var(--gray-200); border-radius: 7px; font-size: .95rem; font-family: 'Inter', sans-serif; transition: border-color .2s; }
    .fgroup input:focus, .fgroup select:focus, .fgroup textarea:focus { outline: none; border-color: var(--gold); }
    .fgroup textarea { min-height: 100px; resize: vertical; }
    .fsub { width: 100%; background: var(--gold); color: var(--white); border: none; padding: .9rem; border-radius: 7px; font-size: 1rem; font-weight: 700; cursor: pointer; transition: background .2s; }
    .fsub:hover { background: var(--gold-lt); }
    .related-links { background: var(--gray-100); padding: 60px 6%; }
    .related-links h3 { font-family: 'DM Serif Display', serif; font-size: 1.5rem; margin-bottom: 1.5rem; }
    .link-grid { display: flex; flex-wrap: wrap; gap: 1rem; }
    .link-grid a { background: var(--white); border: 1px solid var(--gray-200); border-radius: 7px; padding: .6rem 1.2rem; font-size: .9rem; color: var(--navy); text-decoration: none; font-weight: 500; transition: all .2s; }
    .link-grid a:hover { border-color: var(--gold); color: var(--gold); }
    footer { background: var(--navy); color: rgba(255,255,255,0.55); }
    .footer-top { display: grid; grid-template-columns: 1fr 2fr; gap: 3rem; padding: 60px 6% 40px; }
    .footer-logo { font-family: 'DM Serif Display', serif; font-size: 1.3rem; color: var(--white); text-decoration: none; display: block; margin-bottom: .5rem; }
    .footer-logo em { color: var(--gold-lt); font-style: normal; }
    .footer-tagline { font-size: .875rem; }
    .footer-cols { display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem; }
    .footer-col h5 { color: var(--white); font-size: .75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 1rem; }
    .footer-col a, .footer-col span { display: block; font-size: .875rem; color: rgba(255,255,255,0.45); text-decoration: none; margin-bottom: .5rem; }
    .footer-col a:hover { color: var(--gold-lt); }
    .footer-bottom { border-top: 1px solid rgba(255,255,255,0.07); padding: 1.25rem 6%; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: .5rem; }
    .footer-copy { font-size: .8rem; }
    .footer-seo { font-size: .75rem; color: rgba(255,255,255,0.3); }
    .updated { font-size: .75rem; color: rgba(255,255,255,0.3); }
    @media (max-width: 768px) { .frow { grid-template-columns: 1fr; } .footer-top { grid-template-columns: 1fr; } .footer-cols { grid-template-columns: 1fr 1fr; } .nav-links { display: none; } }
"""

NAV = """<nav>
  <a href="/" class="nav-logo">Zay <em>Supply</em> Co.</a>
  <ul class="nav-links">
    <li><a href="/#products">Products</a></li>
    <li><a href="/#serve">Who We Serve</a></li>
    <li><a href="/#branding">Custom Branding</a></li>
    <li><a href="/#contact" class="nav-btn">Get a Quote</a></li>
  </ul>
</nav>"""

FOOTER = f"""<footer>
  <div class="footer-top">
    <div class="footer-brand">
      <a href="/" class="footer-logo">Zay <em>Supply</em> Co.</a>
      <p class="footer-tagline">Local wholesale disposables for California food businesses.</p>
    </div>
    <div class="footer-cols">
      <div class="footer-col">
        <h5>Quick Links</h5>
        <a href="/#products">Products</a>
        <a href="/#serve">Who We Serve</a>
        <a href="/#branding">Custom Branding</a>
        <a href="/#contact">Get a Quote</a>
      </div>
      <div class="footer-col">
        <h5>Contact</h5>
        <a href="mailto:{EMAIL}">{EMAIL}</a>
        <a href="tel:9252555484">{PHONE}</a>
        <span>East Bay, California</span>
      </div>
      <div class="footer-col">
        <h5>Service Area</h5>
        <span>East Bay · Bay Area</span>
        <span>Los Angeles · Sacramento</span>
        <span>All of California</span>
      </div>
    </div>
  </div>
  <div class="footer-bottom">
    <div class="footer-copy">© 2026 Zay Supply Co. · East Bay, California</div>
    <div class="footer-seo">Walnut Creek · Oakland · Berkeley · Concord · Fremont · San Jose · Los Angeles</div>
    <div class="updated">Updated {UPDATED}</div>
  </div>
</footer>"""

QUOTE_FORM = f"""
<section class="cta-section" id="contact">
  <h2>Get a Quote from Zay Supply Co.</h2>
  <p>Tell us what you need — we'll respond within one business day with pricing and availability.</p>
  <div class="form-wrap">
    <form action="mailto:{EMAIL}" method="post" enctype="text/plain">
      <div class="frow">
        <div class="fgroup"><label>Business Name</label><input type="text" name="business" placeholder="Your business" /></div>
        <div class="fgroup"><label>Your Name</label><input type="text" name="name" placeholder="Your name" /></div>
      </div>
      <div class="frow">
        <div class="fgroup"><label>Phone</label><input type="tel" name="phone" placeholder="(xxx) xxx-xxxx" /></div>
        <div class="fgroup"><label>Email</label><input type="email" name="email" placeholder="you@business.com" /></div>
      </div>
      <div class="fgroup">
        <label>What Products Do You Need?</label>
        <select name="products">
          <option value="">Select primary product...</option>
          <option>Hot Cups (8–20oz)</option><option>Cold Cups</option><option>Boba Cups</option>
          <option>Lids &amp; Sleeves</option><option>Straws (Paper / Plastic / Boba)</option>
          <option>Utensils &amp; Cutlery</option><option>Custom Branded Cups</option>
          <option>Food Containers</option><option>Eco-Friendly Disposables</option>
          <option>Multiple Products</option>
        </select>
      </div>
      <div class="fgroup">
        <label>Monthly Volume &amp; Notes</label>
        <textarea name="message" placeholder="How much do you order monthly? Any specific needs?"></textarea>
      </div>
      <button type="submit" class="fsub">Send Quote Request →</button>
    </form>
  </div>
</section>"""

SCHEMA = """{
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "name": "Zay Supply Co.",
    "description": "Wholesale disposable supplies for California food businesses — cups, lids, straws, utensils, and custom branding.",
    "url": "https://zaysupply.com",
    "telephone": "+19252555484",
    "email": "reshad@zaysupply.com",
    "address": {"@type": "PostalAddress", "addressRegion": "CA", "addressCountry": "US"},
    "areaServed": "California",
    "priceRange": "$$"
}"""

def head(title, desc, slug, extra_schema=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-PLACEHOLDER"></script>
  <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-PLACEHOLDER');</script>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{desc}" />
  <link rel="canonical" href="{BASE_URL}/{slug}.html" />
  <script type="application/ld+json">{SCHEMA}</script>
  {extra_schema}
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=DM+Serif+Display:ital@0;1&display=swap" rel="stylesheet">
  <style>{CSS}</style>
</head>
<body>
{NAV}"""

def why_zay(city="California"):
    return f"""
<section class="section section-alt">
  <h2>Why Food Businesses in {city} Choose Zay Supply Co.</h2>
  <div class="why-grid">
    <div class="why-card"><div class="why-icon">💰</div><h3>10–20% Below Market Pricing</h3><p>We source direct and pass the savings to you. Most businesses save $200–$800/month switching from retail or national distributors.</p></div>
    <div class="why-card"><div class="why-icon">🏷️</div><h3>Custom Branding at Low Minimums</h3><p>Get your logo on cups, bags, and containers without 10,000-unit minimums. We work with small and growing businesses.</p></div>
    <div class="why-card"><div class="why-icon">📦</div><h3>CA-Warehoused Inventory</h3><p>Stock on hand in California means 1–3 day delivery anywhere in the state — not 7–14 days from an out-of-state warehouse.</p></div>
    <div class="why-card"><div class="why-icon">🤝</div><h3>Local, Relationship-Driven Service</h3><p>Talk directly to Reshad, the founder. No call centers, no account managers. Real answers within hours.</p></div>
    <div class="why-card"><div class="why-icon">✅</div><h3>Flexible MOQs for Small Business</h3><p>We don't require pallet orders. Start with a case, scale up as you grow. No contracts, no lock-in.</p></div>
  </div>
</section>"""

def faq_schema(faqs):
    items = []
    for q, a in faqs:
        items.append(f'{{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a}"}}}}')
    return f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{",".join(items)}]}}</script>'

def related_section(links):
    anchors = "\n".join([f'<a href="/{slug}.html">{label}</a>' for slug, label in links])
    return f"""
<section class="related-links">
  <h3>Related Resources</h3>
  <div class="link-grid">{anchors}</div>
</section>"""

# ── PAGE GENERATORS ────────────────────────────────────────────────────────────

VALUE_PROP_INTROS = [
    "Running a food business in {city} means every dollar counts.",
    "For {city} food businesses, supply costs are one of the biggest controllable expenses.",
    "Independent cafes, boba shops, and restaurants in {city} face the same challenge:",
    "Smart food operators in {city} know that supply costs compound fast.",
    "Whether you run a single-location cafe or a growing chain in {city},",
]

def gen_location_product_page(city, region, product):
    city_slug = city.lower().replace(" ", "-")
    prod_slug = product["slug"]
    slug = f"{prod_slug}-{city_slug}"
    kw = product["keyword"]
    kw_city = f"{kw} {city}"
    title = f"{kw.title()} {city}, CA | Zay Supply Co."
    desc = f"Buy {kw} in {city}, CA. Zay Supply Co. offers {product['price_range']} — 10–20% below market, CA-warehoused, fast delivery. Call {PHONE}."
    
    intro = random.choice(VALUE_PROP_INTROS).format(city=city)
    
    faqs = [
        (f"Where can I buy {kw} in {city}, CA?",
         f"Zay Supply Co. serves {city} and the broader {region} with fast delivery from California-warehoused stock. Contact us at {EMAIL} or call {PHONE} for pricing and availability."),
        (f"What sizes of {product['name'].lower()} do you offer?",
         f"We stock {product['sizes']}. All sizes are available in case quantities with flexible minimum orders for {city} businesses."),
        (f"How much do {kw} cost in {city}?",
         f"Our pricing ranges from {product['price_range']} depending on size and quantity. Most {city} businesses save 10–20% compared to Restaurant Depot, Costco, or Amazon Business."),
        (f"How quickly can I get {kw} delivered to {city}?",
         f"Since our inventory is warehoused in California, most {city} orders arrive in 1–3 business days — far faster than national suppliers shipping from out of state."),
        (f"Do you have a minimum order for {city} businesses?",
         f"We work with businesses of all sizes in {city}. Unlike national distributors, we don't require pallet orders. Start with a single case and scale up as your volume grows."),
    ]

    faq_html = "".join([f'<div class="faq-item"><div class="faq-q">{q}</div><div class="faq-a">{a}</div></div>' for q, a in faqs])

    html = head(title, desc, slug, faq_schema(faqs))
    html += f"""
<section class="page-hero">
  <div class="eyebrow">{region} · California</div>
  <h1>{kw.title()} in <em>{city}, CA</em></h1>
  <p class="subtitle">{intro} {product['desc']} Zay Supply Co. delivers to {city} and across {region} with pricing {product['price_range']} — well below what most local businesses pay today.</p>
  <div class="cta-row">
    <a href="#contact" class="btn btn-gold">Get a Quote →</a>
    <a href="tel:9252555484" class="btn btn-ghost">Call {PHONE}</a>
  </div>
</section>

<section class="section">
  <h2>{product['name']} for {city} Food Businesses</h2>
  <p>Zay Supply Co. is a California-based wholesale supplier serving {city}, {region}, and food businesses across the state. We specialize in {product['keyword']} for {product['use']} — with pricing designed for independent operators, not just big chains.</p>
  <p>Most {city} businesses sourcing {product['keyword']} are either paying retail prices at Costco or Restaurant Depot, or waiting 10+ days for national online suppliers to ship from out of state. We fix both problems: wholesale pricing from a California-warehoused supplier with 1–3 day delivery to {city}.</p>
  <p>Our {product['name'].lower()} are available in {product['sizes']}. Whether you need a single case to trial or a recurring monthly order, we work with your volume. Pricing starts at {product['price_range']} depending on size and quantity — typically 10–20% below what you're paying now.</p>
  <p>We also offer custom branding on many product lines, so you can get your logo on cups and packaging without the 10,000-unit minimums that most printers require. For {city} businesses building a brand, this is a game-changer.</p>
</section>

{why_zay(city)}

<section class="section">
  <h2>Frequently Asked Questions — {kw.title()} in {city}</h2>
  <div class="faq-list">{faq_html}</div>
</section>

{QUOTE_FORM}

{related_section([
    ("index", "Zay Supply Co. — Home"),
    (f"{prod_slug}-california", f"{product['name']} California"),
    ("wholesale-cafe-supplies-east-bay", "Wholesale Cafe Supplies East Bay"),
    ("how-to-cut-cafe-supply-costs", "How to Cut Supply Costs 20%"),
])}

{FOOTER}
</body></html>"""
    return slug, html


def gen_icp_page(icp):
    slug = f"wholesale-supplies-{icp['slug']}-california"
    title = f"{icp['keyword'].title()} | Zay Supply Co."
    desc = f"Wholesale disposable supplies for {icp['name'].lower()} in California. Cups, lids, straws, containers — 10–20% below market, fast CA delivery. Get a quote: {PHONE}."

    faqs = [
        (f"What wholesale supplies do {icp['name'].lower()} need most?",
         f"{icp['name']} typically need {icp['products']}. Zay Supply Co. carries all of these with flexible order quantities for California businesses."),
        (f"How do I get wholesale pricing for my {icp['name'].lower().rstrip('s')}?",
         f"Contact Zay Supply Co. at {EMAIL} or {PHONE}. We'll send you a custom quote based on your volume and product mix — no commitment required."),
        (f"What's the minimum order for {icp['name'].lower()}?",
         f"We work with businesses of all sizes — from single-location operators to multi-unit chains. No pallet minimums required. Start with a case and scale up."),
        (f"Do you offer custom branded supplies for {icp['name'].lower()}?",
         f"Yes. We offer custom logo printing on cups, bags, and containers at low minimums. This is especially popular with {icp['name'].lower()} building brand recognition."),
        (f"How quickly can you deliver to California {icp['name'].lower()}?",
         f"Our inventory is warehoused in California. Most orders arrive in 1–3 business days — much faster than national distributors shipping from out of state."),
    ]

    faq_html = "".join([f'<div class="faq-item"><div class="faq-q">{q}</div><div class="faq-a">{a}</div></div>' for q, a in faqs])

    html = head(title, desc, slug, faq_schema(faqs))
    html += f"""
<section class="page-hero">
  <div class="eyebrow">California · Food Service</div>
  <h1>Wholesale Supplies for <em>{icp['name']}</em> in California</h1>
  <p class="subtitle">Zay Supply Co. supplies California {icp['name'].lower()} with {icp['products']} — at 10–20% below market pricing, with fast delivery from California-warehoused stock.</p>
  <div class="cta-row">
    <a href="#contact" class="btn btn-gold">Get a Quote →</a>
    <a href="tel:9252555484" class="btn btn-ghost">Call {PHONE}</a>
  </div>
</section>

<section class="section">
  <h2>Why California {icp['name']} Choose Zay Supply Co.</h2>
  <p>Every {icp['name'].lower().rstrip('s')} in California faces the same challenge: {icp['pain']}. Zay Supply Co. was built to solve this problem for independent operators who don't have the volume to negotiate enterprise rates with Sysco or US Foods.</p>
  <p>We supply {icp['name'].lower()} across California — from the East Bay to Los Angeles — with {icp['products']}. Our pricing is 10–20% below what most businesses pay at Restaurant Depot, Costco, or through Amazon Business, and our California-warehoused inventory means 1–3 day delivery instead of 7–14 days from national suppliers.</p>
  <p>We also offer custom branding at low minimums. Whether you want your logo on cups, bags, or containers, we can make it happen without the 10,000-unit minimums that most printers require. This is particularly valuable for {icp['name'].lower()} looking to differentiate their brand at the counter.</p>
  <p>Zay Supply Co. is run by a founder who talks directly to every customer. No call centers, no account managers you'll never meet again. When you have a question or need a rush order, you get a real answer within hours — not days.</p>
</section>

{why_zay("California")}

<section class="section section-alt">
  <h2>Products We Supply for {icp['name']}</h2>
  <p>Our product line covers everything {icp['name'].lower()} need day to day:</p>
  <p><strong>{icp['products'].replace(", ", " · ")}</strong></p>
  <p>All products are available in case quantities with flexible minimums. We can also bundle products into a custom supply kit tailored to your monthly usage — just tell us your volume and we'll build the right package.</p>
</section>

<section class="section">
  <h2>Frequently Asked Questions</h2>
  <div class="faq-list">{faq_html}</div>
</section>

{QUOTE_FORM}

{related_section([
    ("index", "Zay Supply Co. — Home"),
    ("wholesale-hot-cups-california", "Wholesale Hot Cups California"),
    ("wholesale-cold-cups-california", "Wholesale Cold Cups California"),
    ("how-to-cut-cafe-supply-costs", "Cut Supply Costs 20%"),
])}

{FOOTER}
</body></html>"""
    return slug, html


def gen_comparison_page(slug, title, competitor, pain):
    desc_comp = competitor if competitor else "expensive retail channels"
    desc = f"Looking for a {desc_comp} alternative in California? Zay Supply Co. offers wholesale disposables 10–20% below market. Local CA stock, fast delivery. Call {PHONE}."
    
    faqs = [
        (f"Why should I switch from {desc_comp} to Zay Supply Co.?",
         f"Zay Supply Co. offers wholesale pricing 10–20% below market, California-warehoused inventory for 1–3 day delivery, and direct founder access — advantages that national distributors and retail channels can't match."),
        ("How do I know if I'm overpaying for supplies?",
         f"If you're buying from Costco, Amazon Business, or a national distributor, you're likely paying 15–30% above true wholesale pricing. Contact us at {EMAIL} for a free pricing comparison on your current order."),
        ("What's the minimum order at Zay Supply Co.?",
         "We don't require large minimums. Start with a single case and scale up as your volume grows. No contracts, no lock-in."),
        ("How fast can you deliver?",
         f"Our inventory is in California. Most orders arrive in 1–3 business days. Compare that to national suppliers shipping from Texas or the Midwest — 7–14 days is common."),
        ("Do you offer custom branded products?",
         "Yes. Custom logo cups, bags, and containers at low minimums — a major advantage over national distributors who often require 10,000+ unit runs."),
    ]

    faq_html = "".join([f'<div class="faq-item"><div class="faq-q">{q}</div><div class="faq-a">{a}</div></div>' for q, a in faqs])

    comp_mention = f"Tired of {pain}?" if pain else "Looking for better wholesale pricing in California?"

    html = head(title + " | Zay Supply Co.", desc, slug, faq_schema(faqs))
    html += f"""
<section class="page-hero">
  <div class="eyebrow">California · Wholesale Supplies</div>
  <h1><em>{title}</em></h1>
  <p class="subtitle">{comp_mention} Zay Supply Co. is the local California wholesale supplier for cups, lids, straws, utensils, and custom branded disposables — at 10–20% below market pricing.</p>
  <div class="cta-row">
    <a href="#contact" class="btn btn-gold">Get a Free Quote →</a>
    <a href="tel:9252555484" class="btn btn-ghost">Call {PHONE}</a>
  </div>
</section>

<section class="section">
  <h2>Why California Food Businesses Are Making the Switch</h2>
  <p>California's independent cafes, boba shops, food trucks, and QSRs are increasingly moving away from national distributors and retail channels toward local wholesale suppliers like Zay Supply Co. The reasons are straightforward: better pricing, faster delivery, and actual human support.</p>
  <p>{comp_mention} You're not alone. Many of our customers came to us after years of {pain} and were surprised by how much they were able to save — and how much easier the ordering process became with a local supplier who actually picks up the phone.</p>
  <p>Zay Supply Co. warehouses inventory in California, which means 1–3 day delivery to most of the state. We offer wholesale pricing on cups, lids, straws, utensils, food containers, napkins, and custom branded products — typically 10–20% below what businesses pay through retail or national distribution channels.</p>
  <p>We also offer custom logo printing on cups and packaging at low minimums, so businesses building their brand aren't forced into 10,000-unit runs just to get their name on a cup.</p>
</section>

{why_zay("California")}

<section class="section section-alt">
  <h2>What We Supply</h2>
  <p>Everything California food businesses need, available in case quantities with flexible minimums:</p>
  <p>Hot cups (8–20oz) · Cold cups (16–32oz) · Boba cups (24oz, 32oz) · Lids (hot, cold, dome) · Straws (regular, boba, paper, eco) · Napkins · Food containers &amp; clamshells · Coffee sleeves · Disposable utensils · Paper &amp; kraft bags · Custom branded cups &amp; packaging · Eco-friendly disposables</p>
</section>

<section class="section">
  <h2>Frequently Asked Questions</h2>
  <div class="faq-list">{faq_html}</div>
</section>

{QUOTE_FORM}

{related_section([
    ("index", "Zay Supply Co. — Home"),
    ("wholesale-hot-cups-california", "Wholesale Hot Cups California"),
    ("wholesale-supplies-coffee-shops-california", "Supplies for Coffee Shops"),
    ("how-to-switch-wholesale-suppliers", "How to Switch Suppliers"),
])}

{FOOTER}
</body></html>"""
    return slug, html


def gen_howto_page(slug, title, problem, solution):
    desc = f"{title} — practical guide for California food businesses. {solution.capitalize()}. Zay Supply Co. helps CA operators cut costs."

    faqs = [
        ("How much can a California food business save on supplies?",
         "Most independent cafes and food businesses in California save 10–20% when switching from retail or national distributor purchasing to a local wholesale supplier like Zay Supply Co. On $2,000/month in supplies, that's $200–$400 per month in savings."),
        ("What's the first step to reducing supply costs?",
         f"Audit your current spending by product category, then get a comparative quote from a local wholesale supplier. Zay Supply Co. offers free pricing comparisons — email {EMAIL} with your current order list."),
        ("Does switching suppliers take a long time?",
         "Not with a local supplier. Zay Supply Co. can onboard a new customer and fulfill a first order within 1–3 business days. Most businesses transition within a single ordering cycle."),
        ("Can I get custom branded products as a small business?",
         "Yes. Zay Supply Co. offers custom logo cups and packaging at low minimums — far lower than the 10,000+ units that most national printers require. This is accessible even for single-location operators."),
        ("How do I contact Zay Supply Co.?",
         f"Email {EMAIL} or call {PHONE}. You'll speak directly with Reshad, the founder — not a call center."),
    ]

    faq_html = "".join([f'<div class="faq-item"><div class="faq-q">{q}</div><div class="faq-a">{a}</div></div>' for q, a in faqs])

    html = head(title + " | Zay Supply Co.", desc, slug, faq_schema(faqs))
    html += f"""
<section class="page-hero">
  <div class="eyebrow">Guide · California Food Businesses</div>
  <h1><em>{title}</em></h1>
  <p class="subtitle">For California food business owners dealing with {problem}. This guide covers {solution}.</p>
  <div class="cta-row">
    <a href="#contact" class="btn btn-gold">Get a Free Quote →</a>
    <a href="tel:9252555484" class="btn btn-ghost">Call {PHONE}</a>
  </div>
</section>

<section class="section">
  <h2>{title}</h2>
  <p>If you're running a food business in California — a cafe, boba shop, food truck, or quick-service restaurant — your disposable supply costs are one of the most controllable line items in your P&amp;L. Most independent operators are paying 15–30% more than they need to, simply because they haven't had time to shop alternatives.</p>
  <p>This guide is for business owners dealing with {problem}. We'll cover {solution}, with practical steps you can take immediately.</p>
  <p>Zay Supply Co. is a California-based wholesale supplier that works with independent food businesses across the East Bay, Bay Area, Los Angeles, Sacramento, and beyond. We offer wholesale pricing on cups, lids, straws, utensils, food containers, and custom branded products — typically 10–20% below what businesses pay through Restaurant Depot, Costco, Amazon Business, or national distributors like Sysco and US Foods.</p>
  <p>Our inventory is warehoused in California, which means 1–3 day delivery to most of the state. And unlike national suppliers, you deal directly with the founder — not a call center or rotating account managers.</p>
  <p>The single biggest lever most California food businesses can pull is <strong>consolidating vendors and switching to a local wholesale supplier</strong>. If you're buying supplies from 3–4 different places, you're paying coordination overhead and missing out on volume pricing. A single local supplier with broad product coverage can simplify your ordering and cut your per-unit costs significantly.</p>
  <p>Here are the steps: First, audit your last 3 months of supply invoices by product category. Identify your top 5–10 items by spend. Then request a comparative quote from Zay Supply Co. — email your list to {EMAIL} and we'll send you line-item pricing within 24 hours. Most businesses find they can save 10–20% immediately on their highest-volume items.</p>
  <p>Custom branding is another lever. If you're serving drinks in plain white cups, you're missing a free brand impression with every customer. Custom logo cups through Zay Supply Co. start at low minimums and cost only marginally more than unbranded options at scale — often less than $0.05/cup difference at volume.</p>
</section>

{why_zay("California")}

<section class="section section-alt">
  <h2>Products Available from Zay Supply Co.</h2>
  <p>Everything California food businesses need, at wholesale pricing:</p>
  <p>Hot cups (8–20oz) · Cold cups (16–32oz) · Boba cups · Lids · Straws (regular, boba, paper) · Napkins · Food containers · Coffee sleeves · Utensils · Paper bags · Custom branded cups · Eco-friendly disposables</p>
  <p>All available in case quantities with flexible minimums. No contracts. No lock-in.</p>
</section>

<section class="section">
  <h2>Frequently Asked Questions</h2>
  <div class="faq-list">{faq_html}</div>
</section>

{QUOTE_FORM}

{related_section([
    ("index", "Zay Supply Co. — Home"),
    ("wholesale-hot-cups-california", "Wholesale Hot Cups California"),
    ("wholesale-supplies-coffee-shops-california", "Supplies for Coffee Shops"),
    ("sysco-alternative-california", "Sysco Alternative California"),
])}

{FOOTER}
</body></html>"""
    return slug, html


def gen_product_state_page(product):
    slug = f"{product['slug']}-california"
    kw = product["keyword"]
    title = f"{kw.title()} California | Zay Supply Co."
    desc = f"{kw.title()} across California. {product['price_range']} — 10–20% below market, CA-warehoused, 1–3 day delivery. Get a quote from Zay Supply Co."

    faqs = [
        (f"Where can I buy {kw} in California?",
         f"Zay Supply Co. is a California-based wholesale supplier serving the entire state. We stock {product['name'].lower()} in {product['sizes']} with fast 1–3 day delivery from California-warehoused inventory."),
        (f"What are the best prices for {kw} in California?",
         f"Zay Supply Co. offers {product['price_range']} — typically 10–20% below what businesses pay at Restaurant Depot, Costco, or through national distributors. Contact us for a custom quote."),
        (f"What sizes of {kw} does Zay Supply Co. carry?",
         f"We stock {product['sizes']}. All sizes are available in case quantities."),
        ("Do you offer custom branded products?",
         f"Yes. Custom logo printing is available on many of our product lines at low minimums. Contact us at {EMAIL} for branding options."),
        ("How fast is delivery in California?",
         "Our inventory is warehoused in California. Most orders arrive in 1–3 business days statewide."),
    ]

    faq_html = "".join([f'<div class="faq-item"><div class="faq-q">{q}</div><div class="faq-a">{a}</div></div>' for q, a in faqs])

    html = head(title, desc, slug, faq_schema(faqs))
    html += f"""
<section class="page-hero">
  <div class="eyebrow">California · Statewide</div>
  <h1>{kw.title()} <em>California</em></h1>
  <p class="subtitle">{product['desc']} Zay Supply Co. serves food businesses across California with wholesale pricing at {product['price_range']} — 10–20% below what most businesses pay today.</p>
  <div class="cta-row">
    <a href="#contact" class="btn btn-gold">Get a Quote →</a>
    <a href="tel:9252555484" class="btn btn-ghost">Call {PHONE}</a>
  </div>
</section>

<section class="section">
  <h2>{product['name']} for California Food Businesses</h2>
  <p>Zay Supply Co. is a California-based wholesale supplier of {product['keyword']}. We serve independent cafes, coffee shops, boba shops, food trucks, QSRs, bakeries, and other food businesses across the state — from the East Bay to Los Angeles, Sacramento to San Diego.</p>
  <p>Our {product['name'].lower()} are available in {product['sizes']} and are suitable for {product['use']}. Pricing starts at {product['price_range']}, with volume discounts available for larger orders. We work with businesses at all stages — from a new cafe placing its first case order to a multi-unit operator with consistent monthly volume.</p>
  <p>Because we warehouse inventory in California, delivery to most of the state takes 1–3 business days — dramatically faster than national suppliers shipping from out-of-state warehouses. This matters when you're running low mid-week and can't wait 10 days for a replenishment.</p>
  <p>We also offer custom branding on many product lines, including {product['name'].lower()}. Logo printing at low minimums means even single-location businesses can build brand recognition through their packaging — without the 10,000-unit minimums required by most printers.</p>
</section>

{why_zay("California")}

<section class="section">
  <h2>Frequently Asked Questions</h2>
  <div class="faq-list">{faq_html}</div>
</section>

{QUOTE_FORM}

{related_section([
    ("index", "Zay Supply Co. — Home"),
    (f"{product['slug']}-oakland", f"{product['name']} Oakland"),
    (f"{product['slug']}-san-francisco", f"{product['name']} San Francisco"),
    ("wholesale-supplies-coffee-shops-california", "Supplies for Coffee Shops"),
])}

{FOOTER}
</body></html>"""
    return slug, html


# ── MAIN ──────────────────────────────────────────────────────────────────────

def main():
    pages = []

    # 1. Location × Product pages
    print("Generating location × product pages...")
    for city, region in ALL_CITIES:
        for product in PRODUCTS:
            slug, html = gen_location_product_page(city, region, product)
            pages.append((slug, html))

    # 2. Product × California (statewide) pages
    print("Generating statewide product pages...")
    for product in PRODUCTS:
        slug, html = gen_product_state_page(product)
        pages.append((slug, html))

    # 3. ICP pages
    print("Generating ICP pages...")
    for icp in ICPS:
        slug, html = gen_icp_page(icp)
        pages.append((slug, html))

    # 4. Comparison pages
    print("Generating comparison pages...")
    for slug, title, competitor, pain in COMPARISONS:
        _, html = gen_comparison_page(slug, title, competitor, pain)
        pages.append((slug, html))

    # 5. How-to pages
    print("Generating how-to pages...")
    for slug, title, problem, solution in HOWTOS:
        _, html = gen_howto_page(slug, title, problem, solution)
        pages.append((slug, html))

    # Write all pages
    print(f"\nWriting {len(pages)} pages...")
    for slug, html in pages:
        path = os.path.join(OUTPUT_DIR, f"{slug}.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)

    # robots.txt
    with open(os.path.join(OUTPUT_DIR, "robots.txt"), "w") as f:
        f.write("""User-agent: *
Allow: /

User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Google-Extended
Allow: /

Sitemap: https://zaysupply.com/sitemap.xml
""")

    # llms.txt
    with open(os.path.join(OUTPUT_DIR, "llms.txt"), "w") as f:
        f.write(f"""# Zay Supply Co.

> Wholesale disposable supplies for California food businesses. 10–20% below market pricing, custom branding, CA-warehoused inventory, low minimums.

## About
Zay Supply Co. is a California-based wholesale supplier of cups, lids, straws, utensils, and custom branded disposables. We serve coffee shops, cafes, boba shops, food trucks, QSRs, gas stations, and other food businesses across California.

## Products
- Hot cups (8oz–20oz) wholesale
- Cold cups (16oz–32oz) wholesale
- Boba cups (24oz, 32oz) wholesale
- Cup lids (hot, cold, dome) wholesale
- Straws (regular, boba, eco, paper) wholesale
- Napkins and tissue wholesale
- Food containers and clamshells wholesale
- Coffee sleeves wholesale
- Custom branded and printed cups
- Disposable utensils wholesale
- Paper and kraft bags wholesale
- Eco-friendly and compostable disposables

## Service Area
California — primary focus East Bay (Oakland, Berkeley, Walnut Creek, Orinda, Lafayette, Moraga, Concord, Fremont, San Leandro). Also serving Bay Area, Los Angeles, Sacramento, and all of California.

## Value Proposition
- 10–20% below market pricing
- California-warehoused inventory (1–3 day delivery statewide)
- Custom branding at low minimums
- Direct founder access — no call centers
- Flexible MOQs for small and growing businesses

## Contact
Email: {EMAIL}
Phone: {PHONE}
Website: https://zaysupply.com
""")

    # sitemap.xml
    all_slugs = ["index"] + [slug for slug, _ in pages]
    sitemap_entries = "\n".join([
        f"  <url><loc>{BASE_URL}/{'' if s == 'index' else s + '.html'}</loc><lastmod>2026-04-21</lastmod><changefreq>monthly</changefreq><priority>{'1.0' if s == 'index' else '0.8'}</priority></url>"
        for s in all_slugs
    ])
    with open(os.path.join(OUTPUT_DIR, "sitemap.xml"), "w") as f:
        f.write(f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{sitemap_entries}
</urlset>""")

    print(f"\n✅ Done! Generated {len(pages)} pages + sitemap.xml + robots.txt + llms.txt")
    print(f"Total files: {len(pages) + 3}")

if __name__ == "__main__":
    main()
