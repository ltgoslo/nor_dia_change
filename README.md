# NorDiaChange
_NorDiaChange_ is a manually annotated dataset of diachronic semantic change in Norwegian. It is described in full in the following paper:

["NorDiaChange: Diachronic Semantic Change Dataset for Norwegian"](https://aclanthology.org/2022.lrec-1.274/) by Andrey Kutuzov, Samia Touileb, Petter Mæhlum, Tita Ranveig Enstad, Alexandra Wittemann. In Proceedings of LREC'2022.

_NorDiaChange_ contains two subsets, with 40 annotated words in each:
- **[Subset 1](https://github.com/ltgoslo/nor_dia_change/tree/main/subset1)**, changes when comparing 1929-1965 to 1970-2013
- **[Subset 2](https://github.com/ltgoslo/nor_dia_change/tree/main/subset2)**, changes when comparing 1980-1990 to 2012-2019

The respective `subset1` and `subset2` directories contain raw annotation data and inferred diachronic word usage graphs (DWUGs).
Final descriptive statistics including change scores for the annotated words can be found in the `stats` subdirectory.

In the post-annotation reconciliations, three words in each subset were jointly marked as "questionable".
It does not mean that their annotations are wrong, just that they do not fully conform to the intuition of the native speakers.
You are free to either use these words or not.

In the `subset1_clean.tsv` and `subset2_clean.tsv` files, we provide the "cleaned" versions of both subsets with the "questionable" words removed.
This yields 37 annotated words in each subset, sorted by their graded change scores.
The `stats` subdirectories still contain full statistics, including "questionable" words.

The annotation was done using the [DUREL annotation tool](https://durel.ims.uni-stuttgart.de/).
The sentences for the annotation were sampled from the [NBDigital corpus](https://www.nb.no/sprakbanken/ressurskatalog/oai-nb-no-sbr-34/) and the [Norsk Aviskorpus](https://www.nb.no/sprakbanken/ressurskatalog/oai-nb-no-sbr-4/).
Both corpora are publicly avaible for downloading.

[Annotators guidelines](https://github.com/ltgoslo/nor_dia_change/blob/main/guidelines.md)

_NorDiaChange_ is published under the [Creative Commons Attribution license](https://creativecommons.org/licenses/by/4.0/).


## Acknowledgements
The annotation of _NorDiaChange_ was kindly funded by the [Teksthub](https://www.uio.no/tjenester/it/forskning/kompetansehuber/teksthub/) initiative at the University of Oslo.

We thank the three annotators Helle Bollingmo, Tita Ranveig Enstad, and Alexandra Wittemann for all their hard work and contributions. 
A special thanks to Ellisiv Gulnes Heien who provided us with some of the target words.
