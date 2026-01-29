#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional, Tuple
from urllib.parse import urlparse

import requests


GRAPHQL_URL = "https://leetcode.com/graphql"


@dataclass
class ProblemData:
    title: str
    title_slug: str
    difficulty: str  # Easy / Medium / Hard
    content_html: str
    python3_snippet: str
    link: str


def eprint(*args: object) -> None:
    print(*args, file=sys.stderr)


def parse_title_slug(leetcode_url: str) -> str:
    """
    Extracts the 'titleSlug' from:
    https://leetcode.com/problems/minimum-cost-path-with-teleportations/
    """
    u = urlparse(leetcode_url)
    if not u.netloc.endswith("leetcode.com"):
        raise ValueError("Это не похоже на ссылку leetcode.com")

    m = re.search(r"/problems/([^/]+)/?", u.path)
    if not m:
        raise ValueError("Не удалось извлечь slug из ссылки. Ожидаю /problems/<slug>/")
    return m.group(1).strip().lower()


def difficulty_to_folder(difficulty: str) -> str:
    d = difficulty.strip().lower()
    if d == "easy":
        return "easy"
    if d == "medium":
        return "medium"
    if d == "hard":
        return "hard"
    return d


def ensure_deps_for_markdown():
    try:
        import bs4  # noqa: F401
        import markdownify  # noqa: F401
    except Exception:
        raise RuntimeError(
            "Не найдены зависимости для конвертации HTML -> Markdown.\n"
            "Установи так:\n"
            "  pip install beautifulsoup4 markdownify\n"
        )


def graphql_fetch_problem(session: requests.Session, title_slug: str, link: str) -> ProblemData:
    """
    Uses LeetCode GraphQL endpoint to fetch question details.
    """
    query = """
    query questionData($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        title
        titleSlug
        difficulty
        content
        codeSnippets {
          lang
          langSlug
          code
        }
      }
    }
    """

    payload = {
        "query": query,
        "variables": {"titleSlug": title_slug},
    }

    # Иногда LeetCode любит, когда есть "Referer" и "User-Agent"
    headers = {
        "Content-Type": "application/json",
        "Referer": link,
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36",
    }

    resp = session.post(GRAPHQL_URL, headers=headers, data=json.dumps(payload), timeout=30)
    if resp.status_code != 200:
        raise RuntimeError(f"GraphQL запрос не удался: HTTP {resp.status_code}\n{resp.text[:500]}")

    data = resp.json()
    if "errors" in data and data["errors"]:
        raise RuntimeError(f"GraphQL вернул ошибки: {data['errors']}")

    q = (data.get("data") or {}).get("question")
    if not q:
        raise RuntimeError("Не удалось получить данные задачи. Возможно, slug неверный или доступ ограничен.")

    title = q.get("title") or title_slug
    difficulty = q.get("difficulty") or "Unknown"
    content_html = q.get("content") or ""

    snippet = ""
    for s in q.get("codeSnippets") or []:
        if (s.get("langSlug") or "").lower() == "python3":
            snippet = s.get("code") or ""
            break

    if not snippet:
        for s in q.get("codeSnippets") or []:
            if (s.get("langSlug") or "").lower() in {"python", "py"}:
                snippet = s.get("code") or ""
                break

    if not snippet:
        snippet = (
            "class Solution:\n"
            "    def solve(self, *args, **kwargs):\n"
            "        pass\n"
        )

    return ProblemData(
        title=title.strip(),
        title_slug=(q.get("titleSlug") or title_slug).strip().lower(),
        difficulty=difficulty.strip(),
        content_html=content_html,
        python3_snippet=snippet.rstrip() + "\n",
        link=link,
    )


def normalize_image_src(src: str) -> str:
    src = src.strip()
    if not src:
        return src
    if src.startswith("//"):
        return "https:" + src
    if src.startswith("/"):
        return "https://leetcode.com" + src
    return src


def html_to_markdown_and_examples_and_constraints(content_html: str) -> Tuple[str, List[str], List[str]]:
    """
    Returns:
    - description_md (без examples и constraints секций)
    - examples: list of markdown blocks (each block is example_text)
    - constraints: list of lines (each starts without "- ", we will format later)
    """
    ensure_deps_for_markdown()
    from bs4 import BeautifulSoup
    from markdownify import markdownify as md

    soup = BeautifulSoup(content_html or "", "html.parser")

    for img in soup.find_all("img"):
        src = img.get("src") or ""
        img["src"] = normalize_image_src(src)

    for sup in soup.find_all("sup"):
        exp = sup.get_text(strip=True)
        sup.replace_with(f"^{exp}")

    for sub in soup.find_all("sub"):
        idx = sub.get_text(strip=True)
        sub.replace_with(f"_{idx}")

    full_md = md(str(soup), heading_style="ATX").strip()

    lines = full_md.splitlines()

    constraints: List[str] = []
    md_wo_constraints = full_md
    constraints_start = None

    for i, line in enumerate(lines):
        if re.search(r"\bConstraints\b", line, flags=re.IGNORECASE):
            constraints_start = i
            break

    if constraints_start is not None:
        before = lines[:constraints_start]
        after = lines[constraints_start:]

        li_start = None
        for j, line in enumerate(after):
            if re.match(r"^\s*[-*]\s+", line):
                li_start = j
                break
        if li_start is not None:
            k = li_start
            while k < len(after):
                l = after[k].rstrip()
                if re.match(r"^\s*[-*]\s+", l):
                    constraints.append(re.sub(r"^\s*[-*]\s+", "", l).strip())
                    k += 1
                    continue
                if constraints and l.strip() and not re.match(r"^\s*#{1,6}\s+", l):
                    constraints[-1] = (constraints[-1] + " " + l.strip()).strip()
                    k += 1
                    continue
                if not l.strip():
                    k += 1
                    continue
                break

            md_wo_constraints = "\n".join(before).strip()

    examples: List[str] = []
    desc_md = md_wo_constraints

    pattern = re.compile(r"(^|\n)\s*\**Example\s+(\d+)\s*:\**\s*\n", flags=re.IGNORECASE)
    matches = list(pattern.finditer(desc_md))
    if matches:
        first = matches[0].start()
        description_part = desc_md[:first].strip()

        for idx, m in enumerate(matches):
            start = m.end()
            end = matches[idx + 1].start() if idx + 1 < len(matches) else len(desc_md)
            block = desc_md[start:end].strip()

            block = re.split(r"\n\s*\**Constraints\s*:\**\s*\n", block, flags=re.IGNORECASE)[0].strip()
            if block:
                examples.append(block)

        desc_md = description_part

    desc_md = re.sub(r"\n{3,}", "\n\n", desc_md).strip()
    return desc_md, examples, constraints


def write_readme(problem: ProblemData, out_dir: Path) -> None:
    desc_md, examples, constraints = html_to_markdown_and_examples_and_constraints(problem.content_html)

    if constraints:
        constraints_md = "\n".join([f"- {c}" for c in constraints]).strip()
    else:
        constraints_md = "- (нет данных)"

    examples_md_parts: List[str] = []
    for i, ex in enumerate(examples, start=1):
        examples_md_parts.append(
            f"Example {i}:\n\n{ex.strip()}\n"
        )
    examples_md = "\n".join(examples_md_parts).strip()

    readme = [f"# {problem.title}\n"]
    if desc_md:
        readme.append(desc_md + "\n")
    else:
        readme.append("(описание не найдено)\n")

    if examples_md:
        readme.append(examples_md + "\n")
    else:
        readme.append("")

    readme.append("\n**Constraints:**\n")
    readme.append(constraints_md + "\n\n")
    readme.append(f"[Link]({problem.link})\n")

    (out_dir / "README.md").write_text("".join(readme).strip() + "\n", encoding="utf-8")


def write_solution(problem: ProblemData, out_dir: Path) -> None:
    (out_dir / "solution.py").write_text(problem.python3_snippet, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="leetcode_cli",
        description="Скачивает задачу LeetCode по ссылке и создает структуру папок + solution.py + README.md",
    )
    parser.add_argument("url", help="Ссылка на задачу LeetCode вида https://leetcode.com/problems/<slug>/")
    parser.add_argument(
        "--root",
        default=".",
        help="Корневая директория, где будут созданы easy/medium/hard (по умолчанию текущая)",
    )
    args = parser.parse_args()

    url = args.url.strip()
    slug = parse_title_slug(url)

    normalized_link = f"https://leetcode.com/problems/{slug}/"

    session = requests.Session()

    try:
        session.get("https://leetcode.com/", timeout=30)
    except Exception:
        # не критично
        pass

    problem = graphql_fetch_problem(session, slug, normalized_link)

    folder = difficulty_to_folder(problem.difficulty)
    root = Path(args.root).expanduser().resolve()
    dir_name = problem.title_slug.lower().replace("-", " ")
    out_dir = root / folder / dir_name

    out_dir.mkdir(parents=True, exist_ok=True)

    write_solution(problem, out_dir)
    write_readme(problem, out_dir)

    print(str(out_dir))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
