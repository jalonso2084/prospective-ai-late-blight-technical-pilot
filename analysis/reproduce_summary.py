import csv
from pathlib import Path
p=Path(__file__).parents[1]/"data"/"pilot_results_reported.csv"
rows=list(csv.DictReader(p.open()))
prim={r['version_family_id']:r for r in rows if r['run_type']=='primary'}
ret={r['version_family_id']:r for r in rows if r['run_type']=='retest'}
dims=['scientific_quality','methodological_rigor','strength_of_evidence','perceived_novelty']
exact=0; within1=0; total=0
rec_diffs=[]
for vf in ['VF038','VF051','VF064','VF073']:
    for d in dims:
        a=int(prim[vf][d]); b=int(ret[vf][d]); total+=1
        exact += (a==b); within1 += (abs(a-b)<=1)
    rec_diffs.append(abs(float(prim[vf]['scientific_recognition_probability'])-float(ret[vf]['scientific_recognition_probability'])))
print(f"Exact ordinal agreement: {exact}/{total} = {100*exact/total:.2f}%")
print(f"Within ±1 ordinal point: {within1}/{total} = {100*within1/total:.2f}%")
print("Recognition absolute differences:", [round(x,2) for x in rec_diffs])
print(f"Mean absolute difference: {sum(rec_diffs)/len(rec_diffs):.4f} = {100*sum(rec_diffs)/len(rec_diffs):.2f} percentage points")
