def inject_context(compressed_text: str, task_role: str = "Expert Analyst"):
    return f"""
    SYSTEM ROLE: {task_role}
    TASK DATA: {compressed_text}
    INSTRUCTION: Execute the task using only the data provided above. 
    FORMAT: Provide a concise, structured response.
    """