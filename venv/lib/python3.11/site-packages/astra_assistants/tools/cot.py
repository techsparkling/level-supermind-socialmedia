from typing import List

from openai import BaseModel
from pydantic import Field

from astra_assistants.tools.tool_interface import ToolInterface, ToolResult


class ChainOfThought(BaseModel):
    """
    Chain of Thought Tool / Function, this function provides some additional context  to help answer questions.
    It can be called multiple times to get better context. Continue to call it until the thought process is complete.
    Then use the context to answer the question.
    """
    thoughts: str = Field(..., description="Your current stream of consciousness step by step thoughts as you analyze this question.")
    doubts: List[str] = Field(..., description="Doubts that need to be answered to complete the thought, try to break down the question into at least 5 parts.")
    potential_answers: List[str] = Field(..., description="Options for answers that could be provided, may or may not be complete.")
    is_complete: bool = Field(..., description="Whether the thought process is complete. Only True if you are very sure of the answer by now.")

    class Config:
        schema_extra = {
            "example": {
                "thoughts": (
                    "Problem: Refactor the function to use list comprehension instead of a for loop"
                    "Step 1: Understand the problem, what is the function doing?"
                    "Step 2: What is list comprehension and how does it work?"
                    "Step 3: How can we refactor the function to use list comprehension?"
                    "Step 4: What are the benefits of using list comprehension?"
                    "Step 5: What are the potential downsides of using list comprehension?"
                    "Step 6: What are the potential edge cases we need to consider?"
                    "Step 7: How can we test the refactored function to ensure it works as expected?"
                ),
                "doubts": ["Understand the problem", "Understand list comprehension", "Refactor the function", "Benefits of list comprehension", "Downsides of list comprehension", "Edge cases", "Testing"],
                "potential_answer": "[x for x in range(10)]",
                "is_complete": False
            }
        }

    def to_string(self):
        return (
            f"Thoughts: {self.thoughts}\n"
            f"Doubts: {self.doubts}\n"
            f"Potential Answers: {self.potential_answers}\n"
            f"Is Complete: {self.is_complete}"
        )


# Define the chain-of-thought tool
class ChainOfThoughtTool(ToolInterface):
    def __init__(self):
        self.thought_process = []
        self.current_thought = None

    def set_initial_thought(self, thought: ChainOfThought):
        """Initialize the chain of thought."""
        self.current_thought = thought
        self.thought_process.append(thought)

    def call(self, cot: ChainOfThought):
        """Executes the chain of thought process until it's complete."""
        instructions = (
            f"## Context:\n"
            f"So far, we have thought about the problem a bunch and here's what we came up with:\n"
            f"{cot.to_string()}\n"
        )

        if cot.is_complete:
            instructions += f"## Instructions: now answer the question as completely as possible\n"
        else:
            instructions += f"## Instructions: use the Chain of Thought tool again to refine your thoughts.\n"

        print(f"providing instructions: \n{instructions}")
        return {'output': instructions, 'cot': cot, 'tool': self.__class__.__name__}