# check_routes.py (robust)
import os, sys, inspect

# ensure src is importable
sys.path.insert(0, os.path.abspath("src"))

print("PYTHONPATH ->", sys.path[0])
print("Attempting to import module 'api.app' ...")

try:
    import api.app as api_app
except Exception as e:
    print("ERROR: failed to import module 'api.app':", e)
    raise SystemExit(1)

# Try to find any FastAPI instance inside module attributes
try:
    from fastapi import FastAPI
except Exception:
    print("WARNING: fastapi not importable in this environment. Install fastapi in venv.")
    raise SystemExit(1)

found = []
# Common case: module-level variable named 'app'
if hasattr(api_app, 'app') and isinstance(getattr(api_app, 'app'), FastAPI):
    found.append(('api.app:app', getattr(api_app, 'app')))

# As a fallback, inspect members of the module
if not found:
    for name, obj in inspect.getmembers(api_app):
        if isinstance(obj, FastAPI):
            found.append((f'api.app:{name}', obj))

if not found:
    print("No FastAPI app instance found in module 'api.app'.")
    print("Check that src/api/app.py defines a variable named 'app' which is a FastAPI() instance.")
    raise SystemExit(1)

# If we have an app, print routes
for varname, app in found:
    print(f"\nFound FastAPI app as '{varname}'. Listing routes:\n")
    for r in app.routes:
        methods = ",".join(sorted(m for m in (r.methods or set()) if m))
        print(f"{r.path} -> [{methods}]")
