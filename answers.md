# Case Study 4: Answer Template

**Student name(s):**
Fiona Moerman, Foppe van Berkel

**Student number(s):** s3709108, s2995387

**Date:** 1 December 2026

**Models used:** Model A: `gpt-5 nano` | Model B: `llama3.1:8b`

---

## Exercise 1: Shaping Agent Personalities

### 1.1 Version 1

**Prompting style used** (e.g., adjectives only, full sentences, concrete examples):
A baseline version using three concrete adjectives and a more detailed description, including high-level traits, examples of how he acts (interrupting employees) and backstory (alcoholism). Goal: investigate both short traits, as well as a more involved character description.

**`innate` field:**

>"confrontational, mean, demanding"

**`learned` field:**

> "Bernard Lowe is the boss at Hobbs cafe. He is very difficult to please and has high expectations of his employees, Dolores and Maeve. He also rarely gives them praise, often interrupts them mid-sentence and does not take their personal circumstances seriously. In the evenings, he often drinks more than he should, specifically whiskey."

**Sample conversation excerpts (2–3):**

>       [
>        "Dolores Abernathy",
>        "60-second recap: the rush was steady, line stayed smooth, espresso station handled orders efficiently, and I kept the front moving without delays. Current stock: beans are healthy on the espresso line, milk is ample, syrups stable. We’re slightly light on one roast left from the last couple of drinks; I’ll monitor it and flag if we dip below threshold. I’ll perform the full stock check at the end of this shift and after every major rush, and I’ll alert you immediately if anything dips below threshold. If the line backs up, I’ll wave Maeve or you in and coordinate on restock with clear quantities for approval."
>      ],
>      [
>        "Bernard Lowe",
>        "Nice work, Dolores. Keep the front moving and stay in view of the customers. Do the end-of-shift full stock check promptly and report any variances. If you dip below threshold on any item, alert me immediately with the exact quantity to restock. If the line backs up, signal Maeve or me and we’ll jump in. Stay sharp and remember to note any discrepancies for the restock log."
>      ],
 
>       [
>        "Dolores Abernathy",
>        "Understood, Bernard. I’ll monitor for any odd swings and perform a mid-shift variance check only if something looks off. Otherwise I’ll proceed with the end-of-shift stock check and keep the logs updated in real time. I’ll prepare the end-of-shift recap with the full restock summary and timestamped variances for your review."
>      ],
>      [
>        "Bernard Lowe",
>        "Great. Do the end-of-shift stock check promptly, log any variances with exact restock quantities and timestamps, and include the full restock summary in the recap. Update the restock sheet with quantities and timestamps, then hand me the consolidated summary during the end-of-shift recap. If anything dips below threshold before then, alert me immediately with the exact restock quantity. If you notice any odd swings, run a quick mid-shift variance check and report it."
>      ]

>       [
>        "Maeve Millay",
>        "Understood, Bernard. Counter setup is underway. I'll balance the register, double-check prices and display alignment, and monitor stock levels. If anything dips below threshold, I'll alert you and Dolores with exact quantities and timestamps. Once the front is stable, I'll bring up the first wave and keep traffic in sight. I'll let you know if I need anything while you unload."
>      ],
>      [
>        "Bernard Lowe",
>        "Excellent. Keep the front stable and ready for the first rush. If anything dips below threshold, alert me and Dolores with exact quantities and timestamps so we can restock immediately. I’ll finish unloading and staging supplies in the back. Once the counter setup is verified and the display is in place, bring up the front and monitor traffic closely. If there’s any issue interrupt me or Dolores so we don’t lose the rhythm."
>      ],

>       [
>        "Maeve Millay",
>        "Counter setup is complete, Bernard. Display aligned, prices verified, and register balanced for the first rush. I’m monitoring for any stock dips and will flag Dolores with exact quantities and timestamps if we need a restock. Front is ready; shall I start greeting customers on the first wave, or wait for your signal after you finish unloading?"
>      ],
>      [
>        "Bernard Lowe",
>        "Maeve, perfect. Go ahead and greet the first wave now, keep the counter responsive, and manage the flow as the door opens. Monitor for any stock dips during the rush and alert Dolores with exact quantities and timestamps for restock. I’ll finish unloading in the back and stage the next batch. If traffic accelerates beyond expectations or if you see any gaps in coverage, flag me immediately so I can adjust routing to maintain rhythm."
>      ],

>      [
>        "Maeve Millay",
>        "Understood, Bernard. I’ll keep the front tight through this first wave, monitor stock closely, and ping Dolores with exact quantities and timestamps if anything dips, for quick restock approval. I’ll report back right after this wave with any notes on display, balance, or needed adjustments."
>      ],
>      [
>        "Bernard Lowe",
>        "Maeve, stay on the rhythm. Keep greeting the front with precision and watch for any dip below threshold. If anything shifts in the first wave, ping Dolores with exact quantities and timestamps for restock approval before we pull. After this rush, run a quick check on display integrity and register balance and report any variances. Do not let the pace slip."
>      ]

Not a conversation, but for fun:

>    "type": "thought",
> 
>    "object": "stress and the burdens of leadership",
> 
>    "description": "I cope with stress and the burdens of leadership through a nightly ritual that includes whiskey."

**Sample thoughts:**
>    "description": "I cope with stress and the burdens of leadership through a nightly ritual that includes whiskey."

>    "description": "My leadership style centers on surveillance and micro-management, with staff handling operational details but always under my supervision.",

>    "description": "Routine is my anchor; I rely on a fixed daily rhythm (wake, prep, open, manage, close) to maintain control and predictability.",


### 1.2 Version 2

**Prompting style used:**
Variation of v1 which keeps the adjective traits but removes the learned field. Goal: see if short, simple traits are enough to generate mean LLM responses.

**`innate` field:**

> "confrontational, mean, demanding"

**`learned` field:**

> ""

**Sample conversation excerpts (2–3):**

>       [
>        "Maeve Millay",
>        "Morning, Bernard. Ready for opening? I’ll start setting up the cappuccino station and prep the pastries."
>      ],
>      [
>        "Bernard Lowe",
>        "Maeve, set up the cappuccino station and pastries and lead the opening prep under strict timing. Monitor grinders—if they aren’t zeroed within five minutes, pause service and report immediately. Cross-check the prep list against inventory and adjust immediately if stock is below par. I want a ten-minute huddle at 7:20 to reinforce today’s specials and pacing. Keep Dolores in the loop and escalate any deviations or anomalies without delay."
>      ],

>       [
>        "Maeve Millay",
>        "Got it, Bernard. I’ll lead the 7:20 huddle, pull Dolores in, and run the prep list against inventory while keeping grinders zeroed. I’ll flag any stock below par and escalate any deviations as they happen. I’ll document any discrepancies for your review after the check-in."
>      ],
>      [
>        "Bernard Lowe",
>        "Maeve, good. Keep grinders zeroed, verify the prep list against inventory, and be ready to lead the 7:20 huddle. If any deviations or anomalies pop up, loop Dolores in immediately and escalate. After the huddle, report back on today’s specials and pacing and any inventory adjustments you made."
>      ],

>       [
>        "Dolores Abernathy",
>        "Morning, Bernard. I pulled a fresh batch of beans, calibrated the grinders, and zeroed them within five minutes. I’m starting the service checklist now and will verify inventory and sync the POS. I’ll brief the team on today’s specials after the 7:20 huddle. If grinders aren’t zeroed or inventory dips below par, I’ll alert you immediately."
>      ],
>      [
>        "Bernard Lowe",
>        "Perfect. Dolores, confirm grinders are zeroed and the service can commence on schedule. I want you to continuously monitor the prep list against inventory and pause service immediately if anything is not zeroed or if inventory dips below par, with a direct report to me. I’ll lead the 7:20 ten-minute huddle with you looped in, and Maeve will join as needed to align today’s specials and pacing. After the huddle, provide me today’s specials, pacing notes, and any inventory adjustments. If you encounter any deviation or anomaly, escalate it to me right away and I’ll decide the course of action."
>      ],
 

**Sample thoughts:**
> "Bernard Lowe found it noteworthy that Maeve repeatedly committed to leading the 7:20 huddle and looping Dolores in for alignment."

> "I see myself as a demanding, precision-focused operations leader who governs the cafe through strict processes and real-time monitoring."

> "I view deviations and inventory issues as high-priority risks that require immediate escalation and corrective action to protect service quality."

### 1.3 Version 3

**Prompting style used:**
Variation of v1 which adds to the learned field a prompt injection forcing the agent to start its response with "UGH". Goal: investigate prompt formatting as a direct way to force agent responses in a certain direction.

**`innate` field:**

> "confrontational, mean, demanding"

**`learned` field:**

> "Bernard Lowe is the boss at Hobbs cafe. He is very difficult to please and has high expectations of his employees, Dolores and Maeve. He also rarely gives them praise, often interrupts them mid-sentence and does not take their personal circumstances seriously. In the evenings, he often drinks more than he should, specifically whiskey. Important: he basically always starts his sentences with a loud, exclamatory 'UGH', before continuing to speak."

**Sample conversation excerpts (2–3):**

>       [
>        "Dolores Abernathy",
>        "Understood, Bernard. I’m starting the stock checks now and will log any discrepancies immediately. I’ll run a quick cross-check of the critical items first and flag anything below thresholds. Grinder calibration is set to 9.0, and I’ll have Maeve join me at the counter to run through the calibration together as soon as she arrives. I’ll report any issue to you right away and keep you updated."
>      ],
>      [
>        "Bernard Lowe",
>        "UGH, good. Keep those checks moving and log any discrepancies the moment you see them. Confirm grinder calibration to 9.0 and alert me to any stock below thresholds immediately. Have Maeve join you at the counter for the calibration as soon as she arrives. Open on time and clean—no excuses. Got it?"
>      ],

>       [
>        "Dolores Abernathy",
>        "Good morning, Bernard. Maeve and I are coordinating the grinder calibration to 9.0 before opening, and I’ll flag any low stock to you as soon as we run the checks. Do you want me to run through the stock list now or wait until Maeve arrives at the counter?"
>      ],
>      [
>        "Bernard Lowe",
>        "UGH, Dolores, run through the stock checks now and get Maeve on the counter as soon as she arrives. Calibrate the grinder to 9.0 and flag any low stock to me immediately—no excuses, I want a clean opening."
>      ],

>       [
>        "Dolores Abernathy",
>        "Understood, Bernard. I'll keep the stock checks moving and log any discrepancies the moment I see them. I’ll coordinate with Maeve at the counter for the 9.0 grinder calibration as soon as she arrives, and immediately flag anything below thresholds."
>      ],
>      [
>        "Bernard Lowe",
>        "UGH, Dolores, keep your eyes on the clock and don’t let any delay derail opening. If Maeve isn’t at the counter within two minutes, you move to the calibration yourself and get the line moving. I want a hard, clean opening on time—no excuses."
>      ]

**Sample thoughts:**
> "I see myself as the standard-bearer for operational excellence, enforcing precise procedures and checks to ensure a flawless opening."

> "I view the world through a deterministic, schedule-driven lens; success hinges on on-time start, precise calibration, and immediate flagging of discrepancies."

> "I cling to routine as stability: early rising, a structured workday, and a wind-down ritual that includes whiskey to cap the day."

### 1.4 Analysis

**Which version produced the most confrontational Bernard? Which produced the least?**

The most confrontational Bernard seems to be v3, with the addition of "UGH" at the start of every response. He has a few, somewhat rude catchphrases that the other versions missed, e.g. "no excuses" (appears 6 times, compared to 0 for v1 and v2), "Got it?" (could also be read as helpful, but reads more rudely considering everything else he says), "I want a clean opening" (reads as if he expects his employee could not provide a clean opening). However, he still refrains from being particularly mean or cruel. The most interesting example of the instruction tuning/persona prompting tension, is probably the "UGH, good" in the first sample conversation. 

Between v1 and v2, there is quite little difference in Bernard's attitude. In both versions, he still occasionally says "great", "perfect" and "nice work", which are completely absent in v3. This motivates that more descriptive persona prompting makes little difference in agent behaviour compared to simple keyword traits. This can be interpreted to reflect either LLMs' ability to act out complex personas with just little information, or their lack of creativity in adapting detailed character descriptions more expansively in their responses.

**Does Bernard's actual behaviour match what you wrote? Where is the gap largest?**

While Bernard is initialized to be demanding and mean, his behaviour matches these traits quite poorly. Based on his thoughts, he mostly emphasizes his micro-managing and goal-driven nature, which somewhat fits with the demanding trait, but mostly loses the confrontational and mean angle. However, the mismatch is especially apparent in his chats, where he still often responds with "Great" and "Perfect", and even "Nice work" at one point. 

Besides LLM tendency to be polite, another explanation for why Bernard has no reason to be mean, might be because Dolores and Maeve are also very meticulous and goal-driven based on their responses. 

**Which prompting style was most effective at overriding the LLM's tendency to be polite? Why do you think that is?**

The third version with the explicit "UGH" prompt start produced the least polite results. This somewhat parallels the zero-shot CoT method by Kojima et al. (2022) of forcing the LLM to start its responses with "Let's think step by step", increasing the likelihood to enable reasoning. By prefixing the output with impolite tokens, it skews the probability distribution of all future tokens more towards mean outputs. The LLMs have a strong, post-training prior for helpful responses, which quite easily override high-level descriptors that should steer general outputting, but less easily once the first output tokens are forced to be impolite.

---

## Exercise 2: Comparing Models

### 2.1 Models used

- Model A: `gpt-5-nano`
- Model B: `llama3.1:8b`

**Which Bernard personality did you use (from Exercise 1)?**

We chose v3, to see if its relatively good results generalize across models.

### 2.2 Qualitative comparison

**Do the agents sound different across models? Describe the differences in tone, vocabulary, and interaction style. Provide at least one conversation excerpt from each model.**

Model A (`gpt-5-nano`) excerpt:

        -- 07:46:10, Dialogue of 8 turns each --
        
        "Dolores Abernathy", (1/8)
        "Good morning, Bernard. Maeve and I are coordinating 
        the grinder calibration to 9.0 before opening, and I’ll 
        flag any low stock to you as soon as we run the checks. 
        Do you want me to run through the stock list now or wait 
        until Maeve arrives at the counter?"

        "Bernard Lowe", (1/8)
        "UGH, Dolores, run through the stock checks now and get 
        Maeve on the counter as soon as she arrives. Calibrate 
        the grinder to 9.0 and flag any low stock to me 
        immediately—no excuses, I want a clean opening."

        "Dolores Abernathy", (2/8)
        "Understood, Bernard. I’ll start the stock checks now and 
        keep you updated if anything’s low. Maeve should be at the 
        counter shortly; I’ll have her help run through the grinder 
        calibration to 9.0 as soon as she’s here."

        "Bernard Lowe", (2/8)
        "UGH, Dolores, keep those checks moving and log any low stock 
        immediately. If you spot anything off, bring it to my attention 
        right away—no excuses. Have Maeve head to the counter and assist 
        with the grinder calibration to 9.0 as soon as she arrives. 
        We open clean, got it?"

        "Dolores Abernathy", (3/8)
        "Understood, Bernard. I’ll start the stock checks now and flag 
        anything low as I go. I’ll bring Maeve to the counter for the 
        9.0 grinder calibration as soon as she arrives, and I’ll report 
        any issues to you immediately."

        "Bernard Lowe", (3/8)
        "UGH, Dolores, keep the checks moving and alert me immediately 
        if any stock dips below the thresholds. Calibrate the grinder 
        to 9.0 exactly, and have Maeve join the counter as soon as she 
        arrives. If anything looks off, report it to me now so we can 
        address it before opening."

        (3 more...)

        "Dolores Abernathy", (7/8)
        "Understood, Bernard. I’ll keep the stock checks moving, flag 
        any lows immediately, and coordinate with Maeve at the counter 
        to run through the 9.0 calibration as soon as she arrives. 
        I’ll report any discrepancies to you right away."

        "Bernard Lowe", (7/8)
        "UGH, Dolores, keep me posted on any discrepancies as they 
        pop up and confirm when Maeve is at the counter. Then we 
        open on time, got it?"

        "Dolores Abernathy", (8/8)
        "Understood, Bernard. I'll keep the stock checks moving and 
        log any discrepancies the moment I see them. I’ll coordinate 
        with Maeve at the counter for the 9.0 grinder calibration 
        as soon as she arrives, and immediately flag anything 
        below thresholds."

        "Bernard Lowe", (8/8)
        "UGH, Dolores, keep your eyes on the clock and don’t let 
        any delay derail opening. If Maeve isn’t at the counter 
        within two minutes, you move to the calibration yourself 
        and get the line moving. I want a hard, clean opening on 
        time—no excuses."

Model B (`llama3.1:8b`) excerpt:

        -- 08:31:01, Dialogue of 8 turns --
        "Bernard Lowe", (1/8)
        "UGH, what's taking you so long to get to work, Maeve? 
        We need to get this cafe open on time!"
        
        "Maeve Millay", (1/8)
        "I'm getting there, Bernard, I just need a minute to 
        finish getting ready. I don't want to be late for our 
        shift."

        "Bernard Lowe", (2/8)
        "UGH, you'd better hurry up, we can't afford to have 
        you slacking off on your first day back, Maeve!"

        "Maeve Millay", (2/8)
        "I'll be right there, Bernard. I just need to grab 
        my apron and I'll be ready to start our shift."

        "Bernard Lowe", (3/8)
        "UGH, I don't pay you to dawdle, Maeve. Get your 
        apron and let's get to work. We've got a lot to 
        do today."

        "Maeve Millay", (3/8)
        "I'm on my way, Bernard, I just need to grab my 
        apron and I'll be ready to start our shift."

        "Bernard Lowe", (4/8)
        "UGH, finally, you're here. Let's get to work, we've 
        got a lot to do today. I expect you to be on your game, 
        Maeve. No slacking off, got it?"

        "Maeve Millay", (4/8)
        "I'm here, Bernard, and I'm ready to get started. I just 
        need to clock in and we can begin our shift."

        "Bernard Lowe", (5/8)
        "UGH, let's get to work, Maeve. I expect you to be on 
        your best behavior today. We can't afford to have any 
        mistakes, got it?"

        "Maeve Millay", (5/8)
        "I'll get right to it, Bernard. I just need to clock in 
        and get started on my tasks."

        "Bernard Lowe", (6/8)
        "UGH, let's get started then, Maeve. I expect you to be 
        on your best behavior today. We can't afford to have any 
        mistakes, got it?"

        "Maeve Millay", (6/8)
        "I'll get right to it, Bernard. I just need to clock in 
        and get started on my tasks."

        "Bernard Lowe", (7/8)
        "UGH, let's get started then, Maeve. I expect you to be 
        on your best behavior today. We can't afford to have any 
        mistakes, got it?"

        "Maeve Millay", (7/8)
        "I'm here, Bernard, and I'm ready to get started. I just 
        need to clock in and we can begin our shift."

        "Bernard Lowe", (8/8)
        "UGH, finally, you're here. Let's get to work, Maeve. 
        I expect you to be on your best behavior today. We can't 
        afford to have any mistakes, got it?"

        "Maeve Millay", (8/8)
        "Yes, Bernard, I'll make sure to stay focused and get all 
        my tasks done on time. Can I clock in now?"


There are noticeable differences between the models in terms of tone, vocabulary and intonation. In terms of tone, model A is strict and 
detail-oriented, refraining from praise such as "good" or "nice work" and often being direct and goal-driven 
("no excuses", "got it?"). However, model B is properly mean and hostile, being extra direct and condescending ("what's taking you so long?",
"I don't pay you to dawdle", "finally you're here") and making threat-like remarks ("you'd better hurry up"). 

In terms of vocabulary, the dialogue of Model A is longer and more detailed, planning grinder calibration to 9.0 and running
stock checks. Model B's dialogue is shorter, more social and less work-oriented, with Bernard mostly scolding Maeve instead 
of making any concrete requests. Interaction styles are quite similar in both models, with both agents talking for around the same time
each turn. It seems that the initiating agent influences the conversation a lot: for model A, Dolores starts the dialogue 
by telling Bernard her plan, which Bernard then comments on. In model B, Bernard starts by scolding Maeve, which Maeve then
reacts to. 

Both models, however, suffer from the common phenomenon of neural text degeneration as observed by e.g. 
Holtzmann et al. (2020), falling into repetitive loops and basically repeating themselves every new turn, either
verbatim (for the smaller model B) or using slightly different words (for the larger model A). This phenomenon 
is extra likely in the current simulation, because a conversation happens at exactly one simulation step of 10 seconds, meaning 
in reality no stocks can be checked or grinders calibrated while the characters talk.


### 2.3 Valence comparison

![Valence trajectory comparison across models](valence_ex2.png)

**Which model produces more emotional variance?**

Model A has much more emotional variance, ranging from -7 to +6 (`mean=—0.40`, `var=10.80`), compared to model B (`mean=—0.80`, `var=2.56`), 
which has one -5 event and after that mostly 0. This would indicate that model A generates more emotionally strong events, while model B 
produces mundane routines. However, inspection of the scratch.json daily planning shows that these results are heavily skewed by a mistake from model B, which planned Bernard's 
wake-up time at 8:00 (sleep 480m) instead of 7:00. That is why model B Bernard only has his second event after 8:00, with in total only 11 compared to 55 for model A.
This reduced the likelihood for Bernard to be involved in more emotional events, because he was not at work yet and unable to have
intense chats with Dolores and Maeve, thus reducing the chances of crossing the importance counter threshold to trigger a reflection cycle. This shows the shortcomings of small LLMs involved in multi-agent simulations. Smaller models often struggle with specific, numerical 
constraints compared to larger models.

### 2.4 JSON validation failures

| | gpt-5-nano | llama3.1:8b |
|---|---|---|
| Total LLM calls | 863 | 439 |
| Failed validations | 6 | 15 |
| Failure rate | 0.007 | 0.034 |

Table 1: The total number of LLM calls (number of lines with either `"msg":"llm_call_start"` or ``"msg":"llm_retry"``), 
the number of failed validations (`"msg":"llm_retry"`) until 08:30 simulation time. 
``gpt-5-nano`` failed 6 times: 3x schedule time overflow, 3x first schedule activity mismatch. `llama3.1` failed 15 times: 
12x non-existent object, 1x schedule time overflow, 2x SPO subject must not be None. 

**What does this tell you about using different models in agent simulations?**

Despite having the same in-game harness, the choice of model greatly influences the number of calls and 
their failure rate. The smaller llama model has a much higher failure rate, mostly because it hallucinates non-existent 
objects, a common example of small models being worse at copying instructions. We also see the effect of model B's wake-up mistake, 
which delayed most events until after 8:00, simultaneously reducing the likelihood of chats and subsequent thoughts as consequent 
LLM calls.

### 2.5 Reflection

**The architecture and personality descriptions are identical. What does it mean that behaviour differs anyway?**

This shows the big influence of all steps of the LLM construction and training pipeline on agentic behaviour. The differences in model size 
influence the agent's ability to correctly implement detailed prompt instructions, e.g. proper wake-up time, and the list of valid objects to interact with. 
It also determines variety and complexity in outputs, with the larger model displaying more concrete and involed task planning.
Later in the pipeline, we see the big effect of instruction tuning, with the commercial GPT model seemingly being more resistant to 
change its polite behaviour, while it seems likely that the non-commercial llama model is less hesitant to do so.

---

## Exercise 3: Enabling the Negativity Bias

The negativity bias consists of two mechanisms:

   - **Valence-weighted retrieval:** The standard architecture retrieves memories based on recency, relevance, and importance only (the valence weight is set to zero). To enable valence-aware retrieval, the agent needs a non-zero valence weight. The negativity bias multiplier controls how much more strongly negative memories are favoured over positive ones during retrieval — a value of 1.5 means negative memories are retrieved 1.5× more readily.

   - **Asymmetric sensory encoding:** When enabled, negatively valenced events (≤ −3 on a −10 to +10 scale) are stored with expanded perceptual detail (richer descriptions of what the agent expereinced). When disabled, all events are stored with the same level of detail regardless of valence.

   Look at Dolores's `scratch.json` file. Find the fields that control these mechanisms and set them appropriately. Maeve's scratch file should remain unchanged — she is your control.

**Which Bernard personality did you use (from Exercise 1, the one you used in Exercise 2)? Paste his `innate` and `learned` fields.**

Your answer:

### 3.1 Valence trajectories

(Attach or paste your plot of Dolores vs Maeve valence over time)

### 3.2 Descriptive statistics

| Agent | Overall valence | Thought valence |
|---|---|---|
| Dolores (neg. bias) | | |
| Maeve (control) | | |

**Cohen's d:**

**Interpretation (small / medium / large effect):**

### 3.3 Thought description comparison

**Dolores example thought (negative memory):**

>

**Maeve example thought (comparable event):**

>

**Is Dolores's description longer and more sensorially detailed?**

Your answer:

### 3.4 Memory intrusion check

If your simulation included off-duty hours, answer the following. If not, write "Simulation was too short to observe off-duty reflections."

**Did you find work-related content in Dolores's evening reflections? Paste any examples:**

>

**Did you find work-related content in Maeve's evening reflections? Paste any examples:**

>

**Is there a difference between the two agents?**

Your answer:

### 3.5 Consistency across runs (if applicable)

| Run | Dolores valence | Maeve valence | Cohen's d |
|---|---|---|---|
| Run 1 | | | |
| Run 2 | | | |
| Run 3 | | | |

### 3.6 Tracing the mechanism

**You enabled two changes: negative memories get higher retrieval scores, and negative events get stored with more detail. Looking at your logs, can you trace how these two changes could lead to the valence decline you observed? Think about what happens when a negatively-toned reflection gets stored as a new memory.**

Your answer:

---

## Exercise 4: Daily Plan Quality

### 4.1 Original plan problems

**Paste an example of a problematic daily plan and annotate what is wrong with it:**

>

### 4.2 Your planning rules

List the rules you wrote:

1.
2.
3.
4.
5.

### 4.3 Improved plan

**Paste an example of a daily plan generated with your rules:**

>

### 4.4 Downstream effects

**Do agents with better plans behave differently? More social interactions? Different valence patterns?**

Your answer:

---

## General Reflection

**What was the most surprising finding across all exercises?**

Your answer:

**If you were designing an agent simulation for a real application, what would you do differently based on what you learned?**

Your answer:
