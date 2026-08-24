import argparse
from mcp.server.fastmcp import FastMCP
from core.excel_import import import_sca_workbook
from core.model import build_human_assumptions
from core.events import default_events
from core.risk_config import default_correlations, default_schedule_risks
from core.mcp_inbox import save_assessment

p=argparse.ArgumentParser()
p.add_argument("--workbook",required=True)
p.add_argument("--host",default="0.0.0.0")
p.add_argument("--port",type=int,default=8765)
a=p.parse_args()
data=import_sca_workbook(a.workbook)
mcp=FastMCP("SCA Cost Risk",host=a.host,port=a.port)

@mcp.tool()
def get_products()->list[str]:
    return data.products

@mcp.tool()
def get_regions()->dict:
    return data.plants_by_region

@mcp.tool()
def get_bom(product:str)->list[dict]:
    return data.bom[data.bom["product"]==product].to_dict(orient="records")

@mcp.tool()
def get_production_context(region:str,plant:str="All")->dict:
    oh=data.overheads[data.overheads["region"].astype(str)==region]
    exact=oh[oh["plant"].astype(str)==plant]
    if not exact.empty: oh=exact
    prod=data.production_source[data.production_source["region"].astype(str)==region]
    if plant!="All":
        exactp=prod[prod["plant"].astype(str)==plant]
        if not exactp.empty: prod=exactp
    return {"overheads":oh.to_dict(orient="records"),"production_source":prod.to_dict(orient="records")}

@mcp.tool()
def get_human_risk_configuration(region:str)->dict:
    h,_=build_human_assumptions(region)
    e=default_events(region)
    c=default_correlations(h.driver_id.tolist())
    s=default_schedule_risks(region)
    return {"drivers":h.to_dict(orient="records"),"events":e.to_dict(orient="records"),
            "correlations":c.to_dict(orient="records"),"schedule_risks":s.to_dict(orient="records")}

@mcp.tool()
def submit_ai_assessment(assessment: dict)->dict:
    path=save_assessment(assessment)
    return {"saved":True,"path":path,"assessment_id":assessment.get("assessment_id")}

if __name__=="__main__":
    mcp.run(transport="streamable-http")
