# Goal Learning OS

Goal Learning OS is a Codex skill for building and running a local 30-day, goal-oriented learning repository.

It turns a user's learning goal into a concrete repository with daily tasks, exercises, tests, outputs, project logs, reviews, and expert-room discussions. The default cycle is 30 days, with support for follow-up cycles after Day 30.

## What It Does

- Creates a local `learning-repo/` for a specific domain or goal.
- Builds a 30-day roadmap with daily outputs and stage tests.
- Starts a small final project on Day 1.
- Uses learning mechanisms such as Feynman explanation, Socratic questioning, deliberate practice, retrieval practice, Bloom mastery, Kolb reflection, project-based learning, and metacognitive review.
- Runs a simulated expert room with 3-5 expert lenses for questions, critique, and project decisions.
- Validates generated learning repositories with `scripts/check_learning_repo.py`.

## Repository Layout

```txt
.
├── SKILL.md
├── agents/openai.yaml
├── examples/
├── references/
├── scripts/
└── test-prompts.json
```

## Usage

Install the skill by copying this repository folder into your Codex skills directory:

```bash
cp -R goal-learning-os ~/.codex/skills/goal-learning-os
```

Then ask Codex something like:

```txt
我想 30 天学会 AI 产品经理，每天 60 分钟，目标是做一个能放进作品集的 PRD，请帮我创建学习仓库。
```

The skill should create a `learning-repo/` with the required maps, roadmap, daily tasks, tests, logs, and final project files.

## Validation

Validate this skill package:

```bash
python3 scripts/check_skill_package.py
```

Validate a generated learning repository:

```bash
python3 scripts/check_learning_repo.py /path/to/learning-repo
```

## Status

Alpha. The system is ready for real-world trial runs, and future iterations should be based on generated repo quality, daily continuation behavior, and expert-room usefulness.

## License

MIT
