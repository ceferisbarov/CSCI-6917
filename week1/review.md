# Explaining NLP Models via Minimal Contrastive Editing (MiCE)

**Alexis Ross, Ana Marasović, Matthew E. Peters**

This paper proposes a new method of generating counterfactual explanations for text-to-text models.

## Motivation
While there are various methods for explaining generative NLP models, none of the major ones utilizes the idea of counterfactuals. Counterfactual explanations have been extensively used for tabular and image data, but less so for textual models. This paper suggests a method that allows us to create counterfactual explanations for generative language models.


<!-- 3. One sentence description of what the paper is about.
4. What is the author’s motivation for this paper (see abstract, introduction) -->
## Problem statement
<!-- 5. What is the research question/problem focus of this paper (1 paragraph) -->

Counterfactuals explanations (CE) in classification and regression models poses a simple problem, since we have a certain output dimension. In generative models, however, the situation is more complicated. Unlike traditionals models, generative models have input and output of varying dimensions. 

The generated counterfactuals should *minimal* and *fluent*. Minimal here refers to minimal change between the original and counterfactual inputs. Fluent refers to within-distribution inputs, which translates to readable text for humans.

## Methodoloy
<!-- 6. What did the author’s do in research/analysis to address the problem (2- paragraphs) -->
The main contribution of the authors is the Minimal Contrastive Editing (MiCE) method that creates CEs for generative LLMs.

MiCE achieves this in two stages:
1. fine-tuning an EDITOR model for generating minimal and fluent counterfactuals
2. Making edits with the EDITOR with a binary search algorithm

The first stage is necessary to make the second stage more efficient (i.e. minimal). The second stage utilizes the binary search algorithm to find the best changes to the input to create a counterfactual output.

## Analysis
Authors discuss two potential use cases for this method.

1. Debugging Incorrect Outputs: When a model does not give us the result we expect, MiCE can be used to identify the changed input that would get the desired output from the model.


2. Uncovering Dataset Artifacts: Training datasets for LLMs usually contains undesired artifacts. For exampl, IMDB dataset contains rating *directly* within the text, which renders classification performance impossible to calculte. MiCE can help us identify such artifacts.


## Conclusion
Paper proposes the MiCE method, develops and evaluates it against IMDB, NEWSGROUPS and RACE datasets. Furthermore, their utility is demonstrated in two use cases.

## Future work

Several lines of work are suggested for the future:

* Investigate and compare the different kinds of insight that can be btained through human and model-driven contrastive edits.
* Develop more efficient methods of finding edits.
* Explore how to derive causal relationships from targeted interventions.
* Focus on creating methods that require less compute.
