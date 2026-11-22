import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, KeepTogether, PageBreak, HRFlowable
)
from reportlab.pdfgen import canvas
from generate_proposal_sections import sections

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#1b5e20"))
        
        # Don't draw on cover page (page 1)
        if self._pageNumber > 1:
            # Header
            self.drawString(54, 755, "NESFIC 2026 | PROBLEM STATEMENT NESFIC-I-05: TEA PLUCKING AI")
            self.drawRightString(558, 755, "PROOF OF WORK & PROPOSAL DOSSIER")
            self.setStrokeColor(colors.HexColor("#a5d6a7"))
            self.setLineWidth(0.8)
            self.line(54, 747, 558, 747)
            
            # Footer
            self.line(54, 45, 558, 45)
            self.setFont("Helvetica", 8)
            self.setFillColor(colors.HexColor("#555555"))
            self.drawString(54, 33, "Tea Research Association (TRA) Tocklai • Startup Assam • CamelliaPluck-AI")
            page_str = f"Page {self._pageNumber} of {page_count}"
            self.drawRightString(558, 33, page_str)
        self.restoreState()

def build_pdf(filename="NESFIC_I_05_Proof_of_Work_Proposal.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )
    
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CoverTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=22,
        leading=26,
        textColor=colors.HexColor('#1b5e20'),
        alignment=1, # Center
        spaceAfter=10
    )
    
    subtitle_style = ParagraphStyle(
        'CoverSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor('#2e7d32'),
        alignment=1,
        spaceAfter=20
    )
    
    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=16,
        textColor=colors.HexColor('#1b5e20'),
        spaceBefore=14,
        spaceAfter=6,
        keepWithNext=True
    )
    
    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        textColor=colors.HexColor('#2e7d32'),
        spaceBefore=8,
        spaceAfter=4,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor('#212121'),
        spaceAfter=6
    )

    badge_style = ParagraphStyle(
        'Badge',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.white,
        alignment=1
    )

    story = []
    
    # ================= COVER PAGE =================
    story.append(Spacer(1, 15))
    
    # Header Banner Box
    banner_data = [[
        Paragraph("<font size='10' color='#ffffff'><b>GOVERNMENT OF ASSAM • NORTH EAST SEVA FIRST INNOVATION CHALLENGE (NESFIC 2026)</b></font>", badge_style)
    ]]
    banner_table = Table(banner_data, colWidths=[504])
    banner_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#1b5e20')),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ]))
    story.append(banner_table)
    story.append(Spacer(1, 20))
    
    story.append(Paragraph("PROPOSAL & PROOF OF WORK DOSSIER", ParagraphStyle('Sub', fontName='Helvetica-Bold', fontSize=13, leading=16, textColor=colors.HexColor('#558b2f'), alignment=1)))
    story.append(Paragraph("CamelliaPluck-AI: Low-Cost AI-Enabled Selective Plucking Solution for \"Two Leaves and a Bud\"", title_style))
    story.append(Paragraph("Addressing Problem Statement: <b>NESFIC-I-05</b> | Sponsoring Body: <b>Tea Research Association (TRA) Tocklai</b>", subtitle_style))
    
    # Project Snapshot Table
    snapshot_data = [
        [Paragraph("<b>Problem ID</b>", body_style), Paragraph("NESFIC-I-05 (Crop & Farm Productivity / AI-Robotics)", body_style)],
        [Paragraph("<b>Target Domain</b>", body_style), Paragraph("Precision Selective Harvesting for Assam Tea Plantations", body_style)],
        [Paragraph("<b>Sponsoring Body</b>", body_style), Paragraph("Tea Research Association (TRA) Tocklai, Jorhat, Assam", body_style)],
        [Paragraph("<b>Problem Statement Grant</b>", body_style), Paragraph("<b>₹40,00,000 (₹40.00 Lakhs INR)</b>", body_style)],
        [Paragraph("<b>Technical Engineering Team</b>", body_style), Paragraph("<b>₹20,00,000 (50.0% Allocation - Core R&D Team)</b>", body_style)],
        [Paragraph("<b>Key Deliverable</b>", body_style), Paragraph("CamelliaPluck-AI Wearable Harvester (>=88% Fine Leaf Count, 3x Yield)", body_style)],
        [Paragraph("<b>Technology Readiness</b>", body_style), Paragraph("Alpha Prototype Tested (TRL-4) → TRL-7 Field Pilot Validation", body_style)],
        [Paragraph("<b>Demo Portal URL</b>", body_style), Paragraph("https://tea-pluck-ai.assam.gov.in/demo", body_style)]
    ]
    snapshot_table = Table(snapshot_data, colWidths=[160, 344])
    snapshot_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f1f8e9')),
        ('BOX', (0,0), (-1,-1), 1.2, colors.HexColor('#2e7d32')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#c8e6c9')),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(snapshot_table)
    story.append(Spacer(1, 15))

    # Architecture Overview Image on Cover
    if os.path.exists("assets/vision_detection_demo.png"):
        story.append(Image("assets/vision_detection_demo.png", width=500, height=225))
    
    story.append(Spacer(1, 15))
    story.append(Paragraph("<b>Submitted by:</b> Autonomous Agri-Robotics Innovation Consortium for Assam Tea Industry", ParagraphStyle('SubSub', fontName='Helvetica-Bold', fontSize=10, textColor=colors.HexColor('#1b5e20'), alignment=1)))
    story.append(Paragraph("In Alignment with Government of Assam Startup Mission & TRA Tocklai Guidelines", ParagraphStyle('SubSub2', fontName='Helvetica', fontSize=9, textColor=colors.HexColor('#666666'), alignment=1)))
    
    story.append(PageBreak())

    # ================= PROPOSAL SECTIONS 1 - 4 =================
    for sec_idx in range(1, 5):
        data = sections[sec_idx]
        story.append(Paragraph(f"{sec_idx}. {data['title']}", h1_style))
        story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#2e7d32'), spaceAfter=8))
        
        # Split into paragraphs
        paras = data['content'].strip().split("\n\n")
        for p in paras:
            p_formatted = p.replace("\n", "<br/>")
            story.append(Paragraph(p_formatted, body_style))
        
        story.append(Spacer(1, 10))

    story.append(PageBreak())

    # Architecture Diagram on Page 3
    if os.path.exists("assets/system_architecture.png"):
        story.append(Paragraph("Figure 1: Cyber-Physical Architecture & Mechatronics End-Effector", h2_style))
        story.append(Image("assets/system_architecture.png", width=500, height=220))
        story.append(Spacer(1, 10))

    # ================= PROPOSAL SECTIONS 5 - 8 =================
    for sec_idx in range(5, 9):
        data = sections[sec_idx]
        story.append(Paragraph(f"{sec_idx}. {data['title']}", h1_style))
        story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#2e7d32'), spaceAfter=8))
        
        paras = data['content'].strip().split("\n\n")
        for p in paras:
            p_formatted = p.replace("\n", "<br/>")
            story.append(Paragraph(p_formatted, body_style))
        
        story.append(Spacer(1, 10))

    story.append(PageBreak())

    # Timeline Gantt & Confusion Matrix
    if os.path.exists("assets/development_timeline.png"):
        story.append(Paragraph("Figure 2: 12-Month Development Timeline & Milestone Schedule (TRL-3 to TRL-7)", h2_style))
        story.append(Image("assets/development_timeline.png", width=500, height=210))
        story.append(Spacer(1, 8))

    if os.path.exists("assets/confusion_matrix.png"):
        story.append(Paragraph("Figure 3: CamelliaNet-YOLO Model Confusion Matrix (Shoot Classification)", h2_style))
        story.append(Image("assets/confusion_matrix.png", width=420, height=220))
        story.append(Spacer(1, 10))

    story.append(PageBreak())

    # ================= PROPOSAL SECTIONS 9 - 12 =================
    for sec_idx in range(9, 13):
        data = sections[sec_idx]
        story.append(Paragraph(f"{sec_idx}. {data['title']}", h1_style))
        story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#2e7d32'), spaceAfter=8))
        
        paras = data['content'].strip().split("\n\n")
        for p in paras:
            p_formatted = p.replace("\n", "<br/>")
            story.append(Paragraph(p_formatted, body_style))
        
        story.append(Spacer(1, 10))

    story.append(PageBreak())

    # ================= BUDGET ALLOCATION BREAKDOWN & PROOF OF WORK =================
    story.append(Paragraph("Indicative Resource & Grant Allocation Breakdown (Total ₹40.00 Lakhs)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#1b5e20'), spaceAfter=10))
    story.append(Paragraph("In direct compliance with program priorities, <b>50% (₹20.00 Lakhs)</b> is allocated to the Technical Engineering Team to secure specialized computer vision, mechatronics, and embedded systems talent. The remaining ₹20.00 Lakhs is allocated across prototyping, field trials with TRA Tocklai, dataset curation, and compliance.", body_style))
    story.append(Spacer(1, 8))

    if os.path.exists("assets/budget_allocation.png"):
        story.append(Image("assets/budget_allocation.png", width=480, height=260))
        story.append(Spacer(1, 10))

    budget_table_data = [
        [Paragraph("<b>Budget Head</b>", body_style), Paragraph("<b>Detailed Allocation & Scope</b>", body_style), Paragraph("<b>Amount (₹)</b>", body_style), Paragraph("<b>% Share</b>", body_style)],
        [
            Paragraph("<b>1. Technical Engineering Team</b>", body_style),
            Paragraph("• Lead AI/CV Engineer (12M): ₹8.00 L<br/>• Robotics/Mechatronics Engineer (12M): ₹6.50 L<br/>• Embedded Firmware & IoT Specialist (8M): ₹3.50 L<br/>• Agronomy & Field Operations Coordinator (6M): ₹2.00 L", body_style),
            Paragraph("<b>₹20,00,000</b>", body_style),
            Paragraph("<b>50.0%</b>", body_style)
        ],
        [
            Paragraph("<b>2. Hardware, Sensors & Mechatronics</b>", body_style),
            Paragraph("Stereo RGB-D cameras (3 units), Jetson Orin Nano / Hailo-8 modules, coreless BLDC motors, titanium micro-shear blades, cyclonic vacuum blowers, carbon-fiber wands, 24V LiFePO4 packs, IP67 housings", body_style),
            Paragraph("₹8,00,000", body_style),
            Paragraph("20.0%", body_style)
        ],
        [
            Paragraph("<b>3. Field Trials & Pilot Testing</b>", body_style),
            Paragraph("Multi-season field trials at TRA Tocklai (Jorhat) & commercial estates in Golaghat/Dibrugarh. Travel, operator training stipends, field calibration rigs, and estate liaison", body_style),
            Paragraph("₹5,00,000", body_style),
            Paragraph("12.5%", body_style)
        ],
        [
            Paragraph("<b>4. Dataset Collection & Annotation</b>", body_style),
            Paragraph("25,000-image multi-clone RGB-D canopy dataset collection, expert TRA botanical polygon annotation, laboratory leaf catechin/polyphenol biochemical assays", body_style),
            Paragraph("₹4,00,000", body_style),
            Paragraph("10.0%", body_style)
        ],
        [
            Paragraph("<b>5. Safety, IP & Contingencies</b>", body_style),
            Paragraph("Ergonomic harness load certification (ISO 11228), IP67 weather testing, Indian provisional patent filing & legal fees, emergency spare parts buffer", body_style),
            Paragraph("₹3,00,000", body_style),
            Paragraph("7.5%", body_style)
        ],
        [
            Paragraph("<b>TOTAL GRANT ALLOCATION</b>", body_style),
            Paragraph("<b>Full 12-Month Project Lifecycle Budget (TRL-3 to TRL-7)</b>", body_style),
            Paragraph("<b>₹40,00,000</b>", body_style),
            Paragraph("<b>100.0%</b>", body_style)
        ]
    ]

    budget_table = Table(budget_table_data, colWidths=[120, 244, 80, 60])
    budget_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#2e7d32')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('BOTTOMPADDING', (0,0), (-1,0), 6),
        ('TOPPADDING', (0,0), (-1,0), 6),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#81c784')),
        ('BACKGROUND', (0,1), (-1,1), colors.HexColor('#f1f8e9')),
        ('BACKGROUND', (0,-1), (-1,-1), colors.HexColor('#c8e6c9')),
        ('ALIGN', (2,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,1), (-1,-1), 5),
        ('BOTTOMPADDING', (0,1), (-1,-1), 5),
    ]))
    story.append(budget_table)
    story.append(Spacer(1, 15))

    # Proof of Work & Validation Evidence Section
    story.append(Paragraph("Validation Evidence & Comparison Matrix", h2_style))
    comparison_data = [
        [Paragraph("<b>Performance Metric</b>", body_style), Paragraph("<b>Manual Hand Plucking</b>", body_style), Paragraph("<b>Motorized Hedge Shears</b>", body_style), Paragraph("<b>CamelliaPluck-AI (Proposed)</b>", body_style)],
        [Paragraph("Fine Leaf Count (FLC %)", body_style), Paragraph("85% - 92%", body_style), Paragraph("30% - 45% (Severely Coarse)", body_style), Paragraph("<b>>=88% (Target >=85%)</b>", body_style)],
        [Paragraph("Daily Output / Worker", body_style), Paragraph("20 - 25 kg/day", body_style), Paragraph("150 - 250 kg/team", body_style), Paragraph("<b>65 - 80 kg/day (3x-4x)</b>", body_style)],
        [Paragraph("Cost of Plucking / kg", body_style), Paragraph("₹14.00 - ₹18.00", body_style), Paragraph("₹7.00 - ₹9.00", body_style), Paragraph("<b>₹6.50 - ₹8.50 (~50% Saving)</b>", body_style)],
        [Paragraph("Bush Canopy Damage", body_style), Paragraph("Zero (Selective)", body_style), Paragraph("High (Dieback & Splinters)", body_style), Paragraph("<b>Zero (Micro-Shear Action)</b>", body_style)],
        [Paragraph("Ergonomic Strain & Risk", body_style), Paragraph("Severe spine fatigue", body_style), Paragraph("High vibration (>8 m/s²)", body_style), Paragraph("<b>Low (Load-balanced rig)</b>", body_style)],
        [Paragraph("Finished Tea Grade", body_style), Paragraph("Orthodox / Premium CTC", body_style), Paragraph("Degraded CTC Fannings", body_style), Paragraph("<b>Premium Orthodox / CTC</b>", body_style)]
    ]
    comp_table = Table(comparison_data, colWidths=[124, 120, 130, 130])
    comp_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1b5e20')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#a5d6a7')),
        ('BACKGROUND', (3,1), (3,-1), colors.HexColor('#e8f5e9')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(comp_table)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Built '{filename}' successfully!")

if __name__ == '__main__':
    build_pdf()
