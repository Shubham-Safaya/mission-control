# Week 01: Nobody Knows Who Their Customer Is (And What To Do About It)

**Status: FULL DRAFT — polish and publish**

I have spent years building customer identity systems inside one of the largest retail data environments in the world, and I want to start this series with the most useful uncomfortable truth in the field: nobody actually knows who their customer is. Not completely, not continuously, and not with the confidence their dashboards imply.

This is not a failure of any one company. It is the structural condition of customer data, and understanding why is the foundation for everything else I will write in this series.

## The identifier is not the person

Every customer data system rests on identifiers: emails, phone numbers, device IDs, loyalty numbers, payment tokens. The founding fiction of the industry is that these identifiers map cleanly to human beings. They do not, and the ways they fail are consistent enough to catalog.

Emails are shared by families, split between work and personal, abandoned and reborn. In every large customer file I have examined, a meaningful fraction of email addresses behave like group accounts, because they are. Phone numbers get recycled by carriers and handed to strangers. Devices are shared by households. Loyalty cards get borrowed at checkout by the cousin who forgot theirs. Payment cards belong to one person and feed a family of five.

Each identifier is not a key. It is a claim, and claims require corroboration. The entire discipline of identity resolution is the machinery of corroboration: deciding, with evidence and stated confidence, that a set of claims describes one person or one household.

## Fragmentation and collision, the two failure modes

When corroboration fails, it fails in exactly two directions.

Fragmentation: one person appears as several. The customer with four emails is four customers. Your lifetime value model undercounts her by 75 percent, your frequency cap treats her as four strangers and shows her the same ad twenty times, and your churn model panics about three of her fragments while the real person shops happily on.

Collision: several people appear as one. Two strangers merged into a single profile see each other's recommendations, receive each other's offers, and in the worst case surface in each other's privacy disclosures. Fragmentation wastes money quietly. Collision creates incidents loudly. Every threshold in a matching system is a choice about which of these failures you would rather have more of.

## Why this stays broken

Three forces keep the problem alive no matter how good the tooling gets.

People change. Roughly one in ten Americans moves in a year. People marry, divorce, change names, swap phones, abandon inboxes. A graph that is accurate in January degrades by December with zero code changes, because the world it describes has churned underneath it.

Systems multiply. Every acquisition, replatform, and regional stack mints its own customer keys. The average large enterprise does not have an identity problem; it has a portfolio of identity problems with different owners.

Incentives blur. Match rates sell software, so the industry reports recall and whispers precision. Bigger profile counts win earnings calls, so deduplication is nobody's favorite project. Honesty about identity has historically been priced like a luxury.

## What to do about it

The response is not despair and it is not a vendor purchase. It is operating discipline, and it fits in five commitments.

Treat identity as a capability with error budgets, not a project with an end date. Set target precision and split rates, measure them against a maintained truth set, and staff the maintenance like you staff uptime.

Make every merge explainable. When two records become one, the system should record which rule fired, which fields agreed, and what score was earned. This is the difference between an audit and an archaeology dig.

Keep a truth set, even a small one. A few thousand human-verified decisions calibrate everything, and they are the only data in the stack where you know the answer.

Separate the views. Person-level for personalization, household-level for measurement, conservative thresholds for anything privacy-adjacent. One graph, many confidence cuts, each owned by whoever bears its errors.

And write down the why behind every rule, because the system will outlive everyone's memory of the reasoning.

Nobody knows who their customer is. The companies that win are simply honest about the uncertainty, and they engineer for it on purpose.
