import os
os.environ['MPLCONFIGDIR'] = '/tmp/mpl_cache'
os.makedirs('/tmp/mpl_cache', exist_ok=True)
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np

os.makedirs("assets", exist_ok=True)

# 1. Budget Allocation Chart (Total ₹40 Lakhs, ₹20 Lakhs for Technical Team)
labels = [
    'Technical Engineering\nTeam (₹20.00 L)',
    'Hardware, Sensors &\nMechatronics (₹8.00 L)',
    'Field Trials & TRA\nGarden Pilots (₹5.00 L)',
    'Dataset Collection &\nAnnotation (₹4.00 L)',
    'Safety, IP, Compliance &\nContingency (₹3.00 L)'
]
sizes = [20.0, 8.0, 5.0, 4.0, 3.0]
colors = ['#1b5e20', '#2e7d32', '#4caf50', '#81c784', '#c8e6c9']
explode = (0.06, 0.02, 0.02, 0.02, 0.02)

fig, ax = plt.subplots(figsize=(8, 5.2), dpi=300)
wedges, texts, autotexts = ax.pie(
    sizes, explode=explode, labels=labels, autopct='%1.1f%%',
    startangle=140, colors=colors, textprops=dict(color="black", fontsize=10)
)
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_weight('bold')
    autotext.set_fontsize(11)
ax.set_title("NESFIC-I-05: Resource & Grant Allocation (Total ₹40.00 Lakhs)", fontsize=13, weight='bold', pad=15)
plt.tight_layout()
plt.savefig("assets/budget_allocation.png")
plt.close()

# 2. AI Model Performance: Confusion Matrix & Metrics
fig, ax = plt.subplots(figsize=(7, 4.5), dpi=300)
categories = ['Two Leaves & Bud', 'Mature Leaf', 'Banjhi (Dormant)', 'Woody Twig']
cm = np.array([
    [92.4, 4.1, 2.5, 1.0],
    [3.2, 94.6, 1.8, 0.4],
    [4.5, 3.0, 91.2, 1.3],
    [0.8, 1.2, 0.5, 97.5]
])
im = ax.imshow(cm, interpolation='nearest', cmap=plt.cm.YlGn)
cbar = ax.figure.colorbar(im, ax=ax)
cbar.ax.set_ylabel('Classification Accuracy (%)', rotation=-90, va="bottom", fontsize=10)

ax.set(xticks=np.arange(cm.shape[1]),
       yticks=np.arange(cm.shape[0]),
       xticklabels=categories, yticklabels=categories,
       title='CamelliaNet-YOLO Confusion Matrix (Evaluation on 1,200 Tea Shoots)',
       ylabel='True Botanical Class',
       xlabel='Predicted Class')

plt.setp(ax.get_xticklabels(), rotation=20, ha="right", rotation_mode="anchor", fontsize=9)
plt.setp(ax.get_yticklabels(), fontsize=9)

for i in range(cm.shape[0]):
    for j in range(cm.shape[1]):
        val = cm[i, j]
        color = "white" if val > 50 else "black"
        ax.text(j, i, f"{val:.1f}%", ha="center", va="center", color=color, weight='bold', fontsize=9)

plt.tight_layout()
plt.savefig("assets/confusion_matrix.png")
plt.close()

# 3. Development Gantt Chart (Months 1-12)
fig, ax = plt.subplots(figsize=(9, 4.5), dpi=300)
tasks = [
    'Phase 1: Field Discovery & Requirements',
    'Phase 2: Dataset Collection & AI Modeling',
    'Phase 3: Mechatronics & End-Effector Prototyping',
    'Phase 4: Full System Integration (MVP)',
    'Phase 5: Field Pilot Trials & TRA Validation'
]
start_months = [1, 2.5, 4.5, 7, 9.5]
durations = [2, 3, 3, 2.5, 2.5]
colors = ['#388e3c', '#43a047', '#4caf50', '#66bb6a', '#81c784']

y_pos = np.arange(len(tasks))
ax.barh(y_pos, durations, left=start_months, align='center', color=colors, edgecolor='#1b5e20', height=0.55)
ax.set_yticks(y_pos)
ax.set_yticklabels(tasks, fontsize=10, weight='bold')
ax.invert_yaxis()
ax.set_xlabel('Project Month (12-Month Schedule)', fontsize=11, weight='bold')
ax.set_xlim(0, 13)
ax.set_xticks(range(1, 13))
ax.grid(axis='x', linestyle='--', alpha=0.6)
ax.set_title('CamelliaPluck-AI: Development Milestones & Timeline (TRL-3 to TRL-7)', fontsize=12, weight='bold')

plt.tight_layout()
plt.savefig("assets/development_timeline.png")
plt.close()

# 4. System Architecture Diagram (Schematic Representation)
fig, ax = plt.subplots(figsize=(9, 4.2), dpi=300)
ax.axis('off')

boxes = [
    (0.05, 0.55, 0.25, 0.35, "SENSING HEAD\n• Dual Stereo RGB-D\n• Polarized Ring LED\n• 45+ FPS Global Shutter", '#c8e6c9'),
    (0.37, 0.55, 0.26, 0.35, "EDGE AI COMPUTE\n• Nvidia Orin / Hailo-8\n• CamelliaNet-YOLO\n• 3D Internode Cut Point", '#a5d6a7'),
    (0.70, 0.55, 0.26, 0.35, "PRECISION END-EFFECTOR\n• Micro-Shear Blades\n• Centrifugal Vacuum\n• <3% Cellular Bruising", '#81c784'),
    (0.20, 0.08, 0.28, 0.32, "POWER & ERGONOMICS\n• 24V LiFePO4 (8h Run)\n• Active BMS Protection\n• Lightweight Backpack (<3.2kg)", '#e8f5e9'),
    (0.55, 0.08, 0.28, 0.32, "TELEMETRY & CLOUD\n• Offline LoRa / BLE 5.2\n• Weighment & Quality Sync\n• Estate ERP Management", '#e8f5e9'),
]

for x, y, w, h, text, color in boxes:
    patch = FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.02', facecolor=color, edgecolor='#1b5e20', linewidth=1.5)
    ax.add_patch(patch)
    ax.text(x + w/2, y + h/2, text, ha='center', va='center', fontsize=9, weight='bold', color='#1b5e20')

# Arrows
ax.annotate('', xy=(0.37, 0.72), xytext=(0.30, 0.72),
            arrowprops=dict(facecolor='#1b5e20', edgecolor='#1b5e20', arrowstyle='->', lw=2))
ax.annotate('', xy=(0.70, 0.72), xytext=(0.63, 0.72),
            arrowprops=dict(facecolor='#1b5e20', edgecolor='#1b5e20', arrowstyle='->', lw=2))
ax.annotate('', xy=(0.48, 0.55), xytext=(0.34, 0.40),
            arrowprops=dict(facecolor='#1b5e20', edgecolor='#1b5e20', arrowstyle='->', lw=1.5))
ax.annotate('', xy=(0.69, 0.40), xytext=(0.83, 0.55),
            arrowprops=dict(facecolor='#1b5e20', edgecolor='#1b5e20', arrowstyle='->', lw=1.5))

ax.set_title("CamelliaPluck-AI: Cyber-Physical Mechatronic & Vision Architecture", fontsize=12, weight='bold', y=0.98)
plt.tight_layout()
plt.savefig("assets/system_architecture.png")
plt.close()

# 5. Two Leaves and a Bud Optical Detection Simulation Visualizer
fig, ax = plt.subplots(figsize=(8, 4.8), dpi=300)
# Dark foliage background
ax.set_facecolor('#1e392a')
# Draw simulated tea canopy stems and leaves
theta = np.linspace(0, 2*np.pi, 100)

# Draw mature background leaves (darker green)
for offset in [-1.5, -0.8, 0.7, 1.4]:
    leaf_x = np.sin(theta) * 0.8 + offset
    leaf_y = np.cos(theta) * 0.4 - 0.5
    ax.fill(leaf_x, leaf_y, color='#2d5a3f', alpha=0.85)

# Draw tender Shoot: Bud (center top)
bud_x = np.sin(theta) * 0.15 + 0.0
bud_y = np.cos(theta) * 0.5 + 0.6
ax.fill(bud_x, bud_y, color='#9be382', alpha=0.95)

# First tender leaf (left)
leaf1_x = np.sin(theta) * 0.45 - 0.35
leaf1_y = np.cos(theta) * 0.3 + 0.3
ax.fill(leaf1_x, leaf1_y, color='#7cd95f', alpha=0.95)

# Second tender leaf (right)
leaf2_x = np.sin(theta) * 0.5 + 0.4
leaf2_y = np.cos(theta) * 0.32 + 0.25
ax.fill(leaf2_x, leaf2_y, color='#6fcb52', alpha=0.95)

# Tender stem connecting them
ax.plot([0.0, 0.0], [0.1, -0.4], color='#86d860', lw=5)

# AI Bounding Box for "Two Leaves and a Bud"
bbox = plt.Rectangle((-0.9, -0.1), 1.8, 1.3, fill=False, edgecolor='#00e676', linewidth=2.5, linestyle='--')
ax.add_patch(bbox)
ax.text(-0.85, 1.25, "TARGET: Two Leaves & Bud [Conf: 96.8%]", color='#00e676', fontsize=10, weight='bold',
        bbox=dict(boxstyle='square,pad=0.2', facecolor='black', alpha=0.7, edgecolor='none'))

# Keypoint marker for Petiole Internode Cut Point
ax.plot(0.0, -0.2, marker='X', markersize=14, color='#ff1744', markeredgecolor='white', markeredgewidth=2)
ax.annotate('Cut Point: (X: 320, Y: 412, Z: 64mm)\nInternode Shear Target', xy=(0.0, -0.2), xytext=(0.25, -0.55),
            color='yellow', fontsize=9, weight='bold',
            arrowprops=dict(facecolor='yellow', edgecolor='yellow', arrowstyle='->', lw=2),
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#212121', alpha=0.85, edgecolor='yellow'))

# Non-target Mature Leaf Detection (Rejected / Bypassed)
bbox_m = plt.Rectangle((0.6, -0.9), 1.0, 0.7, fill=False, edgecolor='#ff5252', linewidth=1.8, linestyle=':')
ax.add_patch(bbox_m)
ax.text(0.65, -0.25, "MATURE LEAF [BYPASS]", color='#ff5252', fontsize=8, weight='bold',
        bbox=dict(boxstyle='square,pad=0.2', facecolor='black', alpha=0.7, edgecolor='none'))

ax.set_xlim(-1.8, 1.8)
ax.set_ylim(-1.0, 1.5)
ax.set_title("CamelliaNet-YOLO Real-Time Edge Vision Inference: Shoot Segmentation & Cut-Point Estimation", fontsize=11, weight='bold', color='white', pad=12)
ax.axis('off')
fig.patch.set_facecolor('#0d1f14')
plt.tight_layout()
plt.savefig("assets/vision_detection_demo.png")
plt.close()

print("All 5 chart and technical visual assets created successfully!")
