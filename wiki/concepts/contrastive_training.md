## Definition
Contrastive Training is a machine learning technique designed to enhance model performance by differentiating between similar and dissimilar data points. The method involves training a model to increase the similarity between related data points while reducing the similarity between unrelated ones. This technique is particularly beneficial in tasks such as document retrieval and question-answering, where distinguishing relevant from irrelevant information is essential.

## Context
In question-answering systems, contrastive training significantly improves dense passage retrieval. A prominent application is the FetcHR method, which incorporates retrieval into each layer of a transformer network. By utilizing hierarchical representations, FetcHR addresses the underrepresentation of critical features in questions, thereby enhancing the quality of retrieved documents. This approach surpasses traditional dense passage retrieval methods by employing a retrieval score based on the inner product between encoded question and document vectors at each layer. FetcHR has demonstrated state-of-the-art performance on datasets like Natural Question and WebQuestion, achieving notable improvements in exact match scores.

## Related Concepts
- [[Hierarchical Representations]]
- [[Dense Passage Retrieval]]
- [[Transformer Networks]]
- [[Question-Answering Systems]]
- [[Retrieval Score]]
- [[FetcHR]]