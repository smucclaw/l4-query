# l4-query
Query language for blending L4 and LLM reasoning / using L4 in conjunction with more stochastic approaches.

# Sketch of architecture
[TODO]


# Adding metadata capabilities to (a mini) L4

(This is *experimental*, and should not be taken to be examples of current, valid L4.)

Examples:
```
<DATA MODEL...>

EXPORT for llm-specification <comma sep names of preds> 
// so, if one runs smtg like `make-llm-spec <filename>`, it will give you a 'function-calling' schema with each function / predicate in the export list as a 'tool', ordered by their (ascending) order in the export list

"""
METADATA:
  description: "this predicate tells us whether a person can buy a HDB"
  keyphrases: "is eligible for a HDB" | "qualifies for a HDB"
"""
GIVEN person IS A Person
DECIDE person is eligible for a HDB
IF person's age > 18
AND person is Singaporean
```

or if we are calculating things, e.g. how much we can claim:
```
"""
METADATA:
  description: "this function calculates how much an arbitrary life assured can claim for ..."
"""
GIVEN life assured IS A Life Assured
claimable amount =  if life assured is eligible for ....
                    then ...
                    else ...
```

# Inspiration / Further Reading

* [BlendSQL](https://github.com/parkervg/blendsql)
* [Reliable Natural Language Understanding with Large
Language Models and Answer Set Programming](https://arxiv.org/pdf/2302.03780)
* <https://www.honeycomb.io/blog/hard-stuff-nobody-talks-about-llm>

