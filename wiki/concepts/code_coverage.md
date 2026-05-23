## Definition
Code coverage is a measure used in software testing to describe the degree to which the source code of a program is executed when a particular test suite runs. It provides an indication of how thoroughly a program is tested by identifying which parts of the code have been executed and which have not.

## Context
Code coverage is an essential metric in software development and quality assurance as it helps developers identify untested parts of a codebase. High code coverage often correlates with a lower chance of undetected software bugs. Tools that measure code coverage can highlight areas of code that are not exercised by the existing test cases, prompting developers to write additional tests to improve coverage.

Recent advancements in large language models (LLMs) and datasets like UniTSyn have shown potential in enhancing code coverage by improving the accuracy of automated unit test generation. UniTSyn is a large-scale dataset that pairs unit tests with their corresponding functions across multiple programming languages, aiding LLMs in better inferring expected behaviors and verifying logic paths. By leveraging the Language Server Protocol (LSP), UniTSyn collects focal-test pairs without the need for per-project execution setups, thereby improving the test generation capabilities of LLMs and resulting in better code coverage.

## Related Concepts
- [[Unit Test]]
- [[Software Testing]]
- [[Large Language Models (LLMs)]]
- [[Unit Test Synthesis]]
- [[Language Server Protocol (LSP)]]
- [[Test Suite]]
- [[UniTSyn]]