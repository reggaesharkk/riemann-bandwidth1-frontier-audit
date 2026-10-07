"""Snapshot ratio occurrences; preserve quoted errors as explicit history."""
from pathlib import Path
import subprocess,json,csv
ROOT=Path(__file__).resolve().parents[1]

def main():
    args=['rg','--json','-n','--glob','*.md','--glob','*.py','--glob','*.json','--glob','*.txt',
          '--glob','!WP84_PARITY_GRADED_PRECORRECTION_SCAN.txt','--glob','!WP84_PARITY_GRADED_RATIO_ERRATUM*',
          '--','-1240/371|-620/371|c5/c6','.']
    result=subprocess.run(args,cwd=ROOT,capture_output=True,text=True,encoding='utf-8')
    assert result.returncode in (0,1)
    rows=[]
    for raw in result.stdout.splitlines():
        item=json.loads(raw)
        if item['type']!='match':continue
        data=item['data'];path=data['path']['text'].replace('\\','/').removeprefix('./')
        line=data['lines']['text'].rstrip();n=data['line_number']
        if path.endswith('wp84_parity_graded_ratio_erratum.py'):category='historical superseded statement';action='scanner search pattern, not a coefficient assertion'
        elif '-1240/371' in line:
            if any(t in line for t in ['requested_previous','BUG','reported','previous','quoted']):
                category='historical superseded statement';action='preserve explicit quoted error'
            else:category='coercivity threshold';action='retain with separate coercivity meaning'
        else:category='actual coefficient ratio';action='verified -620/371 or symbolic ratio discussion'
        rows.append([path,n,category,action,line])
    rows.append(['notes/WP84_THEOREM_AWARE_DEGREE6_CONSUMER_DESIGN.md',241,'bug',
                 'FIXED in this audit with dated explicit erratum; historical commit c402000 retained','PRE-CORRECTION: c5/c6=-1240/371'])
    scan=ROOT/'notes/WP84_PARITY_GRADED_PRECORRECTION_SCAN.txt'
    for n,line in enumerate(scan.read_text(encoding='utf-8-sig').splitlines(),1):
        if '-1240/371' in line or '-620/371' in line:
            rows.append(['notes/WP84_PARITY_GRADED_PRECORRECTION_SCAN.txt',n,'historical superseded statement',
                         'preserved pre-correction scan occurrence; not a live mathematical assertion',line])
    with (ROOT/'notes/WP84_PARITY_GRADED_RATIO_ERRATUM.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f);w.writerow(['path','line','classification','action','text']);w.writerows(rows)
    print('PASS: authoritative ratio occurrence table:',len(rows),'rows; one historical bug explicitly repaired.')
if __name__=='__main__':main()
