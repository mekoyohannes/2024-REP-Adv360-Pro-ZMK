# Getting Started: What AI Actually Is

No math. No jargon you don't need. Just the mental model.

## The one-sentence version

Modern AI (the chatbot kind) is a system that has read an enormous amount of human writing and learned to predict what words come next — so well that "predicting the next word" starts to look like understanding, reasoning, and conversation.

That's it. Everything else is detail.

## A useful picture

Imagine someone who has read a huge slice of the internet, millions of books, and mountains of code — but who has **no memory of any single source**, **no ability to look things up** (unless you give it tools), and **no inner sense of "I'm not sure."** They've absorbed the *patterns* of human language so deeply that they can talk about almost anything fluently.

That's a large language model (LLM). It's the engine behind tools like Claude, ChatGPT, and Gemini.

This picture explains the two things that confuse people most:

- **Why it's so good:** It has seen how experts write about nearly everything, so it can imitate that fluency on demand.
- **Why it makes things up ("hallucinates"):** It's predicting plausible-sounding text, not retrieving verified facts. A fake citation *looks* exactly like a real one to the model, because both follow the same pattern.

## The vocabulary you'll actually hear

- **Model** — the trained "brain." Bigger/newer usually means more capable.
- **Prompt** — what you type in. The question, the instruction, the context.
- **Token** — a chunk of text (roughly ¾ of a word). Models read and write in tokens, and limits are measured in them.
- **Context window** — the model's short-term memory: how much it can "hold in mind" at once. Big windows can read whole books; everything outside the window is forgotten.
- **Training data** — the text it learned from. It has a **cutoff date**, so it doesn't natively know recent events.
- **Hallucination** — when it states something false with total confidence. The single most important word in this whole package.
- **Multimodal** — can handle more than text: images, audio, sometimes video.

(Full decoder ring in [`07-glossary.md`](07-glossary.md).)

## What it's genuinely great at

- Explaining hard ideas at any level ("explain like I'm 12 / like I'm a grad student")
- First drafts of almost anything — then *you* edit
- Summarizing long things
- Brainstorming — give me 20 angles, then I'll pick
- Translating between languages, tones, and formats
- Rubber-ducking: talking through a problem until *you* see the answer

## What it's bad at (know these cold)

- **Facts, names, numbers, citations** — verify every single one
- **Recent events** past its cutoff (unless it has live search)
- **Math and counting** without a tool to help
- **Knowing what it doesn't know** — it rarely says "I'm not sure"
- **Your specific context** it can't see — your class, your library's catalog, your professor's rules

## The single habit that matters most

> **Trust nothing factual until you've checked it. Use AI for thinking; use real sources for truth.**

You, a future *librarian*, are being trained to be exactly the person who knows how to check. That's not a coincidence — it's why this field is about to matter more than ever.

Next up: [`03-how-to-use-ai-well.md`](03-how-to-use-ai-well.md) — the practical habits.
