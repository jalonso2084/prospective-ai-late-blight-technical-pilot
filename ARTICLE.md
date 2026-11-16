# Can AI Recognize Important Research in Real Time? Lessons from a Technical Pilot in Potato Late Blight

A few months ago, I came across a post by Alberto Rossi about an experiment at Georgetown University built around a simple question:

**Can AI recognize important research in real time?**

The idea was to let a frontier AI model read new economics and finance papers as they appeared, evaluate them, and freeze those assessments before the academic community had reached its own verdict. Then, years later, the forecasts could be compared with what actually happened.

I found the idea fascinating, and I started wondering what would happen if I tried something similar in a very different scientific field: potato late blight.

The question I wanted to explore was essentially the same: **Can a frontier AI model recognize important potato late blight research before we know that it is important?**

Not after the citations arrive, not after a paper is discussed at conferences, and not after other researchers start building on it, but before all that happens.

At first, the design seemed straightforward. A new paper appears, the AI reads it, the AI makes a judgment, I freeze that judgment, and three years later I compare the forecast with what actually happened.

Before doing that with genuinely prospective papers, however, I decided to run a technical pilot. That decision turned out to be important, because the difficult part was not simply asking AI to evaluate science. It was defining exactly what would count as a valid measurement.

One of the first problems was deciding when the clock should start. A scientific contribution may first appear as a preprint, then as an accepted manuscript, then as a publisher version, sometimes with supplementary files appearing later. So the publication date is not necessarily the real starting line.

I needed something more precise, which I called **scientific t0**: the earliest verified moment when a substantively complete scientific version became publicly available. If the experiment is supposed to be prospective, I need to know exactly what scientific information existed when the forecast was made.

A second problem was versioning. The same scientific contribution may exist as several PDFs or versions, so treating each file as a separate paper could mean counting the same science more than once. I therefore started working with **Version Families**, where the unit of the study is the scientific contribution rather than the individual PDF.

Then came another problem: published does not necessarily mean ready to evaluate. Some papers were technically public but still depended on supplementary tables, spreadsheets, appendices, or methodological files that were necessary to understand the science fairly.

For each paper, I therefore prepared a **Controlled Evaluation Document**, or CED. The purpose was to preserve the scientific content while removing avoidable signals that might influence the model for reasons unrelated to the science, such as author names, affiliations, journal identity, DOI information, and prestige signals when they were not scientifically necessary.

The methods, results, figures, tables, and relevant supplementary information remained.

This is not perfect blinding. I cannot prove that a frontier model has never encountered a paper or related information during training, but I can control what I explicitly give it at evaluation time. That distinction matters.

After all that preparation, I finally ran the technical pilot.

Seven potato late blight papers were evaluated with **GPT-5.6 Sol**, using a frozen evaluation procedure. Four of those papers had been selected in advance for an independent test-retest evaluation, before I saw any results.

That gave me seven primary evaluations, four independent retests, and eleven valid model runs. There were also some invalid or interrupted attempts, but those were documented and excluded rather than quietly repaired or counted as valid evaluations.

For each paper, the model scored four present-paper characteristics on a **1-to-4 ordinal scale**: scientific quality, methodological rigor, strength of evidence, and perceived novelty. It also made 36-month forecasts for scientific recognition, epidemiological consequence, and operational uptake.

The main outcome is **substantive scientific recognition within 36 months**. I do not want to treat recognition and importance as exactly the same thing. A paper may receive serious scientific attention because other researchers validate it, extend it, build on it, or even produce an important refutation of it. That would still count as substantive scientific recognition, even if the original paper ultimately turned out to be wrong.

So the 36-month outcome is not a final verdict on whether a paper was historically important. It is an operational horizon that allows the prospective experiment to be tested within a defined period.

The other two outcomes are secondary. They make sense in a field like potato late blight, where research may alter epidemiological understanding or enter agricultural practice without necessarily becoming highly visible in the academic literature.

The first interesting result of the pilot was that the scientific reading was fairly stable. Across the four repeated papers, there were sixteen score comparisons: four papers multiplied by four scientific dimensions. Eleven of the sixteen scores were exactly the same, which is 68.8%, and all sixteen were within one point of each other.

Those sixteen comparisons should not be treated as sixteen independent observations, because they come from only four papers. Still, for a technical pilot, the pattern was useful.

The probabilities, however, were less stable. For the four repeated papers, the differences between the first and second forecasts of scientific recognition were 10, 3, 3, and 15 percentage points. The average absolute difference was about 7.8 percentage points.

The most unstable part of the pilot was the decision about whether a forecast should be made at all. That forced me to distinguish three situations: **forecastable**, **not forecastable from the supplied evidence**, and **construct ambiguous**. Abstention is not necessarily a failure of the model. It is part of the measurement system, but the rules for abstention have to be defined carefully.

I also learned that I was not only testing an AI model. I was testing the platform around the model. The pilot produced wrong-model execution, safety blocks, a missing primary document, and minor copied-output artifacts. None of those problems had anything to do with whether the science was good or bad, but they mattered for the validity of the experiment.

At first, all this felt like infrastructure around the experiment. Eventually I realized that it **is part of the experiment**.

The technical pilot does not answer the original research question yet. It does not show that AI can recognize important potato late blight research, that the probabilities are calibrated, that AI is better than human reviewers, or that high-scoring papers will become influential. The seven pilot papers were used to test the measurement system, not to demonstrate predictive validity.

What the pilot did show is something more basic: I can build a system in which an AI judgment about scientific research is made early enough, under controlled enough conditions, and preserved well enough that several years later I should be able to compare it honestly with what happened.

Before the prospective phase begins, I still need to freeze who will judge the later outcomes and how that judgment will be made without being influenced by the original forecasts. I also need an independent way to establish that each frozen forecast existed before later outcomes were known; a cryptographic hash proves integrity, but not by itself the date of existence.

Once those final pieces are fixed, a new eligible potato late blight contribution can be evaluated under the frozen protocol and left untouched until the outcome window closes.

The original question was: **Can AI recognize important research in real time?**

After building this pilot, I think there is an earlier question that has to be answered first: **Can we design the experiment carefully enough that, three years from now, we will actually know whether it did?**

The experiment is not about asking an AI which papers matter. It is about recording that judgment early enough, cleanly enough, and transparently enough that the future can prove it right or wrong.
