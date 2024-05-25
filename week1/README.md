# Week 1
I spent the first week exploring several potential research topics. These were counterfactual explanations (XAI) and single-cell transcriptomics.

## Counterfactual explanations
This topic had caught my interest several months ago. I skimmed through dozens of papers and read three of them:
* [Explaining Black-Box Models through Counterfactuals](https://arxiv.org/abs/2308.07198)

* [Explaining NLP Models via Minimal Contrastive Editing (MiCE)](https://aclanthology.org/2021.findings-acl.336/)

* [Explaining Machine Learning Classifiers through Diverse Counterfactual Explanations](https://arxiv.org/abs/1905.07697)

I will write a review of the second paper till the next class.

One potential summer project was adding new methods to the `CounterfactualExplanations.jl` package. I decided against it since it was not a research-intensive work.

Another idea is using the [PROPANE](https://arxiv.org/abs/2311.07064) method for generating counterfactuals. I will spend the next week exploring this idea further.

`dice.ipynb` notebook contains my initial attempts to use existing libraries to work with counterfactuals.

## Single-cell transcriptomics

Single-cell transcriptomics provides us with a unique, multidimensional data source (~40,000 dimensions). There are already some foundation models for this dataset, which are used for various tasks that previously required task-specific datasets. My idea was to use these foundation models to generate synthetic data. After playing around with the code base, I realized that these experiments will require substantial hardware resources. I am not planning to pursue this direction further.

* [scGPT: toward building a foundation model for single-cell multi-omics using generative AI](https://www.nature.com/articles/s41592-024-02201-0)
* [Large Scale Foundation Model on Single-cell Transcriptomics](https://www.biorxiv.org/content/10.1101/2023.05.29.542705v3)

`scgpt` folder contains some code samples.
