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
      url: "https://linkedin.com/in/dominick-campbell"
excerpt: >
  **Principal Engineer & AI Architect** · 25+ years shipping systems from Mainframe to modern AI ·
  4 Patent-Pending AI Inventions · Shipped $500M+ in products · Led 50+ engineers

intro:
  - excerpt: >
      I design and build the systems that move money, defend audits, and scale trust — then I teach teams
      how to do the same with AI. Currently open to **Principal / Staff Engineer** and **AI Architect** roles.

feature_row:
  - title: "4 Patent-Pending AI Inventions"
    excerpt: >
      **Data Cake** · **Audit Management Red Black Tree Timber Model** ·
      **Doc Intel** · **Mort AI Nexus Weather Economic Model** —
      all developed at Vertex Inc., targeting tax, audit, and mortgage nexus domains.
    url: "/patents/"
    btn_label: "View Patents"
    btn_class: "btn--primary"
  - title: "25+ Years. Zero Shortcuts."
    excerpt: >
      Mainframe → J2EE → Microservices → Cloud → AI. Every era, every stack.
      Built voice-biometric fraud systems at JPMC, a $500M tax close platform at Vertex,
      and the platform that drove an acquisition at Connect Your Care.
    url: "/experience/"
    btn_label: "See Experience"
    btn_class: "btn--primary"
  - title: "Builder. Teacher. Leader."
    excerpt: >
      Designed and delivered the **"Raise the Boats"** AI curriculum — personally taught
      200+ employees how to build production AI agents. I don't just ship products; I raise the bar
      for the whole team.
    url: "/about/"
    btn_label: "About Me"
    btn_class: "btn--primary"

feature_row2:
  - title: "Tech Stack"
    excerpt: >
      **AI/ML**: crewAI, AutoGen, LangChain, LangGraph, OpenAI, Anthropic, RAG, XGBoost, scikit-learn  
      **Languages**: Python, Java (15+ yrs), TypeScript, Go, C#/.NET, SQL, COBOL  
      **Cloud**: AWS (Lambda, ECS, RDS, S3, SQS), GCP, Terraform, Kubernetes, Docker  
      **Data**: Spark, dbt, Kafka, Airflow, Snowflake, PostgreSQL, DynamoDB  
      **Frontend**: React, Next.js, Angular
---

{% include feature_row id="intro" type="center" %}

{% include feature_row %}

{% include feature_row id="feature_row2" type="center" %}
