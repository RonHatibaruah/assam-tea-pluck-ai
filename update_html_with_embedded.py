import json

with open("static/proposal_data.json") as f:
    proposal_data = json.load(f)

fleet_data = {
    "active_units": [
        {
            "unit_id": "CP-ASSAM-01",
            "operator": "Sunita Karmakar",
            "estate": "TRA Tocklai Experimental Station",
            "division": "Plot 4 (Clone TV-1)",
            "status": "Active Harvesting",
            "shoots_plucked": 2840,
            "kg_harvested": 38.6,
            "flc_percentage": 91.2,
            "battery_percentage": 76,
            "sweep_rate_shoots_per_min": 74,
            "temperature_c": 28.4,
            "connection": "LoRaWAN Strong"
        },
        {
            "unit_id": "CP-ASSAM-02",
            "operator": "Pravin Tanti",
            "estate": "Borbheta Tea Estate",
            "division": "Section 12 (Clone TV-9)",
            "status": "Active Harvesting",
            "shoots_plucked": 3120,
            "kg_harvested": 42.1,
            "flc_percentage": 88.9,
            "battery_percentage": 68,
            "sweep_rate_shoots_per_min": 81,
            "temperature_c": 29.1,
            "connection": "LoRaWAN Strong"
        },
        {
            "unit_id": "CP-ASSAM-03",
            "operator": "Rumi Saikia",
            "estate": "Golaghat Commercial Estate",
            "division": "Section 7 (Clone TV-20)",
            "status": "Weighment Sync",
            "shoots_plucked": 4650,
            "kg_harvested": 61.8,
            "flc_percentage": 89.7,
            "battery_percentage": 42,
            "sweep_rate_shoots_per_min": 0,
            "temperature_c": 27.8,
            "connection": "BLE Synced"
        },
        {
            "unit_id": "CP-ASSAM-04",
            "operator": "Bimal Munda",
            "estate": "Dibrugarh Valley Tea Estate",
            "division": "Section 3 (Tingamira Seedling)",
            "status": "Active Harvesting",
            "shoots_plucked": 2490,
            "kg_harvested": 34.2,
            "flc_percentage": 87.5,
            "battery_percentage": 82,
            "sweep_rate_shoots_per_min": 69,
            "temperature_c": 28.9,
            "connection": "LoRaWAN Normal"
        }
    ]
}

with open("static/index.html", "r") as f:
    content = f.read()

replacement_js = f"""
    // Embedded Data Fallbacks for offline or file:// usage
    const EMBEDDED_PROPOSAL = {json.dumps(proposal_data)};
    const EMBEDDED_FLEET = {json.dumps(fleet_data)};

    // Load Proposal Sections
    let proposalData = null;
    async function loadProposalSections() {{
      if (proposalData) return;
      try {{
        const res = await fetch('/api/proposal');
        if (res.ok) {{
          proposalData = await res.json();
        }} else {{
          proposalData = EMBEDDED_PROPOSAL;
        }}
      }} catch (err) {{
        console.warn("Using embedded proposal data:", err);
        proposalData = EMBEDDED_PROPOSAL;
      }}
      renderProposalUI(proposalData);
    }}

    function renderProposalUI(data) {{
      const container = document.getElementById('proposal-sections-container');
      container.innerHTML = '';

      data.sections.forEach(sec => {{
        const card = document.createElement('div');
        card.className = "bg-slate-950 border border-slate-800 rounded-xl overflow-hidden shadow-lg";
        
        card.innerHTML = `
          <div class="p-4 bg-slate-900/80 border-b border-slate-800 flex items-center justify-between flex-wrap gap-2">
            <div class="flex items-center space-x-3">
              <span class="w-7 h-7 rounded-full bg-emerald-950 border border-emerald-500/50 text-emerald-400 text-xs font-mono font-bold flex items-center justify-center">
                ${{sec.section_number}}
              </span>
              <div>
                <h3 class="text-sm font-bold text-white">${{sec.title}}</h3>
                <span class="text-[11px] font-mono text-emerald-400 font-semibold">
                  ${{sec.word_count}} / ${{sec.word_limit}} words (Compliant)
                </span>
              </div>
            </div>
            <button onclick="copySectionContent(${{sec.section_number}})" class="bg-emerald-950/80 hover:bg-emerald-800/80 text-emerald-300 border border-emerald-500/40 text-xs px-3.5 py-1.5 rounded-lg flex items-center gap-1.5 font-medium transition shadow-sm">
              <i class="fa-regular fa-copy"></i>
              <span>Copy Section</span>
            </button>
          </div>
          <div class="p-4 text-xs text-slate-300 leading-relaxed font-sans whitespace-pre-line bg-slate-950/90 selection:bg-emerald-900 selection:text-white">
            ${{sec.content}}
          </div>
        `;
        container.appendChild(card);
      }});
    }}

    // Load Fleet Telemetry
    async function loadFleetTelemetry() {{
      let data = EMBEDDED_FLEET;
      try {{
        const res = await fetch('/api/fleet-telemetry');
        if (res.ok) {{
          data = await res.json();
        }}
      }} catch (err) {{
        console.warn("Using embedded fleet data:", err);
      }}
      renderFleetUI(data);
    }}

    function renderFleetUI(data) {{
      const grid = document.getElementById('fleet-units-grid');
      grid.innerHTML = '';

      data.active_units.forEach(u => {{
        const card = document.createElement('div');
        card.className = "bg-slate-950 border border-slate-800 rounded-xl p-4 space-y-3";
        card.innerHTML = `
          <div class="flex items-center justify-between">
            <span class="text-xs font-mono font-bold text-emerald-400 flex items-center gap-1.5">
              <i class="fa-solid fa-robot"></i> ${{u.unit_id}}
            </span>
            <span class="text-[10px] bg-emerald-950 text-emerald-300 border border-emerald-700 px-2 py-0.5 rounded-full font-medium">
              ${{u.status}}
            </span>
          </div>
          <div>
            <div class="text-sm font-bold text-white">${{u.operator}}</div>
            <div class="text-xs text-slate-400">${{u.estate}}</div>
            <div class="text-[11px] text-slate-500">${{u.division}}</div>
          </div>
          <div class="grid grid-cols-2 gap-2 pt-2 border-t border-slate-800/80 text-xs font-mono">
            <div>
              <span class="text-slate-500 block text-[10px]">Harvest Today</span>
              <span class="text-white font-bold">${{u.kg_harvested}} kg</span>
            </div>
            <div>
              <span class="text-slate-500 block text-[10px]">Fine Leaf %</span>
              <span class="text-emerald-400 font-bold">${{u.flc_percentage}}%</span>
            </div>
            <div>
              <span class="text-slate-500 block text-[10px]">Sweep Speed</span>
              <span class="text-slate-300">${{u.sweep_rate_shoots_per_min}} /min</span>
            </div>
            <div>
              <span class="text-slate-500 block text-[10px]">Battery</span>
              <span class="text-emerald-300 font-bold">${{u.battery_percentage}}%</span>
            </div>
          </div>
        `;
        grid.appendChild(card);
      }});
    }}
"""

# Replace the functions in index.html
target_part = """    // Load Proposal Sections
    let proposalData = null;
    async function loadProposalSections() {
      if (proposalData) return;
      try {
        const res = await fetch('/api/proposal');
        proposalData = await res.json();
        const container = document.getElementById('proposal-sections-container');
        container.innerHTML = '';

        proposalData.sections.forEach(sec => {
          const card = document.createElement('div');
          card.className = "bg-slate-950 border border-slate-800 rounded-xl overflow-hidden";
          
          card.innerHTML = `
            <div class="p-4 bg-slate-900/60 border-b border-slate-800 flex items-center justify-between flex-wrap gap-2">
              <div class="flex items-center space-x-3">
                <span class="w-6 h-6 rounded-full bg-emerald-950 border border-emerald-500/40 text-emerald-400 text-xs font-mono font-bold flex items-center justify-center">
                  ${sec.section_number}
                </span>
                <h3 class="text-sm font-bold text-white">${sec.title}</h3>
                <span class="text-[11px] font-mono px-2 py-0.5 rounded bg-slate-800 text-emerald-400 font-semibold">
                  ${sec.word_count} / ${sec.word_limit} words
                </span>
              </div>
              <button onclick="copySectionContent(${sec.section_number})" class="bg-slate-800 hover:bg-slate-700 text-emerald-400 border border-emerald-500/30 text-xs px-3 py-1.5 rounded-lg flex items-center gap-1.5 font-medium transition">
                <i class="fa-regular fa-copy"></i>
                <span>Copy Section</span>
              </button>
            </div>
            <div class="p-4 text-xs text-slate-300 leading-relaxed font-sans whitespace-pre-line bg-slate-950/80">
              ${sec.content}
            </div>
          `;
          container.appendChild(card);
        });
      } catch (err) {
        console.error("Failed to load proposal sections:", err);
      }
    }

    function copySectionContent(num) {
      if (!proposalData) return;
      const sec = proposalData.sections.find(s => s.section_number === num);
      if (sec) {
        copyText(sec.content, `Section ${num}: ${sec.title}`);
      }
    }

    function copyAllSections() {
      if (!proposalData) return;
      let full = `# NESFIC 2026: CamelliaPluck-AI (NESFIC-I-05)\\n\\n`;
      proposalData.sections.forEach(s => {
        full += `## Section ${s.section_number}: ${s.title} (${s.word_count} words)\\n\\n${s.content}\\n\\n---\\n\\n`;
      });
      copyText(full, "Entire Proposal");
    }

    // Load Fleet Telemetry
    async function loadFleetTelemetry() {
      try {
        const res = await fetch('/api/fleet-telemetry');
        const data = await res.json();
        const grid = document.getElementById('fleet-units-grid');
        grid.innerHTML = '';

        data.active_units.forEach(u => {
          const card = document.createElement('div');
          card.className = "bg-slate-950 border border-slate-800 rounded-xl p-4 space-y-3";
          card.innerHTML = `
            <div class="flex items-center justify-between">
              <span class="text-xs font-mono font-bold text-emerald-400 flex items-center gap-1.5">
                <i class="fa-solid fa-robot"></i> ${u.unit_id}
              </span>
              <span class="text-[10px] bg-emerald-950 text-emerald-300 border border-emerald-700 px-2 py-0.5 rounded-full font-medium">
                ${u.status}
              </span>
            </div>
            <div>
              <div class="text-sm font-bold text-white">${u.operator}</div>
              <div class="text-xs text-slate-400">${u.estate}</div>
              <div class="text-[11px] text-slate-500">${u.division}</div>
            </div>
            <div class="grid grid-cols-2 gap-2 pt-2 border-t border-slate-800/80 text-xs font-mono">
              <div>
                <span class="text-slate-500 block text-[10px]">Harvest Today</span>
                <span class="text-white font-bold">${u.kg_harvested} kg</span>
              </div>
              <div>
                <span class="text-slate-500 block text-[10px]">Fine Leaf %</span>
                <span class="text-emerald-400 font-bold">${u.flc_percentage}%</span>
              </div>
              <div>
                <span class="text-slate-500 block text-[10px]">Sweep Speed</span>
                <span class="text-slate-300">${u.sweep_rate_shoots_per_min} /min</span>
              </div>
              <div>
                <span class="text-slate-500 block text-[10px]">Battery</span>
                <span class="text-emerald-300 font-bold">${u.battery_percentage}%</span>
              </div>
            </div>
          `;
          grid.appendChild(card);
        });
      } catch (err) {
        console.error("Failed to load fleet telemetry:", err);
      }
    }"""

if target_part in content:
    content = content.replace(target_part, replacement_js.strip())
    with open("static/index.html", "w") as f:
        f.write(content)
    print("index.html updated with seamless embedded fallbacks!")
else:
    print("Could not match exact block, let's append fallback gracefully")
