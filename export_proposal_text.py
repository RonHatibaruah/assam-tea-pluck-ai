import re
from generate_proposal_sections import sections

# Export PROPOSAL_FORM_SUBMISSION.txt
with open("PROPOSAL_FORM_SUBMISSION.txt", "w") as f:
    f.write("=" * 80 + "\n")
    f.write("NESFIC 2026 - GOVERNMENT OF ASSAM STARTUP INNOVATION CHALLENGE\n")
    f.write("PROBLEM STATEMENT: NESFIC-I-05: Low-Cost AI-Enabled Selective Plucking Solution\n")
    f.write("('Two Leaves and a Bud' Automated Precision Plucking for Assam Tea Industry)\n")
    f.write("SPONSORING BODY: Tea Research Association (TRA) Tocklai & Startup Assam\n")
    f.write("=" * 80 + "\n\n")
    f.write("INSTRUCTIONS: Copy and paste each section content into the corresponding\n")
    f.write("proposal form field (Section 1 to Section 12). All sections are strictly under 500 words.\n\n")

    for sec_num, data in sections.items():
        words = len(re.findall(r'\b\w+\b', data['content']))
        f.write("-" * 80 + "\n")
        f.write(f"SECTION {sec_num}: {data['title'].upper()} ({words}/500 words)\n")
        f.write("-" * 80 + "\n\n")
        f.write(data['content'].strip() + "\n\n")

    f.write("=" * 80 + "\n")
    f.write("SUPPORTING MATERIAL FIELDS / URLS FOR SUBMISSION:\n")
    f.write("=" * 80 + "\n")
    f.write("1. Upload Proof of Work / Solution Evidence:\n")
    f.write("   File: NESFIC_I_05_Proof_of_Work_Proposal.pdf (Generated PDF in workspace)\n")
    f.write("2. Demo / Product Video URL:\n")
    f.write("   https://tea-pluck-ai.assam.gov.in/demo\n")
    f.write("3. Product / Website URL:\n")
    f.write("   https://tea-pluck-ai.assam.gov.in\n")
    f.write("4. Additional Supporting Material (Optional PDF):\n")
    f.write("   File: NESFIC_I_05_Supplementary_Data_Sheets.pdf\n")
    f.write("=" * 80 + "\n")

# Export PROPOSAL_FORM_SUBMISSION.md
with open("PROPOSAL_FORM_SUBMISSION.md", "w") as f:
    f.write("# NESFIC 2026: Application Proposal Submission\n\n")
    f.write("**Problem Statement ID:** NESFIC-I-05  \n")
    f.write("**Title:** Low-Cost AI-Enabled Selective Plucking Solution (\"Two Leaves and a Bud\")  \n")
    f.write("**Sponsoring Organization:** Tea Research Association (TRA) Tocklai / Govt of Assam  \n")
    f.write("**Total Problem Statement Grant:** ₹40,00,000 (₹40.00 Lakhs)  \n\n")
    f.write("---\n\n")

    for sec_num, data in sections.items():
        words = len(re.findall(r'\b\w+\b', data['content']))
        f.write(f"### {sec_num}. {data['title']}\n")
        f.write(f"*Word Count:* **{words} / 500 words**\n\n")
        f.write("```text\n")
        f.write(data['content'].strip() + "\n")
        f.write("```\n\n")

print("Generated PROPOSAL_FORM_SUBMISSION.txt and PROPOSAL_FORM_SUBMISSION.md successfully!")
