# linear-algebra-for-machine-learning

## week 1 Key take aways (dicriminative vs. generative AI)

Dicriminative AI is when the AI has to categorise a certain input and determine which category the input belongs too. Some examples of discriminative AI are:
* Handwriting to text conversion (the AI would need to determine which symbol the handwritten text falls under)
* Speech to text conversion (the AI would need to determine which symbol the phonetics fall under)

Generative AI is when the AI has to produce/generate a output from the input. Generative AI only utlises LLMs Some examples of generative AI are:
* Test to handwriting conversion (the AI would need to produce the handwriting)
* Test to speech conversion (the AI would need to generate phonetics to read the text outloud)

Both, discriminative and generative AI, **_can_** fall under deep learning. Some of the AI models don't use neural networks which does not place them under the category of deep learning

| Examples of discriminative models (not deep learning)  | Examples of discriminative models using deep learning |
| ------------- | ------------- |
| Logistic regression | Convolutional Neural Networks (CNNs) → image classification  |
| Support Vector Machines (SVMs)  | BERT → language classification (e.g., sentiment analysis)  |
| Decision trees  | Whisper → audio-to-text transcription  | 
| Random forests  |   |

| Generative AI Models That Do Not Use Deep Learning  | Generative AI Models That Use Deep Learning |
| ------------- | ------------- |
| Rule-Based Generators: Template-based systems, MadLib-style text generators | Text Generation: GPT (Generative Pretrained Transformer), Claude, PaLM, LLaMA — other LLMs, T5, BART — for summarization, translation  |
| Probabilistic Models (Shallow): Markov chains which generate text by using probabilities of word sequences (e.g., “The cat” → “sat” → “on” → “the” → “mat”), n-gram models, PCFGs (Probabilistic Context-Free Grammars)  | Image Generation: DALL·E (text-to-image), Stable Diffusion (image generation with diffusion models), StyleGAN (faces and art), BigGAN (high-quality image generation)  |
| Genetic Algorithms / Evolutionary Art which generate images or music by evolving patterns over time.  | Audio & Speech Generation: WaveNet (text-to-speech waveform generation), Tacotron 2 (text-to-speech spectrogram synthesis), VALL-E (voice cloning), Jukebox (music generation from text)  | 
| Expert Systems with Random Variation: Some creative expert systems used rules plus randomness to generate poetry, names, or trivia — but without learning from data  | Video / Multimodal Generation: Sora (OpenAI's text-to-video), Make-A-Video (Meta), Runway Gen-2  |
|  | Code Generation: Codex (used in GitHub Copilot), AlphaCode (from DeepMind)  |

## week 1 Key take aways (separation line, regression line, line of best fit, and perceptron)

separation line
* A boundary (line, curve, or plane) that divides data into categories
* Used in classification problems (i.e., discriminative AI)
* Can be used in perceptrons (for simple cases)

Regression line (aka line of best fit)
* A line that predicts a continuous value based on input data
* Used in regression problems (not classification)
* Used in any model where the output is numeric

Perceptron line
* The perceptron is a model that finds a separation line (or hyperplane) between classes
* A simple binary classifier in neural networks
* It uses a linear decision boundary (aka separation line) to decide which class a data point belongs to
* The "perceptron line" = separation line in the context of a single-layer perceptron. If it is multi-layered then it becomes a complex, nonlinear decision surface that’s harder to interpret geometrically.
* A perceptron can still be considered linearly separable in 3D or higher dimensions — as long as a linear decision boundary (called a hyperplane) can divide the classes without error. It is just that in a 3D space the perceptron will be referred to as a plane. If it is a 4D space or higher it becomes a hyperplane.

## week 1 discussion post

<ins> How would you describe relation between the 2 classes  of data which can be separated by single perceptron?  </ins>

After listening to the lectures and demos I would say that there is no relationship between 2 classes of data which can be separated by a single perceptron. The only relationship that I can think about is that the two classes/groups of data have certain features/characteristics that make the groups of data unique. 

I say this because in a linear relationship the x variable is the independent variable and the y variable is the dependent variable. Based on how the points are scattered you can identify if the variables have a linear or non-linear positive/negative correlation. This relationship is illustrated through the line of best fit or regression line which is the line that illustrates how far apart the data points are from the actual and predicted y-values. 

The line of separation or single perceptron line does not represent the predicted y-value points and it only acts as a line which makes a distinction of the different types of groups that exist in a dataset.

To conclude, I believe regression line illustrates the relationship between two variables while the single perceptron line acts as a boundary which only indicates two separate groups of data within the dataset. 

 <ins> do you have any idea for application of GPT4 "omni" neural network announced last month by OpenAI?  </ins>

To me, it seems like the GPT4-o (GPT4-omni) can perform a variety of tasks related to discriminative and generative AI since it is a multimodal model which can perform a variety of tasks such as image to text conversion (discriminative AI task), text/response generation using LLMs (generative AI task), audio to text conversion (discriminative AI task), etc

<ins> Response to comments </ins>

> As others have mentioned, per the lecture, classes of data that can be separated by a single perceptron means they must be **_linearly separable_**, such that the features in the dataset are distinct. The relation between two classes of data that can be separated by a single perceptron must either (or both) relatively simplistic or so distinct that using a single-line boundary is viable to separate the data.

I like how you (and others) in the discussion form have made this distinction. Even though, the points don't have a linear relationship (when we look at regression/the line of best fit) they are still linearly separable since the perceptron represents the decision boundary of the binary classification of the 0 and 1 groups.

To me, it seems that a single-layer perceptron is similar to logistic regression since both categorize data points through binary classification into groups labeled 0 and 1.
