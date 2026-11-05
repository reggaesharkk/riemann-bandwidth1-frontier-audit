from pathlib import Path
import hashlib, json, re, zipfile
D=Path(__file__).resolve().parent
def require(condition,message):
    if not condition: raise RuntimeError(message)
old=(D/'failed_drafts/terminal18/Terminal18_chunked_failed.lean').read_text(encoding='utf-8-sig')
lookup=(D/'reference/previous_objects/Catalog18Lookup.lean').read_text(encoding='utf-8')
records=json.loads((D/'leaf_data_summary.json').read_text())['catalog_declarations']
def array_decl(src,name):
    m=re.search(rf'^def {name} : Array MacroPiece := (.*)$',src,re.M)
    if not m: raise ValueError('missing array '+name)
    return m.group(1)
def literal_arrays(expression):
    groups=re.findall(r'#\[([^\]]*)\]',expression)
    if not groups: raise ValueError('no literal arrays in expression')
    return [[x.strip() for x in part.split(',') if x.strip()] for part in groups]
def named_array(src,name):
    return literal_arrays(array_decl(src,name))[0]
terminal_expr=array_decl(old,'catalog')
terminal_blocks=literal_arrays(terminal_expr)
terminal=[x for block in terminal_blocks for x in block]
original=named_array(lookup,'original')
blocks=[named_array(lookup,f'block{i}') for i in range(3)]
require(len(records)==171 and len(terminal)==len(original)==171,'catalog count')
require([len(x) for x in terminal_blocks]==[57,57,57],'terminal block sizes')
require([len(x) for x in blocks]==[57,57,57],'named block sizes')
require(terminal==original==sum(blocks,[])==records,'catalog order/content mismatch')
new=(D/'Terminal18Compositional.lean').read_text(encoding='utf-8')
require(new.count('theorem catalog_ref_')==171,'lookup theorem count')
require(len(re.findall(r'^theorem decode_segment_\d+_\d+ :',old,re.M))==350,
        'expected all 350 original segment decoder theorems')
require(len(re.findall(r'^theorem row_checked_\d+ :',new,re.M))==15,
        'expected all 15 compact row-check theorems')
all_lookups=(D/'Catalog18AllLookups.lean').read_text(encoding='utf-8')
for prefix in ('blocked_lookup', 'original_lookup'):
    found=[int(x) for x in re.findall(rf'^theorem {prefix}_(\d+) :',all_lookups,re.M)]
    require(found==list(range(171)),f'{prefix}: expected each ordered index 0..170 exactly once')
old_catalog_line='def catalog : Array MacroPiece := '+terminal_expr

def normalize(s,is_new=False):
    s=s.replace('import Catalog18AllLookups\n','')
    if is_new:
        s=re.sub(r'^def catalog : Array MacroPiece := Catalog18\.original$',old_catalog_line,s,count=1,flags=re.M)
    lines=s.splitlines();out=[];i=0
    while i<len(lines):
        line=lines[i]
        if line.startswith('theorem catalog_ref_'):
            statement=line.split(' := by',1)[0]
            out.append(statement+' := by <catalog-reference-proof>')
            i+=1
            while i<len(lines) and (lines[i].startswith('  ') or lines[i]==''):
                i+=1
            continue
        out.append(line);i+=1
    return '\n'.join(out)+'\n'
require(normalize(old)==normalize(new,is_new=True),'unexpected Terminal18 source differences outside catalog storage/reference proofs')
archive=D/'reference/input/A1294_SOURCE_FREE_REPLAY_PACKAGE_V2.zip'
expected='3ecf4d268a74d94310d4d5d8863160e5d6f1fe8a6dd00afef9afe6a80a4ed1a5'
hashv=hashlib.sha256(archive.read_bytes()).hexdigest()
require(hashv==expected,f'frozen V2 hash mismatch: {hashv}')
with zipfile.ZipFile(archive) as z:
    bad=z.testzip(); require(bad is None,f'ZIP CRC failure: {bad}')
print('PASS exact ordered catalog: original Terminal18 inline 57+57+57 = Catalog18.original = three named blocks = leaf summary (171 entries)')
print('PASS all three block lengths 57; Lean module contains all 171 lookup statements')
print('PASS all 350 segment theorem occurrences and 15 row theorem occurrences retained')
print('PASS Terminal18 normalized source unchanged outside catalog storage/reference proofs')
print('PASS frozen V2 SHA-256 and ZIP CRC:',hashv)

