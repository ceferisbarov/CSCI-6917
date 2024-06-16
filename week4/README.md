# Week 4

Done:
* Had a meeting with Patrick Altmayer about Counterfactual Explanations research topics.

* Stopped working on CNNs. You can find the last code in `cnss` folder.

* Started developing the necessary pipeline and utilities for the explainable LLM project.

This consists of the following options:
* Remove option, where we remove a single token ad observe its effect on the output.
* Replace option, where we replace a token with another. A problem here is deciding which new token to choose.
* Comparing the original and perturbed output is another issue. Right now, I am using entailment models for this.

For next week, I intend to complete the replace option.
