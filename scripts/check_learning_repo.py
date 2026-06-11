#!/usr/bin/env python3
"""Validate a Goal Learning OS learning-repo."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


REQUIRED_FILES = [
    "AGENTS.md",
    "README.md",
    "progress.md",
    "00_meta/intake.md",
    "00_meta/assumptions.md",
    "00_meta/sources_policy.md",
    "01_maps/knowledge_map.md",
    "01_maps/core_concepts_20.md",
    "02_roadmap/30_day_plan.md",
    "03_daily_tasks/template_day.md",
    "03_daily_tasks/day_01.md",
    "04_glossary/glossary.md",
    "06_mistakes/mistake_book.md",
    "07_cases/case_library.md",
    "09_project/project_brief.md",
    "09_project/project_tasks.md",
    "09_project/deliverable_checklist.md",
]

TEMPLATE_FILES = [
    "05_exercises/drills.md",
    "05_exercises/practice_log.md",
    "05_exercises/answer_key.md",
    "07_cases/case_template.md",
    "08_tests/test_template.md",
    "08_tests/stage_test_01_day_07.md",
    "08_tests/stage_test_02_day_14.md",
    "08_tests/stage_test_03_day_21.md",
    "08_tests/final_test_day_30.md",
    "09_project/project_log.md",
    "10_outputs/daily_outputs.md",
    "10_outputs/weekly_outputs.md",
    "10_outputs/final_showcase.md",
]

DAILY_FILES = [
    "day_01.md",
    "day_02.md",
    "day_03.md",
    "day_04.md",
    "day_05.md",
    "day_06.md",
    "day_07_review.md",
    "day_08.md",
    "day_09.md",
    "day_10.md",
    "day_11.md",
    "day_12.md",
    "day_13.md",
    "day_14_review.md",
    "day_15.md",
    "day_16.md",
    "day_17.md",
    "day_18.md",
    "day_19.md",
    "day_20.md",
    "day_21_review.md",
    "day_22.md",
    "day_23.md",
    "day_24.md",
    "day_25.md",
    "day_26.md",
    "day_27.md",
    "day_28.md",
    "day_29.md",
    "day_30_final.md",
]

DAILY_MARKERS = ["目标", "学习", "练习", "输出", "自测", "项目", "完成"]
STAGE_DAILY = {
    "day_07_review.md": "stage_test_01_day_07.md",
    "day_14_review.md": "stage_test_02_day_14.md",
    "day_21_review.md": "stage_test_03_day_21.md",
    "day_30_final.md": "final_test_day_30.md",
}
PROJECT_START_MARKERS = ["Day 1", "day_01", "第1天", "第一天", "今日"]


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text()


def check(root: Path) -> list[str]:
    issues: list[str] = []
    if not root.is_dir():
        return [f"Missing learning repo directory: {root}"]

    for rel in REQUIRED_FILES + TEMPLATE_FILES:
        path = root / rel
        if not path.is_file():
            issues.append(f"Missing file: {rel}")
        elif path.stat().st_size == 0:
            issues.append(f"Empty file: {rel}")

    daily_root = root / "03_daily_tasks"
    for name in DAILY_FILES:
        path = daily_root / name
        if not path.is_file():
            issues.append(f"Missing daily task: 03_daily_tasks/{name}")
            continue
        text = read_text(path)
        missing = [marker for marker in DAILY_MARKERS if marker not in text]
        if missing:
            issues.append(
                f"Daily task 03_daily_tasks/{name} missing markers: {', '.join(missing)}"
            )

    for daily_name, test_name in STAGE_DAILY.items():
        daily_path = daily_root / daily_name
        test_path = root / "08_tests" / test_name
        if daily_path.is_file():
            text = read_text(daily_path)
            if test_name not in text and "阶段测试" not in text and "stage" not in text.lower():
                issues.append(f"Stage day {daily_name} does not point to {test_name}")
        if test_path.is_file():
            text = read_text(test_path)
            for marker in ["概念", "应用", "案例", "项目", "反思"]:
                if marker not in text:
                    issues.append(f"Stage test 08_tests/{test_name} missing marker: {marker}")

    day1 = root / "03_daily_tasks/day_01.md"
    if day1.is_file():
        text = read_text(day1)
        for marker in ["今日目标", "自测", "参考答案", "项目推进", "完成标准"]:
            if marker not in text:
                issues.append(f"Day 1 missing marker: {marker}")

    plan = root / "02_roadmap/30_day_plan.md"
    if plan.is_file():
        text = read_text(plan)
        for marker in ["Day 7", "Day 14", "Day 21", "Day 30"]:
            if marker not in text and marker.replace("Day ", "day_") not in text:
                issues.append(f"30-day plan missing stage marker: {marker}")

    project = root / "09_project/project_brief.md"
    if project.is_file():
        text = read_text(project)
        if "最小可展示版本" not in text and "Minimum" not in text:
            issues.append("Project brief missing minimum showcase version")

    project_tasks = root / "09_project/project_tasks.md"
    if project_tasks.is_file():
        text = read_text(project_tasks)
        if not any(marker in text for marker in PROJECT_START_MARKERS):
            issues.append("Project tasks must include a Day 1 project step")

    daily_outputs = root / "10_outputs/daily_outputs.md"
    if daily_outputs.is_file():
        text = read_text(daily_outputs)
        if "day_01" not in text and "Day 1" not in text and "第1天" not in text:
            issues.append("daily_outputs.md should reserve a Day 1 output slot")

    concepts = root / "01_maps/core_concepts_20.md"
    if concepts.is_file():
        rows = [line for line in read_text(concepts).splitlines() if line.strip().startswith("|")]
        if len(rows) < 22:
            issues.append("core_concepts_20.md should contain a table with 20 concepts")

    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description="Check a Goal Learning OS learning-repo.")
    parser.add_argument("path", nargs="?", default="learning-repo")
    args = parser.parse_args()

    root = Path(args.path).resolve()
    issues = check(root)
    if issues:
        print("Learning repo check failed:")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print("Learning repo check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
