# Contributing

Goal Learning OS is optimized through real learning runs.

## Useful Contributions

- Better repository contracts for generated `learning-repo/` folders.
- Stronger daily task patterns that produce visible learning artifacts.
- New examples from real 30-day learning goals.
- Better expert-room lenses that create practice, tests, or project decisions.
- Validation improvements in `scripts/check_learning_repo.py`.

## Local Checks

Run:

```bash
python3 scripts/check_skill_package.py
python3 -m json.tool test-prompts.json
python3 -m py_compile scripts/check_learning_repo.py scripts/check_skill_package.py
```

For generated learning repos, run:

```bash
python3 scripts/check_learning_repo.py /path/to/learning-repo
```

## Pull Request Notes

Keep changes scoped. If a change modifies behavior, add or update one prompt in `test-prompts.json` or one compact example under `examples/`.
