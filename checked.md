# Run log

## 2026-10-20 (initial comprehensive search)
37 openings recorded. Checked with no relevant robotics PhD intern posting open:
- Intrinsic (Greenhouse board: no intern roles)
- Toyota Research Institute (only non-robotics interns: causal reasoning, driving world models)
- Sony AI (only audio ML intern)
- Disney Research (Zurich Studio Intern postings, graphics/motion — not robotics)
- Generalist AI, Skild AI, Figure (engineering only), Boston Dynamics, Samsung AI Center, Nokia Bell Labs
- Amazon Robotics / Lab126 (no 2027 PhD intern yet)
- Microsoft Research (only weak matches)
- NVIDIA "2027 Internships: Ph.D. Research Robotics" seen only on aggregators

## 2026-10-26 (weekly run)
16 new openings recorded (6 Meta, 4 NVIDIA, 1 TRI, 4 FieldAI, 1 Dyna Robotics).
Sources: NVIDIA Workday API, Greenhouse/Lever/Ashby APIs, amazon.jobs search, dion-jy.github.io/phd-intern-board feed, web search.
No new relevant postings: Intrinsic (Greenhouse, no interns), Ai2, Amazon, Physical Intelligence, RAI Institute (only engineering interns), Figure (engineering only), Google/DeepMind (general Student Researcher pipeline unchanged), Microsoft Research, Disney Research, Sony AI.
Not recorded (engineering / China-only, lower fit): NVIDIA Shanghai robotics interns (Applied Research Intern Robotics, Humanoid Loco-Manipulation, Robotics Software), FieldAI Sim-to-Real and Mechanical interns.

## 2026-11-02 (weekly run)
23 new openings recorded: Boston Dynamics (1), Meta (6), TRI (5, incl. one duplicate listing), Amazon (1), NVIDIA (3), FieldAI (1), General Motors (2), Palona AI (1), Applied Intuition (3).
Sources: Meta careers sitemap (+ JSON-LD of all 1,300 job pages), NVIDIA / GM / Boston Dynamics / ABB / Disney Workday APIs, Greenhouse/Lever/Ashby APIs, amazon.jobs search, Google careers search, Microsoft careers API, dion-jy.github.io/phd-intern-board.

Manual note (2026-10-27): "Meta positions 1-5 were not posted anymore". These were the 5 Meta rows added 2026-10-26 that returned 404 during the 2026-10-28 archive run. Rechecked via the Meta sitemap and /profile/job_details/ pages (metacareers.com/jobs/<id> now redirects there):
- Still live (archived now): Policy Learning for Robotics (2554989011673624), Multimodal Learning for Robotics (1656954472496223), Robot Foundation Models (27730225806654441).
- Gone, marked `closed`: Dexterous Manipulation and Contact-Rich Control (2053489871986285), Foundational Models for Robotics Research (1078644001656413). They are not in the sitemap and their pages have no JobPosting data.

Archive notes: FieldAI Humanoid Whole Body Learning posting has an empty description in the Lever API, so only the header text was saved. Palona AI (workable.com) is rate-limited by Cloudflare (HTTP 429 / error 1015); the HTML shell was saved and the .md holds a summary of the API description (verbatim text was not obtainable).
No new relevant postings: Intrinsic (Greenhouse, no interns), Ai2, Physical Intelligence, RAI Institute, Dyna, Figure, Disney Research, Sony AI, Google/DeepMind (only new regional Student Researcher pipelines for China, Canada, Israel), Microsoft Research.
Not recorded (lower fit): Waymo 2027 PhD interns (autonomous driving), GM SEAM / Data Scaling Embodied AI, Qualcomm Embodied AI intern (Markham), ABB AI Robotics Intern (Fall 2026), Amazon Robotics SDE/engineering co-ops, NVIDIA Shanghai robotics interns, Dexmate (2025 listing), Bedrock Robotics engineering interns.

## 2026-11-09 (weekly run)
13 new openings recorded: Meta (5: Interactive Physics Simulation for Robotics, Robotic Control Policy, Humanoid Control & Dexterous Manipulation, Robotics Foundation Models Agentic RL, FAIR World Model Foundations [Montreal, missed earlier, weaker match]), TRI (3: World Action Models for Robot Policy, Human-Robot Interaction, Robotics Research Intern Manipulation), NVIDIA (1: Physics Simulation/Newton SWE intern, Zurich), Amazon (1: Robotics Applied Scientist II Intern/Co-op 2027, Taiwan), Samsung Research America (1: Robotics Lab Intern), Intel (1: Robotics PhD Intern), Cambridge Consultants (1: PhD Robotics Engineering Intern, UK, missed earlier).
Sources: Meta careers sitemap (+ JSON-LD of all 1,333 job pages), NVIDIA / Boston Dynamics / GM / Disney / Intel Workday APIs, Greenhouse/Lever/Ashby APIs, amazon.jobs search JSON, Google careers search, Microsoft careers API, dion-jy.github.io/phd-intern-board, web search (Sony AI, Generalist AI, Disney Research).

Manual notes: no new notes since 2026-10-27 (already handled in the 2026-11-02 run).

Closed: 4 Meta rows are no longer in the Meta sitemap and their pages have no JobPosting data — Robotics Foundation Models Mid-Training (1658187582680157), 3D-grounded Generalist Model for Robotics (2267351860492630), Robotics Foundation Models Zurich (1085375117813817), Computational Imaging And Robotics (2857194467985784). Marked `closed`.

Archive notes: Meta pages were fetched from /profile/job_details/<id>/ (the /jobs/<id>/ URL returns HTTP 400 to plain clients); description from JSON-LD. Cambridge Consultants: EU Greenhouse API host is blocked by the network proxy, so the description was extracted from the JSON embedded in the job page. All other postings via public APIs (Lever, Workday cxs, Greenhouse, amazon.jobs). No 404s.
No new relevant postings: Intrinsic (Greenhouse, no interns), Ai2, Physical Intelligence, Dyna, RAI Institute, Applied Intuition, FieldAI, Figure, Boston Dynamics, GM, Disney Research, Sony AI, Generalist AI, Google/DeepMind (only India-region Student Researcher / Research Scientist PhD Intern pipelines), Microsoft Research.
Not recorded (lower fit): TRI Robotics Intern Mechanical Engineering (Cambridge), TRI Accelerated Science / Human Interactive Driving interns, Waymo world-model/simulation PhD interns (autonomous driving), NVIDIA China RL / Cosmos infra interns, Intuitive Surgical / Trace Labs robotics engineering interns.

## 2026-11-16 (weekly run)
14 new rows recorded: Honda Research Institute USA (8: Scaling Multimodal Robot Policy Learning for Dexterous Manipulation, Intelligent Multimodal Representation for Dexterous Manipulation, Physical HRI, Robust Robotic Manipulation, Online Learning for Dexterous Manipulation, High-Fidelity Robotics Simulation and Learning, Heterogeneous Multi-Robot TAMP using LLMs, Disturbance-Resilient Motion Control for Marine Robotics [weaker match]), MERL (3: OR0354 Humanoid Dexterous Manipulation, OR0334 Physical AI for Contact-Rich Humanoid Manipulation, OR0317 VLA Models for Robotic Manipulation), TRI (2: Continual Adaptation for Robotics, Teleoperation and Spatial Computing), Amazon (1: re-post of 2027 Applied Science Internship - Robotics - US under new ID 10604778).
Sources: NVIDIA / Boston Dynamics / GM / Disney / Intel / ABB Workday APIs (via curl; Python urllib now gets a Cloudflare challenge), Greenhouse/Lever/Ashby APIs, Meta careers sitemap (+ JSON-LD of all 1,343 job pages), amazon.jobs search JSON, Google careers search, Microsoft careers API (heavily rate-limited, partial), dion-jy.github.io/phd-intern-board, merl.com internship openings page, usa.honda-ri.com/intern-positions, web search.

Manual notes: no new notes since 2026-10-27. Re-checked the Meta positions from that note: Policy Learning for Robotics, Multimodal Learning for Robotics, Robot Foundation Models are still live in the sitemap; Dexterous Manipulation and Contact-Rich Control and Foundational Models for Robotics Research are still gone. All other `open` Meta rows are still in the sitemap.

Honda RI and MERL had not been rechecked since 2026-10-20. The new Honda rows are all from the new P26INT job-number series. The MERL OR0334 and OR0317 postings may have been up before this run.
Closed: Amazon 10591833 (404, re-posted as 10604778), MERL OR0313 Foundation Models for Humanoid Robots (no longer on the openings page), Honda Memory Representation for Dexterous Manipulation (page 404, not on the intern list).
Re-posts not recorded: Honda P26INT-05/15/16 are second listings of Learning-Based Motion Planning, Policy Learning and Action Grounding, and Test-Time Adaptation, which are already in the CSV.

Archive notes: the MERL clearcompany pages are JS shells, so each .html also holds the matching merl.com openings-page section, and the .md was built from that section. TRI came from the Lever API, Amazon from search.json, and Honda from the page HTML. No 404s on new postings.
No new relevant postings: Meta, NVIDIA (only China-based engineering interns), Intrinsic, Ai2 (only AI for Science / Neuroscience / Open Ecosystem), Physical Intelligence, Dyna, RAI Institute, Applied Intuition, FieldAI, Figure, Skild AI, Boston Dynamics, GM, Disney Research, Sony AI, Generalist AI, Google/DeepMind (only Israel/India Student Researcher pipelines), Microsoft Research.
Not recorded (lower fit): TRI Prototyping and Research Operations intern (undergrad/MS), MERL OR0351 humanoid teleop data collection, MERL SA0336 HRI via multimodal scene understanding, Honda marine-robotics perception/vehicle-dynamics interns, Waymo 2027 PhD interns (autonomous driving), Meta Neural Network Training & HW-SW Co-Design intern, Persona AI humanoid software intern, Intuitive Surgical robotics engineering interns.
