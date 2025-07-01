from langchain.llms.base import LLM
from langchain.chains import LLMChain
from flask import Flask, render_template, request
from typing import ClassVar



class Qwen2LLM(LLM):
    ollama_url: ClassVar[str] = "http://localhost:11434/api/generate"
    model_name: ClassVar[str] = "qwen2"

    def _call(self, prompt: str, stop=None):
        import requests
        data = {"model": self.model_name, "prompt": prompt, "stream": False}
        try:
            r = requests.post(self.ollama_url, json=data)
            r.raise_for_status()
            return r.json()["response"].strip()
        except Exception as e:
            return f"Erreur Qwen2: {e}"

    @property
    def _llm_type(self):
        return "custom_qwen2"