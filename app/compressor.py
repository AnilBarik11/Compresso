from llmlingua import PromptCompressor

# Initialize the compressor
compressor = PromptCompressor(model_name="microsoft/llmlingua-2-xlm-roberta-large-meetingbank",use_llmlingua2=True,
    device_map="cpu")

def compress(text: str, rate: float = 0.4):
    result = compressor.compress_prompt(text, rate=rate)
    return result["compressed_prompt"]