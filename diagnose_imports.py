# diagnose_imports.py
import sys, os, traceback
sys.path.insert(0, os.path.abspath("src"))

modules = [
    "main",
    "src.main",
    "agents.research_agent",
    "agents.factcheck_agent",
    "agents.writing_agent",
    "vectorstore.chroma_store",
    "orchestrator.langgraph_orchestrator",
    "utils.gemini_client",
]

for m in modules:
    try:
        __import__(m)
        print(f"OK import: {m}")
    except Exception as e:
        print(f"FAILED import: {m}")
        traceback.print_exc()
