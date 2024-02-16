# Swedish Language Interesting Irregularities
This project is a diving into the topic of language patterns. It specifically focuses on the Swedish language, a North Germanic language spoken natively by millions of people predominantly in Sweden and in parts of Finland.

## Overview

Articles are a fundamental component of sentence structure, and their usage can reveal a lot about a language’s grammar rules and structure. 
In Swedish, nouns are divided into two grammatical genders - ‘en’ and ‘ett’, similar to ‘der’ and ‘die’ in German, or ‘le’ and ‘la’ in French. grammatical genders are pretty much unrelated to human genders or identity, therefore it is often believed the best way to learn such structures is to memorize them.
However, there are certain patterns and tendencies that can be observed. 
The primary objective of this project is to find patterns from a dataset containing 91869 Swedish words. The dataset encompass a wide range of words used in various contexts. 
This could provide valuable insights into the structure and usage of articles, contributing to the broader field of computational linguistics. These insights could be particularly useful for language learning applications, machine translation systems, and linguistic research.
A long(er!) goal of this project is not just about discovering patterns. It’s about understanding what these patterns mean and interpreting them in the context of the Swedish language.
<img src="https://github.com/Hirbod-JORFlint/Language-Analysis/blob/37354651a50452b4405371818d48e06aa711002f/Stage_2/Swedish/props/Pattern_mining_connections.jpeg"></img>

### Stats
statistical patterns in gender assignment of nouns in Swedish can be quite complex and are influenced by several factors(e.g. origins, frequency of usage, ...). 
Articles are directly related to the noun they precede, it might be possible to derive them from features of nouns.A brief explanation of what each column might represent:
	1.Substantiv: The noun itself.
	2.Singular obestämd: The indefinite singular form of the noun.
	3.Singular obestämd genitiv: The genitive case of the indefinite singular form of the noun.
	4.Singular bestämd: The definite singular form of the noun.
	5.Singular bestämd genitiv: The genitive case of the definite singular form of the noun.
	6.Plural obestämd: The indefinite plural form of the noun.
	7.Plural obestämd genitiv: The genitive case of the indefinite plural form of the noun.
	8.Plural bestämd: The definite plural form of the noun.
	9.Plural bestämd genitiv: The genitive case of the definite plural form of the noun.
	10.Articles: The article used with the noun (“en” or “ett”).
	11. Första/Initial Två/Tre Bokstäver: The first letter or first two/three letters of the indefinite/definite singular form of the noun. 
	12. Sista/Slutlig Två/Tre Bokstäver: The last letter or last two/three letters of the indefinite/definite singular form of the noun. 
	13. Vokalratio: The ratio of vowels in the indefinite/definite singular form of the noun.
	14. Ord Längd: The length of the indefinite/definite singular form of the noun.
	
#### Patterns

Of all words, 76 % are assigned with 'en' article. Some of the observed patterns can be seen in the following tables:
Table 1- one letter indicator
\begin{tabular}{l|ll}
\multicolumn{1}{l}{ rule } & article & proportion \\
\hline all & en & $76.0 \%$ \\
indefinite form of word starts with $s$ & en & $75.5 \%$ \\
indefinite form of word starts with $y$ & en & $73.4 \%$ \\
indefinite form of word starts with ä & en & $76.6 \%$ \\
indefinite form of word starts with c & en & $78.9 \%$ \\
indefinite form of word ends with $g$ & en & $89.7 \%$ \\
indefinite form of word ends with $e$ & en & $97.9 \%$ \\
indefinite form of word ends with $t$ & en & $83.6 \%$ \\
indefinite form of word starts with å & ett & $26.6 \%$ \\
indefinite form of word ends with $v$ & ett & $58.2 \%$ \\
indefinite form of word ends with $p$ & ett & $45.2 \%$ \\
indefinite form of word ends with $m$ & ett & $42.7 \%$
\end{tabular}

$$
\begin{aligned}
&\text { Table 2- two letter indicator }\\
&\begin{array}{l|ll}
\text { rule } & \text { article } & \text { proportion } \\
\hline \text { indefinite form of word starts with fo } & \text { en } & 75.0 \% \\
\text { indefinite form of word starts with pi } & \text { en } & 77.7 \% \\
\text { indefinite form of word starts with od } & \text { en } & 87.5 \% \\
\text { indefinite form of word starts with os } & \text { en } & 87.7 \% \\
\text { indefinite form of word ends with sa } & \text { en } & 100 \% \\
\text { indefinite form of word ends with sm } & \text { en } & 99.8 \% \\
\text { indefinite form of word ends with } \mathrm{ka} & \text { en } & 99.6 \% \\
\text { indefinite form of word starts with el } & \text { ett } & 26.6 \% \\
\text { indefinite form of word starts with hu } & \text { ett } & 28.0 \% \\
\text { indefinite form of word ends with um } & \text { ett } & 97.8 \% \\
\text { indefinite form of word ends with äd } & \text { ett } & 89.2 \%
\end{array}
\end{aligned}
$$

Due to continues nature of word length and Vokalratio, they were separated into 10 distinct intervals. Number of intervals can be changed in 'Arules.ipynb'.
All extracted rules are stored in 'rules.txt'. Further association can be generated through 'Arules.ipynb'. As an example:
{Obestämd Slutlig Två Bokstäver=ka, Obestämd Vokalratio=4} -> {Article=en}
{Obestämd Slutlig Två Bokstäver=ka, Obestämd Vokalratio=4}: This is the antecedent or the “if” part of the rule. It states that if the last two letters of the indefinite form of a word are “ka” and the ratio of vowels in the indefinite form is from group 4.
{Article=en}: This is the consequent or the “then” part of the rule. It states that then the article of the word is “en”.
conf: 1.000: This is the confidence of the rule. A confidence of 1.000 means that 100% of the time when the antecedent is true, the consequent is also true. In other words, every time the last two letters of the indefinite form of a word are “ka” and the ratio of vowels in the indefinite form is 4, the article of the word is “en”.
supp: 0.004: This is the support of the rule. It indicates how frequently the antecedent and consequent occur together in the dataset. A support of 0.004 means that 0.4% of all words in the dataset have “ka” as the last two letters in their indefinite form, a vowel ratio of 4 in the indefinite form, and use “en” as their article.
lift: 1.316: This is the lift of the rule. Lift measures how much more often the antecedent and consequent occur together than we would expect if they were statistically independent. A lift greater than 1, like 1.316, suggests that the antecedent and consequent are positively associated.
conv: 240355727.783: This is the conviction of the rule. Conviction compares the probability that the antecedent occurs without the consequent if they were dependent with the actual frequency of the antecedent without the consequent.

#### TODO

- Word Origin: Tracking word origins(i.e. loan words) might be helpful.
- Number of syllables: This might be a useful factor for prediction.
- compound words: It appears the article follows the last part of the such words, it might be worthwhile to check the structure.
- Plural form: It is a known fact that indefinite form of Swedish words can be categorized into 5 classes. Finding a pattern to these groups might be helpful to predict articles as well.
- Causality for Articles: Investigate if there’s a causal relationship between the structure of a word and its article. This could involve statistical tests or ml models.
- Phonetic Analysis: The phonetics of a word, such as its sounds or pronunciation, might influence the choice of article. A phonetic analysis could reveal interesting patterns.
- Influence of Dialects: Study the influence of different Swedish dialects on article usage. Dialects often have unique linguistic features.

##### Acknowledgements

I would like to express my appreciation to Jenny Myrdal, who provided invaluable insights into word genders and the idea of historical context of articles, which improved the aims of this project. 

