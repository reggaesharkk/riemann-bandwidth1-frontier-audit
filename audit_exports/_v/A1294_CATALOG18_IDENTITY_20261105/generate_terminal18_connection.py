from pathlib import Path
import re
D=Path('audit_exports/sharkbridge01_worktree/A1294_CATALOG18_IDENTITY_20261105')
old=(D/'failed_drafts/terminal18/Terminal18_chunked_failed.lean').read_text(encoding='utf-8-sig')
m=re.search(r'^def catalog : Array MacroPiece := (.*)$',old,re.M)
assert m
expr=m.group(1)
out='''import Catalog18Identity
open Zeta23.ThmD.Sextuple Zeta23.ThmD.Sextuple.MacroPrototype
namespace Catalog18TerminalLiteral

def historicalTerminal18Catalog : Array MacroPiece := '''+expr+'''

theorem historicalTerminal18_eq_blocked : historicalTerminal18Catalog = Catalog18.catalog := by
  rfl

theorem historicalTerminal18_eq_original : historicalTerminal18Catalog = Catalog18.original := by
  calc
    historicalTerminal18Catalog = Catalog18.catalog := historicalTerminal18_eq_blocked
    _ = Catalog18.original := Catalog18Identity.original_eq_catalog.symm

#print Catalog18TerminalLiteral.historicalTerminal18_eq_blocked
#print Catalog18TerminalLiteral.historicalTerminal18_eq_original
#print axioms Catalog18TerminalLiteral.historicalTerminal18_eq_blocked
#print axioms Catalog18TerminalLiteral.historicalTerminal18_eq_original
end Catalog18TerminalLiteral
'''
(D/'Terminal18CatalogConnection.lean').write_text(out,encoding='utf-8')
print('generated exact historical three-array definition',len(re.findall(r'#\[',expr)),'array blocks')
