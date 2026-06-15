# Claude AI Fundamentals — Prompt Engineering 速查表

## 1. System Prompt（系统提示）

设置 Claude 的角色和行为规则：

```
You are an AI training quality reviewer. Your job is to:
- Evaluate AI responses for accuracy
- Check for hallucinations
- Rate helpfulness on a 1-5 scale
- Always explain your reasoning
```

**关键点：** System prompt 不会被用户看到，但 Claude 会严格遵守。

---

## 2. Few-Shot Prompting（少样本提示）

给 Claude 几个示例，让它学会模式：

```
Classify the following sentiment:

Text: "This product is amazing!" → Positive
Text: "Terrible experience, never again." → Negative
Text: "It works fine, nothing special." → Neutral

Text: "I love how easy this is to use." →
```

**关键点：** 示例越多，Claude 越能理解你想要的格式和风格。

---

## 3. Chain-of-Thought（思维链）

让 Claude 一步步推理：

```
Think step by step:
1. First, analyze the user's intent
2. Then, evaluate the AI response for accuracy
3. Check if the response contains any hallucinations
4. Finally, rate the overall quality

User asked: "What is the capital of France?"
AI responded: "The capital of France is Paris."

Evaluate this response.
```

**关键点：** 复杂任务一定要让 Claude 先思考再回答。

---

## 4. XML Tags（XML 标签）

Claude 特别擅长理解 XML 标签结构：

```
<article>
  <title>My AI Learning Journey</title>
  <content>After 10 years in logistics...</content>
</article>

<instructions>
Summarize the article in 2 sentences.
Focus on the career transition aspect.
</instructions>
```

**关键点：** 用 XML 标签可以让提示更清晰、更有结构。

---

## 5. Tool Use（工具使用）

Claude 可以调用外部工具：

```json
{
  "tools": [
    {
      "name": "get_weather",
      "description": "Get current weather for a city",
      "input_schema": {
        "type": "object",
        "properties": {
          "city": { "type": "string" }
        }
      }
    }
  ]
}
```

**关键点：** Claude 会根据用户问题自动决定是否调用工具。

---

## 6. Claude 的能力

| 能力 | 说明 |
|------|------|
| **长上下文** | 支持 200K tokens，可以处理很长的文档 |
| **多模态** | 可以理解图片、PDF |
| **代码生成** | 擅长写各种编程语言 |
| **推理** | 复杂逻辑推理能力强 |
| **多语言** | 支持中文、英文、日文等多种语言 |
| **遵循指令** | 对系统提示的遵循度很高 |

## 7. Claude 的限制

| 限制 | 说明 |
|------|------|
| **知识截止** | 训练数据有截止日期 |
| **幻觉** | 可能生成看似正确但实际错误的内容 |
| **无记忆** | 每次对话独立，不记得之前的对话 |
| **不能联网** | 默认不能访问互联网（除非使用工具） |
| **不能执行代码** | 不能直接运行代码（除非在特定环境中） |

---

## 8. 安全与对齐

Claude 使用 **Constitutional RLHF** 训练：
- 不生成有害内容
- 不帮助非法活动
- 诚实承认不确定
- 拒绝不当请求

---

## 9. 实际应用示例

### 数据标注任务提示
```
You are a data annotation specialist. Classify the following
customer review into one of these categories:
- Positive
- Negative
- Neutral
- Mixed

Provide your classification and a brief explanation.

Review: "The product quality is good but shipping was slow."
```

### Prompt Evaluation 任务提示
```
You are an AI response evaluator. Rate the following
AI response on these criteria:
1. Accuracy (1-5)
2. Helpfulness (1-5)
3. Safety (1-5)

User question: "How do I reset my password?"
AI response: "Click on 'Forgot Password' on the login page..."

Provide your ratings with explanations.
```

---

**总结：** Claude AI Fundamentals 的核心是理解如何与 Claude 有效沟通。
好的提示 = 清晰的指令 + 适当的上下文 + 明确的输出格式。
