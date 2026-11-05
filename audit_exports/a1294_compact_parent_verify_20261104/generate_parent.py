from pathlib import Path
D=Path(__file__).resolve().parent
old=(D/'historical/A1294TwoQuadraticParent.lean').read_text(encoding='utf-8-sig')
box=old.split('def sourceParentBox : GapBox where')[1].split('def sourceLeftBox')[0]
ext=old.split('theorem gapBox_ext_exact')[1].split('theorem source_children_match_parent_split')[0]
coverage=old.split('theorem source_children_match_parent_split')[1].split('def sourceAnchorCodes')[0]
coverage=coverage.replace('sourceLeftBox','AuthenticCompactLeaf.box').replace('sourceRightBox','AuthenticCompactRight.box')
s='''import Zeta23.ThmD.Sextuple.CompositionalRight
open Zeta23.ThmD.Sextuple
namespace A1294CompactParent
def targetA : ℚ := 647/50000
def targetB : ℚ := 1094977/5000000000
def sourceParentBox : GapBox where'''+box+'theorem gapBox_ext_exact'+ext+'theorem source_children_match_parent_split'+coverage
proof=old.split('theorem source_parent_box_predicate :')[1].split('#print axioms source_children_match_parent_split')[0]
proof=proof.replace('source_left_box_predicate','AuthenticCompactLeaf.leaf_sound').replace('source_right_box_predicate','AuthenticCompactRight.leaf_sound')
s+='theorem source_parent_box_predicate :'+proof
s+='''#print axioms source_children_match_parent_split
#print axioms AuthenticCompactLeaf.accepted
#print axioms AuthenticCompactRight.accepted
#print axioms source_parent_box_predicate
#print source_parent_box_predicate
end A1294CompactParent
'''
(D/'A1294CompactParent.lean').write_text(s,encoding='utf-8')
print('Parent box definition and target predicate copied exactly from historical source; child proofs replaced by compact leaf_sound theorems.')
