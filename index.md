---
layout: splash
permalink: /
hidden: true
header:
  overlay_color: "#1a1a2e"
  overlay_filter: "0.6"
  actions:
    - label: "<i class='fas fa-file-pdf'></i> View Resume"
      url: "/resume/"
    - label: "<i class='fab fa-linkedin'></i> LinkedIn"
      url: "https://www.linkedin.com/in/dominick-campbell-70b3619b/"
excerpt: >
  **Principal Engineer & AI Architect** · 25+ years shipping systems from Mainframe to modern AI ·
  Inventor on 4 patent-pending AI systems · Production tax systems serving Fortune 500 customers · Led 50+ engineers

intro:
  - excerpt: >
      I design and build the systems that move money, defend audits, and scale trust — then I teach teams
      how to do the same with AI. Currently open to **Principal / Staff Engineer** and **AI Architect** roles.

feature_row:
  - title: "25+ Years. Zero Shortcuts."
    excerpt: >
      Mainframe → J2EE → Microservices → Cloud → AI. Every era, every stack.
      Built voice-biometric fraud systems at JPMC handling 10M accounts in 90 days, the Indirect Tax Close platform at Vertex,
      and the HRCommand decomposition that drove the United Health acquisition of Connect Your Care.
    url: "/experience/"
    btn_label: "See Experience"
    btn_class: "btn--primary"
  - title: "Builder. Teacher. Leader."
    excerpt: >
      Designed and delivered the **"Raise the Boats"** AI curriculum — personally taught
      ~50 employees across engineering, product, and data science how to build production AI agents.
      I don't just ship products; I raise the bar for the whole team.
    url: "/about/"
    btn_label: "About Me"
    btn_class: "btn--primary"

feature_row2:
  - title: "Tech Stack"
    excerpt: >
      **AI / Agents**: crewAI, AutoGen, LangChain, LangGraph, MCP, RAG, OpenAI, Anthropic, Langfuse  
      **ML**: XGBoost, scikit-learn, PyTorch, NLP, synthetic data generation, SageMaker, Snowflake Cortex  
      **Cloud-native**: AWS (Lambda, ECS, EKS, RDS, S3, DynamoDB, Kinesis), GCP, Azure, Terraform, Kubernetes, Docker  
      **Backend**: Python, Java (15+ yrs), Go, TypeScript, FastAPI, Spring Boot, microservices, REST/GraphQL  
      **Data**: Snowflake, PostgreSQL, Kafka, Spark, dbt, Airflow  
      **Frontend**: React, Next.js, Vue.js, Angular  
      **Earlier career**: C#/.NET, COBOL, J2EE, Assembly

selected_work:
  - image_path: /assets/linkedin/robby.png
    alt: "Robby — multi-agent AI for the SDLC"
    title: "Robby"
    excerpt: "A multi-agent system for SDLC orchestration — built to remove process friction so engineers can spend time on the work they came here for."
    url: "/ai/engineering/leadership/2026/02/19/robby-ai-sdlc-system.html"
    btn_label: "Read"
    btn_class: "btn--primary"
  - image_path: /assets/linkedin/data-cake.png
    alt: "Data Cake — synthetic tax data"
    title: "Data Cake"
    excerpt: "Inventing synthetic tax data from scratch — privacy-preserving training fuel for AI in a regulated industry."
    url: "/engineering/ai/2025/12/11/how-data-cake-got-built.html"
    btn_label: "Read"
    btn_class: "btn--primary"
  - image_path: /assets/linkedin/mort-ai-nexus.png
    alt: "Mort AI Nexus — economic-nexus prediction"
    title: "Mort AI Nexus"
    excerpt: "Predicting economic sales-tax nexus before it bites you. State-by-state thresholds, ML-augmented."
    url: "/engineering/ai/2026/01/14/mort-ai-nexus-patent.html"
    btn_label: "Read"
    btn_class: "btn--primary"

selected_work_b:
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

{% include feature_row id="intro" type="center" %}

{% include feature_row %}

<h2 id="selected-work" style="text-align:center; margin-top:2em;">Selected Work</h2>

{% include feature_row id="selected_work" %}
{% include feature_row id="selected_work_b" %}

{% include feature_row id="feature_row2" type="center" %}
