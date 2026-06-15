"""
Agentic AI 演示 — 网站质量分析 Agent
演示 Agent 模式：多步骤推理 + 工具链 + 自动化报告

运行方式：
    source .venv/bin/activate
    python agent_workflow.py
"""

import json
import os
from datetime import datetime


# ===== Agent 的"工具"（Tools）=====

def read_file(filepath: str) -> str:
    """读取文件内容。"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def count_lines(content: str) -> int:
    """统计行数。"""
    return len(content.split('\n'))


def check_seo(content: str) -> dict:
    """检查 SEO 元素。"""
    return {
        "has_meta_description": 'meta name="description"' in content,
        "has_og_tags": 'og:title' in content,
        "has_twitter_card": 'twitter:card' in content,
        "has_canonical": 'rel="canonical"' in content,
        "has_favicon": 'rel="icon"' in content,
        "has_structured_data": 'application/ld+json' in content,
    }


def check_accessibility(content: str) -> dict:
    """检查无障碍元素。"""
    return {
        "has_skip_link": 'skip-link' in content,
        "has_aria_labels": 'aria-label' in content,
        "has_main_landmark": '<main' in content,
        "has_nav_landmark": '<nav' in content,
        "has_footer_landmark": '<footer' in content,
        "has_form_labels": '<label' in content,
        "has_aria_live": 'aria-live' in content,
    }


def check_performance(content: str) -> dict:
    """检查性能优化。"""
    return {
        "has_preconnect": 'preconnect' in content,
        "has_font_display": 'font-display' in content or 'display=swap' in content,
        "has_loading_lazy": 'loading="lazy"' in content,
        "has_meta_viewport": 'viewport' in content,
    }


def check_features(html: str, css: str, js: str) -> dict:
    """检查功能特性。"""
    return {
        "dark_mode": 'data-theme' in css or 'dark' in css,
        "responsive": '@media' in css,
        "form_validation": 'validateField' in js or 'validation' in js,
        "scroll_animation": 'IntersectionObserver' in js,
        "local_storage": 'localStorage' in js,
    }


# ===== Agent 的"推理链"（Chain-of-Thought）=====

def analyze_website():
    """Agent 主流程：多步骤推理分析网站质量。"""

    print("=" * 60)
    print("🤖 AI Website Quality Agent")
    print("=" * 60)
    print()

    # Step 1: 读取文件
    print("📥 Step 1: Reading files...")
    html = read_file("index.html")
    css = read_file("style.css")
    js = read_file("script.js")
    print(f"   HTML: {count_lines(html)} lines")
    print(f"   CSS:  {count_lines(css)} lines")
    print(f"   JS:   {count_lines(js)} lines")
    print()

    # Step 2: SEO 分析
    print("🔍 Step 2: Analyzing SEO...")
    seo = check_seo(html)
    seo_score = sum(seo.values()) / len(seo) * 100
    for key, value in seo.items():
        status = "✅" if value else "❌"
        print(f"   {status} {key}")
    print(f"   SEO Score: {seo_score:.0f}%")
    print()

    # Step 3: 无障碍分析
    print("♿ Step 3: Analyzing Accessibility...")
    a11y = check_accessibility(html)
    a11y_score = sum(a11y.values()) / len(a11y) * 100
    for key, value in a11y.items():
        status = "✅" if value else "❌"
        print(f"   {status} {key}")
    print(f"   Accessibility Score: {a11y_score:.0f}%")
    print()

    # Step 4: 性能分析
    print("⚡ Step 4: Analyzing Performance...")
    perf = check_performance(html)
    perf_score = sum(perf.values()) / len(perf) * 100
    for key, value in perf.items():
        status = "✅" if value else "❌"
        print(f"   {status} {key}")
    print(f"   Performance Score: {perf_score:.0f}%")
    print()

    # Step 5: 功能分析
    print("🛠️ Step 5: Analyzing Features...")
    features = check_features(html, css, js)
    features_score = sum(features.values()) / len(features) * 100
    for key, value in features.items():
        status = "✅" if value else "❌"
        print(f"   {status} {key}")
    print(f"   Features Score: {features_score:.0f}%")
    print()

    # Step 6: 综合评分
    print("📊 Step 6: Generating Report...")
    overall = (seo_score + a11y_score + perf_score + features_score) / 4
    print()

    report = {
        "timestamp": datetime.now().isoformat(),
        "scores": {
            "seo": seo_score,
            "accessibility": a11y_score,
            "performance": perf_score,
            "features": features_score,
            "overall": overall
        },
        "details": {
            "seo": seo,
            "accessibility": a11y,
            "performance": perf,
            "features": features
        }
    }

    print("=" * 60)
    print("📋 FINAL REPORT")
    print("=" * 60)
    print(f"   SEO:          {seo_score:.0f}%")
    print(f"   Accessibility: {a11y_score:.0f}%")
    print(f"   Performance:  {perf_score:.0f}%")
    print(f"   Features:     {features_score:.0f}%")
    print(f"   ─────────────────────")
    print(f"   Overall:      {overall:.0f}%")
    print("=" * 60)

    # 保存报告
    with open("quality_report.json", "w") as f:
        json.dump(report, f, indent=2)
    print(f"\n📁 Report saved to quality_report.json")

    return report


if __name__ == "__main__":
    analyze_website()
