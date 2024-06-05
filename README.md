# l4-query

Extends the L4 ecosystem with capabilities for querying L4 programs --- or querying external information sources *with* L4 programs -- alongside more stochastic approaches like LLMs.

## Sketch of architecture / todos

In the simplest case ('function calling / evaluation'), this will require:

1. equipping L4 with metadata capabilities
2. a simple semantic parser (see next sub-section)

## Adding metadata capabilities to (a mini) L4

This is *experimental*, and should not be taken to be examples of current, valid L4.

Examples:

```Mini-L4
<DATA MODEL...>

EXPORT for llm-specification <comma sep names of preds/functions> 
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

```Mini-L4
"""
METADATA:
  description: "this function calculates how much an arbitrary life assured can claim for ..."
"""
GIVEN life assured IS A Life Assured
claimable amount =  if life assured is eligible for ....
                    then ...
                    else ...
```

## Semantic parser

The semantic parser will be something that uses stochastic methods like LLMs and potentially other NLP methods (e.g. embedding similarity).

The semantic parser will be given:

* a specification of the data model, translated from the L4 specification
* metadata for / a specification of each of the L4 predicates / functions we want to export and their parameters

The semantic parser will then use that to do the following:

1. Give us a structured specification of what the user wants to be done with the relevant L4 predicates / functions, if the user's query contains enough information for that.

    * One common thing that a user might want, of course, is 'function calling': Evaluate the relevant functions with (sanitized or validated versions of) inputs that the user supplies, or from other info sources.

    * But there are also other things a user might want to do with the exported L4 functions: e.g. figuring out what inputs must be given to get certain outputs. The underlying abductive reasoning would be done by a more classical / symbolic reasoner; where a LLM / NLP model comes in is in figuring out whether that's what the user wants, based on their unstructured query.

2. Figure out which of the exported predicates / functions are relevant to the user's query.

To put it another way, the semantic parser will generate, in a constrained way, what is in effect a simple query language.

```ebnf
<QUERY> ::= <CMD> <L4-FUNCTION-SPEC> <LIST UserInput>
<L4-FUNCTION-SPEC> ::= <L4-FunctionName>  // tentative!
<CMD> ::= 'EVAL'
```

And potentially in the future

```ebnf
<QUERY> ::= <CMD> <L4-FUNCTION-SPEC> <LIST UserInput>
<L4-FUNCTION-SPEC> ::= <L4-FunctionName>
<CMD> ::= 'EVAL' | 'ABDUCT'
```

In terms used by the LLM APIs: each variant of CMD will correspond to a 'tool', with parameters like which L4 function the user seems to be interested in.

## Inspiration / Further Reading

* [BlendSQL](https://github.com/parkervg/blendsql)
* [Reliable Natural Language Understanding with Large
Language Models and Answer Set Programming](https://arxiv.org/pdf/2302.03780)
* <https://www.honeycomb.io/blog/hard-stuff-nobody-talks-about-llm>
