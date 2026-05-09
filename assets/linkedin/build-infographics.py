#!/usr/bin/env python3
"""Generate 5 LinkedIn infographic HTML+PNG files from a project config.

Outputs: 1080x1080 PNG files ready to upload to LinkedIn.
"""

import os
import subprocess
from pathlib import Path

OUT_DIR = Path(__file__).parent
HTML_DIR = OUT_DIR / "html"
HTML_DIR.mkdir(exist_ok=True)

PROJECTS = [
    {
        "slug": "robby",
        "title": "Robby",
        "subtitle": "Multi-Agent SDLC System",
        "kicker": "AI · Production · 2024–2026",
        "accent": "#e34a33",       # warm red
        "accent2": "#f3a953",      # amber
        "stats": [
            {"value": "70", "label": "Skills"},
            {"value": "15", "label": "Specialized Agent Roles"},
            {"value": "50+", "label": "Engineers Trained"},
            {"value": "MCP", "label": "ArgoCD · Datadog · GitHub Actions"},
        ],
        "stack": ["crewAI", "AutoGen", "LangChain", "MCP", "Vue.js", "ArgoCD"],
        "punchline": "An AI head chef. 15 specialist agents. Code as the source of truth.",
    },
    {
        "slug": "mort-ai-nexus",
        "title": "Mort AI Nexus",
        "subtitle": "Multi-State Economic Nexus Detection",
        "kicker": "Patent Pending · Tax Tech · 2024–2026",
        "accent": "#3a7d99",       # deep teal
        "accent2": "#f3a953",
        "stats": [
            {"value": "50", "label": "US Jurisdictions Monitored"},
            {"value": "$100K – $500K", "label": "Exposure Per Missed State"},
            {"value": "Real-Time", "label": "vs Quarterly Reactive Reviews"},
            {"value": "Wayfair-Aware", "label": "Pattern Analysis Model"},
        ],
        "stack": ["Java", "Spring Boot", "AWS", "ML Pattern Analysis", "Streaming"],
        "punchline": "Customers stopped finding out from state notices. They started finding out from the platform.",
    },
    {
        "slug": "voice-bio",
        "title": "Voice Biometric Fingerprinting",
        "subtitle": "JPMorgan Chase · Call-Center Authentication",
        "kicker": "Production · Fintech · 2018–2019",
        "accent": "#1f6f8b",       # navy-teal
        "accent2": "#e34a33",
        "stats": [
            {"value": "~10M", "label": "JPMC Accounts Onboarded in 90 Days"},
            {"value": "20 sec", "label": "Saved Per Authenticated Call"},
            {"value": "~$830B", "label": "Industry-Wide Fraud Loss Plateau"},
            {"value": "1,300", "label": "Opt-Outs (out of ~10M)"},
        ],
        "stack": ["Python", "ML / Biometrics", "Sapiens", "Angular", "REST"],
        "punchline": "Not a security tool that customers tolerated. A security tool that made their day better.",
    },
    {
        "slug": "data-cake",
        "title": "Data Cake",
        "subtitle": "NLP Synthetic Tax Data Generation",
        "kicker": "Patent Pending · AI Research · 2024–2026",
        "accent": "#5d3a9b",       # deep purple
        "accent2": "#f3a953",
        "stats": [
            {"value": "0", "label": "PII Exposed in Training"},
            {"value": "<2%", "label": "Performance Gap vs Real Data"},
            {"value": "Days", "label": "Not Quarters to Spin Up Data"},
            {"value": "Rules-Validated", "label": "Every Synthetic Tx Is Tax-Law Valid"},
        ],
        "stack": ["Python", "XGBoost", "scikit-learn", "NLP", "Rules Engine"],
        "punchline": "Some bottlenecks aren't technical. They're contractual. The right move is the path through, not around.",
    },
    {
        "slug": "connect-your-care",
        "title": "HRCommand",
        "subtitle": "Strangler-Fig Decomposition · Connect Your Care",
        "kicker": "Architecture · HealthTech · 2019–2021",
        "accent": "#2b8c5d",       # forest green
        "accent2": "#e34a33",
        "stats": [
            {"value": "0", "label": "Production Outages During Migration"},
            {"value": "5", "label": "Engineers on the Decomposition Team"},
            {"value": "Acquired", "label": "By United Health / Optum Financial 2021"},
            {"value": "Strangler-Fig", "label": "Pattern, Not Rip-and-Replace"},
        ],
        "stack": ["Spring Boot", "J2EE", "WebLogic", "React", "Kubernetes", "Figma"],
        "punchline": "Rip-and-replace looks bold and fails quietly. Strangler fig actually ships.",
    },
]

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{title}</title>
<style>
  @page {{ size: 1080px 1080px; margin: 0; }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}

  html, body {{
    font-family: 'Inter', 'Helvetica Neue', Arial, sans-serif;
    width: 1080px;
    height: 1080px;
    background: #0f1419;
    color: #e8e8e8;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
    overflow: hidden;
  }}

  .frame {{
    width: 1080px;
    height: 1080px;
    padding: 70px 75px;
    background:
      radial-gradient(circle at 90% 0%, rgba({accent_rgb}, 0.18) 0%, transparent 40%),
      radial-gradient(circle at 0% 100%, rgba({accent2_rgb}, 0.10) 0%, transparent 50%),
      linear-gradient(180deg, #0f1419 0%, #161b22 100%);
    position: relative;
    display: flex;
    flex-direction: column;
  }}

  .accent-bar {{
    position: absolute;
    top: 0;
    left: 0;
    width: 14px;
    height: 100%;
    background: linear-gradient(180deg, {accent} 0%, {accent2} 100%);
  }}

  .corner-mark {{
    position: absolute;
    top: 50px;
    right: 60px;
    font-size: 14px;
    font-weight: 600;
    color: rgba(255,255,255,0.4);
    letter-spacing: 3px;
    text-transform: uppercase;
  }}

  .kicker {{
    font-size: 16px;
    color: {accent2};
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 3px;
    margin-bottom: 20px;
  }}

  .title {{
    font-size: 72px;
    font-weight: 800;
    color: #ffffff;
    line-height: 1.0;
    letter-spacing: -2px;
    margin-bottom: 16px;
  }}

  .subtitle {{
    font-size: 24px;
    font-weight: 500;
    color: #b0b8bf;
    line-height: 1.3;
    margin-bottom: 50px;
    border-bottom: 2px solid {accent};
    padding-bottom: 24px;
    width: fit-content;
    max-width: 100%;
  }}

  .stats-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 22px;
    margin-bottom: 38px;
  }}

  .stat-card {{
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    border-left: 4px solid {accent};
    border-radius: 8px;
    padding: 28px 30px;
    min-height: 130px;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }}

  .stat-value {{
    font-size: 42px;
    font-weight: 800;
    color: #ffffff;
    line-height: 1.0;
    letter-spacing: -1.2px;
    margin-bottom: 10px;
  }}

  .stat-label {{
    font-size: 16px;
    color: #b0b8bf;
    font-weight: 500;
    line-height: 1.3;
  }}

  .punchline {{
    font-size: 22px;
    font-weight: 500;
    color: #e8e8e8;
    line-height: 1.45;
    font-style: italic;
    padding: 24px 28px;
    border-left: 4px solid {accent2};
    background: rgba(255,255,255,0.03);
    margin-bottom: 32px;
  }}

  .stack-row {{
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-bottom: 30px;
  }}

  .stack-pill {{
    font-size: 13px;
    font-weight: 600;
    color: #ffffff;
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.12);
    padding: 8px 14px;
    border-radius: 100px;
    letter-spacing: 0.3px;
  }}

  .footer {{
    margin-top: auto;
    padding-top: 24px;
    border-top: 1px solid rgba(255,255,255,0.1);
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}

  .footer-left {{
    font-size: 17px;
    font-weight: 700;
    color: #ffffff;
  }}

  .footer-left .small {{
    display: block;
    font-size: 13px;
    font-weight: 500;
    color: #8a9199;
    margin-top: 3px;
    letter-spacing: 0.3px;
  }}

  .footer-right {{
    font-size: 14px;
    color: #b0b8bf;
    text-align: right;
    line-height: 1.4;
  }}

  .footer-right .url {{
    color: {accent2};
    font-weight: 600;
    margin-top: 3px;
    display: block;
  }}
</style>
</head>
<body>
<div class="frame">
  <div class="accent-bar"></div>
  <div class="corner-mark">Case Study {idx} / 5</div>

  <div class="kicker">{kicker}</div>
  <div class="title">{title}</div>
  <div class="subtitle">{subtitle}</div>

  <div class="stats-grid">
    {stat_cards}
  </div>

  <div class="punchline">"{punchline}"</div>

  <div class="stack-row">
    {stack_pills}
  </div>

  <div class="footer">
    <div class="footer-left">
      Dominick A. Campbell
      <span class="small">Principal Engineer · AI Architect · 25+ years</span>
    </div>
    <div class="footer-right">
      Five Systems I Shipped
      <span class="url">ethos71.github.io/blog</span>
    </div>
  </div>
</div>
</body>
</html>"""


def hex_to_rgb(h: str) -> str:
    h = h.lstrip("#")
    return ", ".join(str(int(h[i:i+2], 16)) for i in (0, 2, 4))


def render_project(idx: int, p: dict) -> Path:
    stat_cards = "\n    ".join(
        f'<div class="stat-card"><div class="stat-value">{s["value"]}</div>'
        f'<div class="stat-label">{s["label"]}</div></div>'
        for s in p["stats"]
    )
    stack_pills = "\n    ".join(
        f'<div class="stack-pill">{t}</div>' for t in p["stack"]
    )
    html = HTML_TEMPLATE.format(
        title=p["title"],
        subtitle=p["subtitle"],
        kicker=p["kicker"],
        accent=p["accent"],
        accent2=p["accent2"],
        accent_rgb=hex_to_rgb(p["accent"]),
        accent2_rgb=hex_to_rgb(p["accent2"]),
        stat_cards=stat_cards,
        stack_pills=stack_pills,
        punchline=p["punchline"],
        idx=idx,
    )
    html_path = HTML_DIR / f"{p['slug']}.html"
    html_path.write_text(html)
    return html_path


def render_to_png(html_path: Path) -> Path:
    png_path = OUT_DIR / f"{html_path.stem}.png"
    subprocess.run([
        "google-chrome",
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        "--hide-scrollbars",
        f"--window-size=1080,1080",
        f"--screenshot={png_path}",
        f"file://{html_path.resolve()}",
    ], check=True, capture_output=True)
    return png_path


def main():
    for idx, p in enumerate(PROJECTS, 1):
        html = render_project(idx, p)
        png = render_to_png(html)
        print(f"  {idx}. {p['slug']}: {png.name} ({png.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
