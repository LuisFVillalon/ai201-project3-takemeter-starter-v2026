# TakeMeter

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first** — setup, the
> notebook, the baseline, and what to do when something breaks.
>
> Once `python test.py` passes:
>
> ```bash
> head -5 data/practice_labels.csv     # the shape your labels.csv needs
> ```
>
> Then open `takemeter.ipynb` **in this folder** — in VS Code, or with
> `jupyter notebook` if you prefer. Pick the kernel: the `.venv` inside this
> project. Run section 1, which reports the hardware you'll be training on.
> Everything else waits until you have data.
>
> Nothing to upload, nothing to connect, no accounts and no keys. The notebook
> runs on your machine and writes next to your code.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     HOW TO USE THIS FILE

     Unit 5 asks for the first five sections. Unit 6 adds the five below them.

     Everything is pasted as TEXT. No screenshots, no images.

     ⚠️ The confusion matrix especially. The notebook prints one as a markdown
     table, ready to copy. A screenshot of a matrix earns nothing. Paste the
     table.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 5 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- Your community, and what your classifier sorts posts into. Three or four
     sentences. -->

**Community:** r/SaaS

I reviewed the 40 newest posts in this community and found that posts usually talk about four things:

1. People posting about their product ideas and looking for validation.
2. People posting with marketing intentions, to acquire more customers for their product.
3. People asking for information or help on how to increase their sales, set their pricing, or monetize their product.
4. People asking for technical and business help for their product or company.

---

## Label Taxonomy

<!-- Each label: a one-sentence definition and two real examples from your
     reading. Then your decision rule for the hardest boundary.

     The decision rule is worth a point on its own and it's the thing most
     people leave out. Every taxonomy has a hardest boundary. Name yours. -->

### `idea_validation`

**Definition:**
When the main purpose is deciding what to build, identifying customer problems, testing product-market fit, or improving the product experience.

**Example 1:**
> **I'm exploring a PDF-based AI chat tool. Which industries would actually find this useful?**
>
> Hi everyone!
>
> I'm a .NET developer exploring ideas for a small SaaS product, and I'd like to validate a problem before spending time building it.
>
> The idea
> I'm considering building a simple AI-powered document chat tool using RAG (Retrieval-Augmented Generation).
>
> The concept is straightforward:
>
> Users upload PDFs and ask questions about their contents through an AI chat interface.
>
> The AI answers based on the uploaded documents and provides references to the relevant pages or sections.
>
> Businesses can optionally integrate a small chat widget into their existing websites so their customers or employees can ask questions about approved documents.
>
> Users can manage their documents and chat through a web dashboard.
>
> For example, a business might use it to answer questions about product manuals, policies, technical documentation, training materials, or other documents relevant to its industry.
>
> I'm not limiting this to any particular industry. I'd like to discover where this would solve a genuine problem.
>
> I'd appreciate your feedback:
> Which industry or type of business would benefit most from this product?
>
> What specific problem could it solve for that industry?
>
> Are businesses or individuals already using similar tools? What is missing from the existing solutions?
>
> Would you prefer uploading documents to a separate platform, or embedding a chat widget directly into your own website?
>
> Would this be valuable enough to pay for? If yes, what pricing model would make sense?
>
> I'm looking for honest feedback, including reasons why this might not be a viable product.
>
> I haven't committed to building it yet. My goal is to identify a specific use case where people have a genuine need, existing solutions fall short, and customers would be willing to pay.
>
> Thanks for sharing your thoughts!

**Example 2:**
> **Would freelancers actually use a single link to onboard new clients?**
>
> Hey everyone,
>
> I'm exploring a small SaaS idea and wanted to validate whether this is a real problem before building anything.
>
> The idea is a simple client onboarding tool for freelancers and small agencies.
>
> The workflow would be straightforward: instead of sending clients multiple emails, Google Forms, Drive links, and documents, you send them one link where they can complete everything.
>
> For example, a web developer could send a client a link where they can:
>
> Fill out a project brief and answer relevant questions.
>
> Upload files, images, logos, and other assets.
>
> Select a package or service.
>
> Review project timelines and milestones.
>
> Complete an onboarding checklist.
>
> The freelancer gets all the information organized in one place, without having to chase clients for missing details.
>
> I'm not trying to build another full CRM or project management platform. The goal is to make client onboarding as simple as possible.
>
> I'd love your honest feedback on a few questions:
>
> How do you currently onboard new clients? What tools do you use?
>
> What's the most annoying part of the process?
>
> Would having a single shareable onboarding link genuinely make things easier, or is your current workflow good enough?
>
> Would you pay around $5–$15/month for something like this? If not, what would make it worth paying for?
>
> Are there existing tools that already solve this problem well?
>
> I'm particularly interested in hearing from freelance designers, web developers, video editors, and small agency owners.
>
> I'm still at the validation stage, so I'm looking for honest criticism rather than encouragement. If this already exists and solves the problem well, I'd love to know that too.
>
> Thanks!

### `marketing`

**Definition:**
When the main purpose is attracting visitors, generating awareness, or choosing promotional channels.

**Example 1:**
> **It took me a year but I have crossed 1M+ impressions finally**
>
> Everyone was building a directory last year so I thought of building one but growing it was tough as I don't have any audience on social media.
>
> So I learnt pSEO and revamped the website a couple of times and now it's been more than a year and it has more than 1000 pages and last month 5K+ traffic is coming from Google only (total traffic is almost 12K per month). And today I checked it has crossed 1M+ impressions in the last 12 months.
>
> Earlier I focussed on pSEO and building backlinks and from the last couple of months I have started content, a newsletter, and recently started consistently on twitter as well.
>
> The next goal is to reach 20k visitors per month, I could not believe I could say something like this as when I launched last year the traffic was 5-10 people only. So if u are building something and don't have an audience then plz start doing seo from day 1. If u have any questions I'm happy to help.

**Example 2:**
> **Marketing ideas?**
>
> I'm building a PC audio enhancer for audiophiles and audio professionals. It works on pretty much all audio devices; speakers, home theaters, headphones, etc.
>
> It has an easy-to-use room calibration, a technologically impressive spatial audio engine for both headphone- and speaker-based listening (really proud of each, they're better than anything I've ever tried, and I've tried a lot), algorithmic EQ (also very proud of that, works extremely well even for people with no audio experience), a manual EQ, and volume riding.
>
> It's an app for people with taste, who want to get the absolute most out of their listening devices.
>
> There are still quite some things to optimize and fine-tune with the app, but it's nearly ready for release. It looks aesthetic and feels premium and soulful. Also the user tests have been very positive; 100% of the test users prefer having it on and would spend money on it (well, the group was very small haha). I'm planning on offering it at $30-70 per year, with a free or a cheap trial.
>
> But I have no idea how I'll do marketing or actually find potential users. This is not my forte at all. My only ideas are to post on audiophile and professional forums, and also reach out to content creators to give them free lifetime access to the app, so that they could make videos on it if they're interested (that one might be a bit too optimistic?). But that's about all I've got...
>
> Idk, I do have a great vision for the app, but I don't know how to communicate it very effectively and how to reach the largest possible audiences that could be interested in something like this. And how to convert them into buying customers, etc.
>
> I feel like this is the biggest dark cloud over me right now, and I'd appreciate any and all ideas, resources, or anything at all from you fine people. I need help.

### `sales_monetization`

**Definition:**
When the post focuses on turning visitors into signups, charging customers, setting prices, accepting payments, generating revenue, or closing deals.

**Example 1:**
> **I've read 300+ indie SaaS pricing pages this month. A few things I keep seeing**
>
> I've been writing to SaaS founders one by one for a few weeks, and I always read their pricing page first so the message is about something real. I'm past 300 now so here's what keeps showing up. No names.
>
> The big one is the jump between plans. $39 and then $160. $97 and then $495 and nothing in between. If you outgrow the first plan and don't need the second you squeeze into the small one or you leave, because almost nobody writes to ask.
>
> Trials are mostly 7 or 14 days and a few are 3. On the last day it's pay or go and I can count on one hand the pages that say what actually happens that day.
>
> Annual is nearly always 2 months free or something close to 20% off. Then every now and then someone does half price for the year and I really want to know how many people take that.
>
> Lots of founding prices too. $60 instead of $99, first year cheaper, launch price until some date... What happens to those people when it runs out, no idea, the page never says.
>
> "Talk to us" appears once you're big enough, 5+ seats or a lot of volume. Below that there's no button for "can we do something different".
>
> And the free plans. Very common and the wall is almost always a number: answers, credits, sites, searches...
>
> Full disclosure, the trial thing is what I'm building for (HAGGIN, a page where people about to leave can make an offer instead) so I'm not neutral on that one. Curious which of these you'd recognise in your own pricing.

**Example 2:**
> **Lost my first two deals, one to a junior hire and one to "we'll do it with Claude"**
>
> I'm building an AI product for companies.
>
> I sent my first two proposals, around R$4,500 a month (about $800).
>
> The first one was a travel agency with 20 people. The team told me they spend 2 to 3 hours on each material plus 1 hour reviewing. The pain was clear. The owner said no and decided to hire a junior full time.
>
> The second one was another agency. They said it was too expensive and wanted a one time project. A few weeks later they told me they were doing it themselves with Claude.
>
> So my real competitor is not other software, it's a junior or Claude.
>
> How do you price against "I'll just hire someone"? Compare with the salary, charge per user, or something else?

### `operations`

**Definition:**
When the main issue concerns internal processes, customer support systems, infrastructure, compliance, hiring, or technical administration.

**Example 1:**
> **For those running support at a small startup, what was the hardest part of setting up your helpdesk?**
>
> I've built support operations from scratch a few times and I'm curious where other people get stuck. Macros? Tagging and reporting? Escalation rules? Knowing what to automate? If you've been through this, what do you wish you'd had on day one?

**Example 2:**
> **How do you tell a self-hosted customer “that’s your infra”**
>
> Say a paying customer’s app stops working. They host it themselves, and the problem turns out to be something they changed in their setup.
>
> From their side, they paid for your product and it isn’t working. I can understand why they’d come to you.
>
> What I’d struggle with is knowing when to stop helping. You might need to spend hours investigating before you can even explain why it’s their setup. By then, you’ve already done a fair amount of the work.
>
> I wouldn’t want to leave them stuck, but I also wouldn’t want every ticket to become our engineering team fixing someone else’s environment.
>
> If you offer self-hosting options, how do you navigate this conversation?

### The hardest boundary

**Which two labels:**
marketing vs. sales_monetization

**The decision rule I used every time:**
<!-- e.g. "If the post names a specific checkable fact, it's `analysis`, even
     if the tone is heated." -->
If a post is about getting attention or traffic, it is marketing; if it is about converting prospects into signups, pricing, or payment, it is sales_monetization.


---

## The Dataset

<!-- Where you collected from, how you labelled, your counts, and three hard
     cases. -->

**Where the posts came from:**
299 public posts from r/SaaS, collected from the subreddit's "New" feed using Reddit's public RSS feed (no login). I wrote `collect_posts.py` to pull each post's title and full body text into `labels.csv`, removed one duplicate, and did not trim any posts.

**How I labelled them:** I labelled the first 20 posts cold, with no AI help, using only my README definitions (marked `cold` in the `note` column). The remaining 279 posts were pre-labelled by Claude using my label definitions and decision rule, then I reviewed every one (marked `pre-labeled, checked`). While writing my hard cases, I changed rows 130 and 222 from `marketing` to `sales_monetization` to follow my decision rule.

**Counts per label:**

| Label | Count | Share |
|---|---|---|
| idea_validation | 106 | 35% |
| marketing | 69 | 23% |
| sales_monetization | 64 | 21% |
| operations | 60 | 20% |
| **Total** | 299 | 100% |

**Three hard cases**

<!-- Any post that made you pause: what it was, which two labels it could have
     been, and what you chose. These are worth more than the easy 190. -->

**1.**
> *The post:* Row 130: "Spent 6 months building, been a month since launch. What's wrong?" Launched 2 months ago, 50 visits, 0 users, "none converted."
>
> *Could have been:* `marketing` or `sales_monetization`
>
> *I chose, because:* `sales_monetization`, because the post already has visitors (50) and says none of them converted. The problem is turning existing visitors into signups, which my decision rule places under sales_monetization.

**2.**
> *The post:* Row 158: "Built a genuinely fast, non-wrapper AI tool for a "boring" B2B problem (OCR + data extraction). 100 cold emails and 6 warm dev leads later: everyone says "cool" and ghosts."
>
> *Could have been:* `marketing` or `sales_monetization`
>
> *I chose, because:* `sales_monetization`, because the founder already has leads and the problem is converting them into paying customers, which my decision rule places under sales_monetization.

**3.**
> *The post:* Row 222: "Built a tool for PostHog users, launched it, and got 13 visitors and 0 users. Tell me why."
>
> *Could have been:* `marketing` or `sales_monetization`
>
> *I chose, because:* `sales_monetization`, because the post already has visitors (13) and none became users. Like case 1, the problem is converting existing visitors into signups, so my decision rule places it under sales_monetization.

---

## The Training Run

<!-- Your starting model, your settings, and anything you changed and why. -->

**Base model:**

**Settings:** <!-- epochs, learning rate, batch size, seed -->
**Device:** CPU (PyTorch 2.14.1+cpu, 15.8 GB RAM)

**Anything I changed from the defaults, and why:**

**Split sizes:** <!-- train / val / test, and per-label counts in the test
split. If a label had fewer than about 8 in test, say so — it explains a lot
of next unit's variance. -->



---

## How I Used AI

<!-- Two specific moments — what you asked, what came back, what you changed.

     ⚠️ Plus disclosure of any pre-labelling. If you had a model pre-label a
     batch and then read and corrected every one, say that. It's an allowed
     workflow and disclosing it costs you nothing. Not disclosing it is the
     problem. -->

**Moment 1**

- *What I asked for:*
- *What came back:*
- *What I changed:*

**Moment 2**

- *What I asked for:*
- *What came back:*
- *What I changed:*

**Pre-labelling disclosure:**

<!-- ═══════════════════════ UNIT 6 — THE TEST ═══════════════════════

     Don't fill these in during unit 5.
     ═══════════════════════════════════════════════════════════════════ -->

---

## Baseline vs. Trained

<!-- Both models on the same posts. `python baseline.py --trained results.json`
     prints this table for you. -->

| Measure | Baseline | Trained | Difference |
|---|---|---|---|
| Overall accuracy |  |  |  |
| Macro F1 |  |  |  |
| F1 — `label_one` |  |  |  |
| F1 — `label_two` |  |  |  |

**What I predicted before I looked:**
<!-- Milestone 1 asks you to write this BEFORE seeing the trained numbers. A
     prediction made afterwards isn't one. -->

**What the gap actually means:**
<!-- If the baseline matched your trained model, your fine-tuning added
     nothing — and that is a real finding, not a failure. Say it plainly. -->



---

## Run Log — Before

<!-- Five criteria across three seeds. The notebook's section 6 prints the
     spread table; the Target and Verdict columns are yours. -->

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

### Confusion matrix

<!-- ⚠️ TYPED AS A MARKDOWN TABLE. The notebook prints one ready to paste.
     An image of a matrix earns nothing. -->

| true \ predicted |  |  |  |
|---|---|---|---|
| **** |  |  |  |
| **** |  |  |  |
| **** |  |  |  |

**My biggest off-diagonal number, and what it means:**
<!-- Not "the model made mistakes" — WHICH boundary it didn't learn, and which
     direction. "7 real analysis posts were called hot_take and only 3 went the
     other way" is a direction, not just an error rate. -->



---

## Verdicts and Diagnoses

<!-- MET or MISSED against LAST UNIT's target. The target has to hold across
     all three seeds, not turn up sometimes. -->

| # | Criterion | Target | Verdict | How I decided |
|---|---|---|---|---|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
| 4 |  |  |  |  |
| 5 |  |  |  |  |

**Diagnoses**

<!-- For each miss: the cause, and how you know. The four common causes are:
     too few examples for a label, a boundary you applied inconsistently, a
     genuinely hard label pair, and a task the model can't reach from this
     much data.

     ⚠️ Use your agreement report as evidence. It is the only instrument you
     have that can tell a LABELLING problem from a MODEL problem, and this
     section is graded on whether you used it that way. -->



---

## Agreement Report

<!-- Your rate against the staff set, and every disagreement adjudicated.

     Remember you labelled these 30 under the STAFF taxonomy in
     data/staff_taxonomy.md, not your own — so every argument below is made
     from those definitions and those decision rules. -->

**Agreement rate:** ___ / 30 = ___%

<!-- Nobody grades this number. A 60% who argues every disagreement from the
     stated rules beats a 95% who wrote "staff was right" nine times. Several
     of the 30 were chosen because they're genuinely ambiguous — you should be
     winning some of these. -->

**Disagreements**

<!-- Three lines each: the post, both labels, and who you think is right and
     why — grounded in the staff definitions you were both applying.

     Then sort each into one of three piles:
       (a) the rule covered it and I applied it loosely → a consistency problem
       (b) the rule genuinely doesn't say               → a gap in the definitions
       (c) the rule is ambiguous here and my reading is defensible → argue it.
           This is a legitimate win.

     Pile (a) is the one that matters most for your diagnosis: if you applied a
     written rule two different ways on 30 posts, that is direct evidence about
     what you did across your own 200. -->

**1.**
> *The post:*
>
> *Staff said / I said:*
>
> *My call, and why:*
>
> *Which pile:*

**2.**
> *The post:*
>
> *Staff said / I said:*
>
> *My call, and why:*
>
> *Which pile:*

**What the pattern in my disagreements tells me:**



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Run Log — After

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Did it help, and how do I know:**

<!-- If it didn't, say so. Relabelling that didn't help is a genuinely
     interesting result and earns full credit. -->



---

## What's Still Broken

<!-- For each criterion still missed: what you'd do, and why you stopped. -->



**The gap between what I meant my labels to capture and what the model
learned:**
<!-- Two sentences. Your confusion matrix is the evidence. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 5

       [ ] criteria.md has five numbered criteria, each naming a NUMBER
       [ ] Each has a reason underneath tied to your data or taxonomy
       [ ] labels.csv: at least 150 rows, text/label/note, ONE file not split
       [ ] No label above 70%
       [ ] All five unit 5 sections have real content
       [ ] Label Taxonomy includes the decision rule for your hardest boundary
       [ ] The Dataset includes three hard cases
       [ ] results.json and test_split.csv committed (the notebook does this)
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 6

       [ ] Baseline vs. Trained table, with your prediction written beforehand
       [ ] Run Log — Before, five criteria across three seeds
       [ ] Confusion matrix TYPED AS A MARKDOWN TABLE
       [ ] A verdict on every criterion
       [ ] A diagnosis for every miss, using the agreement report as evidence
       [ ] Agreement Report with every disagreement adjudicated
       [ ] One improvement, with Run Log — After
       [ ] What's Still Broken
       [ ] results_three_seeds_before.json, results_three_seeds_after.json,
           baseline_results.json and
           agreement_results.json committed
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
