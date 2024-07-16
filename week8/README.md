# Week 8

Done:
- Discovered a new paper: [ReAGent: A Model-agnostic Feature Attribution Method for Generative Language Models](https://arxiv.org/abs/2402.00794#:~:text=ReAGent%3A%20A%20Model%2Dagnostic%20Feature%20Attribution%20Method%20for%20Generative%20Language%20Models,-Zhixue%20Zhao%2C%20Boxuan&text=Feature%20attribution%20methods%20(FAs)%2C,features%20to%20the%20model%20predictions.). This paper solves the same problem that I am working on. Their approach is different in some aspects. I spent a lot of time analyzing these differences and decided that it is worth continuing the project.
- Discussed this matter with prof. Kaiseler from GWU and prof. Zhou from University of Sheffield.
- Finalized the code for the first method: replace-roberta. This method maskes each word and used the RoBERTA model to fill this mask. This perturbed prompt is fed to the model and output is recorded. Rest of the method remains same as others.  
  
Next week:
- Integrate replace-roberta with the existing infrastructure.
- Deploy the first version in Streamlit Cloud.
