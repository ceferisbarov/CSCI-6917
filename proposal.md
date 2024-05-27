<!-- Answer the Heilmeier Questions in Times New Roman, 12-point, Single spacing. -->
# Observing hidden changes in deep neural network during the training process

## 1. What are you going to do?
I am going to develop a tool that will allow us to observe internal state changes of a deep neural network during the training process. This tool is going to log the main parameters of the training loop to a file which can later be used for visualization. It is also going to contain data processing and visualization utilities for the said log files.

Later, I will use this tool to analyze the changes in hidden layers during the training process.
 

## 2. How is it done today? Current Limitations?
No research work that I am aware of concentrates on this problem. PyTorch supports adding hooks to its `nn` modules. It is good starting point for develeping the software.
 

## 3. What is your new idea?
To observe the changes happining in inner layers in relation to the model output. More specifically, trace the following:
- The most influential nodes at each iteration.
- Gradients and changes to weights for each node.
- Inputs, weights, outputs for each layer.

No project so far has attempted to log the processes with so much detail. I belive that this will allow us make important observations regarding the training process.

## 4. Who will benefit from your work? Why?

Researchers who are trying to gain insight into who a deep neural network learns the data distribution.
 

## 5. What risks do you anticipate?

We expect little technical challenge, since we will be building on top of existing frameworks like PyTorch. It is possible that our work will hit a wall in terms of conceptual progress, since it is an unexplored area.
 
## 6. Out of pocket costs? Complete within 11 weeks?

We can have an expense of around 100 USD for GPU usage. The project has parts that can be isolated and finished in 11 weeks. If succesfull, it can be extended as a Master's thesis.

## 7. Midterm Demonstration?

- The logging toolkit will be demonstrated. Some parts may be missing at this time, since I intend to develop it iteratively alongside the analytical part of the project.

- Visualization of internal state changes in a classification model training on tabular data.
 

## 8. Final Demonstration (August)?

- The entire toolkit including the codebase and an open-source development guidelines.
- More advanced visualization and analysis on image and/or text models.
