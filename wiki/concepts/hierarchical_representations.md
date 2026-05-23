## Definition
Hierarchical Representations refer to the use of multiple levels of abstraction within a model, such as a transformer network, to capture and utilize information at different granularities. This approach is particularly useful in enhancing tasks like dense passage retrieval in question-answering systems, where understanding the nuances of both questions and documents is crucial.

## Context
In the realm of question-answering systems, hierarchical representations have been leveraged to improve the retrieval of relevant documents. The FetcHR method exemplifies this by integrating retrieval processes into each layer of a transformer network. By doing so, it utilizes the diverse levels of abstraction available in these layers to enhance the quality of document retrieval. This method has shown to outperform traditional dense passage retrieval (DPR) techniques, particularly in capturing critical features of questions that are often underrepresented in retrieved documents. FetcHR has demonstrated improved performance on benchmarks like the Natural Question and WebQuestion datasets, achieving state-of-the-art results without altering the underlying language model. The approach involves training only the retrieval networks, which contributes to its efficiency.

## Related Concepts
- [[Dense Passage Retrieval]]
- [[Transformer Networks]]
- [[Question-Answering Systems]]
- [[Contrastive Training]]
- [[Retrieval Score]]