with open("static/index.html", "r") as f:
    html = f.read()

seo_block = """  <!-- Primary Meta Tags -->
  <title>CamelliaPluck-AI | Low-Cost AI-Enabled Selective Tea Plucker (NESFIC-I-05)</title>
  <meta name="title" content="CamelliaPluck-AI | Low-Cost AI-Enabled Selective Tea Plucker (NESFIC-I-05)">
  <meta name="description" content="Autonomous AI-driven selective tea plucking solution for 'Two Leaves and a Bud' under NESFIC 2026 (Govt of Assam & TRA Tocklai). Edge computer vision, gentle pneumatic micro-shear end-effector, and estate telemetry.">
  <meta name="keywords" content="tea plucking ai, two leaves and a bud, nesfic-i-05, tra tocklai, assam tea innovation, selective tea harvesting, agri-robotics, camellia sinensis, fine leaf count, edge ai, computer vision yolo">
  <meta name="author" content="Ron Hatibaruah">
  <meta name="robots" content="index, follow">
  <meta name="theme-color" content="#062413">
  <link rel="canonical" href="https://assam-tea-pluck-ai.pages.dev/">

  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <link rel="apple-touch-icon" href="/favicon.svg">

  <!-- Open Graph / Facebook -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://assam-tea-pluck-ai.pages.dev/">
  <meta property="og:title" content="CamelliaPluck-AI | Low-Cost AI Selective Tea Plucker (NESFIC-I-05)">
  <meta property="og:description" content="AI-enabled selective harvesting of tender 'Two Leaves and a Bud' for Assam tea gardens. >=88% Fine Leaf Count, 3.4x productivity, zero bush canopy damage.">
  <meta property="og:image" content="https://assam-tea-pluck-ai.pages.dev/assets/vision_detection_demo.png">
  <meta property="og:site_name" content="CamelliaPluck-AI">

  <!-- Twitter -->
  <meta property="twitter:card" content="summary_large_image">
  <meta property="twitter:url" content="https://assam-tea-pluck-ai.pages.dev/">
  <meta property="twitter:title" content="CamelliaPluck-AI | Selective Tea Plucker (NESFIC-I-05)">
  <meta property="twitter:description" content="Official AI-driven selective tea plucking solution for 'Two Leaves and a Bud' under NESFIC 2026 (Govt of Assam & TRA Tocklai).">
  <meta property="twitter:image" content="https://assam-tea-pluck-ai.pages.dev/assets/vision_detection_demo.png">

  <!-- JSON-LD Structured Data for Rich Search Snippets -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "CamelliaPluck-AI",
    "operatingSystem": "Linux / Embedded TensorRT / FreeRTOS",
    "applicationCategory": "AgricultureRoboticsApplication",
    "offers": {
      "@type": "Offer",
      "price": "0",
      "priceCurrency": "INR"
    },
    "description": "Low-Cost AI-Enabled Selective Plucking Solution for 'Two Leaves and a Bud' under Assam Startup Mission NESFIC-I-05 and Tea Research Association (TRA) Tocklai.",
    "author": {
      "@type": "Person",
      "name": "Ron Hatibaruah"
    },
    "provider": {
      "@type": "Organization",
      "name": "Tea Research Association (TRA) Tocklai & Startup Assam",
      "url": "https://startup.assam.gov.in/nesfic26/problem-statements/nesfic-i-05"
    }
  }
  </script>
"""

# Replace the existing title and basic meta tags with full SEO suite
old_head_part = """  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CamelliaPluck-AI | NESFIC-I-05 Selective Tea Plucker & Proposal Suite</title>"""

new_head_part = """  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
""" + seo_block.strip()

if old_head_part in html:
    html = html.replace(old_head_part, new_head_part)
    with open("static/index.html", "w") as f:
        f.write(html)
    with open("index.html", "w") as f:
        f.write(html)
    print("SEO tags and Favicon successfully injected into static/index.html and index.html!")
else:
    print("Could not find exact match in head")
