<p align="center">
  <img src="./assets/ascii-core-dense.gif" width="1200" alt="Mohamed Hachicha. Animated ASCII reactor surrounded by retrieval, evidence, agent-policy and recovery project diagnostics. Illustrative animation, not live telemetry." />
</p>

<p align="center">
  <a href="https://hachicha.netlify.app">Portfolio</a> &nbsp; / &nbsp;
  <a href="https://www.linkedin.com/in/hachicham/">LinkedIn</a> &nbsp; / &nbsp;
  <a href="mailto:contact.hachicha@gmail.com">Email</a> &nbsp; / &nbsp;
  <a href="https://cal.com/mohamed-hachicha-yqcufo/30min">Talk shop</a>
</p>

### I build interfaces people can use—and systems I can explain.

My work connects retrieval research, agent infrastructure, platform engineering, and product development. I like the point where an interesting idea has to survive real data, explicit permissions, and a production deployment.

Lately: comparing retrieval optimizers, giving agents durable evidence, and building tools that check whether their actions actually worked.

### `01 / flagship research & systems`

**Hybrid Legal Retrieval · How much does the optimizer actually help?**  
Seven search algorithms, hybrid dense/BM25 retrieval, saved ranking traces, and uncertainty analysis. The work includes reproducible metric audits and manuscript drafts. The question is retrieval performance; generated legal answers are outside the evaluation.

`Python` · `Information retrieval` · `Metaheuristics` · `Experimental design`

**Validator · Give research a memory. Make conclusions earn their place.**  
A private MCP harness for typed evidence graphs, supporting and contradicting observations, and versioned research state. Hypotheses move through deterministic validation gates. A model’s confidence cannot promote them on its own.

`MCP` · `Python` · `SQLite WAL` · `Evidence graphs` — implemented private V1

**SAPER · Let agents execute. Keep policy in charge.**  
An internal control plane connecting durable goals to policy-gated workers, exact-commit CI verification, and draft-PR delivery. The implemented V0 includes restart and idempotency protections; broader security and deployment workflows are still in development.

`Agent orchestration` · `Policy engines` · `GitHub CI` · `Outcome verification`

**Recovery Engineering · The restore is the test.**  
Encrypted snapshots, isolated database restore drills, bounded workloads, and release gates that verify the running application. Operational work where a successful command is only the start of the evidence.

`Linux` · `PostgreSQL` · `Redis` · `restic` · `Docker`

<sub>These projects are private. Descriptions cover the engineering; source, research artifacts, and infrastructure details stay private.</sub>

### `02 / flagship products`

Research and systems work feed back into products people use:

| Product | The work |
| :--- | :--- |
| [**Rovelo ↗**](https://rovelo.fr) | Restaurant routines, schedules, HACCP workflows, and the admin tools behind client access and subscriptions. |
| [**Trena ↗**](https://trena.pro) | Multi-tenant gym operations: memberships, reservations, billing, and access workflows. |

### `03 / platform engineering`

I build the path from a repository to a running service: the checks that decide whether a release can proceed, the deployment boundary, and the evidence that it worked.

**Production Engineering Runbook & Operator Console**  
A workload-aware engineering workflow backed by a machine-readable control catalogue and a Node.js operator console. Read-only discovery comes first; deterministic gates control production writes. The system brings risk assessment, release readiness, immutable references, and rollback planning into the same workflow.

**VPS Recovery & Operations**  
Private infrastructure automation for encrypted backups, isolated PostgreSQL/Redis/SQLite recovery checks, host monitoring, and resource-bounded workloads. Restore drills test the recovery path; post-deployment checks test the running service.

```text
                      THE DELIVERY PATH

  source -> CI gates -> versioned artifact -> deploy -> readiness
                |                               |          |
             evidence                        rollback   live checks

  PLATFORM CONCERNS
  [x] workload discovery         [x] explicit write boundaries
  [x] tenant & access isolation  [x] resource limits
  [x] recovery verification      [x] release evidence
```

`Platform engineering` · `SRE practices` · `CI/CD` · `Linux` · `Containers` · `Recovery`

### `04 / technologies`

**Research & agent infrastructure**

<p>
  <img src="./assets/tech/python.svg" width="36" height="36" alt="Python" title="Python" /> &nbsp;
  <img src="./assets/tech/fastapi.svg" width="36" height="36" alt="FastAPI" title="FastAPI" /> &nbsp;
  <img src="./assets/tech/sqlite.svg" width="36" height="36" alt="SQLite" title="SQLite" />
</p>

Python · FastAPI · MCP · hybrid dense/BM25 retrieval · metaheuristic optimization · evidence graphs · LLM integrations

**Interfaces & mobile**

<p>
  <img src="./assets/tech/typescript.svg" width="36" height="36" alt="TypeScript" title="TypeScript" /> &nbsp;
  <img src="./assets/tech/react.svg" width="36" height="36" alt="React" title="React" /> &nbsp;
  <img src="./assets/tech/nextjs.svg" width="36" height="36" alt="Next.js" title="Next.js" /> &nbsp;
  <img src="./assets/tech/tailwindcss.svg" width="36" height="36" alt="Tailwind CSS" title="Tailwind CSS" /> &nbsp;
  <img src="./assets/tech/flutter.svg" width="36" height="36" alt="Flutter" title="Flutter" /> &nbsp;
  <img src="./assets/tech/figma.svg" width="36" height="36" alt="Figma" title="Figma" />
</p>

TypeScript · React · Next.js · Tailwind CSS · Flutter / Dart · Figma

**Services & state**

<p>
  <img src="./assets/tech/nodejs.svg" width="36" height="36" alt="Node.js" title="Node.js" /> &nbsp;
  <img src="./assets/tech/nestjs.svg" width="36" height="36" alt="NestJS" title="NestJS" /> &nbsp;
  <img src="./assets/tech/postgresql.svg" width="36" height="36" alt="PostgreSQL" title="PostgreSQL" /> &nbsp;
  <img src="./assets/tech/redis.svg" width="36" height="36" alt="Redis" title="Redis" /> &nbsp;
  <img src="./assets/tech/prisma.svg" width="36" height="36" alt="Prisma" title="Prisma" /> &nbsp;
  <img src="./assets/tech/firebase.svg" width="36" height="36" alt="Firebase" title="Firebase" />
</p>

Node.js · NestJS · Express · PostgreSQL · Prisma · Redis · SQLite · Firebase · Spring Boot · ASP.NET

**Platform & delivery**

<p>
  <img src="./assets/tech/linux.svg" width="36" height="36" alt="Linux" title="Linux" /> &nbsp;
  <img src="./assets/tech/docker.svg" width="36" height="36" alt="Docker" title="Docker" /> &nbsp;
  <img src="./assets/tech/githubactions.svg" width="36" height="36" alt="GitHub Actions" title="GitHub Actions" /> &nbsp;
  <img src="./assets/tech/git.svg" width="36" height="36" alt="Git" title="Git" /> &nbsp;
  <img src="./assets/tech/nginx.svg" width="36" height="36" alt="NGINX" title="NGINX" />
</p>

Linux · Docker · Coolify · GitHub Actions · Git · NGINX · restic · automated release verification

<sub>Technology marks from <a href="https://github.com/devicons/devicon">Devicon</a>, stored in this repository with attribution.</sub>

### `05 / how I work`

<p align="center"><img src="./assets/ascii-trace.gif" width="1100" alt="Animated illustrative workflow: signal, retrieve, reason, verify, ship." /></p>

Ask what would prove the idea wrong. Keep the permissions explicit. Make the interface readable. Test the boundary, then check the live result.

That is the thread through the research, the infrastructure, and the product work.

<p align="center"><code>curiosity → experiment → evidence → working software</code></p>
