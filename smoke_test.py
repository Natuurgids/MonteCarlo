import sys
from core.excel_import import import_sca_workbook
from core.model import build_human_assumptions, driver_costs
from core.monte_carlo import run_simulation

if len(sys.argv) != 2:
    raise SystemExit("Usage: python smoke_test.py <path-to-SCA-xlsx>")

imp = import_sca_workbook(sys.argv[1])
assert len(imp.products) >= 1
assert len(imp.bom) >= 1
human, event = build_human_assumptions(imp.regions[0])
dc = driver_costs(imp.bom, imp.products[0])
summary, sensitivity, draws = run_simulation(dc, human, human, human, event, event, event, iterations=1000)
print("OK")
print("Products:", len(imp.products))
print("BOM rows:", len(imp.bom))
print("Regions:", len(imp.regions))
print(summary)
