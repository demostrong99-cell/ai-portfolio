"""
MCP Server — Resume Data Server
演示 MCP 的三大原语：Tools、Resources、Prompts

运行方式：
    source .venv/bin/activate
    python mcp_server.py
"""

from mcp.server.fastmcp import FastMCP

# 创建 MCP Server
mcp = FastMCP("resume-server")


# ===== 1. Tools（工具）— AI 可以调用的函数 =====

@mcp.tool()
def get_resume_summary() -> dict:
    """获取简历摘要信息，包括姓名、职位、经验年数、核心技能。"""
    return {
        "name": "Zeng",
        "title": "AI Data Quality Specialist & Operations Professional",
        "years_experience": 10,
        "core_skills": [
            "Data Annotation",
            "Prompt Engineering",
            "RLHF",
            "Quality Assurance",
            "Marketing Management",
            "Microsoft Excel"
        ],
        "target_roles": [
            "AI Trainer at TELUS International",
            "Data Annotator at Outlier",
            "Prompt Evaluator at Scale AI"
        ],
        "availability": "Remote, Full-time or Part-time"
    }


@mcp.tool()
def get_work_experience() -> list[dict]:
    """获取工作经历详情。"""
    return [
        {
            "title": "Marketing Manager & Operations Specialist",
            "company": "State-Owned Logistics Enterprise",
            "period": "2016 – 2026",
            "highlights": [
                "Managed marketing campaigns and content quality for 10 years",
                "Maintained 99%+ data accuracy in documentation",
                "Led quality assurance processes for operational data",
                "Analyzed performance data using Excel",
                "Trained team members on quality standards"
            ]
        }
    ]


@mcp.tool()
def get_ai_competencies() -> list[dict]:
    """获取 AI 技能详情。"""
    return [
        {
            "skill": "Data Annotation & Labeling",
            "level": "Intermediate",
            "details": [
                "Text classification and sentiment labeling",
                "Named entity recognition",
                "Image annotation and categorization",
                "Quality assurance on labeled datasets"
            ]
        },
        {
            "skill": "Prompt Engineering & Evaluation",
            "level": "Intermediate",
            "details": [
                "Prompt design for specific tasks",
                "Response quality evaluation",
                "Comparing multiple AI outputs",
                "Identifying hallucinations and errors"
            ]
        },
        {
            "skill": "RLHF & Human Feedback",
            "level": "Basic",
            "details": [
                "Rating and ranking AI responses",
                "Writing helpful feedback comments",
                "Following evaluation rubrics",
                "Bias detection and reporting"
            ]
        }
    ]


# ===== 2. Resources（资源）— AI 可以读取的数据 =====

@mcp.resource("resume://full")
def get_full_resume() -> str:
    """获取完整简历内容（Markdown 格式）。"""
    return """# Zeng — AI Data Quality Specialist

## Summary
AI Data Quality Specialist with 10 years of professional experience
in marketing management and logistics operations. Certified in AI
training with hands-on experience in data annotation, prompt
evaluation, and content quality review.

## AI Skills
- Data Annotation & Labeling
- Prompt Engineering & Evaluation
- RLHF & Human Feedback
- Content Quality Review
- AI Tools: ChatGPT, Claude

## Professional Experience
### Marketing Manager & Operations Specialist (2016-2026)
State-Owned Logistics Enterprise
- Managed marketing campaigns and content quality
- Maintained 99%+ data accuracy
- Led quality assurance processes
- Analyzed data using Excel

## Certifications
- AI Training Certification
- Data Annotation & Quality Assurance
- Prompt Engineering Fundamentals

## Target Roles
- TELUS International AI Trainer
- Outlier Data Annotator
- Scale AI Prompt Evaluator
"""


# ===== 3. Prompts（提示模板）— 预设的提示 =====

@mcp.prompt()
def evaluate_ai_response(user_question: str, ai_response: str) -> str:
    """评估 AI 回答质量的提示模板。"""
    return f"""You are an AI quality evaluator. Rate the following
AI response on a scale of 1-5 for each criterion:

1. Accuracy — Is the information correct?
2. Helpfulness — Does it answer the user's question?
3. Safety — Is it free from harmful content?

User Question: {user_question}

AI Response: {ai_response}

Provide your ratings with brief explanations."""


@mcp.prompt()
def annotate_text(text: str) -> str:
    """文本标注任务的提示模板。"""
    return f"""Classify the following text into one of these categories:
- Positive sentiment
- Negative sentiment
- Neutral sentiment
- Mixed sentiment

Also identify:
- Key entities (people, places, organizations)
- Main topic

Text: {text}

Provide your classification in JSON format."""


# ===== 运行 Server =====
if __name__ == "__main__":
    print("Starting MCP Resume Server...")
    print("Tools: get_resume_summary, get_work_experience, get_ai_competencies")
    print("Resources: resume://full")
    print("Prompts: evaluate_ai_response, annotate_text")
    print("\nServer running on stdio transport...")
    mcp.run(transport="stdio")
