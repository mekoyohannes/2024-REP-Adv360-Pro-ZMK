# Glossary: The Decoder Ring

Plain-English definitions. When a professor or article throws a buzzword at you, come here.

### The essentials

- **AI (Artificial Intelligence)** — software that does things we used to think needed human intelligence: understanding language, recognizing images, making predictions.
- **Machine Learning (ML)** — the main way modern AI is built: instead of being programmed with rules, the system *learns patterns* from lots of examples.
- **Large Language Model (LLM)** — an AI trained on huge amounts of text that predicts likely next words so well it can converse, write, and explain. Claude, ChatGPT, and Gemini are powered by LLMs.
- **Generative AI** — AI that *creates* new content (text, images, audio, code), as opposed to just sorting or labeling existing things.
- **Model** — a single trained AI system. Newer/bigger models are generally more capable.

### How you talk to it

- **Prompt** — what you type to the AI: your question, instruction, and context.
- **Prompt engineering** — the craft of writing prompts that get good results. (See the C.R.A.F.T. checklist in `03`.)
- **System prompt** — hidden instructions that set an AI's overall behavior and personality before you ever type.
- **Token** — a chunk of text, roughly ¾ of a word. AIs read and write in tokens; limits and pricing are measured in them.
- **Context window** — how much text the model can "hold in mind" at once (your prompt + its reply + any documents). Anything beyond it is forgotten.

### The things that go wrong

- **Hallucination** — when AI states false information confidently. The word to remember above all others.
- **Bias** — unfair patterns the AI absorbed from its training data (reflecting real-world prejudice).
- **Training cutoff** — the date after which the model wasn't trained on new information, so it doesn't natively know recent events.
- **Overfitting** — (more technical) when a model memorizes its examples instead of learning the general pattern. You'll meet this in any ML course.

### The library-science crossover terms

- **Information retrieval** — the science of finding relevant information in a collection. The shared root of search engines, databases, and AI.
- **RAG (Retrieval-Augmented Generation)** — AI that looks things up in a trusted source *before* answering, instead of relying on memory. "A chatbot with a library card." Learn this one.
- **Semantic search** — search by *meaning* rather than exact keywords ("find things about this idea").
- **Embedding** — turning text into a list of numbers that captures its meaning, so a computer can measure how "similar" two pieces of text are. The quiet engine behind semantic search and RAG.
- **Metadata** — data about data (author, date, subject, format). The lifeblood of catalogs — and increasingly something AI helps generate.
- **Ontology / taxonomy** — structured systems for organizing concepts and their relationships. Your field's specialty; AI's helper.
- **OCR (Optical Character Recognition)** — turning images of text (scans, photos) into machine-readable text. Key for digitizing collections.

### The tools you'll keep hearing about

- **Chatbot / AI assistant** — the conversational apps: **Claude** (Anthropic), **ChatGPT** (OpenAI), **Gemini** (Google), and others.
- **API** — a way for software to talk to an AI model directly (you'll meet this if you take any technical course).
- **Agent** — an AI set up to take actions and use tools on your behalf, not just chat.
- **Multimodal** — handles more than text: images, audio, sometimes video.
- **Open source / open weights** — models anyone can download and run, vs. closed ones you only access through a company's app.

> Don't try to memorize this. Skim it once, then come back when a word trips you up. Understanding beats vocabulary every time.
