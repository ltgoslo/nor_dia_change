# Annotation Guidelines for Diachronic Usage Relatedness annotation in Norwegian

(loosely based on "[DWUG: A large Resource of Diachronic Word Usage Graphs in Four Languages](https://arxiv.org/abs/2104.08540)")

## Introduction

Your task is to rate the semantic relatedness between two uses of a word. For instance, presented with a sentence pair as in (0), you are asked to rate the
semantic relatedness between the two uses of _ris_ in (a) and (b):

(0a) I den islandske debatten gis det ros og **ris** til systemet.

(0b) Da krigen brøt ut i .1807, var briggen på hjemreise fra Middelhavet, låstet med sukker, **ris** og bomull.

## Task structure

You are provided with the [annotation interface](https://durel.ims.uni-stuttgart.de/).
Each annotation instance corresponds to one sentence pair. For each such pair, you have the columns
named `Sentence 1` and `Sentence 2`, illustrating two uses of the same word and
their contexts. The target word is marked in bold font in both contexts. Your task is
to rate, for these pairs of sentences, how related in meaning the two uses of the target
word in the two sentences are.

Since language is often ambiguous, please read each sentence separately first, and
decide upon the most plausible meaning of the target word in each sentence BEFORE
comparing the two uses.

## The judgment scale

The scale that you will be using for your judgments ranges
from **1** (the two uses of the word have completely unrelated meanings) to **4** (the two
uses of the word have identical meanings).
This four-point scale is shown in detail below:

* 4: Identical
* 3: Closely Related
* 2: Distantly Related
* 1: Unrelated
* 0: Cannot decide


Please try to ignore differences between the uses that do not impact their meaning.
For example, _spiser_ and _spiste_ can express the same meaning, even though one is in present
tense, and the other is in past tense. Also, distinctions between singular and plural
(as in _treet_ vs. _trærne_) are typically irrelevant for the meanings.
Note that there are no right or wrong answers in this task, so please provide your
subjective opinion. However, please try to be consistent in your judgments.

## Annotation examples

We now zoom into the individual annotation instances and provide rating examples, in order to illustrate the different degrees of relatedness
that you may find in the judgment task.
Note again that these are just examples and you should provide your own subjective opinion.

(1a) Men så blev det vekk igjen. Da opdaget jeg at jeg hadde glemt å ta kapslen av foran den ytre **linsen** på kikkerten!

(1b) Videre omfatter bransjen produksjon av fotografisk materiell, fotokopieringsutstyr, **linser** og optiske instrumenter.

The two instances of **linse(n/r)** in this example are judged identical in meaning (rating: **4**),
because both uses refer to a lens as a transmissive optical device.

In the following two sentences, the word **bit** also have the identical meaning of ''piece'' (rating **4**):

(2a) Det eneste som trøstet meg, var at jeg slapp å se Carolus i hvit saus i et lokkefat på middagsbordet. Ja, for aldri — aldri i verden hadde jeg smakt en **bit** av Carolus! SLUTNING Kjære dere!

(2b) Den første **bit** var besk, og den annen var besk. Men hun svelget allikevel og tok den tredje. «Giv med deg,» hvisket det. Og Hilma Sofie gav med seg. Og innen hun sluttet, syntes henne smaken så søt som søteste vin.

A rating of **1** is used for two uses of a word that are completely unrelated in their
meaning, as it is the case for **rev** in the next example.

(3a) Den kom i drift, sier du?» «Ja, den dreiv nedover mot et **rev** utfor nærmeste pynt.

(3b) Etter tillatelse fra politiet kan det brukes gift til fangst av ulv, jerv og **rev** i Uleåborgs og Lapplands len. Slik tillatelse gis for én fangstsesong av gangen.

Here, **rev** in (3a) refers to bank of sand, mountains or corals that do not protrude from the sea, while **rev** in (2b) refers to the animal (fox).

Another example of semantically unrelated meanings is the meaning of **ris** in the following examples:

(4a) Sidene pagineres i hver bok fra 1—500: Papiret koster pr. **ris** å 500 ark kr. 32,80, hvorpå beregnes 20 pet. fortjeneste.

(4b) I saltvann produseres primært grønn tang til en samlet verdi av $ 440 mill. (1973). Denne tangen spises til **ris** som en slags grønnsak.

In (4a), **ris** refers to a unit of quantity of paper, while in (4b) it refers to rice.

Finally, there is also the option for you to provide the `Cannot decide` judgment (rating: **0**).
Please use this rating only if absolutely necessary, when you are unable to
make a decision as to the degree of relatedness in meaning between the two bold
words.
Please provide a comment for why you cannot decide about this pair of uses.

## Historical language data

The sentences provided for the annotation task were gathered from historical corpora.
Sentences may occur more than once in your annotation instances.
As language changes over time, words might be used differently from what you are
familiar with.

If you are unsure about the meaning of a word or construction in a
sentence, try to infer it from the meaning of the context or consult with a dictionary.
The sentences may be very short or very long and some may seem ungrammatical.
Also, words may be spelled in a different way than you are used to.
Try to ignore these issues; focus only on the meaning of the target words in their
contexts.

If you find that a sentence is too flawed to understand it, or the meaning of
the target word is ambiguous, or the two instances of the target word do not match
(i.e., they do not have the same lemma), please provide a comment to this effect.
