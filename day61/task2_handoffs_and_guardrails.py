"""
Day 61 · Task 2: Handoffs and guardrails

Hand off between agents; add an input guardrail.

Complete every TODO, run the file, and tick this task on the tracker.
"""
from agents import Agent, GuardrailFunctionOutput, Runner, input_guardrail

billing = Agent(name="Billing", instructions="Answer billing questions.")
tech = Agent(name="Tech support", instructions="Answer technical questions.")
triage = Agent(name="Triage", instructions="Hand off to the right agent.", handoffs=[billing, tech])

# TODO: an input guardrail that blocks requests containing card numbers
# TODO: run 3 questions through triage and print which agent answered
