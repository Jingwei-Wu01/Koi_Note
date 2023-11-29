## KEMI: Mixed-initiative Dialogue System for Emotional Support Conversations



### ESC问题定义definition

Given the dialogue context $C = {u1, u2, ..., ut}$ and the description of the user’s problematic situation $ s$, the goal is to estimate a function $p(r|C, s)$ that generates the target response r. In the light of the challenges discussed in Section 3.3: 

> 1) When should the system take the initiative during the conversation?
> 2) What kind of information is required for the
>    system to initiate a subdialogue?
> 3) What kind of information is required for the
>    system to initiate a subdialogue?

we further define the **mixed-initiative emotion support conversation problem** with the following three sub-tasks, corresponding to the above three challenges:

1) Strategy Prediction predicts the support strategy
$y$ that can be regarded as the fine-grained initiative.
2) Knowledge Selection selects appropriate knowl-
edge $k$ from the available resources $K$.
3) Response Generation generates the mixed-
initiative response $r$ based on the predicted strategy
and the selected knowledge.



* **FROM CLAUDE2**

这篇论文的主要创新点包括:

1. 提出了一种新的方法来分析情感支持对话系统中的混合主动性交互,包括**EAFR注释模式**和对应的**情感支持指标**。这使得研究人员可以更好地评估和分析系统的主动性。

   > EAFR注释模式是该论文提出的用于分析情感支持对话系统中混合主动性交互的注释方式。它将语句分类为以下四种类型:
   >
   > E (Expression):用户主动描述详情或表达感受的语句。
   >
   > A (Action):系统主动请求信息或提供建议和信息的语句。
   >
   > F (Feedback):用户对系统请求或声明的回复语句。
   >
   > R (Reflection):系统表达对用户情感的同理或分享类似经历的语句。

   > 论文提出了四个情感支持指标来量化混合主动性交互的不同方面:
   >
   > Proactivity:系统在对话中主动提出建议的比例。
   >
   > Information:系统贡献的新信息量。
   >
   > Repetition:系统重复用户提到的信息的比例。
   >
   > Relaxation:系统对减轻用户情感强度的影响。

2. 提出了一个**知识增强**的混合主动性框架KEMI,用于情感支持对话。该方法通过**子图检索**从大规模的心理健康知识图谱中获取外部知识,并通过**多任务学习**来预测策略和生成回复。

   > 在该论文中,知识增强(Knowledge Enhancement)指的是利用外部知识来增强情感支持对话系统的能力。
   >
   > 论文提出了以下知识增强方法:
   >
   > 1. 利用COMET模型进行查询扩展,为用户查询添加共识知识,以提供更多背景信息。（不是创新点）
   > 2. 将扩展后的查询表示为图,进行子图检索,从**心理健康知识图谱HEAL中检索**相关的实际案例知识。
   > 3. 将检索到的知识与对话上下文编码成序列,用于多任务学习,即联合进行策略预测和知识增强的回复生成。
   >
   > 相比仅利用对话上下文,引入外部知识可以提供更多情感推理所需的信息,包括用户的情感状态、问题起因等。实际案例知识比抽象的共识知识更有利于生成有意义和信息性的回复。这种知识增强方法提高了模型理解语义和生成回复的能力。
   >
   > 整体来说,知识增强使得情感支持对话系统可以利用大规模的外部知识图谱,生成更高质量的混合主动性回复,以提供更好的情感支持服务。这是该论文的重要创新之一。

   > 论文中的子图检索主要包含以下步骤:
   >
   > 1. 查询扩展:利用<u>COMET模型</u>为原始用户查询添加共识知识,获取扩展查询。
   > 2. 查询图构建:将扩展查询<u>表示为图形式</u>,包含用户查询、情感状态、问题起因等节点。
   > 3. 实体检索:使用sentence-BERT模型计算扩展查询图中的节点与知识图谱HEAL中的实体之间的相似度,检索每个节点的top-K相似实体。
   > 4. 子图合并:根据知识图谱中的边连接关系,合并不同类型节点的top-K实体,构造候选子图。
   > 5. 子图排序:计算每个候选子图的相似度分数,保留top-N子图作为检索结果。

   > 多任务学习包含联合进行策略预测和知识增强的回复生成:
   >
   > 1. 将对话上下文与检索到的知识子图拼接成输入序列。
   > 2. 预训练语言模型以序列到序列的方式进行fine-tuning,最大化回复的生成概率。
   > 3. 同时预测下一个回复的支持策略。
   > 4. 最终生成同时符合策略预测结果和知识增强的回复。

3. 在两个情感支持对话数据集上进行了广泛的实验比较和分析。结果表明,相比existing方法,KEMI在**保留内容的评估和混合主动性分析**方面都取得了显著提升。

   > 保留内容的评估指的是用来评测文本生成质量的自动评估指标,比如困惑度、BLEU、ROUGE等。这些指标可以评估生成回复在多大程度上保留了原始输入内容的信息。
   >
   > 混合主动性分析指的是论文提出的基于EAFR注释和情感支持指标的分析方法,用来评估系统在多大程度上进行了主动性交互。具体的分析包括:
   >
   > 1. 对话流分析:观察用户和系统之间主动权转换的模式。
   > 2. 会话进度分析:观察不同阶段系统主动性语句以及用户情感强度的变化。
   > 3. 情感支持指标:计算Proactivity、Information、Repetition和Relaxation等指标,量化主动性交互的特征。
   >
   > 论文进行了大量定量实验比较和案例分析。具体来说:
   >
   > - 表2和表3报告了不同方法在保留内容评估指标上的结果。KEMI相比其他baseline取得显著提升。
   > - 表4提供了人工评估结果,说明KEMI生成的回复更有意义和更有帮助。
   > - 表6和图3-4给出了在情感支持指标和会话进度分析上的定量结果,说明了KEMI的主动性交互确实取得了改进。
   > - 案例分析(图4)直观对比了不同方法生成回复的区别以及各情感支持指标的分数。

4. 通过对话流分析、会话进度分析和情感支持指标评估,初步分析了主动性在情感支持对话中的必要性和重要性。识别了建立混合主动性ESC系统的三大挑战。

   > 论文识别的建立混合主动性情感支持对话(ESC)系统的三大挑战是:
   >
   > 1. 系统应该在什么时候主动接管对话?不同阶段的主动性会对用户产生不同影响。
   >
   > 2. 系统需要什么样的信息来启动子对话?需要识别出必要的知识进行适当的主动性交互。 
   >
   > 3. 如何促进系统与用户之间的混合主动性交互?即生成适当的主动性回复。
   >
   > 对应地,论文提出的KEMI框架采取以下技术手段来应对这些挑战:
   >
   > 1. 联合学习策略预测,预测下一轮的支持策略,判断是否需要主动出击。
   >
   > 2. 通过子图检索从知识图谱获取实际案例知识,提供主动性交互所需信息。
   >
   > 3. 序列到序列框架进行多任务学习,生成兼具策略和知识的混合主动性回复。
   >
   > 从实验结果来看,KEMI相比其他baseline在情感支持指标上确实显示出了更好的主动性交互特征。所以可以认为KEMI在一定程度上缓解了这些挑战。当然由于任务的复杂性,仍有很大改进空间。但这个框架为建立混合主动性ESC系统提供了有价值的启发和借鉴。

5. 正式定义了混合主动性情感支持对话的**问题**,包含三个子任务:策略预测、知识选择和回复生成。

   > 给定对话上下文$C$和用户问题描述$s$,目标是预测一个函数$p(r|C, s)$来生成目标回复$r$,其中$r$既遵循预测的策略$y$又包含选择的知识$k$。

   > 策略预测控制主动性类型,知识选择提供信息,回复生成则整合二者形成最终输出。三者互相配合,共同促进系统的混合主动性交互能力。这种多任务学习框架是该论文的核心贡献之一。
   >
   > 1. 策略预测:在输出层,增加预测下一回复策略的分支。
   > 2. 知识选择:通过子图检索获得的知识编码成序列,拼接在输入序列中。
   > 3. 回复生成:Seq2Seq模型的主要任务,输出回复的词序列。
   >
   > 三个子任务共享输入序列的编码层和Seq2Seq模型的decoder解码层。策略预测只有额外的输出分支。知识选择影响输入表示。回复生成作为主任务。

6. 提出了查询扩展和子图检索的方法,利用COMET模型扩展查询,并从知识图谱中检索相关的实际案例知识。

7. 利用序列到序列框架进行多任务学习,实现策略预测和知识增强的回复生成。

###  Method

KEMI是在Seq2Seq框架的基础上,进行了以下几点改进:

1. 输入序列:
   - 将检索获得的**知识子图编码成序列**,拼接在**原输入序列后**。
   - 相比仅使用对话上下文,增加了相关的外部知识。
2. 编码器:
   - 使用预训练语言模型(**BlenderBot**)作为编码器,利用其对对话的先验理解。
   - 相比标准Seq2Seq,增强了编码器对输入语义的建模能力。
3. 解码器:
   - 增加了**预测next utterance策略**的分支,引入策略信息指导解码。
   - 进行多任务学习,相比单一生成任务,增加了对回复主动性的建模。
   - 增强了解码器生成回复的语义适当性。

此外,从训练目标上,KEMI联合最大化生成回复的概率和预测策略的概率,进行多任务学习。

#### 知识获取

##### 查询扩展

##### 图谱构建

论文中,子图检索将扩展查询表示为图的具体过程如下:

1. 对原始查询使用COMET模型进行扩展,得到额外的commonsense知识。
2. 原始查询作为图的一个节点。
3. COMET生成的additional knowledge每个关系作为图的一个节点。
4. 根据<u>semantic相关性</u>,添加原始查询和additional knowledge节点之间的链接。
5. 构成一个包含查询节点和额外知识节点及边的简单图结构。

> 举例如下:
>
> 原始查询:"I lost my job."
>
> COMET扩展知识:
>
> [xReact]: I feel sad
> [xIntent]: I want a new job
> [xWant]: find a new job
>
> 则扩展查询图包含:
>
> 节点:原始查询,xReact, xIntent, xWant
>
> 边:原始查询-xReact,原始查询-xIntent,原始查询-xWant

综上,该方法通过COMET扩展获得查询语句的额外语义信息,以图的方式组织表示,便于后续的子图检索过程获得相关知识。

##### 子图检索

#### 生成回答



* <!--BlenderBot的输入序列是？-->



### BERT

> 该论文中没有直接使用BERT模型,但采用了以下基于BERT预训练的模型:
>
> 1. RoBERTa
>
> 论文使用了RoBERTa大模型来微调获得用户语句的主动性分类模型和情感强度预测模型,以进行自动化分析。
>
> 1. Sentence-BERT
>
> 在子图检索时,采用sentence-BERT模型来计算查询和知识图谱中实体之间的语义相似度,进行近似的语义匹配检索。
>
> 1. BlenderBot
>
> Seq2Seq框架中的对话模型BlenderBot也是在BERT基础上进行预训练获得,inherent了BERT的表示能力。

### 实验部分

#### Experimental Setup

##### Datasets 

ESConv

##### Baselines

non-PLM and PLM-based methods （pre-train language model）blenderbot是pretrain??

Transformer-based methods: 

1. **Transformer**: Seq2Seq response generation
2. **MoEL**: Involves multi-decoders to enhance the empathy for different emotions
3. **MIME**: Mimics the emotion of the speaker for empathetic response generation

BlenderBot-based methods: 

1. **BlenderBot:** Open-domain dialogue model pretrained with multiple skills, including empathetic responding
2. **BlenderBot-Joint**: Jointly predicts strategies and generates responses.
3. **GLHG**: Employs a hierarchical graph network to encode multi-source information.
4. **MISC**: Incorporates commonsense knowledge and mixed support strategy to jointly predicts support strategies and generates responses.

##### Metrics

Perplexity (PPL), BLEU-n (B-n), and ROUGE-L (R-L)

###### 1. Perplexity (PPL)
Perplexity 是一个评估语言模型的指标。对于一个给定的语言模型，它表示在测试集上的平均分支数。数学上，它是根据模型的概率分布计算的。其计算公式是：

$\text{PPL}(W) = P(w_1w_2\ldots w_N)^{-\frac{1}{N}} = \sqrt[N]{\frac{1}{P(w_1w_2\ldots w_N)}}$

或者

$\text{PPL}(W) = \exp\left(-\frac{1}{N} \sum_{i=1}^{N} \log P(w_i|w_1\ldots w_{i-1})\right)$

这里，
- \(W = w_1w_2\ldots w_N\) 是测试集中的一个词序列。
- \(N\) 是序列中的总词数。
- \(P(w_1w_2\ldots w_N)\) 是整个序列的概率，由语言模型给出。

###### 2. BLEU-n (B-n)
BLEU（Bilingual Evaluation Understudy）用于评估机器翻译模型的性能。BLEU-n 是指使用 n-gram 精度的 BLEU。其计算公式为：

$\text{BLEU} = BP \cdot \exp\left(\sum_{n=1}^N w_n \log p_n\right)$

其中，
- \(p_n\) 是 n-gram 精度。

- \(N\) 是 n-gram 的大小。

- \(w_n\) 是权重，通常对所有的 n 设置为相等。

- \(BP\) 是短句惩罚因子，计算公式为：

  $BP =
  \begin{cases} 
  1 & \text{if } c>r \\
  \exp(1-\frac{r}{c}) & \text{if } c\leq r 
  \end{cases}$

这里，\(c\) 是候选翻译的长度，\(r\) 是参考翻译的长度。

###### 3. ROUGE-L (R-L)
ROUGE（Recall-Oriented Understudy for Gisting Evaluation）主要用于评估自动摘要和机器翻译的质量。ROUGE-L 是基于最长公共子序列（LCS）的评估指标。其计算公式为：

$\text{ROUGE-L} = \frac{1+\beta^2}{{\text{precision}}^{-1} + \beta^2 \times {\text{recall}}^{-1}}$

这里，
- $\beta^2$ 是用于调整精度和召回率之间的权重的参数。
- $\text{precision} = \frac{{\text{LCS}}(X, Y)}{X}$
- $\text{recall} = \frac{{\text{LCS}}(X, Y)}{Y}$

这里，$X$是候选文本的长度，$Y$是参考文本的长度，${\text{LCS}}(X, Y)$是最长公共子序列的长度。

这三个指标都有其自己的应用场景和限制，一般需要根据具体的评估任务和目标来选择合适的评估指标。

#### Task

1. ##### Strategy Prediction

   >  Macro-F1

2. ##### Response Generation 

   > Perplexity (PPL), BLEU-n (B-n), and ROUGE-L (R-L)
