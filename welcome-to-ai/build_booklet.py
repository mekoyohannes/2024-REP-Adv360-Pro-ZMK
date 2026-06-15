#!/usr/bin/env python3
"""Render Tezeta's 'Welcome to the World of AI' package into a single PDF booklet."""
from weasyprint import HTML

CSS = """
@page {
  size: A4;
  margin: 22mm 20mm 20mm 20mm;
  @bottom-center {
    content: "Welcome to the World of AI  \\00B7  for Tezeta";
    font-family: 'Bitstream Charter', serif;
    font-size: 8pt; color: #b08968;
  }
  @bottom-right {
    content: counter(page);
    font-family: 'Liberation Sans', sans-serif;
    font-size: 8pt; color: #b08968;
  }
}
@page cover { margin: 0; @bottom-center { content: none; } @bottom-right { content: none; } }
@page divider { @bottom-center { content: none; } @bottom-right { content: none; } }

* { box-sizing: border-box; }
body { font-family: 'Bitstream Charter', Georgia, serif; color: #2b2622; font-size: 11pt; line-height: 1.5; }

h1, h2, h3, .display { font-family: 'Liberation Sans', 'DejaVu Sans', sans-serif; color: #7a4a2b; }
h2 { font-size: 19pt; margin: 0 0 4pt 0; color: #8a3b1e; }
h3 { font-size: 13pt; margin: 16pt 0 4pt 0; color: #a85a32; }
p { margin: 6pt 0; }
strong { color: #5a3a22; }
a { color: #9a5a2e; text-decoration: none; }
ul, ol { margin: 6pt 0 6pt 0; padding-left: 18pt; }
li { margin: 3pt 0; }

.cover { page: cover; height: 297mm; width: 210mm;
  background: linear-gradient(150deg, #f6ede1 0%, #efd9c2 45%, #e3b894 100%);
  display: flex; flex-direction: column; justify-content: center; align-items: center;
  text-align: center; padding: 0 26mm; }
.cover .kicker { font-family: 'Liberation Sans', sans-serif; letter-spacing: 4pt;
  text-transform: uppercase; font-size: 10pt; color: #a85a32; margin-bottom: 10mm; }
.cover h1 { font-size: 40pt; line-height: 1.05; color: #6b3a1e; margin: 0; }
.cover .sub { font-size: 15pt; color: #8a5a3a; margin-top: 8mm; font-style: italic; }
.cover .rule { width: 60mm; height: 2px; background: #c1815a; margin: 12mm 0; }
.cover .meaning { font-size: 12pt; color: #6b4a32; max-width: 120mm; line-height: 1.6; }
.cover .from { margin-top: 16mm; font-size: 12pt; color: #8a5a3a; }

.divider { page: divider; page-break-before: always; height: 235mm;
  display: flex; flex-direction: column; justify-content: center; align-items: flex-start; }
.divider .num { font-family: 'Liberation Sans', sans-serif; font-size: 13pt; color: #c1815a;
  letter-spacing: 3pt; }
.divider h1 { font-size: 30pt; color: #7a4a2b; margin: 4mm 0 0 0; line-height: 1.1; }
.divider .blurb { font-size: 12pt; color: #6b5a4a; font-style: italic; margin-top: 6mm; max-width: 130mm; }

.section { page-break-before: always; }
.lead { font-size: 12pt; color: #5a4a3a; }

.callout { background: #fbf3e9; border-left: 4px solid #c1815a; padding: 8pt 12pt;
  margin: 10pt 0; border-radius: 0 6px 6px 0; }
.callout.rule-box { background: #f3ead9; border-left-color: #8a3b1e; }
blockquote { margin: 10pt 0; padding: 8pt 12pt; background: #fbf3e9;
  border-left: 4px solid #c1815a; border-radius: 0 6px 6px 0; font-style: italic; color: #5a3a22; }

table { width: 100%; border-collapse: collapse; margin: 10pt 0; font-size: 10pt; }
th { background: #e9c9a8; color: #5a3a22; text-align: left; padding: 6pt 8pt;
  font-family: 'Liberation Sans', sans-serif; }
td { padding: 6pt 8pt; border-bottom: 1px solid #ecdcc8; vertical-align: top; }
tr:nth-child(even) td { background: #fbf5ec; }

.letter { font-size: 11.5pt; line-height: 1.65; }
.signature { font-style: italic; color: #7a4a2b; margin-top: 8pt; }
.ps { font-size: 10pt; color: #6b5a4a; background: #f3ead9; padding: 8pt 12pt;
  border-radius: 6px; margin-top: 12pt; }

.fill .line { color: #b08968; }
.fill p { margin: 9pt 0; }
hr { border: none; border-top: 1px solid #e3cbb0; margin: 12pt 0; }
.small { font-size: 9.5pt; color: #6b5a4a; }
"""

def divider(num, title, blurb):
    return f'<section class="divider"><div class="num">{num}</div><h1>{title}</h1><div class="blurb">{blurb}</div></section>'

cover = """
<div class="cover">
  <div class="kicker">A starter kit &middot; 2026</div>
  <h1>Welcome to the<br>World of AI</h1>
  <div class="sub">made for Tezeta &mdash; Berkeley, Library Science &amp; AI</div>
  <div class="rule"></div>
  <div class="meaning">Your name means <em>memory</em> &mdash; the longing to hold onto
  what matters. You are about to spend your life learning how humanity keeps,
  organizes, and protects exactly that. You were practically named for this.</div>
  <div class="from">made with love by your cousin &nbsp;<span style="color:#d99a2b">&#9829;</span></div>
</div>
"""

intro = """
<section class="section">
  <h2>Start here</h2>
  <p class="lead">This is a map, not a textbook. Read it in any order. Skip what's boring.
  Come back whenever you feel lost. It's not homework &mdash; it's a thing to keep.</p>
  <h3>What's inside</h3>
  <table>
    <tr><th>Part</th><th>What it's for</th></tr>
    <tr><td>1 &middot; A Letter</td><td>A personal note &mdash; read this first.</td></tr>
    <tr><td>2 &middot; Getting Started</td><td>What AI actually is, in plain language. No math.</td></tr>
    <tr><td>3 &middot; Using AI Well</td><td>How to prompt, verify, and not get fooled.</td></tr>
    <tr><td>4 &middot; AI for Library Science</td><td>Why your field + AI is a superpower.</td></tr>
    <tr><td>5 &middot; Ethics &amp; Staying Human</td><td>The rules that matter most.</td></tr>
    <tr><td>6 &middot; First Projects</td><td>Five things to actually try this week.</td></tr>
    <tr><td>7 &middot; Glossary</td><td>Decoder ring for the buzzwords.</td></tr>
    <tr><td>8 &middot; Resources</td><td>Where to keep learning.</td></tr>
    <tr><td>9 &middot; Cheat Sheet</td><td>The whole thing on one printable page.</td></tr>
    <tr><td>10 &middot; Dear Future Tezeta</td><td>A letter to fill in now, open at graduation.</td></tr>
  </table>
  <div class="callout"><strong>If you read nothing else:</strong> AI is astonishingly good at
  language and astonishingly confident when it's wrong. Treat it like a brilliant, fast, slightly
  unreliable intern: great for first drafts and explaining hard things &mdash; but <em>you</em> are
  always the editor, the fact-checker, and the one whose name is on the work. Stay curious, stay
  skeptical, never outsource your judgment. That's the whole game.</div>
</section>
"""

letter = """
<section class="section letter">
  <h2>1 &middot; A Letter Before You Start</h2>
  <p>Hey Tezeta &mdash;</p>
  <p>So. Berkeley. Full scholarship. Library science <em>and</em> AI. I keep re-reading that
  sentence because I'm so proud of you I don't totally know what to do with myself.</p>
  <p>I have to start with your name, because I don't think you picked your path by accident.
  <em>Tezeta</em> &mdash; memory, the ache to hold onto what matters, the thing we don't want
  to lose. And here you are about to spend your life learning how humanity keeps, organizes, and
  protects exactly that. You were practically named for this. Knowledge is just memory that
  outlives the person who had it, and you're going to learn to be its keeper.</p>
  <p>A few things I wish someone had told me when I was starting something big:</p>
  <p><strong>You belong there.</strong> The scholarship isn't a fluke and it isn't charity.
  Somebody read your story and bet on you. When the impostor feeling shows up &mdash; and it will,
  probably around week three &mdash; remember that everyone feels it, and that feeling it means
  you're in a room worth being in.</p>
  <p><strong>AI is a tool, not an oracle.</strong> It will sound confident and be wrong. It will
  write you a beautiful paragraph with a fake citation in it. Your job &mdash; your whole training,
  really &mdash; is to be the person who can tell the difference. That makes you more valuable in
  the AI age, not less.</p>
  <p><strong>Stay a beginner on purpose.</strong> The field moves so fast that everyone is a
  beginner at something. Being comfortable not knowing is a superpower.</p>
  <p><strong>Don't let the machine think for you &mdash; let it think <em>with</em> you.</strong>
  Use AI to go faster and understand hard things. Never use it to skip the part where <em>you</em>
  understand. The understanding is the thing you're actually there to get.</p>
  <p>I made you this little package &mdash; guides, guardrails, things to try. Open it when you're
  curious or stuck, and close it when you've got it.</p>
  <p>Go be brilliant, Tezeta. Call me when you find something cool. I want to hear all of it.</p>
  <p class="signature">Love always,<br>your cousin <span style="color:#d99a2b">&#9829;</span></p>
  <div class="ps"><strong>P.S.</strong> &mdash; This is in my words. If you're printing it, make it
  yours: tell her the story behind her name, the thing only you'd say, the memory only the two of
  you share. That's the part no AI could ever write &mdash; which is sort of the whole point.</div>
</section>
"""

getting_started = """
<section class="section">
  <h2>2 &middot; What AI Actually Is</h2>
  <p class="lead">No math. No jargon you don't need. Just the mental model.</p>
  <h3>The one-sentence version</h3>
  <p>Modern AI (the chatbot kind) is a system that has read an enormous amount of human writing and
  learned to predict what words come next &mdash; so well that "predicting the next word" starts to
  look like understanding, reasoning, and conversation. That's it. Everything else is detail.</p>
  <h3>A useful picture</h3>
  <p>Imagine someone who has read a huge slice of the internet, millions of books, and mountains of
  code &mdash; but who has <strong>no memory of any single source</strong>, <strong>no ability to
  look things up</strong> (unless you give it tools), and <strong>no inner sense of "I'm not
  sure."</strong> That's a large language model (LLM): the engine behind Claude, ChatGPT, and
  Gemini. It explains the two things that confuse people most:</p>
  <ul>
    <li><strong>Why it's so good:</strong> it has seen how experts write about nearly everything.</li>
    <li><strong>Why it makes things up ("hallucinates"):</strong> it predicts plausible-sounding
    text, not verified facts. A fake citation <em>looks</em> exactly like a real one to the model.</li>
  </ul>
  <h3>What it's genuinely great at</h3>
  <ul>
    <li>Explaining hard ideas at any level ("explain like I'm 12 / like a grad student")</li>
    <li>First drafts of almost anything &mdash; then <em>you</em> edit</li>
    <li>Summarizing long things; translating tone, language, and format</li>
    <li>Brainstorming &mdash; "give me 20 angles, then I'll pick"</li>
    <li>Rubber-ducking: talking through a problem until <em>you</em> see the answer</li>
  </ul>
  <h3>What it's bad at (know these cold)</h3>
  <ul>
    <li><strong>Facts, names, numbers, citations</strong> &mdash; verify every one</li>
    <li><strong>Recent events</strong> past its training cutoff (unless it has live search)</li>
    <li><strong>Math and counting</strong> without a tool to help</li>
    <li><strong>Knowing what it doesn't know</strong> &mdash; it rarely says "I'm not sure"</li>
  </ul>
  <blockquote>Trust nothing factual until you've checked it. Use AI for thinking; use real sources
  for truth. You, a future <em>librarian</em>, are being trained to be exactly the person who knows
  how to check. That's why this field is about to matter more than ever.</blockquote>
</section>
"""

using_well = """
<section class="section">
  <h2>3 &middot; How to Use AI Well</h2>
  <p class="lead">Not secret tricks &mdash; just a handful of habits.</p>
  <h3>1. Write better prompts &mdash; the C.R.A.F.T. checklist</h3>
  <ul>
    <li><strong>Context</strong> &mdash; who you are, what's going on</li>
    <li><strong>Role</strong> &mdash; who you want the AI to be ("act as a patient research librarian")</li>
    <li><strong>Ask</strong> &mdash; the actual task, specific</li>
    <li><strong>Format</strong> &mdash; how you want the answer</li>
    <li><strong>Tone</strong> &mdash; length and style</li>
  </ul>
  <div class="callout"><strong>Weak:</strong> "Tell me about AI in libraries."<br>
  <strong>Strong:</strong> "Act as a research librarian. I'm a first-year student writing a 5-page
  paper. Give me three specific, debatable research questions about AI in public libraries, each
  with one reason it matters. Bullet points, plain English."</div>
  <h3>2. Iterate &mdash; don't accept the first answer</h3>
  <p>"Make it simpler." "What's the strongest counterargument?" "Give me three more, weirder this
  time." The good stuff usually shows up in round two or three.</p>
  <h3>3. Verify everything factual (the 30-second rule)</h3>
  <p>If a fact, name, date, statistic, or citation matters, confirm it from a real source first.
  Especially <strong>citations</strong> &mdash; AI invents real-looking sources with completely
  fake details, and your professors <em>will</em> catch it. Library databases (JSTOR, your catalog,
  Google Scholar) are your truth layer.</p>
  <h3>4. Never paste in things you shouldn't</h3>
  <p>Treat a chatbot like a postcard, not a diary. No passwords, no other people's private data, no
  confidential work, no unpublished work you're not ready to risk.</p>
  <h3>5. Keep your fingerprints on the work</h3>
  <p>Draft with AI, then rewrite in your own voice and make sure you understand every line. If you
  couldn't explain it to a friend with the chatbot closed, you're not done.</p>
  <h3>6. The trust thermometer</h3>
  <table>
    <tr><th>Stakes</th><th>How much to verify</th></tr>
    <tr><td>Brainstorming, explaining a concept to yourself</td><td>Low &mdash; sanity-check</td></tr>
    <tr><td>A draft you'll heavily edit</td><td>Medium &mdash; verify key facts</td></tr>
    <tr><td>Anything you'll submit, cite, or publish</td><td>High &mdash; verify everything, cite real sources</td></tr>
    <tr><td>Health, legal, financial, safety decisions</td><td>Don't rely on it &mdash; ask a qualified human</td></tr>
  </table>
  <blockquote>You're the pilot. AI is the autopilot. Autopilot is amazing &mdash; and you never take
  your hands fully off the controls.</blockquote>
</section>
"""

library = """
<section class="section">
  <h2>4 &middot; AI for Library Science</h2>
  <p class="lead">A secret not enough people have noticed: library science and AI are the same
  project wearing different clothes.</p>
  <p>Both answer one question &mdash; <em>how do humans find the right knowledge at the right moment
  and trust it?</em> Librarians have built the findable systems forever: catalogs, classification,
  metadata, reference. AI is a new, powerful way to do information retrieval and organization. You're
  not learning a field AI threatens &mdash; you're learning the field that <em>makes sense of</em> AI.</p>
  <h3>Concepts where your two worlds collide</h3>
  <ul>
    <li><strong>Information retrieval</strong> &mdash; the science of finding relevant things; the shared root of search, databases, and AI.</li>
    <li><strong>Metadata</strong> &mdash; data about data. AI consumes it to work better and can help generate it at scale.</li>
    <li><strong>Classification &amp; taxonomies</strong> &mdash; Dewey, LCSH, ontologies. AI suggests; humans decide what's fair and unbiased.</li>
    <li><strong>RAG (Retrieval-Augmented Generation)</strong> &mdash; <em>the</em> one to know. AI that looks things up in a trusted collection before answering. Basically "give the chatbot a library card."</li>
    <li><strong>Digital archives &amp; preservation</strong> &mdash; AI helps with transcription (handwriting!), translation, and search across huge collections.</li>
    <li><strong>Information literacy</strong> &mdash; teaching people to evaluate sources. In the AI age, the most important thing a librarian gives the public.</li>
  </ul>
  <h3>Where you, the human, stay essential</h3>
  <ul>
    <li><strong>Truth &amp; verification</strong> &mdash; was that source real? Does it say what's claimed?</li>
    <li><strong>Bias &amp; fairness</strong> &mdash; AI learns society's biases; someone has to notice and correct them.</li>
    <li><strong>Privacy</strong> &mdash; libraries fiercely protect what people read; AI tools often want exactly that data. You'll be a guardian.</li>
    <li><strong>Judgment &amp; ethics</strong> &mdash; deciding what <em>should</em> be done, not just what <em>can</em>.</li>
  </ul>
  <blockquote>The card catalog, the search engine, and the AI assistant are the same idea a century
  apart: a bridge between a person and the knowledge they're looking for. You're learning to build
  the next bridge &mdash; and to make sure it's honest, open, and for everyone.</blockquote>
</section>
"""

ethics = """
<section class="section">
  <h2>5 &middot; Ethics &amp; Staying Human</h2>
  <p class="lead">The technical stuff you'll pick up fast. This is the part that actually matters.</p>
  <div class="callout rule-box"><strong>The line that keeps you out of trouble:</strong> Use AI to
  <em>do</em> your work better. Never use it to <em>avoid doing</em> your work. The honest uses are
  the ones that leave you smarter at the end.</div>
  <h3>Academic integrity, concretely</h3>
  <ul>
    <li><strong>Ask first.</strong> Each professor and assignment may differ. "Is AI allowed here, and for what?"</li>
    <li><strong>Disclose when unsure.</strong> "I used AI to brainstorm and check grammar" is almost always the safe move.</li>
    <li><strong>Never submit unverified AI text as fact.</strong> Fake citations are the classic way students get caught.</li>
    <li><strong>The work has to be yours.</strong> If you can't explain it without the chatbot open, you haven't learned it.</li>
  </ul>
  <h3>Things AI gets wrong &mdash; watch for them</h3>
  <ul>
    <li><strong>Bias.</strong> Models inherit human prejudice. Noticing and naming it is part of your job.</li>
    <li><strong>Hallucination.</strong> Confident, fluent, and wrong. Assume facts need checking.</li>
    <li><strong>Erasure.</strong> AI can sideline smaller voices, dialects, and histories. Libraries exist partly to protect those.</li>
    <li><strong>False neutrality.</strong> "The computer said so" feels objective. It isn't.</li>
  </ul>
  <h3>Privacy &mdash; your field's superpower value</h3>
  <p>Libraries hold one of the strongest privacy ethics on earth: what you read is nobody's
  business. Many AI tools are built on the opposite instinct. Start the habit now &mdash; don't feed
  private data into chatbots, and champion the patron's right to read without being tracked.</p>
  <h3>Staying human</h3>
  <p>Keep your curiosity, your voice, your relationships, and your struggle. The hard, slow,
  confusing part of learning <em>is</em> the learning &mdash; don't let AI smooth it all away.</p>
  <blockquote>Let AI make you faster, never make you smaller. Stay curious, stay honest, stay kind
  &mdash; the point of every tool is to help real people, which is the same reason libraries exist.</blockquote>
</section>
"""

projects = """
<section class="section">
  <h2>6 &middot; Your First Five Projects</h2>
  <p class="lead">Reading about AI is like reading about swimming. Get in the water. Pick a free
  assistant (Claude, ChatGPT, Gemini all have free tiers) and go.</p>
  <h3>1 &middot; "Explain it five ways"</h3>
  <p>Take something confusing. Ask the AI to explain it like you're 10, like a grad student, with a
  cooking analogy, in 3 bullets, and as a short story. Feel how flexible it is.</p>
  <h3>2 &middot; Catch a hallucination on purpose</h3>
  <p>Ask for five scholarly sources on the history of library classification, with authors and
  years &mdash; then <strong>check every one</strong> in Google Scholar. Some will be invented.
  This is the most important lesson here, and you only believe it once you've caught it yourself.</p>
  <h3>3 &middot; Build a research plan</h3>
  <p>"Turn this broad topic into three debatable questions." "What sources would I need?" "What's the
  strongest argument against my position?" "What am I not thinking of?" You did the thinking; it
  widened your view.</p>
  <h3>4 &middot; Compare three models</h3>
  <p>Ask Claude, ChatGPT, and Gemini the same meaty question. Where do they agree? Which was most
  honest about uncertainty? You'll develop taste for which to reach for.</p>
  <h3>5 &middot; Make AI tutor you, then quiz you</h3>
  <p>"Teach me this step by step, checking my understanding after each step." "Now quiz me, one
  question at a time." A patient tutor at 2 a.m. that never sighs at your questions. Use it a lot.</p>
  <blockquote>Every time you use AI, ask: did this make me understand <em>more</em>, or let me
  understand <em>less</em>? Aim for "more," every time.</blockquote>
</section>
"""

glossary = """
<section class="section">
  <h2>7 &middot; Glossary</h2>
  <p class="lead">Plain-English definitions. Come here when a buzzword trips you up.</p>
  <table>
    <tr><th>Term</th><th>What it means</th></tr>
    <tr><td>LLM (Large Language Model)</td><td>AI trained on huge amounts of text that predicts likely next words &mdash; the engine behind chatbots.</td></tr>
    <tr><td>Generative AI</td><td>AI that creates new content (text, images, audio), not just sorts existing things.</td></tr>
    <tr><td>Prompt</td><td>What you type in: your question, instruction, and context.</td></tr>
    <tr><td>Token</td><td>A chunk of text, ~3/4 of a word. Models read and write in tokens.</td></tr>
    <tr><td>Context window</td><td>The model's short-term memory &mdash; how much it can hold in mind at once.</td></tr>
    <tr><td>Hallucination</td><td>When AI states something false with total confidence. The word to remember.</td></tr>
    <tr><td>Training cutoff</td><td>The date after which the model wasn't trained, so it doesn't natively know recent events.</td></tr>
    <tr><td>Bias</td><td>Unfair patterns absorbed from training data, reflecting real-world prejudice.</td></tr>
    <tr><td>RAG</td><td>Retrieval-Augmented Generation &mdash; AI that looks things up in a trusted source before answering. "A chatbot with a library card."</td></tr>
    <tr><td>Semantic search</td><td>Search by meaning rather than exact keywords.</td></tr>
    <tr><td>Embedding</td><td>Turning text into numbers that capture meaning, so a computer can measure similarity. Engine behind semantic search and RAG.</td></tr>
    <tr><td>Metadata</td><td>Data about data (author, date, subject). The lifeblood of catalogs.</td></tr>
    <tr><td>Multimodal</td><td>Handles more than text: images, audio, sometimes video.</td></tr>
    <tr><td>Agent</td><td>An AI set up to take actions and use tools on your behalf, not just chat.</td></tr>
  </table>
  <p class="small">Don't memorize this. Skim once, return when needed. Understanding beats vocabulary.</p>
</section>
"""

resources = """
<section class="section">
  <h2>8 &middot; Where to Keep Learning</h2>
  <p class="lead">Curated, not overwhelming. Pick one thing that sparks you and follow the thread.
  Treat specific tools as "true as of 2026" &mdash; the ideas age slower than the products.</p>
  <h3>Start here (gentle, free)</h3>
  <ul>
    <li><strong>Just talk to the tools.</strong> Free tiers of Claude, ChatGPT, and Gemini. Two weeks of daily use teaches more than any course.</li>
    <li><strong>Elements of AI</strong> &mdash; a free, famous, non-technical intro course.</li>
    <li><strong>Your university library's own guides.</strong> Berkeley will have research guides on AI tools and integrity. It's literally your field.</li>
  </ul>
  <h3>For the library + AI crossover</h3>
  <ul>
    <li><strong>The American Library Association (ALA)</strong> &mdash; their work on AI, privacy, and intellectual freedom is your professional compass.</li>
    <li>Search <strong>"AI literacy for librarians"</strong> &mdash; a fast-growing area aimed exactly at you.</li>
    <li>The <strong>ACRL Framework for Information Literacy</strong> &mdash; the backbone of evaluating any source.</li>
  </ul>
  <h3>Books to grow into</h3>
  <ul>
    <li><em>Weapons of Math Destruction</em> &mdash; Cathy O'Neil (how algorithms can be unfair)</li>
    <li><em>Atlas of AI</em> &mdash; Kate Crawford (the real-world costs and politics of AI)</li>
    <li><em>The Alignment Problem</em> &mdash; Brian Christian (making AI do what we actually want)</li>
  </ul>
  <h3>Habits that beat any reading list</h3>
  <ul>
    <li>Follow thoughtful people who say "it depends" and "I'm not sure" &mdash; the honest ones.</li>
    <li>Keep an <strong>ai-notebook</strong>: prompts that worked, answers that surprised you, times it was wrong.</li>
    <li>Teach someone else &mdash; the fastest way to find out what you actually understand.</li>
  </ul>
  <p>You do <em>not</em> need to keep up with every headline. Check in monthly, not hourly. Depth
  beats novelty. And call me when you build something cool. I mean that. <span style="color:#d99a2b">&#9829;</span></p>
</section>
"""

cheat = """
<section class="section">
  <h2>9 &middot; The One-Page Cheat Sheet</h2>
  <p class="small">Print this. Pin it above your desk. The whole package in 60 seconds.</p>
  <blockquote><strong>The golden rule:</strong> AI makes you faster. Never let it make you smaller.
  Use it to think <em>with</em>, never to <em>skip</em> the thinking.</blockquote>
  <h3>The 5-part prompt &mdash; C.R.A.F.T.</h3>
  <p><strong>C</strong>ontext &middot; <strong>R</strong>ole &middot; <strong>A</strong>sk &middot;
  <strong>F</strong>ormat &middot; <strong>T</strong>one</p>
  <h3>Before you trust it</h3>
  <ul>
    <li>Verify every fact, name, date, and citation. AI invents real-looking sources.</li>
    <li>Ask: does this make me understand <em>more</em>, or <em>less</em>? Aim for more.</li>
    <li>If you can't explain it without the chatbot open, you're not done.</li>
  </ul>
  <h3>The trust thermometer</h3>
  <table>
    <tr><th>Stakes</th><th>Verify how much?</th></tr>
    <tr><td>Brainstorming / explaining to yourself</td><td>Sanity-check</td></tr>
    <tr><td>A draft you'll edit</td><td>Key facts</td></tr>
    <tr><td>Anything you'll submit or cite</td><td>Everything &mdash; real sources</td></tr>
    <tr><td>Health / legal / money / safety</td><td>Ask a qualified human</td></tr>
  </table>
  <h3>Never paste in</h3>
  <p>Passwords &middot; other people's private data &middot; confidential work &middot; anything
  you'd put on a diary page, not a postcard.</p>
  <h3>In class</h3>
  <p>Ask <strong>before</strong> each assignment: "Is AI allowed here, and for what?" When unsure,
  disclose how you used it.</p>
  <div class="callout"><strong>Your superpower:</strong> you're training to be the person who can
  tell true from plausible, real source from fake, fair from biased. In the AI age, that's worth
  <em>more</em>, not less. <span style="color:#d99a2b">&#9829;</span></div>
</section>
"""

future = """
<section class="section fill">
  <h2>10 &middot; Dear Future Tezeta</h2>
  <p class="small">A page to fill in by hand &mdash; today, before classes start. Seal it. Open it
  the week you graduate.</p>
  <p>Today's date: <span class="line">________________</span></p>
  <p>Right now, I am feeling <span class="line">________________________________________</span><br>
  <span class="small">(nervous? electric? both? write the truth.)</span></p>
  <p>The thing I'm most excited to learn is <span class="line">______________________________</span></p>
  <p>The thing I'm most scared of is <span class="line">__________________________________</span><br>
  <span class="small">(name it &mdash; it gets smaller once it's on paper.)</span></p>
  <p>One reason I belong at Berkeley, even on the days I doubt it:<br>
  <span class="line">________________________________________________________________</span></p>
  <p>What I hope AI helps me do (without doing it <em>for</em> me):<br>
  <span class="line">________________________________________________________________</span></p>
  <p>A promise to myself about how I'll use these tools honestly:<br>
  <span class="line">________________________________________________________________</span></p>
  <p>The kind of librarian I want to become:<br>
  <span class="line">________________________________________________________________</span></p>
  <p>Something I never want to lose, no matter how the tech changes:<br>
  <span class="line">________________________________________________________________</span></p>
  <hr>
  <p>By the time you read this again, you'll have caught a hundred hallucinations, written things
  you're proud of, and helped real people find what they were looking for.</p>
  <p>Your name means <em>memory</em>. So remember this beginning &mdash; the nerves, the hope, all of
  it. You did something brave today. I'm proud of you. I was always going to be.</p>
  <p class="signature">&mdash; your cousin, and now also <em>you</em> <span style="color:#d99a2b">&#9829;</span></p>
</section>
"""

html = ("<!DOCTYPE html><html><head><meta charset='utf-8'></head><body>"
        + cover + intro + letter + getting_started + using_well + library
        + ethics + projects + glossary + resources + cheat + future
        + "</body></html>")

HTML(string=html).write_pdf("/home/user/2024-REP-Adv360-Pro-ZMK/welcome-to-ai/Tezeta-Welcome-to-AI.pdf",
                            stylesheets=[__import__("weasyprint").CSS(string=CSS)])
print("PDF written.")
