# Week 3

I have concentrated on two different parts of the proposal this week:

## Developing a toolkit for tracking gradients in a neural network

I started with testing existing tools:
- Weights & Biases: It has very high-level (i.e. less customizable interface). This makes it useless for our project.
- TensorBoard: Gives lower-level access. I succesfully used it to track and visualize the gradients. Visualization part is automatic. I have not tried custom visualization yet.
- MlFlow: I have more experience with this one, but TensorBoard offers better UI, so I will stick with it.

So far, my conclusion is that **we do not need a custom tool to track and visualize gradients.** TensorBoard offers:
- Logging with a few lines of code
- Data persistence
- Out-of-box visualization

Instead of building something from scratch, I suggest developing our skills with PyTorch + TensorBoard stack and maybe develop a guideline for future researchers who are interested in doing similar work.

## Analyzing CNNs

I have begun exploring a potential method that will allow us understand how CNNs make their decisions.
(1) I start by training a simple CNN model, and then
(2) During the inference, remove (make weights zero) a single convolutional filter and calculate the loss.
(3) Pick the filters that affect the loss the most.

These filters give us some idea about which features of the image are more important.

I am thinking about how I can expand this method.
