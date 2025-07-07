# linear-algebra-for-machine-learning

## week 1 Key take aways

Dicriminative AI is when the AI has to categorise a certain input and determine which category the input belongs too. Some examples of discriminative AI are:
* Handwriting to text conversion (the AI would need to determine which symbol the handwritten text falls under)
* Speech to text conversion (the AI would need to determine which symbol the phonetics fall under)

Generative AI is when the AI has to produce/generate a output from the input. Generative AI only utlises LLMs Some examples of generative AI are:
* Test to handwriting conversion (the AI would need to produce the handwriting)
* Test to speech conversion (the AI would need to generate phonetics to read the text outloud)

Both, discriminative and generative AI, **_can_** fall under deep learning.

| Examples of discriminative models (not deep learning)  | Examples of discriminative models using deep learning |
| ------------- | ------------- |
| Logistic regression | Content Cell  |
| Support Vector Machines (SVMs)  | Content Cell  |
| Decision trees  | Content Cell  |
| Random forests  | Content Cell  |

Examples of discriminative models (not deep learning):
* Logistic regression
* Support Vector Machines (SVMs)
* Decision trees
* Random forests

Examples of discriminative models using deep learning:
* Convolutional Neural Networks (CNNs) → image classification
* BERT → language classification (e.g., sentiment analysis)
* Whisper → audio-to-text transcription

Generative AI Models That Use Deep Learning
* Text Generation: GPT (Generative Pretrained Transformer), Claude, PaLM, LLaMA — other LLMs, T5, BART — for summarization, translation
* Image Generation: DALL·E (text-to-image), Stable Diffusion (image generation with diffusion models), StyleGAN (faces and art), BigGAN (high-quality image generation)
* Audio & Speech Generation: WaveNet (text-to-speech waveform generation), Tacotron 2 (text-to-speech spectrogram synthesis), VALL-E (voice cloning), Jukebox (music generation from text)
* Video / Multimodal Generation: Sora (OpenAI's text-to-video), Make-A-Video (Meta), Runway Gen-2
* Code Generation: Codex (used in GitHub Copilot), AlphaCode (from DeepMind)

Generative AI Models That Do Not Use Deep Learning
_These are earlier or simpler techniques that can still generate content, but don’t use neural nets._
* Rule-Based Generators: Template-based systems, MadLib-style text generators
* Probabilistic Models (Shallow): Markov chains which generate text by using probabilities of word sequences (e.g., “The cat” → “sat” → “on” → “the” → “mat”), n-gram models, PCFGs (Probabilistic Context-Free Grammars)
* Genetic Algorithms / Evolutionary Art which generate images or music by evolving patterns over time.
* Expert Systems with Random Variation: Some creative expert systems used rules plus randomness to generate poetry, names, or trivia — but without learning from data.

