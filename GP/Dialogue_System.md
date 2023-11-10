# 对话系统

### 任务型（task-oriented）

有明确任务目标，能够精确地定义用户的意图和动作

智能助手（订票，导航等）

**pipeline式（主流）、端到端式（End-to-End）**

![img](https://pic3.zhimg.com/80/v2-6b33e453da4496a8722cc7fd6db676ae_1440w.jpg)

#### NLU

NLU（Natural Language Understanding）就是对用户输入的自然语言进行理解，通常我们会将其解析为诸如 (domain, intent, slot) 形式的结构化数据，便于下游模块更好地生成action。

#### DM



#### NLG

### 问答型（QA）

需要准确地回答用户的问题，满足用户需求

银行、电信运营商、电商店铺的语音客服系统等

**KBQA**主流的解决方案可分为两种：

- 基于语义解析（Semantic Parsing-based，SP）：对问句进行深度句法解析，并将解析结果组合成可执行的逻辑表达式（SparQL），直接从图数据库中查询答案；这种方案的范式是“解析-执行”
- 基于信息抽取（Information Retrieval-based，IR）：先解析出问句的主实体，再从KG中查询出主实体关联的多个三元组，组成子图路径（也称多跳子图），之后分别对问句和子图路径编码、排序，返回分数最高的路径作为答案；这种方案的范式是“检索-排序”





### 开放域（open-domain）

聊天机器人等

检索式和生成式