## MISC: A MIxed Strategy-Aware Model Integrating COMET for Emotional Support Conversation

该模型首先利用COMET模型来推断用户的**细粒度情感状态**,然后使用**混合策略识别模块**生成支持性回复。主要创新点是:

1. 使用COMET模型捕捉用户的瞬时心理状态,进行细粒度的情感理解。
2. 将回复策略建模为策略代码簿上的概率分布,引导回复生成使用混合策略。

##### COMET:

> COMET可以自动生成事件的因果关系和个体相关的心理状态,这对MISC中的细粒度情感理解非常有帮助。MISC模型使用COMET生成的知识块来捕捉用户的精细情感,从而产生更有同理心的回复。可以说,COMET为MISC提供了**常识推理能力**,是MISC得以实现细粒度情感识别的关键。

KEMI和MISC使用COMET的主要区别在于:

1) 使用目的不同

- KEMI使用COMET进行查询扩展,从精神健康知识图谱中检索相关的案例知识。

- MISC使用COMET推断用户的精细情感状态,以进行细粒度的情感理解。

2) COMET使用的领域知识不同

- KEMI使用COMET生成的常识知识对原查询进行扩展,然后在精神健康领域的知识图谱中进行子图检索。

- MISC直接使用COMET根据几个预定义的关系(xReact等)生成用户相关的心理状态信息。

3) COMET使用方式不同

- KEMI将COMET生成的查询扩展结果构建成查询图,进行图上的子图检索。

- MISC通过注意力机制选择相关的COMET知识块,直接融合到模型中。

4) 目标任务不同

- KEMI的目标是生成混合主动性的回复。

- MISC的目标是预测支持策略并生成回复。

总而言之,两篇论文都使用了COMET模型,但使用目的、领域知识、使用方式以及最终目标任务都不太相同。KEMI更多关注从外部知识中检索相关案例,而MISC更多利用COMET进行用户情感理解。