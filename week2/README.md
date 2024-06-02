# Week 2
I spend this week finalizing the proposal. Most of my time was spent reading and thinking instead of writing code. 

## Papers
In this section, I will give a brief review of each paper that has contributed to my proposal this week.
### TRADI: Tracking deep neural network weight distributions for uncertainty estimation

This paper concentrates on using training *history* for uncertainty estimation. Instead of using deep ensembles for this, they sample from the weight distributions that change during the training process. This allows them to achieve high-level OOD detection without training multiple models.

One of my project ideas was analyzing weights instead of gradients, but I decided against it since I failed to build a bridge between that idea and the existing literature. 

### GAIA: Delving into Gradient-based Attribution Abnormality for Out-of-distribution Detection

This is one of few papers that uses gradients as an uncertainty estimation method.

### Gradients as a Measure of Uncertainty in Neural Networks

The original paper that proposed the idea of uncertainty estimation with weights. They offer an idea that solves the problem of obtaining gradients during inference: confounding labels. Too long to explain here, but it will be a central part of my summer project.

### Probing the Purview of Neural Networks via Gradient Analysis

This paper builds on the ideas proposed by the previous paper. TBH I have not had time to read it completely, but will do so next week.

### Gradient-Based Novelty Detection Boosted by Self-Supervised Binary Classification

This is the third and final paper on uncertainty estimation via weight analysis.

### Explanatory Paradigms in Neural Networks

I decided to read a review paper on explanatory paradigms in neural networks. I am not through with it yet, but it will help me place my project on a more comprehensive framework.

## Proposal
I finalized my proposal this week. I started with the email exchange and the video cal that we had, but tried to make it more specific and more relevant to the existing body of work.

## PyTorch Hooks

I continued working on PyTorch Hooks:

[Documentation](https://pytorch.org/docs/stable/generated/torch.Tensor.register_hook.html)

I created a simple deep learning model and registered backward hooks which allow us observe changes happening during backpropogation.
