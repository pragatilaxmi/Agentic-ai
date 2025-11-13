import sys, importlib, os
sys.path.insert(0, "src")
try:
    m = importlib.import_module("utils.gemini_client")
    print("import ok:", m.__name__)
    print("has call_gemini_rest:", hasattr(m, "call_gemini_rest"))
    print("has generate:", hasattr(m, "generate"))
    print("PY sees GEMINI_API_KEY set:", bool(os.getenv("GEMINI_API_KEY")))
    print("PY sees GEMINI_COMPLETION_ENDPOINT set:", bool(os.getenv("GEMINI_COMPLETION_ENDPOINT")))
except Exception as e:
    import traceback
    print("import failed:")
    traceback.print_exc()
