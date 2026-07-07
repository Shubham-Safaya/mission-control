# Week 03: I Built a Synthetic Population So I Could Stop Guessing

**Status: FULL DRAFT — polish and publish**

The hardest problem in identity resolution is not matching. It is grading. You can compute a match rate on production data, but you cannot compute precision, because you do not know the truth. Nobody labeled reality for you.

This is the quiet reason the industry argues in adjectives. Vendors claim high accuracy; buyers cannot verify; everyone settles for match rate, which is the recall half of a two-number story. After years of this, I did the only thing that produces truth you can ethically own: I manufactured it.

## The recipe

I generated a synthetic population of roughly one hundred thousand people using public Census distributions: age by sex, household size and structure, geography, income brackets. Statistically faithful at the aggregate level, entirely fabricated at the individual level. No real person, no licensed record, nothing to leak.

Each synthetic person got a persistent ID, a household assignment, and a set of identifiers with realistic imperfections: emails with plus-tags and typos, phones in mixed formats, names with nicknames, transliteration variants, and the occasional marriage-driven surname change. Each household got shared devices and a shared address rendered in multiple inconsistent styles, because that is what addresses do.

Then the crucial step: I fragmented the population into overlapping record sets, the way real enterprises hold customers across systems, and kept the answer key. Which records belong to which person is known, because I decided it.

## What the simulator caught

Running my own open-source matching engine against this population was humbling within the hour.

The engine over-merged young adults living with their parents: same surname, same address, close ages. Real systems make this mistake at scale and never know, because production has no answer key. My precision on that segment was visibly worse than the headline number, and the headline number was itself the average hiding it.

It under-matched women across surname changes, which I knew abstractly and had never quantified. The recall gap was large enough to matter for any lifecycle marketing use case, and it was invisible in aggregate metrics.

And transitive closure did what transitive closure does: one operationally-corrupted identifier, planted deliberately, assembled a mega-cluster with the enthusiasm of a conspiracy theorist. Frequency caps on identifier reuse fixed it, and the fix now exists because the simulator made the failure observable.

## Why this matters beyond my weekend

Every claim in the identity industry becomes testable the moment ground truth exists. A vendor pitch says 90 percent accuracy: run their matcher on a synthetic benchmark and read the actual precision curve. A threshold change is proposed: rerun the benchmark and watch which segments pay. A new normalizer ships: the answer key says instantly whether it helped.

The benchmark also travels. Because the population is synthetic, I can publish it, write about it, and demonstrate the full mechanics of identity resolution in public without a single privacy question. The machinery that commercial identity companies operate at scale on licensed data can be demonstrated honestly on manufactured people, and the demonstration is legally boring in the best way.

A flight simulator does not replace flying. It replaces crashing during training. Every identity team should keep one in the drawer, and no team should accept an accuracy claim from anyone who cannot show you theirs.
