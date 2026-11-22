import os
import json
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from generate_proposal_sections import sections

app = FastAPI(
    title="CamelliaPluck-AI | NESFIC-I-05",
    description="Low-Cost AI-Enabled Selective Tea Plucker & Estate Telemetry Suite",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

os.makedirs("static", exist_ok=True)
os.makedirs("assets", exist_ok=True)

# Mount static and assets directories
app.mount("/assets", StaticFiles(directory="assets"), name="assets")

@app.get("/api/health")
def health_check():
    return {
        "status": "healthy",
        "system": "CamelliaPluck-AI Edge Server",
        "problem_id": "NESFIC-I-05",
        "sponsoring_body": "Tea Research Association (TRA) Tocklai",
        "grant_amount_inr": 4000000,
        "technical_team_cost_inr": 2000000
    }

@app.get("/api/proposal")
def get_proposal_sections():
    """Returns the 12 Proposal Sections with exact word counts and budget."""
    data = []
    for num, sec in sections.items():
        words = len(sec["content"].split())
        data.append({
            "section_number": num,
            "title": sec["title"],
            "word_count": words,
            "word_limit": 500,
            "content": sec["content"].strip()
        })
    return JSONResponse(content={
        "problem_statement_id": "NESFIC-I-05",
        "title": "Low-Cost AI-Enabled Selective Plucking Solution ('Two Leaves and a Bud')",
        "sponsoring_organization": "Tea Research Association (TRA) Tocklai / Govt of Assam",
        "grant_total_inr": 4000000,
        "grant_total_lakhs": 40.0,
        "budget_breakdown": [
            {
                "head": "Technical Engineering Team Cost",
                "amount_lakhs": 20.0,
                "amount_inr": 2000000,
                "percentage": 50.0,
                "details": "Lead AI/CV Engineer (12M: ₹8L), Robotics/Mechatronics Engineer (12M: ₹6.5L), Embedded Firmware & IoT Specialist (8M: ₹3.5L), Agronomy & Field Operations Coordinator (6M: ₹2L)"
            },
            {
                "head": "Hardware, Sensors & Mechatronics End-Effector Prototyping",
                "amount_lakhs": 8.0,
                "amount_inr": 800000,
                "percentage": 20.0,
                "details": "Stereo RGB-D cameras (3 units), Jetson Orin Nano / Hailo-8 modules, coreless BLDC motors, titanium micro-shear blades, cyclonic vacuum blowers, carbon-fiber wands, 24V LiFePO4 packs, IP67 housings"
            },
            {
                "head": "Field Trials & Pilot Testing in Assam Tea Estates",
                "amount_lakhs": 5.0,
                "amount_inr": 500000,
                "percentage": 12.5,
                "details": "Multi-season field trials at TRA Tocklai (Jorhat) & commercial estates in Golaghat/Dibrugarh. Travel, operator training stipends, field calibration rigs, and estate liaison"
            },
            {
                "head": "Dataset Collection, Annotation & Agro-Agronomy Benchmarking",
                "amount_lakhs": 4.0,
                "amount_inr": 400000,
                "percentage": 10.0,
                "details": "25,000-image multi-clone RGB-D canopy dataset collection, expert TRA botanical polygon annotation, laboratory leaf catechin/polyphenol biochemical assays"
            },
            {
                "head": "Safety, Ergonomics, IP & Contingencies",
                "amount_lakhs": 3.0,
                "amount_inr": 300000,
                "percentage": 7.5,
                "details": "Ergonomic harness load certification (ISO 11228), IP67 weather testing, Indian provisional patent filing & legal fees, emergency spare parts buffer"
            }
        ],
        "sections": data
    })

@app.get("/api/download-pdf")
def download_pdf():
    pdf_path = "NESFIC_I_05_Proof_of_Work_Proposal.pdf"
    if os.path.exists(pdf_path):
        return FileResponse(
            pdf_path,
            media_type="application/pdf",
            filename="NESFIC_I_05_Proof_of_Work_Proposal.pdf"
        )
    raise HTTPException(status_code=404, detail="PDF not found. Please build the PDF first.")

@app.get("/api/fleet-telemetry")
def get_fleet_telemetry():
    return {
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
        ],
        "aggregate_summary": {
            "total_green_leaf_today_kg": 176.7,
            "average_flc_percent": 89.3,
            "target_flc_percent": 85.0,
            "average_productivity_kg_per_operator": 44.2,
            "manual_baseline_kg": 22.0,
            "productivity_gain": "2.0x (Shift in progress)",
            "plucking_round_compliance": "98.4%"
        }
    }

# Serve frontend HTML
@app.get("/")
def serve_index():
    return FileResponse("static/index.html")

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8085))
    print(f"Starting CamelliaPluck-AI Server on http://localhost:{port}...")
    uvicorn.run("server:app", host="0.0.0.0", port=port, reload=False)
