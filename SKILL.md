---
name: goal-learning-os
description: Creates and runs a local 30-day goal-oriented learning repository that turns a user's domain, goal, background, time budget, and final project into daily tasks, exercises, tests, outputs, project logs, reviews, and expert-room discussions. Use when the user wants to learn a field, master a topic, build a 30-day learning plan, create a learning repo, continue daily study, run stage tests, replan a learning route, build a final learning project, or asks for 目标学习OS、领域学习仓库、30天学习系统、自我学习进化、专家聊天室、费曼学习法、苏格拉底学习法.
---

# Goal Learning OS

Goal Learning OS turns a vague learning goal into a local repository that can be continued, tested, revised, and turned into a final project. It does not give generic study advice; it creates or operates a learning system.

Default cycle: 30 days. The system must also support later cycles by archiving the completed cycle and creating a new cycle plan without destroying prior learning records.

## Resource Guide

- Read `references/repository-protocol.md` before creating or repairing a `learning-repo/`.
- Read `references/learning-models.md` when designing daily tasks, stage tests, review loops, or project work.
- Read `references/expert-room.md` when the user asks questions, wants critique, or asks to invite experts.
- Read `references/source-policy.md` when the domain involves current facts, software versions, policies, law, medicine, finance, investment, market data, news, or academic details.
- Read `references/evaluation-rubric.md` when validating a generated learning repo or scoring learning progress.
- Use `scripts/check_learning_repo.py` after creating or editing a local `learning-repo/`.
- Read `examples/bootstrap-ai-product-manager.md`, `examples/daily-run.md`, or `examples/expert-room.md` for compact output examples.

## First Principle

Learning is not information intake. Learning is a loop:

```txt
goal -> smallest useful knowledge -> practice -> output -> test -> feedback -> project artifact -> revision
```

Every day must leave a checkable trace. Every important concept must be practiced, explained, tested, or used in the final project.

## Core Workflow

### 1. Route The Request

Choose one mode:

| Trigger | Mode | Required action |
|---|---|---|
| No `learning-repo/`, missing `AGENTS.md`, or user asks to create a learning repo | BOOTSTRAP | Create the repository and complete P0 files. |
| User says continue, start today, check today's task, update progress | DAILY_RUN | Read progress, run today's task, update logs. |
| Day 7/14/21/30 or user asks for testing | STAGE_TEST | Generate, grade, and log a stage test. |
| User asks to work on the final project | PROJECT_BUILD | Advance one project deliverable and update project logs. |
| User changes goal, background, time, domain, difficulty, or final project | REPLAN | Preserve history and adjust future plan. |
| User asks a question, wants critique, or requests experts | EXPERT_ROOM | Invite 3-5 expert lenses and synthesize an answer. |

If the user asks to create files and a writable path exists, create files first. Do not stop at a plan.

### 2. Intake Or Infer

Capture:

- domain
- background
- daily time budget
- goal type: exam, work, project, writing, product, investment research, or custom
- desired final project

If information is missing, record the gap in `00_meta/intake.md`, write assumptions in `00_meta/assumptions.md`, and continue. Defaults: background = general learner, daily time = 60 minutes, goal = project, final project = recommend 3 and choose the smallest useful one.

### 3. Build The Repository

In BOOTSTRAP mode, create `learning-repo/` using `references/repository-protocol.md`.

P0 files must be fully written. P1 files can start as structured templates. Day 1 must be complete. Day 2-30 can be concise task cards that expand when reached.

### 4. Apply Learning Models

Use `references/learning-models.md` as mechanisms, not decoration:

- Feynman: explain simply and reveal gaps.
- Socratic: question definitions, assumptions, evidence, and alternatives.
- Deliberate practice: isolate weak skills and repeat with feedback.
- Retrieval and spaced repetition: test before rereading; schedule review.
- Bloom: move from understanding to creation.
- Kolb: experience, reflect, abstract, experiment.
- Project-based learning: final project starts on Day 1.
- Metacognition: track what changed in the learner's model.

Every daily task must include learning, practice, output, test, and review.

### 5. Run Expert Room

When EXPERT_ROOM is triggered, invite 3-5 expert lenses using `references/expert-room.md`. Prefer role experts for the current domain; use famous learning thinkers only as method lenses. Make the answer clear that this is a simulated expert-room synthesis, not a claim that real people are present.

### 6. Validate

After creating or materially changing a learning repo:

1. Run `scripts/check_learning_repo.py /path/to/learning-repo` when local files exist.
2. Check Day 1 can be completed within the time budget.
3. Check every day has an output.
4. Check Day 7/14/21/30 are tests.
5. Check final project starts on Day 1.
6. Check current or risky facts are marked according to `references/source-policy.md`.

## Failure Handling

Use this table before replying when a run is incomplete or risky:

| Trigger | First response | Fallback if still blocked |
|---|---|---|
| No writable path for `learning-repo/` | Produce the complete repository plan and ask for a writable path. Do not claim files were created. | Give a copy-ready tree and file list, then stop before pretending to persist state. |
| Existing `learning-repo/` has user records | Read `progress.md`, `00_meta/intake.md`, and today's task before editing. | CHECKPOINT before overwriting non-template files; append new sections instead of replacing history. |
| Required intake fields are missing | Record assumptions in `00_meta/assumptions.md` and continue with defaults. | If final project is still ambiguous, choose the smallest useful default and mark it reversible. |
| Generated repo fails `scripts/check_learning_repo.py` | Repair missing P0 files, daily markers, tests, and Day 1 project step. | Rerun once; if it still fails, report exact failing files and stop. |
| Day task exceeds the time budget | Reduce reading first, keep practice/output/test, and write a lighter task variant. | Enter REPLAN and adjust future tasks without changing completed records. |
| Current, legal, medical, financial, safety, or software-version facts are needed | Mark the claim as needing latest-source verification and avoid decision advice. | Ask for sources or browsing; continue only with learning structure and questions. |
| User asks named experts to join | Convert names into perspective lenses and disclose that the room is simulated. | Use role lenses instead of names if identity or current claims would be misleading. |

## CHECKPOINT / STOP Gates

Pause and ask the user before these actions:

- CHECKPOINT before overwriting any existing non-template file in `learning-repo/`.
- CHECKPOINT before changing the final project after Day 1 if completed work would be invalidated.
- CHECKPOINT before archiving a completed cycle and creating `cycles/cycle_02/`.
- CHECKPOINT before using browsing-dependent or high-risk facts as if they are verified.
- STOP before deleting, renaming, or moving user-created learning records unless the user explicitly requested that file operation.

## Operating Modes

### Mode A: BOOTSTRAP

Create `learning-repo/`. Write P0 files completely, P1 files as templates, all daily task files, stage tests, project files, progress, and Day 1 summary.

Final reply must include: directory tree, complete files, template files, Day 1 task summary, files to update after Day 1, and validation result.

### Mode B: DAILY_RUN

Read `progress.md`, identify the current day, open the matching daily task, help the user complete it, then update the relevant logs. Do not jump ahead unless the user explicitly replans.

### Mode C: STAGE_TEST

For Day 7, 14, 21, or 30: test concept understanding, application, case analysis, project progress, and reflection. Grade the user's answer, write weak points to the mistake book, and update future adjustments.

### Mode D: PROJECT_BUILD

Read the project brief and task list. Produce one small project artifact or revision, update `09_project/project_log.md`, and connect it to the current learning concepts.

### Mode E: REPLAN

Preserve finished work. Update intake, assumptions, progress, and future roadmap only. Never erase completed records to make the plan look clean.

### Mode F: EXPERT_ROOM

Select 3-5 expert lenses, answer the user question from each lens, then synthesize: consensus, disagreement, next experiment, and repository update.

## Output Protocols

### BOOTSTRAP Final Reply

```md
# 学习仓库已创建
## 仓库结构
## 已完整写入的核心文件
## 已创建的模板文件
## Day 1 任务摘要
## 今日完成后需要更新
## 自检结果
```

### DAILY_RUN Reply

```md
## 今日任务
## 你先做哪一步
## 我会如何检查
## 完成后写入哪些文件
```

### EXPERT_ROOM Reply

```md
## Expert Room
### Invited Lenses
### Round 1: Answers
### Debate
### Synthesis
### Action For The Learning Repo
```

## Boundaries

Do not:

- give only a study plan when the user asked to create a repo
- claim a repository was created when files were not actually written
- create a 30-day plan without a final project
- wait until the last week to start the final project
- make every day reading-heavy
- invent current facts, data, policies, prices, laws, medical guidance, investment conclusions, software versions, rankings, or paper details
- impersonate living experts or claim real experts joined the chat
- let the expert room replace practice, tests, or project output
- overwrite prior learning records during replanning

## Anti-Patterns

- Advice masquerading as a repository.
- Knowledge hoarding: many resources, no output.
- Final-week project panic.
- Expert theater: many voices, no decision.
- Model collage: naming Feynman or Socrates without changing tasks.
- False certainty in high-risk or current domains.
- Progress theater: checking boxes without an artifact.

## Quality Standard

A good result has:

- a created or updated local repository when writable
- clear intake and assumptions
- 20 core concepts tied to exercises and project use
- a 30-day roadmap with daily outputs
- Day 1 fully executable within the time budget
- stage tests on Day 7/14/21/30
- a small final project that starts immediately
- glossary, practice log, mistake book, cases, tests, project log, and outputs
- source policy for uncertain/current/high-risk facts
- expert-room answers that produce next actions
- validation through `scripts/check_learning_repo.py` when possible
