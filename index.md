---
layout: splash
permalink: /
hidden: true
header:
  overlay_color: "#1a1a2e"
  overlay_filter: "0.6"
  actions:
    - label: "<i class='fas fa-file-pdf'></i> View Resume"
      url: "/experience/"
    - label: "<i class='fab fa-linkedin'></i> LinkedIn"
      url: "https://www.linkedin.com/in/dominick-campbell-70b3619b/"
excerpt: >
  **Principal Engineer & AI Architect** · 25+ years shipping systems from Mainframe to modern AI ·
  Inventor on 4 patent-pending AI systems · Production tax systems serving Fortune 500 customers · Led 50+ engineers

feature_row:
  - title: "Twenty-five years, mainframe to AI"
    excerpt: >
      Mainframe → J2EE → microservices → cloud → AI. I've shipped through every era and watched
      each one get oversold. Voice-biometric fraud detection at JPMC (10M accounts in 90 days),
      the Indirect Tax Close platform at Vertex, and the HRCommand decomposition that drove the
      Optum acquisition of Connect Your Care.
    url: "/experience/"
    btn_label: "See Experience"
    btn_class: "btn--primary"
  - title: "Skeptical of trends, not of progress"
    excerpt: >
      A trend is a solution looking for a problem. Before adopting anything, I make it finish the
      sentence: "right now we can't ___." I'd rather build the capability than buy the dependency —
      the **"Raise the Boats"** curriculum taught ~50 people across engineering, product, and data
      science to build production AI agents from scratch.
    url: "/about/"
    btn_label: "About Me"
    btn_class: "btn--primary"
  - title: "Field notes from the build"
    excerpt: >
      I write about the work while it's still warm — weekly notes on agent toolkits,
      cost-aware model routing, and the plumbing that keeps production AI running on
      hardware I own. The posts come from the week's real commits, not a content calendar.
    url: "/blog/"
    btn_label: "Read the Blog"
    btn_class: "btn--primary"

selected_work:
  - image_path: /assets/linkedin/robby.png
    alt: "Robby — multi-agent AI for the SDLC"
    title: "Robby"
    excerpt: "A multi-agent system for SDLC orchestration — built to remove process friction so engineers can spend time on the work they came here for."
    url: "/ai/engineering/leadership/2026/02/19/robby-ai-sdlc-system.html"
    btn_label: "Read"
    btn_class: "btn--primary"
  - image_path: /assets/linkedin/voice-bio.png
    alt: "Voice biometric authentication"
    title: "Voice biometric auth"
    excerpt: "$830B fraud prevented at JPMorgan. 99.87% adoption across 10M+ accounts."
    url: "/engineering/case%20studies/2026/05/30/voice-biometric-fraud.html"
    btn_label: "Read"
    btn_class: "btn--primary"
  - image_path: /assets/linkedin/connect-your-care.png
    alt: "Connect Your Care modernization"
    title: "Strangler-fig modernization"
    excerpt: "Decoupling a J2EE/EJB monolith into Spring Boot microservices. Contributed to the Optum acquisition."
    url: "/engineering/leadership/2026/06/06/strangler-fig-modernization.html"
    btn_label: "Read"
    btn_class: "btn--primary"
---

{% include feature_row %}

<h2 id="selected-work" style="text-align:center; margin-top:2em;">Selected Work</h2>

{% include feature_row id="selected_work" %}
