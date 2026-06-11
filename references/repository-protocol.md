# Repository Protocol

Use this reference when creating or repairing a `learning-repo/`.

## Repository Shape

```txt
learning-repo/
├── AGENTS.md
├── README.md
├── progress.md
├── 00_meta/
│   ├── intake.md
│   ├── assumptions.md
│   ├── learning_contract.md
│   └── sources_policy.md
├── 01_maps/
│   ├── knowledge_map.md
│   ├── core_concepts_20.md
│   └── learning_dependencies.md
├── 02_roadmap/
│   ├── 30_day_plan.md
│   ├── weekly_milestones.md
│   └── final_project_plan.md
├── 03_daily_tasks/
│   ├── template_day.md
│   ├── day_01.md ... day_30_final.md
├── 04_glossary/glossary.md
├── 05_exercises/
│   ├── drills.md
│   ├── practice_log.md
│   └── answer_key.md
├── 06_mistakes/mistake_book.md
├── 07_cases/
│   ├── case_library.md
│   └── case_template.md
├── 08_tests/
│   ├── test_template.md
│   ├── stage_test_01_day_07.md
│   ├── stage_test_02_day_14.md
│   ├── stage_test_03_day_21.md
│   └── final_test_day_30.md
├── 09_project/
│   ├── project_brief.md
│   ├── project_tasks.md
│   ├── project_log.md
│   └── deliverable_checklist.md
└── 10_outputs/
    ├── daily_outputs.md
    ├── weekly_outputs.md
    └── final_showcase.md
```

## File Priority

P0 complete files:

- `AGENTS.md`
- `README.md`
- `progress.md`
- `00_meta/intake.md`
- `00_meta/assumptions.md`
- `00_meta/sources_policy.md`
- `01_maps/knowledge_map.md`
- `01_maps/core_concepts_20.md`
- `02_roadmap/30_day_plan.md`
- `03_daily_tasks/template_day.md`
- `03_daily_tasks/day_01.md`
- `04_glossary/glossary.md`
- `06_mistakes/mistake_book.md`
- `07_cases/case_library.md`
- `09_project/project_brief.md`
- `09_project/project_tasks.md`
- `09_project/deliverable_checklist.md`

P1 templates:

- exercise logs and answer key
- case template
- stage tests
- project log
- daily, weekly, and final outputs

P2 concise task cards:

- Day 2 through Day 30 can start concise.
- Each card must include topic, goal, learning focus, practice, output, test, project step, and completion standard.
- Expand the card when the learner reaches that day.

## Core File Contracts

### AGENTS.md

Must define the local learning coach role, startup sequence, file update rules, teaching rules, daily task format, stage test rules, and final project rules.

### README.md

Must explain repository purpose, domain, background, daily time, goal type, final project, 30-day method, daily usage, stage tests, and final project.

### Intake And Assumptions

`00_meta/intake.md` records user input and missing information. `00_meta/assumptions.md` records default assumptions, their effect, and how to revise them.

### Knowledge Map

Must include one-sentence overview, problem solved by the domain, 5-8 modules, dependency order, beginner traps, and what not to study in the first 30 days.

### Core Concepts

`core_concepts_20.md` must be a table with: concept, explanation, importance, example, practice, misconception, project use.

### 30-Day Plan

Must have four phases:

1. Day 1-7: global understanding and basic concepts.
2. Day 8-14: core skills and case application.
3. Day 15-21: integrated practice and project build.
4. Day 22-30: project polish and showcase.

Every day needs output, test method, and project progress. Day 7/14/21/30 are tests.

### Day 1

Day 1 must be complete and feasible within the daily time budget. It must include 3-5 concepts, a concrete output, 5 self-test questions, answers, scoring, common errors, project step, and progress update instructions.

### Final Project

The project must be small, complete, visible, and built from daily outputs. If the user does not provide a project, recommend three options and choose the smallest useful default.

## Goal-Type Adaptation

| Goal type | Emphasis | Best final project |
|---|---|---|
| Exam | definitions, retrieval, question types, mistake book | knowledge cards, solved question set, mock test report |
| Work | scenarios, decisions, cases, reusable templates | work manual, SOP pack, case report |
| Project | minimum viable ability, practice, iteration | small demo, project document, portfolio page |
| Writing | concept clarity, argument, evidence, cases | long essay, article series, research notes |
| Product | user problem, scenes, requirements, prototype | PRD, prototype brief, scenario report |
| Investment research | industry structure, business model, risks, fact checking | research memo or company framework; no buy/sell advice |

## Time Budget Rules

| Daily time | Learning | Practice | Output | Test | Review |
|---|---:|---:|---:|---:|---:|
| <= 30 min | 10 | 10 | 5 | 3 | 2 |
| 31-60 min | 20 | 20 | 10 | 5 | 5 |
| 61-120 min | 30% | 35% | 20% | 10% | 5% |
| > 120 min | 25% | 35% | 25% | 10% | 5% |

## Long-Term Continuation

After Day 30:

1. Archive the cycle under `cycles/cycle_01/` if the user asks to continue.
2. Preserve final showcase, mistakes, project, and concept mastery.
3. Create Cycle 2 with a higher-level goal.
4. Carry forward weak concepts and project backlog.
5. Do not overwrite the completed cycle.
