import StandaloneCore
open Zeta23.ThmD.Sextuple Zeta23.ThmD.Sextuple.MacroPrototype
open A1294GenericChecker A1294Compact A1294FifteenBridge IndependentEngine
noncomputable section
namespace IndependentTerminal22
set_option maxRecDepth 6000
set_option maxHeartbeats 2000000

def q0 : CompactRat := ⟨(0),1⟩
def q1 : CompactRat := ⟨(1755263779336959657910023102330969),7812500000000000000000000000000000000000⟩
def q2 : CompactRat := ⟨(29727308394007168144031841183195847081),500000000000000000000000000000000000000000⟩
def q3 : CompactRat := ⟨(6876046637736468087644507155946023489),80000000000000000000000000000000000000000⟩
def q4 : CompactRat := ⟨(7594713117315031921983662976367761841),80000000000000000000000000000000000000000⟩
def q5 : CompactRat := ⟨(12892869620170946020955818564495929),50000000000000000000000000000000000000⟩
def q6 : CompactRat := ⟨(5170581624709583018970186520240204081),3200000000000000000000000000000000000000⟩
def q7 : CompactRat := ⟨(21287960894909617826490440080249),5000000000000000000000000000000000⟩
def q8 : CompactRat := ⟨(795),128⟩
def q9 : CompactRat := ⟨(250723),40000⟩
def q10 : CompactRat := ⟨(62837),10000⟩
def q11 : CompactRat := ⟨(251973),40000⟩
def q12 : CompactRat := ⟨(126299),20000⟩
def q13 : CompactRat := ⟨(405),64⟩
def q14 : CompactRat := ⟨(253223),40000⟩
def q15 : CompactRat := ⟨(31731),5000⟩
def q16 : CompactRat := ⟨(254473),40000⟩
def q17 : CompactRat := ⟨(127549),20000⟩
def q18 : CompactRat := ⟨(255723),40000⟩
def q19 : CompactRat := ⟨(64087),10000⟩
def q20 : CompactRat := ⟨(256973),40000⟩
def q21 : CompactRat := ⟨(128799),20000⟩
def q22 : CompactRat := ⟨(825),128⟩
def q23 : CompactRat := ⟨(258223),40000⟩
def q24 : CompactRat := ⟨(8089),1250⟩
def q25 : CompactRat := ⟨(259473),40000⟩
def q26 : CompactRat := ⟨(130049),20000⟩
def q27 : CompactRat := ⟨(260723),40000⟩
def q28 : CompactRat := ⟨(65337),10000⟩
def q29 : CompactRat := ⟨(261973),40000⟩
def q30 : CompactRat := ⟨(105),16⟩
def q31 : CompactRat := ⟨(405),32⟩
def q32 : CompactRat := ⟨(633077),50000⟩
def q33 : CompactRat := ⟨(2535433),200000⟩
def q34 : CompactRat := ⟨(1269279),100000⟩
def q35 : CompactRat := ⟨(2541683),200000⟩
def q36 : CompactRat := ⟨(318101),25000⟩
def q37 : CompactRat := ⟨(2547933),200000⟩
def q38 : CompactRat := ⟨(1275529),100000⟩
def q39 : CompactRat := ⟨(12755291),1000000⟩
def q40 : CompactRat := ⟨(825),64⟩
def q41 : CompactRat := ⟨(1215),64⟩
def q42 : CompactRat := ⟨(4748093),250000⟩
def q43 : CompactRat := ⟨(19007997),1000000⟩
def q44 : CompactRat := ⟨(9511811),500000⟩
def q45 : CompactRat := ⟨(19039247),1000000⟩
def q46 : CompactRat := ⟨(2381859),125000⟩
def q47 : CompactRat := ⟨(19070497),1000000⟩
def q48 : CompactRat := ⟨(9543061),500000⟩
def q49 : CompactRat := ⟨(2445),128⟩
def q50 : CompactRat := ⟨(19101747),1000000⟩
def q51 : CompactRat := ⟨(4779343),250000⟩
def q52 : CompactRat := ⟨(19132997),1000000⟩
def q53 : CompactRat := ⟨(9574311),500000⟩
def q54 : CompactRat := ⟨(19164247),1000000⟩
def q55 : CompactRat := ⟨(599371),31250⟩
def q56 : CompactRat := ⟨(19195497),1000000⟩
def q57 : CompactRat := ⟨(9605561),500000⟩
def q58 : CompactRat := ⟨(19226747),1000000⟩
def q59 : CompactRat := ⟨(4810593),250000⟩
def q60 : CompactRat := ⟨(19257997),1000000⟩
def q61 : CompactRat := ⟨(9636811),500000⟩
def q62 : CompactRat := ⟨(19289247),1000000⟩
def q63 : CompactRat := ⟨(2413109),125000⟩
def q64 : CompactRat := ⟨(19320497),1000000⟩
def q65 : CompactRat := ⟨(2475),128⟩
def q66 : CompactRat := ⟨(9668061),500000⟩
def q67 : CompactRat := ⟨(19351747),1000000⟩
def q68 : CompactRat := ⟨(1245),64⟩
def q69 : CompactRat := ⟨(3255),128⟩
def q70 : CompactRat := ⟨(5086319),200000⟩
def q71 : CompactRat := ⟨(1272361),50000⟩
def q72 : CompactRat := ⟨(5092569),200000⟩
def q73 : CompactRat := ⟨(2547847),100000⟩
def q74 : CompactRat := ⟨(5098819),200000⟩
def q75 : CompactRat := ⟨(637743),25000⟩
def q76 : CompactRat := ⟨(5105069),200000⟩
def q77 : CompactRat := ⟨(2554097),100000⟩
def q78 : CompactRat := ⟨(5111319),200000⟩
def q79 : CompactRat := ⟨(1278611),50000⟩
def q80 : CompactRat := ⟨(5117569),200000⟩
def q81 : CompactRat := ⟨(2560347),100000⟩
def q82 : CompactRat := ⟨(5123819),200000⟩
def q83 : CompactRat := ⟨(160217),6250⟩
def q84 : CompactRat := ⟨(5130069),200000⟩
def q85 : CompactRat := ⟨(2566597),100000⟩
def q86 : CompactRat := ⟨(5136319),200000⟩
def q87 : CompactRat := ⟨(1284861),50000⟩
def q88 : CompactRat := ⟨(5142569),200000⟩
def q89 : CompactRat := ⟨(2572847),100000⟩
def q90 : CompactRat := ⟨(5148819),200000⟩
def q91 : CompactRat := ⟨(643993),25000⟩
def q92 : CompactRat := ⟨(5155069),200000⟩
def q93 : CompactRat := ⟨(2579097),100000⟩
def q94 : CompactRat := ⟨(5161319),200000⟩
def q95 : CompactRat := ⟨(1291111),50000⟩
def q96 : CompactRat := ⟨(5167569),200000⟩
def q97 : CompactRat := ⟨(2585347),100000⟩
def q98 : CompactRat := ⟨(5173819),200000⟩
def q99 : CompactRat := ⟨(323559),12500⟩
def q100 : CompactRat := ⟨(3315),128⟩
def q101 : CompactRat := ⟨(5180069),200000⟩
def q102 : CompactRat := ⟨(2591597),100000⟩
def q103 : CompactRat := ⟨(5186319),200000⟩
def q104 : CompactRat := ⟨(1297361),50000⟩
def q105 : CompactRat := ⟨(5192569),200000⟩
def q106 : CompactRat := ⟨(2597847),100000⟩
def q107 : CompactRat := ⟨(1665),64⟩
def q108 : CompactRat := ⟨(4065),128⟩
def q109 : CompactRat := ⟨(1587913),50000⟩
def q110 : CompactRat := ⟨(6354777),200000⟩
def q111 : CompactRat := ⟨(3178951),100000⟩
def q112 : CompactRat := ⟨(6361027),200000⟩
def q113 : CompactRat := ⟨(795519),25000⟩
def q114 : CompactRat := ⟨(6367277),200000⟩
def q115 : CompactRat := ⟨(3185201),100000⟩
def q116 : CompactRat := ⟨(6373527),200000⟩
def q117 : CompactRat := ⟨(6448527),200000⟩
def q118 : CompactRat := ⟨(4155),128⟩
def qs : Array CompactRat := #[q0,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25,q26,q27,q28,q29,q30,q31,q32,q33,q34,q35,q36,q37,q38,q39,q40,q41,q42,q43,q44,q45,q46,q47,q48,q49,q50,q51,q52,q53,q54,q55,q56,q57,q58,q59,q60,q61,q62,q63,q64,q65,q66,q67,q68,q69,q70,q71,q72,q73,q74,q75,q76,q77,q78,q79,q80,q81,q82,q83,q84,q85,q86,q87,q88,q89,q90,q91,q92,q93,q94,q95,q96,q97,q98,q99,q100,q101,q102,q103,q104,q105,q106,q107,q108,q109,q110,q111,q112,q113,q114,q115,q116,q117,q118]
def catalog : Array MacroPiece := #[refinementPiece3,refinementPiece4,refinementPiece5,refinementPiece6,refinementPiece7,refinementPiece8,refinementPiece9,refinementPiece10,refinementPiece11,macroPiece11,refinementPiece48,refinementPiece49,refinementPiece50,refinementPiece51,refinementPiece52,refinementPiece53,refinementPiece54,refinementPiece55,refinementPiece56,refinementPiece57,refinementPiece58,refinementPiece59,refinementPiece60,refinementPiece61,refinementPiece62,refinementPiece63,refinementPiece64,refinementPiece65,refinementPiece66,refinementPiece67,refinementPiece68,refinementPiece69,refinementPiece70,refinementPiece84,refinementPiece85,refinementPiece86,refinementPiece87,refinementPiece88,refinementPiece89,refinementPiece90,refinementPiece91,refinementPiece92,refinementPiece93,refinementPiece94,refinementPiece95,macroPiece24,refinementPiece98,refinementPiece99,refinementPiece100,refinementPiece101,refinementPiece102,refinementPiece103,refinementPiece104,refinementPiece105,refinementPiece106,refinementPiece107,refinementPiece108,refinementPiece109,refinementPiece110,refinementPiece111,refinementPiece112,refinementPiece113,refinementPiece114,refinementPiece160,refinementPiece161,refinementPiece162,refinementPiece163,refinementPiece164,refinementPiece165,refinementPiece166,refinementPiece167,macroPiece30,macroPiece31,refinementPiece12,refinementPiece13,refinementPiece14,refinementPiece15,refinementPiece16,refinementPiece17,refinementPiece18,refinementPiece41,refinementPiece42,refinementPiece43,refinementPiece44,refinementPiece45,refinementPiece46,macroPiece9,macroPiece10,refinementPiece71,macroPiece18,refinementPiece115,refinementPiece116,refinementPiece117,refinementPiece118,refinementPiece119,macroPiece25,macroPiece2,refinementPiece0,refinementPiece1,refinementPiece2]
def segmentRefs : Array SegmentRef := #[⟨8,9,96⟩,⟨9,10,97⟩,⟨10,11,98⟩,⟨11,12,99⟩,⟨12,13,0⟩,⟨13,14,0⟩,⟨14,15,1⟩,⟨15,16,2⟩,⟨16,17,3⟩,⟨17,18,4⟩,⟨18,19,5⟩,⟨19,20,6⟩,⟨20,21,7⟩,⟨21,22,8⟩,⟨21,23,8⟩,⟨22,23,8⟩,⟨23,24,73⟩,⟨24,25,74⟩,⟨25,26,75⟩,⟨26,27,76⟩,⟨27,28,77⟩,⟨28,29,78⟩,⟨29,30,79⟩,⟨31,32,80⟩,⟨32,33,81⟩,⟨33,34,82⟩,⟨34,35,83⟩,⟨35,36,84⟩,⟨36,37,85⟩,⟨37,38,86⟩,⟨38,39,87⟩,⟨39,40,9⟩,⟨41,42,10⟩,⟨42,43,11⟩,⟨43,44,12⟩,⟨44,45,13⟩,⟨45,46,14⟩,⟨46,47,15⟩,⟨47,48,16⟩,⟨48,50,17⟩,⟨49,50,17⟩,⟨50,51,18⟩,⟨51,52,19⟩,⟨52,53,20⟩,⟨53,54,21⟩,⟨54,55,22⟩,⟨55,56,23⟩,⟨56,57,24⟩,⟨57,58,25⟩,⟨58,59,26⟩,⟨59,60,27⟩,⟨60,61,28⟩,⟨61,62,29⟩,⟨62,63,30⟩,⟨63,64,31⟩,⟨64,65,32⟩,⟨64,66,32⟩,⟨66,67,88⟩,⟨67,68,89⟩,⟨69,70,33⟩,⟨70,71,34⟩,⟨71,72,35⟩,⟨72,73,36⟩,⟨73,74,37⟩,⟨74,75,38⟩,⟨75,76,39⟩,⟨76,77,40⟩,⟨77,78,41⟩,⟨78,79,42⟩,⟨79,80,43⟩,⟨80,81,44⟩,⟨81,82,45⟩,⟨82,83,45⟩,⟨83,84,46⟩,⟨84,85,47⟩,⟨85,86,48⟩,⟨86,87,49⟩,⟨87,88,50⟩,⟨88,89,51⟩,⟨89,90,52⟩,⟨90,91,53⟩,⟨91,92,54⟩,⟨92,93,55⟩,⟨93,94,56⟩,⟨94,95,57⟩,⟨95,96,58⟩,⟨96,97,59⟩,⟨97,98,60⟩,⟨98,99,61⟩,⟨99,100,62⟩,⟨99,101,62⟩,⟨101,102,90⟩,⟨102,103,91⟩,⟨103,104,92⟩,⟨104,105,93⟩,⟨105,106,94⟩,⟨106,107,95⟩,⟨108,109,63⟩,⟨109,110,64⟩,⟨110,111,65⟩,⟨111,112,66⟩,⟨112,113,67⟩,⟨113,114,68⟩,⟨114,115,69⟩,⟨115,116,70⟩,⟨116,117,71⟩,⟨117,118,72⟩]
def c0 : CompactSegment := {lo := q8, hi := q9, pieceRef := 96}
def s0 : SourceSegment := {lo := interpRat q8, hi := interpRat q9, piece := macroPiece2}
theorem maxcheck_0 : sourceSegmentCheck (21287960894909617826490440080249/5000000000000000000000000000000000) s0 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s0, q8, q9, interpRat, macroPiece2, MacroPiece.box]

def c1 : CompactSegment := {lo := q9, hi := q10, pieceRef := 97}
def s1 : SourceSegment := {lo := interpRat q9, hi := interpRat q10, piece := refinementPiece0}
theorem maxcheck_1 : sourceSegmentCheck (21287960894909617826490440080249/5000000000000000000000000000000000) s1 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s1, q9, q10, interpRat, refinementPiece0, MacroPiece.box]

def c2 : CompactSegment := {lo := q10, hi := q11, pieceRef := 98}
def s2 : SourceSegment := {lo := interpRat q10, hi := interpRat q11, piece := refinementPiece1}
theorem maxcheck_2 : sourceSegmentCheck (21287960894909617826490440080249/5000000000000000000000000000000000) s2 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s2, q10, q11, interpRat, refinementPiece1, MacroPiece.box]

def c3 : CompactSegment := {lo := q11, hi := q12, pieceRef := 99}
def s3 : SourceSegment := {lo := interpRat q11, hi := interpRat q12, piece := refinementPiece2}
theorem maxcheck_3 : sourceSegmentCheck (21287960894909617826490440080249/5000000000000000000000000000000000) s3 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s3, q11, q12, interpRat, refinementPiece2, MacroPiece.box]

def c4 : CompactSegment := {lo := q12, hi := q13, pieceRef := 0}
def s4 : SourceSegment := {lo := interpRat q12, hi := interpRat q13, piece := refinementPiece3}
theorem maxcheck_4 : sourceSegmentCheck (21287960894909617826490440080249/5000000000000000000000000000000000) s4 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s4, q12, q13, interpRat, refinementPiece3, MacroPiece.box]

def c5 : CompactSegment := {lo := q13, hi := q14, pieceRef := 0}
def s5 : SourceSegment := {lo := interpRat q13, hi := interpRat q14, piece := refinementPiece3}
theorem maxcheck_5 : sourceSegmentCheck (5170581624709583018970186520240204081/3200000000000000000000000000000000000000) s5 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s5, q13, q14, interpRat, refinementPiece3, MacroPiece.box]

def c6 : CompactSegment := {lo := q14, hi := q15, pieceRef := 1}
def s6 : SourceSegment := {lo := interpRat q14, hi := interpRat q15, piece := refinementPiece4}
theorem maxcheck_6 : sourceSegmentCheck (5170581624709583018970186520240204081/3200000000000000000000000000000000000000) s6 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s6, q14, q15, interpRat, refinementPiece4, MacroPiece.box]

def c7 : CompactSegment := {lo := q15, hi := q16, pieceRef := 2}
def s7 : SourceSegment := {lo := interpRat q15, hi := interpRat q16, piece := refinementPiece5}
theorem maxcheck_7 : sourceSegmentCheck (5170581624709583018970186520240204081/3200000000000000000000000000000000000000) s7 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s7, q15, q16, interpRat, refinementPiece5, MacroPiece.box]

def c8 : CompactSegment := {lo := q16, hi := q17, pieceRef := 3}
def s8 : SourceSegment := {lo := interpRat q16, hi := interpRat q17, piece := refinementPiece6}
theorem maxcheck_8 : sourceSegmentCheck (5170581624709583018970186520240204081/3200000000000000000000000000000000000000) s8 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s8, q16, q17, interpRat, refinementPiece6, MacroPiece.box]

def c9 : CompactSegment := {lo := q17, hi := q18, pieceRef := 4}
def s9 : SourceSegment := {lo := interpRat q17, hi := interpRat q18, piece := refinementPiece7}
theorem maxcheck_9 : sourceSegmentCheck (5170581624709583018970186520240204081/3200000000000000000000000000000000000000) s9 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s9, q17, q18, interpRat, refinementPiece7, MacroPiece.box]

def c10 : CompactSegment := {lo := q18, hi := q19, pieceRef := 5}
def s10 : SourceSegment := {lo := interpRat q18, hi := interpRat q19, piece := refinementPiece8}
theorem maxcheck_10 : sourceSegmentCheck (5170581624709583018970186520240204081/3200000000000000000000000000000000000000) s10 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s10, q18, q19, interpRat, refinementPiece8, MacroPiece.box]

def c11 : CompactSegment := {lo := q19, hi := q20, pieceRef := 6}
def s11 : SourceSegment := {lo := interpRat q19, hi := interpRat q20, piece := refinementPiece9}
theorem maxcheck_11 : sourceSegmentCheck (5170581624709583018970186520240204081/3200000000000000000000000000000000000000) s11 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s11, q19, q20, interpRat, refinementPiece9, MacroPiece.box]

def c12 : CompactSegment := {lo := q20, hi := q21, pieceRef := 7}
def s12 : SourceSegment := {lo := interpRat q20, hi := interpRat q21, piece := refinementPiece10}
theorem maxcheck_12 : sourceSegmentCheck (5170581624709583018970186520240204081/3200000000000000000000000000000000000000) s12 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s12, q20, q21, interpRat, refinementPiece10, MacroPiece.box]

def c13 : CompactSegment := {lo := q21, hi := q22, pieceRef := 8}
def s13 : SourceSegment := {lo := interpRat q21, hi := interpRat q22, piece := refinementPiece11}
theorem maxcheck_13 : sourceSegmentCheck (5170581624709583018970186520240204081/3200000000000000000000000000000000000000) s13 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s13, q21, q22, interpRat, refinementPiece11, MacroPiece.box]

def c14 : CompactSegment := {lo := q21, hi := q23, pieceRef := 8}
def s14 : SourceSegment := {lo := interpRat q21, hi := interpRat q23, piece := refinementPiece11}
theorem maxcheck_14 : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) s14 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s14, q21, q23, interpRat, refinementPiece11, MacroPiece.box]

def c15 : CompactSegment := {lo := q22, hi := q23, pieceRef := 8}
def s15 : SourceSegment := {lo := interpRat q22, hi := interpRat q23, piece := refinementPiece11}
theorem maxcheck_15 : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) s15 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s15, q22, q23, interpRat, refinementPiece11, MacroPiece.box]

def c16 : CompactSegment := {lo := q23, hi := q24, pieceRef := 73}
def s16 : SourceSegment := {lo := interpRat q23, hi := interpRat q24, piece := refinementPiece12}
theorem maxcheck_16 : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) s16 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s16, q23, q24, interpRat, refinementPiece12, MacroPiece.box]

def c17 : CompactSegment := {lo := q24, hi := q25, pieceRef := 74}
def s17 : SourceSegment := {lo := interpRat q24, hi := interpRat q25, piece := refinementPiece13}
theorem maxcheck_17 : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) s17 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s17, q24, q25, interpRat, refinementPiece13, MacroPiece.box]

def c18 : CompactSegment := {lo := q25, hi := q26, pieceRef := 75}
def s18 : SourceSegment := {lo := interpRat q25, hi := interpRat q26, piece := refinementPiece14}
theorem maxcheck_18 : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) s18 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s18, q25, q26, interpRat, refinementPiece14, MacroPiece.box]

def c19 : CompactSegment := {lo := q26, hi := q27, pieceRef := 76}
def s19 : SourceSegment := {lo := interpRat q26, hi := interpRat q27, piece := refinementPiece15}
theorem maxcheck_19 : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) s19 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s19, q26, q27, interpRat, refinementPiece15, MacroPiece.box]

def c20 : CompactSegment := {lo := q27, hi := q28, pieceRef := 77}
def s20 : SourceSegment := {lo := interpRat q27, hi := interpRat q28, piece := refinementPiece16}
theorem maxcheck_20 : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) s20 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s20, q27, q28, interpRat, refinementPiece16, MacroPiece.box]

def c21 : CompactSegment := {lo := q28, hi := q29, pieceRef := 78}
def s21 : SourceSegment := {lo := interpRat q28, hi := interpRat q29, piece := refinementPiece17}
theorem maxcheck_21 : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) s21 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s21, q28, q29, interpRat, refinementPiece17, MacroPiece.box]

def c22 : CompactSegment := {lo := q29, hi := q30, pieceRef := 79}
def s22 : SourceSegment := {lo := interpRat q29, hi := interpRat q30, piece := refinementPiece18}
theorem maxcheck_22 : sourceSegmentCheck (12892869620170946020955818564495929/50000000000000000000000000000000000000) s22 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s22, q29, q30, interpRat, refinementPiece18, MacroPiece.box]

def c23 : CompactSegment := {lo := q31, hi := q32, pieceRef := 80}
def s23 : SourceSegment := {lo := interpRat q31, hi := interpRat q32, piece := refinementPiece41}
theorem maxcheck_23 : sourceSegmentCheck (0) s23 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s23, q31, q32, interpRat, refinementPiece41, MacroPiece.box]

def c24 : CompactSegment := {lo := q32, hi := q33, pieceRef := 81}
def s24 : SourceSegment := {lo := interpRat q32, hi := interpRat q33, piece := refinementPiece42}
theorem maxcheck_24 : sourceSegmentCheck (0) s24 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s24, q32, q33, interpRat, refinementPiece42, MacroPiece.box]

def c25 : CompactSegment := {lo := q33, hi := q34, pieceRef := 82}
def s25 : SourceSegment := {lo := interpRat q33, hi := interpRat q34, piece := refinementPiece43}
theorem maxcheck_25 : sourceSegmentCheck (0) s25 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s25, q33, q34, interpRat, refinementPiece43, MacroPiece.box]

def c26 : CompactSegment := {lo := q34, hi := q35, pieceRef := 83}
def s26 : SourceSegment := {lo := interpRat q34, hi := interpRat q35, piece := refinementPiece44}
theorem maxcheck_26 : sourceSegmentCheck (0) s26 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s26, q34, q35, interpRat, refinementPiece44, MacroPiece.box]

def c27 : CompactSegment := {lo := q35, hi := q36, pieceRef := 84}
def s27 : SourceSegment := {lo := interpRat q35, hi := interpRat q36, piece := refinementPiece45}
theorem maxcheck_27 : sourceSegmentCheck (0) s27 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s27, q35, q36, interpRat, refinementPiece45, MacroPiece.box]

def c28 : CompactSegment := {lo := q36, hi := q37, pieceRef := 85}
def s28 : SourceSegment := {lo := interpRat q36, hi := interpRat q37, piece := refinementPiece46}
theorem maxcheck_28 : sourceSegmentCheck (0) s28 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s28, q36, q37, interpRat, refinementPiece46, MacroPiece.box]

def c29 : CompactSegment := {lo := q37, hi := q38, pieceRef := 86}
def s29 : SourceSegment := {lo := interpRat q37, hi := interpRat q38, piece := macroPiece9}
theorem maxcheck_29 : sourceSegmentCheck (0) s29 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s29, q37, q38, interpRat, macroPiece9, MacroPiece.box]

def c30 : CompactSegment := {lo := q38, hi := q39, pieceRef := 87}
def s30 : SourceSegment := {lo := interpRat q38, hi := interpRat q39, piece := macroPiece10}
theorem maxcheck_30 : sourceSegmentCheck (0) s30 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s30, q38, q39, interpRat, macroPiece10, MacroPiece.box]

def c31 : CompactSegment := {lo := q39, hi := q40, pieceRef := 9}
def s31 : SourceSegment := {lo := interpRat q39, hi := interpRat q40, piece := macroPiece11}
theorem maxcheck_31 : sourceSegmentCheck (0) s31 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s31, q39, q40, interpRat, macroPiece11, MacroPiece.box]

def c32 : CompactSegment := {lo := q41, hi := q42, pieceRef := 10}
def s32 : SourceSegment := {lo := interpRat q41, hi := interpRat q42, piece := refinementPiece48}
theorem maxcheck_32 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) s32 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s32, q41, q42, interpRat, refinementPiece48, MacroPiece.box]

def c33 : CompactSegment := {lo := q42, hi := q43, pieceRef := 11}
def s33 : SourceSegment := {lo := interpRat q42, hi := interpRat q43, piece := refinementPiece49}
theorem maxcheck_33 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) s33 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s33, q42, q43, interpRat, refinementPiece49, MacroPiece.box]

def c34 : CompactSegment := {lo := q43, hi := q44, pieceRef := 12}
def s34 : SourceSegment := {lo := interpRat q43, hi := interpRat q44, piece := refinementPiece50}
theorem maxcheck_34 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) s34 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s34, q43, q44, interpRat, refinementPiece50, MacroPiece.box]

def c35 : CompactSegment := {lo := q44, hi := q45, pieceRef := 13}
def s35 : SourceSegment := {lo := interpRat q44, hi := interpRat q45, piece := refinementPiece51}
theorem maxcheck_35 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) s35 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s35, q44, q45, interpRat, refinementPiece51, MacroPiece.box]

def c36 : CompactSegment := {lo := q45, hi := q46, pieceRef := 14}
def s36 : SourceSegment := {lo := interpRat q45, hi := interpRat q46, piece := refinementPiece52}
theorem maxcheck_36 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) s36 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s36, q45, q46, interpRat, refinementPiece52, MacroPiece.box]

def c37 : CompactSegment := {lo := q46, hi := q47, pieceRef := 15}
def s37 : SourceSegment := {lo := interpRat q46, hi := interpRat q47, piece := refinementPiece53}
theorem maxcheck_37 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) s37 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s37, q46, q47, interpRat, refinementPiece53, MacroPiece.box]

def c38 : CompactSegment := {lo := q47, hi := q48, pieceRef := 16}
def s38 : SourceSegment := {lo := interpRat q47, hi := interpRat q48, piece := refinementPiece54}
theorem maxcheck_38 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) s38 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s38, q47, q48, interpRat, refinementPiece54, MacroPiece.box]

def c39 : CompactSegment := {lo := q48, hi := q50, pieceRef := 17}
def s39 : SourceSegment := {lo := interpRat q48, hi := interpRat q50, piece := refinementPiece55}
theorem maxcheck_39 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) s39 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s39, q48, q50, interpRat, refinementPiece55, MacroPiece.box]

def c40 : CompactSegment := {lo := q49, hi := q50, pieceRef := 17}
def s40 : SourceSegment := {lo := interpRat q49, hi := interpRat q50, piece := refinementPiece55}
theorem maxcheck_40 : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) s40 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s40, q49, q50, interpRat, refinementPiece55, MacroPiece.box]

def c41 : CompactSegment := {lo := q50, hi := q51, pieceRef := 18}
def s41 : SourceSegment := {lo := interpRat q50, hi := interpRat q51, piece := refinementPiece56}
theorem maxcheck_41 : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) s41 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s41, q50, q51, interpRat, refinementPiece56, MacroPiece.box]

def c42 : CompactSegment := {lo := q51, hi := q52, pieceRef := 19}
def s42 : SourceSegment := {lo := interpRat q51, hi := interpRat q52, piece := refinementPiece57}
theorem maxcheck_42 : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) s42 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s42, q51, q52, interpRat, refinementPiece57, MacroPiece.box]

def c43 : CompactSegment := {lo := q52, hi := q53, pieceRef := 20}
def s43 : SourceSegment := {lo := interpRat q52, hi := interpRat q53, piece := refinementPiece58}
theorem maxcheck_43 : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) s43 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s43, q52, q53, interpRat, refinementPiece58, MacroPiece.box]

def c44 : CompactSegment := {lo := q53, hi := q54, pieceRef := 21}
def s44 : SourceSegment := {lo := interpRat q53, hi := interpRat q54, piece := refinementPiece59}
theorem maxcheck_44 : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) s44 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s44, q53, q54, interpRat, refinementPiece59, MacroPiece.box]

def c45 : CompactSegment := {lo := q54, hi := q55, pieceRef := 22}
def s45 : SourceSegment := {lo := interpRat q54, hi := interpRat q55, piece := refinementPiece60}
theorem maxcheck_45 : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) s45 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s45, q54, q55, interpRat, refinementPiece60, MacroPiece.box]

def c46 : CompactSegment := {lo := q55, hi := q56, pieceRef := 23}
def s46 : SourceSegment := {lo := interpRat q55, hi := interpRat q56, piece := refinementPiece61}
theorem maxcheck_46 : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) s46 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s46, q55, q56, interpRat, refinementPiece61, MacroPiece.box]

def c47 : CompactSegment := {lo := q56, hi := q57, pieceRef := 24}
def s47 : SourceSegment := {lo := interpRat q56, hi := interpRat q57, piece := refinementPiece62}
theorem maxcheck_47 : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) s47 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s47, q56, q57, interpRat, refinementPiece62, MacroPiece.box]

def c48 : CompactSegment := {lo := q57, hi := q58, pieceRef := 25}
def s48 : SourceSegment := {lo := interpRat q57, hi := interpRat q58, piece := refinementPiece63}
theorem maxcheck_48 : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) s48 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s48, q57, q58, interpRat, refinementPiece63, MacroPiece.box]

def c49 : CompactSegment := {lo := q58, hi := q59, pieceRef := 26}
def s49 : SourceSegment := {lo := interpRat q58, hi := interpRat q59, piece := refinementPiece64}
theorem maxcheck_49 : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) s49 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s49, q58, q59, interpRat, refinementPiece64, MacroPiece.box]

def c50 : CompactSegment := {lo := q59, hi := q60, pieceRef := 27}
def s50 : SourceSegment := {lo := interpRat q59, hi := interpRat q60, piece := refinementPiece65}
theorem maxcheck_50 : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) s50 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s50, q59, q60, interpRat, refinementPiece65, MacroPiece.box]

def c51 : CompactSegment := {lo := q60, hi := q61, pieceRef := 28}
def s51 : SourceSegment := {lo := interpRat q60, hi := interpRat q61, piece := refinementPiece66}
theorem maxcheck_51 : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) s51 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s51, q60, q61, interpRat, refinementPiece66, MacroPiece.box]

def c52 : CompactSegment := {lo := q61, hi := q62, pieceRef := 29}
def s52 : SourceSegment := {lo := interpRat q61, hi := interpRat q62, piece := refinementPiece67}
theorem maxcheck_52 : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) s52 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s52, q61, q62, interpRat, refinementPiece67, MacroPiece.box]

def c53 : CompactSegment := {lo := q62, hi := q63, pieceRef := 30}
def s53 : SourceSegment := {lo := interpRat q62, hi := interpRat q63, piece := refinementPiece68}
theorem maxcheck_53 : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) s53 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s53, q62, q63, interpRat, refinementPiece68, MacroPiece.box]

def c54 : CompactSegment := {lo := q63, hi := q64, pieceRef := 31}
def s54 : SourceSegment := {lo := interpRat q63, hi := interpRat q64, piece := refinementPiece69}
theorem maxcheck_54 : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) s54 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s54, q63, q64, interpRat, refinementPiece69, MacroPiece.box]

def c55 : CompactSegment := {lo := q64, hi := q65, pieceRef := 32}
def s55 : SourceSegment := {lo := interpRat q64, hi := interpRat q65, piece := refinementPiece70}
theorem maxcheck_55 : sourceSegmentCheck (1755263779336959657910023102330969/7812500000000000000000000000000000000000) s55 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s55, q64, q65, interpRat, refinementPiece70, MacroPiece.box]

def c56 : CompactSegment := {lo := q64, hi := q66, pieceRef := 32}
def s56 : SourceSegment := {lo := interpRat q64, hi := interpRat q66, piece := refinementPiece70}
theorem maxcheck_56 : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) s56 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s56, q64, q66, interpRat, refinementPiece70, MacroPiece.box]

def c57 : CompactSegment := {lo := q66, hi := q67, pieceRef := 88}
def s57 : SourceSegment := {lo := interpRat q66, hi := interpRat q67, piece := refinementPiece71}
theorem maxcheck_57 : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) s57 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s57, q66, q67, interpRat, refinementPiece71, MacroPiece.box]

def c58 : CompactSegment := {lo := q67, hi := q68, pieceRef := 89}
def s58 : SourceSegment := {lo := interpRat q67, hi := interpRat q68, piece := macroPiece18}
theorem maxcheck_58 : sourceSegmentCheck (29727308394007168144031841183195847081/500000000000000000000000000000000000000000) s58 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s58, q67, q68, interpRat, macroPiece18, MacroPiece.box]

def c59 : CompactSegment := {lo := q69, hi := q70, pieceRef := 33}
def s59 : SourceSegment := {lo := interpRat q69, hi := interpRat q70, piece := refinementPiece84}
theorem maxcheck_59 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) s59 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s59, q69, q70, interpRat, refinementPiece84, MacroPiece.box]

def c60 : CompactSegment := {lo := q70, hi := q71, pieceRef := 34}
def s60 : SourceSegment := {lo := interpRat q70, hi := interpRat q71, piece := refinementPiece85}
theorem maxcheck_60 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) s60 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s60, q70, q71, interpRat, refinementPiece85, MacroPiece.box]

def c61 : CompactSegment := {lo := q71, hi := q72, pieceRef := 35}
def s61 : SourceSegment := {lo := interpRat q71, hi := interpRat q72, piece := refinementPiece86}
theorem maxcheck_61 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) s61 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s61, q71, q72, interpRat, refinementPiece86, MacroPiece.box]

def c62 : CompactSegment := {lo := q72, hi := q73, pieceRef := 36}
def s62 : SourceSegment := {lo := interpRat q72, hi := interpRat q73, piece := refinementPiece87}
theorem maxcheck_62 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) s62 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s62, q72, q73, interpRat, refinementPiece87, MacroPiece.box]

def c63 : CompactSegment := {lo := q73, hi := q74, pieceRef := 37}
def s63 : SourceSegment := {lo := interpRat q73, hi := interpRat q74, piece := refinementPiece88}
theorem maxcheck_63 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) s63 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s63, q73, q74, interpRat, refinementPiece88, MacroPiece.box]

def c64 : CompactSegment := {lo := q74, hi := q75, pieceRef := 38}
def s64 : SourceSegment := {lo := interpRat q74, hi := interpRat q75, piece := refinementPiece89}
theorem maxcheck_64 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) s64 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s64, q74, q75, interpRat, refinementPiece89, MacroPiece.box]

def c65 : CompactSegment := {lo := q75, hi := q76, pieceRef := 39}
def s65 : SourceSegment := {lo := interpRat q75, hi := interpRat q76, piece := refinementPiece90}
theorem maxcheck_65 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) s65 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s65, q75, q76, interpRat, refinementPiece90, MacroPiece.box]

def c66 : CompactSegment := {lo := q76, hi := q77, pieceRef := 40}
def s66 : SourceSegment := {lo := interpRat q76, hi := interpRat q77, piece := refinementPiece91}
theorem maxcheck_66 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) s66 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s66, q76, q77, interpRat, refinementPiece91, MacroPiece.box]

def c67 : CompactSegment := {lo := q77, hi := q78, pieceRef := 41}
def s67 : SourceSegment := {lo := interpRat q77, hi := interpRat q78, piece := refinementPiece92}
theorem maxcheck_67 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) s67 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s67, q77, q78, interpRat, refinementPiece92, MacroPiece.box]

def c68 : CompactSegment := {lo := q78, hi := q79, pieceRef := 42}
def s68 : SourceSegment := {lo := interpRat q78, hi := interpRat q79, piece := refinementPiece93}
theorem maxcheck_68 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) s68 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s68, q78, q79, interpRat, refinementPiece93, MacroPiece.box]

def c69 : CompactSegment := {lo := q79, hi := q80, pieceRef := 43}
def s69 : SourceSegment := {lo := interpRat q79, hi := interpRat q80, piece := refinementPiece94}
theorem maxcheck_69 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) s69 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s69, q79, q80, interpRat, refinementPiece94, MacroPiece.box]

def c70 : CompactSegment := {lo := q80, hi := q81, pieceRef := 44}
def s70 : SourceSegment := {lo := interpRat q80, hi := interpRat q81, piece := refinementPiece95}
theorem maxcheck_70 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) s70 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s70, q80, q81, interpRat, refinementPiece95, MacroPiece.box]

def c71 : CompactSegment := {lo := q81, hi := q82, pieceRef := 45}
def s71 : SourceSegment := {lo := interpRat q81, hi := interpRat q82, piece := macroPiece24}
theorem maxcheck_71 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) s71 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s71, q81, q82, interpRat, macroPiece24, MacroPiece.box]

def c72 : CompactSegment := {lo := q82, hi := q83, pieceRef := 45}
def s72 : SourceSegment := {lo := interpRat q82, hi := interpRat q83, piece := macroPiece24}
theorem maxcheck_72 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) s72 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s72, q82, q83, interpRat, macroPiece24, MacroPiece.box]

def c73 : CompactSegment := {lo := q83, hi := q84, pieceRef := 46}
def s73 : SourceSegment := {lo := interpRat q83, hi := interpRat q84, piece := refinementPiece98}
theorem maxcheck_73 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) s73 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s73, q83, q84, interpRat, refinementPiece98, MacroPiece.box]

def c74 : CompactSegment := {lo := q84, hi := q85, pieceRef := 47}
def s74 : SourceSegment := {lo := interpRat q84, hi := interpRat q85, piece := refinementPiece99}
theorem maxcheck_74 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) s74 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s74, q84, q85, interpRat, refinementPiece99, MacroPiece.box]

def c75 : CompactSegment := {lo := q85, hi := q86, pieceRef := 48}
def s75 : SourceSegment := {lo := interpRat q85, hi := interpRat q86, piece := refinementPiece100}
theorem maxcheck_75 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) s75 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s75, q85, q86, interpRat, refinementPiece100, MacroPiece.box]

def c76 : CompactSegment := {lo := q86, hi := q87, pieceRef := 49}
def s76 : SourceSegment := {lo := interpRat q86, hi := interpRat q87, piece := refinementPiece101}
theorem maxcheck_76 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) s76 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s76, q86, q87, interpRat, refinementPiece101, MacroPiece.box]

def c77 : CompactSegment := {lo := q87, hi := q88, pieceRef := 50}
def s77 : SourceSegment := {lo := interpRat q87, hi := interpRat q88, piece := refinementPiece102}
theorem maxcheck_77 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) s77 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s77, q87, q88, interpRat, refinementPiece102, MacroPiece.box]

def c78 : CompactSegment := {lo := q88, hi := q89, pieceRef := 51}
def s78 : SourceSegment := {lo := interpRat q88, hi := interpRat q89, piece := refinementPiece103}
theorem maxcheck_78 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) s78 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s78, q88, q89, interpRat, refinementPiece103, MacroPiece.box]

def c79 : CompactSegment := {lo := q89, hi := q90, pieceRef := 52}
def s79 : SourceSegment := {lo := interpRat q89, hi := interpRat q90, piece := refinementPiece104}
theorem maxcheck_79 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) s79 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s79, q89, q90, interpRat, refinementPiece104, MacroPiece.box]

def c80 : CompactSegment := {lo := q90, hi := q91, pieceRef := 53}
def s80 : SourceSegment := {lo := interpRat q90, hi := interpRat q91, piece := refinementPiece105}
theorem maxcheck_80 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) s80 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s80, q90, q91, interpRat, refinementPiece105, MacroPiece.box]

def c81 : CompactSegment := {lo := q91, hi := q92, pieceRef := 54}
def s81 : SourceSegment := {lo := interpRat q91, hi := interpRat q92, piece := refinementPiece106}
theorem maxcheck_81 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) s81 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s81, q91, q92, interpRat, refinementPiece106, MacroPiece.box]

def c82 : CompactSegment := {lo := q92, hi := q93, pieceRef := 55}
def s82 : SourceSegment := {lo := interpRat q92, hi := interpRat q93, piece := refinementPiece107}
theorem maxcheck_82 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) s82 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s82, q92, q93, interpRat, refinementPiece107, MacroPiece.box]

def c83 : CompactSegment := {lo := q93, hi := q94, pieceRef := 56}
def s83 : SourceSegment := {lo := interpRat q93, hi := interpRat q94, piece := refinementPiece108}
theorem maxcheck_83 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) s83 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s83, q93, q94, interpRat, refinementPiece108, MacroPiece.box]

def c84 : CompactSegment := {lo := q94, hi := q95, pieceRef := 57}
def s84 : SourceSegment := {lo := interpRat q94, hi := interpRat q95, piece := refinementPiece109}
theorem maxcheck_84 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) s84 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s84, q94, q95, interpRat, refinementPiece109, MacroPiece.box]

def c85 : CompactSegment := {lo := q95, hi := q96, pieceRef := 58}
def s85 : SourceSegment := {lo := interpRat q95, hi := interpRat q96, piece := refinementPiece110}
theorem maxcheck_85 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) s85 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s85, q95, q96, interpRat, refinementPiece110, MacroPiece.box]

def c86 : CompactSegment := {lo := q96, hi := q97, pieceRef := 59}
def s86 : SourceSegment := {lo := interpRat q96, hi := interpRat q97, piece := refinementPiece111}
theorem maxcheck_86 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) s86 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s86, q96, q97, interpRat, refinementPiece111, MacroPiece.box]

def c87 : CompactSegment := {lo := q97, hi := q98, pieceRef := 60}
def s87 : SourceSegment := {lo := interpRat q97, hi := interpRat q98, piece := refinementPiece112}
theorem maxcheck_87 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) s87 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s87, q97, q98, interpRat, refinementPiece112, MacroPiece.box]

def c88 : CompactSegment := {lo := q98, hi := q99, pieceRef := 61}
def s88 : SourceSegment := {lo := interpRat q98, hi := interpRat q99, piece := refinementPiece113}
theorem maxcheck_88 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) s88 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s88, q98, q99, interpRat, refinementPiece113, MacroPiece.box]

def c89 : CompactSegment := {lo := q99, hi := q100, pieceRef := 62}
def s89 : SourceSegment := {lo := interpRat q99, hi := interpRat q100, piece := refinementPiece114}
theorem maxcheck_89 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) s89 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s89, q99, q100, interpRat, refinementPiece114, MacroPiece.box]

def c90 : CompactSegment := {lo := q99, hi := q101, pieceRef := 62}
def s90 : SourceSegment := {lo := interpRat q99, hi := interpRat q101, piece := refinementPiece114}
theorem maxcheck_90 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) s90 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s90, q99, q101, interpRat, refinementPiece114, MacroPiece.box]

def c91 : CompactSegment := {lo := q101, hi := q102, pieceRef := 90}
def s91 : SourceSegment := {lo := interpRat q101, hi := interpRat q102, piece := refinementPiece115}
theorem maxcheck_91 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) s91 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s91, q101, q102, interpRat, refinementPiece115, MacroPiece.box]

def c92 : CompactSegment := {lo := q102, hi := q103, pieceRef := 91}
def s92 : SourceSegment := {lo := interpRat q102, hi := interpRat q103, piece := refinementPiece116}
theorem maxcheck_92 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) s92 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s92, q102, q103, interpRat, refinementPiece116, MacroPiece.box]

def c93 : CompactSegment := {lo := q103, hi := q104, pieceRef := 92}
def s93 : SourceSegment := {lo := interpRat q103, hi := interpRat q104, piece := refinementPiece117}
theorem maxcheck_93 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) s93 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s93, q103, q104, interpRat, refinementPiece117, MacroPiece.box]

def c94 : CompactSegment := {lo := q104, hi := q105, pieceRef := 93}
def s94 : SourceSegment := {lo := interpRat q104, hi := interpRat q105, piece := refinementPiece118}
theorem maxcheck_94 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) s94 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s94, q104, q105, interpRat, refinementPiece118, MacroPiece.box]

def c95 : CompactSegment := {lo := q105, hi := q106, pieceRef := 94}
def s95 : SourceSegment := {lo := interpRat q105, hi := interpRat q106, piece := refinementPiece119}
theorem maxcheck_95 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) s95 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s95, q105, q106, interpRat, refinementPiece119, MacroPiece.box]

def c96 : CompactSegment := {lo := q106, hi := q107, pieceRef := 95}
def s96 : SourceSegment := {lo := interpRat q106, hi := interpRat q107, piece := macroPiece25}
theorem maxcheck_96 : sourceSegmentCheck (6876046637736468087644507155946023489/80000000000000000000000000000000000000000) s96 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s96, q106, q107, interpRat, macroPiece25, MacroPiece.box]

def c97 : CompactSegment := {lo := q108, hi := q109, pieceRef := 63}
def s97 : SourceSegment := {lo := interpRat q108, hi := interpRat q109, piece := refinementPiece160}
theorem maxcheck_97 : sourceSegmentCheck (7594713117315031921983662976367761841/80000000000000000000000000000000000000000) s97 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s97, q108, q109, interpRat, refinementPiece160, MacroPiece.box]

def c98 : CompactSegment := {lo := q109, hi := q110, pieceRef := 64}
def s98 : SourceSegment := {lo := interpRat q109, hi := interpRat q110, piece := refinementPiece161}
theorem maxcheck_98 : sourceSegmentCheck (7594713117315031921983662976367761841/80000000000000000000000000000000000000000) s98 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s98, q109, q110, interpRat, refinementPiece161, MacroPiece.box]

def c99 : CompactSegment := {lo := q110, hi := q111, pieceRef := 65}
def s99 : SourceSegment := {lo := interpRat q110, hi := interpRat q111, piece := refinementPiece162}
theorem maxcheck_99 : sourceSegmentCheck (7594713117315031921983662976367761841/80000000000000000000000000000000000000000) s99 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s99, q110, q111, interpRat, refinementPiece162, MacroPiece.box]

def c100 : CompactSegment := {lo := q111, hi := q112, pieceRef := 66}
def s100 : SourceSegment := {lo := interpRat q111, hi := interpRat q112, piece := refinementPiece163}
theorem maxcheck_100 : sourceSegmentCheck (7594713117315031921983662976367761841/80000000000000000000000000000000000000000) s100 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s100, q111, q112, interpRat, refinementPiece163, MacroPiece.box]

def c101 : CompactSegment := {lo := q112, hi := q113, pieceRef := 67}
def s101 : SourceSegment := {lo := interpRat q112, hi := interpRat q113, piece := refinementPiece164}
theorem maxcheck_101 : sourceSegmentCheck (7594713117315031921983662976367761841/80000000000000000000000000000000000000000) s101 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s101, q112, q113, interpRat, refinementPiece164, MacroPiece.box]

def c102 : CompactSegment := {lo := q113, hi := q114, pieceRef := 68}
def s102 : SourceSegment := {lo := interpRat q113, hi := interpRat q114, piece := refinementPiece165}
theorem maxcheck_102 : sourceSegmentCheck (7594713117315031921983662976367761841/80000000000000000000000000000000000000000) s102 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s102, q113, q114, interpRat, refinementPiece165, MacroPiece.box]

def c103 : CompactSegment := {lo := q114, hi := q115, pieceRef := 69}
def s103 : SourceSegment := {lo := interpRat q114, hi := interpRat q115, piece := refinementPiece166}
theorem maxcheck_103 : sourceSegmentCheck (7594713117315031921983662976367761841/80000000000000000000000000000000000000000) s103 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s103, q114, q115, interpRat, refinementPiece166, MacroPiece.box]

def c104 : CompactSegment := {lo := q115, hi := q116, pieceRef := 70}
def s104 : SourceSegment := {lo := interpRat q115, hi := interpRat q116, piece := refinementPiece167}
theorem maxcheck_104 : sourceSegmentCheck (7594713117315031921983662976367761841/80000000000000000000000000000000000000000) s104 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s104, q115, q116, interpRat, refinementPiece167, MacroPiece.box]

def c105 : CompactSegment := {lo := q116, hi := q117, pieceRef := 71}
def s105 : SourceSegment := {lo := interpRat q116, hi := interpRat q117, piece := macroPiece30}
theorem maxcheck_105 : sourceSegmentCheck (7594713117315031921983662976367761841/80000000000000000000000000000000000000000) s105 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s105, q116, q117, interpRat, macroPiece30, MacroPiece.box]

def c106 : CompactSegment := {lo := q117, hi := q118, pieceRef := 72}
def s106 : SourceSegment := {lo := interpRat q117, hi := interpRat q118, piece := macroPiece31}
theorem maxcheck_106 : sourceSegmentCheck (7594713117315031921983662976367761841/80000000000000000000000000000000000000000) s106 = true := by
  norm_num [sourceSegmentCheck, segmentMinimum, clampRational, s106, q117, q118, interpRat, macroPiece31, MacroPiece.box]

def wire0 : RowRef := .floor 6 [5,6,7,8,9,10,11,12,13]
def row0 : CompactRow := .floor q6 [c5,c6,c7,c8,c9,c10,c11,c12,c13]
def segments0 : List SourceSegment := [s5,s6,s7,s8,s9,s10,s11,s12,s13]
def model0 : ModelRow := .floor (interpRat q6) segments0
theorem rowseg_0_5 : sourceSegmentCheck (interpRat q6) s5 = true :=
  segmentCheck_mono (by norm_num [interpRat, q6]) maxcheck_5
theorem rowseg_0_6 : sourceSegmentCheck (interpRat q6) s6 = true :=
  segmentCheck_mono (by norm_num [interpRat, q6]) maxcheck_6
theorem rowseg_0_7 : sourceSegmentCheck (interpRat q6) s7 = true :=
  segmentCheck_mono (by norm_num [interpRat, q6]) maxcheck_7
theorem rowseg_0_8 : sourceSegmentCheck (interpRat q6) s8 = true :=
  segmentCheck_mono (by norm_num [interpRat, q6]) maxcheck_8
theorem rowseg_0_9 : sourceSegmentCheck (interpRat q6) s9 = true :=
  segmentCheck_mono (by norm_num [interpRat, q6]) maxcheck_9
theorem rowseg_0_10 : sourceSegmentCheck (interpRat q6) s10 = true :=
  segmentCheck_mono (by norm_num [interpRat, q6]) maxcheck_10
theorem rowseg_0_11 : sourceSegmentCheck (interpRat q6) s11 = true :=
  segmentCheck_mono (by norm_num [interpRat, q6]) maxcheck_11
theorem rowseg_0_12 : sourceSegmentCheck (interpRat q6) s12 = true :=
  segmentCheck_mono (by norm_num [interpRat, q6]) maxcheck_12
theorem rowseg_0_13 : sourceSegmentCheck (interpRat q6) s13 = true :=
  segmentCheck_mono (by norm_num [interpRat, q6]) maxcheck_13
theorem coverage_0 : sourceCoverFrom (405/64) (825/128) segments0 = true := by
  norm_num [sourceCoverFrom, segments0, s5, s6, s7, s8, s9, s10, s11, s12, s13, q13, q14, q15, q16, q17, q18, q19, q20, q21, q22, interpRat]
theorem piecewise_0 : certifiedPiecewiseCheck (405/64) (825/128) (interpRat q6) segments0 = true := by
  have hn : decide (0 < segments0.length) = true := by norm_num [segments0]
  have hs : segments0.all (sourceSegmentCheck (interpRat q6)) = true := by
    simp only [segments0, List.all_cons, List.all_nil, rowseg_0_5, rowseg_0_6, rowseg_0_7, rowseg_0_8, rowseg_0_9, rowseg_0_10, rowseg_0_11, rowseg_0_12, rowseg_0_13, Bool.true_and]
  have hp : segments0.all (fun s => s.piece.check) = true := by
    simp only [segments0, s5, s6, s7, s8, s9, s10, s11, s12, s13, List.all_cons, List.all_nil, refinementPiece3_check, refinementPiece4_check, refinementPiece5_check, refinementPiece6_check, refinementPiece7_check, refinementPiece8_check, refinementPiece9_check, refinementPiece10_check, refinementPiece11_check, Bool.true_and]
  simp [certifiedPiecewiseCheck, sourcePiecewiseCheck, hn, coverage_0, hs, hp]

theorem wire_success_0 : decodeRow qs segmentRefs catalog wire0 = some row0 := by rfl
theorem model_success_0 : interpCompactRow catalog row0 = some model0 := by rfl
theorem canonical_0 : compactRowCanonical row0 = true := by decide
def wire1 : RowRef := .direct 9
def row1 : CompactRow := .direct 9
def model1 : ModelRow := .direct macroPiece11
theorem wire_success_1 : decodeRow qs segmentRefs catalog wire1 = some row1 := by rfl
theorem model_success_1 : interpCompactRow catalog row1 = some model1 := by rfl
theorem canonical_1 : compactRowCanonical row1 = true := by decide
def wire2 : RowRef := .floor 1 [32,33,34,35,36,37,38,39,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55]
def row2 : CompactRow := .floor q1 [c32,c33,c34,c35,c36,c37,c38,c39,c41,c42,c43,c44,c45,c46,c47,c48,c49,c50,c51,c52,c53,c54,c55]
def segments2 : List SourceSegment := [s32,s33,s34,s35,s36,s37,s38,s39,s41,s42,s43,s44,s45,s46,s47,s48,s49,s50,s51,s52,s53,s54,s55]
def model2 : ModelRow := .floor (interpRat q1) segments2
theorem rowseg_2_32 : sourceSegmentCheck (interpRat q1) s32 = true :=
  segmentCheck_mono (by norm_num [interpRat, q1]) maxcheck_32
theorem rowseg_2_33 : sourceSegmentCheck (interpRat q1) s33 = true :=
  segmentCheck_mono (by norm_num [interpRat, q1]) maxcheck_33
theorem rowseg_2_34 : sourceSegmentCheck (interpRat q1) s34 = true :=
  segmentCheck_mono (by norm_num [interpRat, q1]) maxcheck_34
theorem rowseg_2_35 : sourceSegmentCheck (interpRat q1) s35 = true :=
  segmentCheck_mono (by norm_num [interpRat, q1]) maxcheck_35
theorem rowseg_2_36 : sourceSegmentCheck (interpRat q1) s36 = true :=
  segmentCheck_mono (by norm_num [interpRat, q1]) maxcheck_36
theorem rowseg_2_37 : sourceSegmentCheck (interpRat q1) s37 = true :=
  segmentCheck_mono (by norm_num [interpRat, q1]) maxcheck_37
theorem rowseg_2_38 : sourceSegmentCheck (interpRat q1) s38 = true :=
  segmentCheck_mono (by norm_num [interpRat, q1]) maxcheck_38
theorem rowseg_2_39 : sourceSegmentCheck (interpRat q1) s39 = true :=
  segmentCheck_mono (by norm_num [interpRat, q1]) maxcheck_39
theorem rowseg_2_41 : sourceSegmentCheck (interpRat q1) s41 = true :=
  segmentCheck_mono (by norm_num [interpRat, q1]) maxcheck_41
theorem rowseg_2_42 : sourceSegmentCheck (interpRat q1) s42 = true :=
  segmentCheck_mono (by norm_num [interpRat, q1]) maxcheck_42
theorem rowseg_2_43 : sourceSegmentCheck (interpRat q1) s43 = true :=
  segmentCheck_mono (by norm_num [interpRat, q1]) maxcheck_43
theorem rowseg_2_44 : sourceSegmentCheck (interpRat q1) s44 = true :=
  segmentCheck_mono (by norm_num [interpRat, q1]) maxcheck_44
theorem rowseg_2_45 : sourceSegmentCheck (interpRat q1) s45 = true :=
  segmentCheck_mono (by norm_num [interpRat, q1]) maxcheck_45
theorem rowseg_2_46 : sourceSegmentCheck (interpRat q1) s46 = true :=
  segmentCheck_mono (by norm_num [interpRat, q1]) maxcheck_46
theorem rowseg_2_47 : sourceSegmentCheck (interpRat q1) s47 = true :=
  segmentCheck_mono (by norm_num [interpRat, q1]) maxcheck_47
theorem rowseg_2_48 : sourceSegmentCheck (interpRat q1) s48 = true :=
  segmentCheck_mono (by norm_num [interpRat, q1]) maxcheck_48
theorem rowseg_2_49 : sourceSegmentCheck (interpRat q1) s49 = true :=
  segmentCheck_mono (by norm_num [interpRat, q1]) maxcheck_49
theorem rowseg_2_50 : sourceSegmentCheck (interpRat q1) s50 = true :=
  segmentCheck_mono (by norm_num [interpRat, q1]) maxcheck_50
theorem rowseg_2_51 : sourceSegmentCheck (interpRat q1) s51 = true :=
  segmentCheck_mono (by norm_num [interpRat, q1]) maxcheck_51
theorem rowseg_2_52 : sourceSegmentCheck (interpRat q1) s52 = true :=
  segmentCheck_mono (by norm_num [interpRat, q1]) maxcheck_52
theorem rowseg_2_53 : sourceSegmentCheck (interpRat q1) s53 = true :=
  segmentCheck_mono (by norm_num [interpRat, q1]) maxcheck_53
theorem rowseg_2_54 : sourceSegmentCheck (interpRat q1) s54 = true :=
  segmentCheck_mono (by norm_num [interpRat, q1]) maxcheck_54
theorem rowseg_2_55 : sourceSegmentCheck (interpRat q1) s55 = true :=
  segmentCheck_mono (by norm_num [interpRat, q1]) maxcheck_55
theorem coverage_2 : sourceCoverFrom (1215/64) (2475/128) segments2 = true := by
  norm_num [sourceCoverFrom, segments2, s32, s33, s34, s35, s36, s37, s38, s39, s41, s42, s43, s44, s45, s46, s47, s48, s49, s50, s51, s52, s53, s54, s55, q41, q42, q43, q44, q45, q46, q47, q48, q50, q51, q52, q53, q54, q55, q56, q57, q58, q59, q60, q61, q62, q63, q64, q65, interpRat]
theorem piecewise_2 : certifiedPiecewiseCheck (1215/64) (2475/128) (interpRat q1) segments2 = true := by
  have hn : decide (0 < segments2.length) = true := by norm_num [segments2]
  have hs : segments2.all (sourceSegmentCheck (interpRat q1)) = true := by
    simp only [segments2, List.all_cons, List.all_nil, rowseg_2_32, rowseg_2_33, rowseg_2_34, rowseg_2_35, rowseg_2_36, rowseg_2_37, rowseg_2_38, rowseg_2_39, rowseg_2_41, rowseg_2_42, rowseg_2_43, rowseg_2_44, rowseg_2_45, rowseg_2_46, rowseg_2_47, rowseg_2_48, rowseg_2_49, rowseg_2_50, rowseg_2_51, rowseg_2_52, rowseg_2_53, rowseg_2_54, rowseg_2_55, Bool.true_and]
  have hp : segments2.all (fun s => s.piece.check) = true := by
    simp only [segments2, s32, s33, s34, s35, s36, s37, s38, s39, s41, s42, s43, s44, s45, s46, s47, s48, s49, s50, s51, s52, s53, s54, s55, List.all_cons, List.all_nil, refinementPiece48_check, refinementPiece49_check, refinementPiece50_check, refinementPiece51_check, refinementPiece52_check, refinementPiece53_check, refinementPiece54_check, refinementPiece55_check, refinementPiece56_check, refinementPiece57_check, refinementPiece58_check, refinementPiece59_check, refinementPiece60_check, refinementPiece61_check, refinementPiece62_check, refinementPiece63_check, refinementPiece64_check, refinementPiece65_check, refinementPiece66_check, refinementPiece67_check, refinementPiece68_check, refinementPiece69_check, refinementPiece70_check, Bool.true_and]
  simp [certifiedPiecewiseCheck, sourcePiecewiseCheck, hn, coverage_2, hs, hp]

theorem wire_success_2 : decodeRow qs segmentRefs catalog wire2 = some row2 := by rfl
theorem model_success_2 : interpCompactRow catalog row2 = some model2 := by rfl
theorem canonical_2 : compactRowCanonical row2 = true := by decide
def wire3 : RowRef := .floor 3 [59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89]
def row3 : CompactRow := .floor q3 [c59,c60,c61,c62,c63,c64,c65,c66,c67,c68,c69,c70,c71,c72,c73,c74,c75,c76,c77,c78,c79,c80,c81,c82,c83,c84,c85,c86,c87,c88,c89]
def segments3 : List SourceSegment := [s59,s60,s61,s62,s63,s64,s65,s66,s67,s68,s69,s70,s71,s72,s73,s74,s75,s76,s77,s78,s79,s80,s81,s82,s83,s84,s85,s86,s87,s88,s89]
def model3 : ModelRow := .floor (interpRat q3) segments3
theorem rowseg_3_59 : sourceSegmentCheck (interpRat q3) s59 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_59
theorem rowseg_3_60 : sourceSegmentCheck (interpRat q3) s60 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_60
theorem rowseg_3_61 : sourceSegmentCheck (interpRat q3) s61 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_61
theorem rowseg_3_62 : sourceSegmentCheck (interpRat q3) s62 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_62
theorem rowseg_3_63 : sourceSegmentCheck (interpRat q3) s63 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_63
theorem rowseg_3_64 : sourceSegmentCheck (interpRat q3) s64 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_64
theorem rowseg_3_65 : sourceSegmentCheck (interpRat q3) s65 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_65
theorem rowseg_3_66 : sourceSegmentCheck (interpRat q3) s66 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_66
theorem rowseg_3_67 : sourceSegmentCheck (interpRat q3) s67 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_67
theorem rowseg_3_68 : sourceSegmentCheck (interpRat q3) s68 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_68
theorem rowseg_3_69 : sourceSegmentCheck (interpRat q3) s69 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_69
theorem rowseg_3_70 : sourceSegmentCheck (interpRat q3) s70 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_70
theorem rowseg_3_71 : sourceSegmentCheck (interpRat q3) s71 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_71
theorem rowseg_3_72 : sourceSegmentCheck (interpRat q3) s72 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_72
theorem rowseg_3_73 : sourceSegmentCheck (interpRat q3) s73 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_73
theorem rowseg_3_74 : sourceSegmentCheck (interpRat q3) s74 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_74
theorem rowseg_3_75 : sourceSegmentCheck (interpRat q3) s75 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_75
theorem rowseg_3_76 : sourceSegmentCheck (interpRat q3) s76 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_76
theorem rowseg_3_77 : sourceSegmentCheck (interpRat q3) s77 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_77
theorem rowseg_3_78 : sourceSegmentCheck (interpRat q3) s78 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_78
theorem rowseg_3_79 : sourceSegmentCheck (interpRat q3) s79 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_79
theorem rowseg_3_80 : sourceSegmentCheck (interpRat q3) s80 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_80
theorem rowseg_3_81 : sourceSegmentCheck (interpRat q3) s81 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_81
theorem rowseg_3_82 : sourceSegmentCheck (interpRat q3) s82 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_82
theorem rowseg_3_83 : sourceSegmentCheck (interpRat q3) s83 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_83
theorem rowseg_3_84 : sourceSegmentCheck (interpRat q3) s84 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_84
theorem rowseg_3_85 : sourceSegmentCheck (interpRat q3) s85 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_85
theorem rowseg_3_86 : sourceSegmentCheck (interpRat q3) s86 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_86
theorem rowseg_3_87 : sourceSegmentCheck (interpRat q3) s87 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_87
theorem rowseg_3_88 : sourceSegmentCheck (interpRat q3) s88 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_88
theorem rowseg_3_89 : sourceSegmentCheck (interpRat q3) s89 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_89
theorem coverage_3 : sourceCoverFrom (3255/128) (3315/128) segments3 = true := by
  norm_num [sourceCoverFrom, segments3, s59, s60, s61, s62, s63, s64, s65, s66, s67, s68, s69, s70, s71, s72, s73, s74, s75, s76, s77, s78, s79, s80, s81, s82, s83, s84, s85, s86, s87, s88, s89, q69, q70, q71, q72, q73, q74, q75, q76, q77, q78, q79, q80, q81, q82, q83, q84, q85, q86, q87, q88, q89, q90, q91, q92, q93, q94, q95, q96, q97, q98, q99, q100, interpRat]
theorem piecewise_3 : certifiedPiecewiseCheck (3255/128) (3315/128) (interpRat q3) segments3 = true := by
  have hn : decide (0 < segments3.length) = true := by norm_num [segments3]
  have hs : segments3.all (sourceSegmentCheck (interpRat q3)) = true := by
    simp only [segments3, List.all_cons, List.all_nil, rowseg_3_59, rowseg_3_60, rowseg_3_61, rowseg_3_62, rowseg_3_63, rowseg_3_64, rowseg_3_65, rowseg_3_66, rowseg_3_67, rowseg_3_68, rowseg_3_69, rowseg_3_70, rowseg_3_71, rowseg_3_72, rowseg_3_73, rowseg_3_74, rowseg_3_75, rowseg_3_76, rowseg_3_77, rowseg_3_78, rowseg_3_79, rowseg_3_80, rowseg_3_81, rowseg_3_82, rowseg_3_83, rowseg_3_84, rowseg_3_85, rowseg_3_86, rowseg_3_87, rowseg_3_88, rowseg_3_89, Bool.true_and]
  have hp : segments3.all (fun s => s.piece.check) = true := by
    simp only [segments3, s59, s60, s61, s62, s63, s64, s65, s66, s67, s68, s69, s70, s71, s72, s73, s74, s75, s76, s77, s78, s79, s80, s81, s82, s83, s84, s85, s86, s87, s88, s89, List.all_cons, List.all_nil, refinementPiece84_check, refinementPiece85_check, refinementPiece86_check, refinementPiece87_check, refinementPiece88_check, refinementPiece89_check, refinementPiece90_check, refinementPiece91_check, refinementPiece92_check, refinementPiece93_check, refinementPiece94_check, refinementPiece95_check, macroPiece24_check, refinementPiece98_check, refinementPiece99_check, refinementPiece100_check, refinementPiece101_check, refinementPiece102_check, refinementPiece103_check, refinementPiece104_check, refinementPiece105_check, refinementPiece106_check, refinementPiece107_check, refinementPiece108_check, refinementPiece109_check, refinementPiece110_check, refinementPiece111_check, refinementPiece112_check, refinementPiece113_check, refinementPiece114_check, Bool.true_and]
  simp [certifiedPiecewiseCheck, sourcePiecewiseCheck, hn, coverage_3, hs, hp]

theorem wire_success_3 : decodeRow qs segmentRefs catalog wire3 = some row3 := by rfl
theorem model_success_3 : interpCompactRow catalog row3 = some model3 := by rfl
theorem canonical_3 : compactRowCanonical row3 = true := by decide
def wire4 : RowRef := .floor 4 [97,98,99,100,101,102,103,104,105,106]
def row4 : CompactRow := .floor q4 [c97,c98,c99,c100,c101,c102,c103,c104,c105,c106]
def segments4 : List SourceSegment := [s97,s98,s99,s100,s101,s102,s103,s104,s105,s106]
def model4 : ModelRow := .floor (interpRat q4) segments4
theorem rowseg_4_97 : sourceSegmentCheck (interpRat q4) s97 = true :=
  segmentCheck_mono (by norm_num [interpRat, q4]) maxcheck_97
theorem rowseg_4_98 : sourceSegmentCheck (interpRat q4) s98 = true :=
  segmentCheck_mono (by norm_num [interpRat, q4]) maxcheck_98
theorem rowseg_4_99 : sourceSegmentCheck (interpRat q4) s99 = true :=
  segmentCheck_mono (by norm_num [interpRat, q4]) maxcheck_99
theorem rowseg_4_100 : sourceSegmentCheck (interpRat q4) s100 = true :=
  segmentCheck_mono (by norm_num [interpRat, q4]) maxcheck_100
theorem rowseg_4_101 : sourceSegmentCheck (interpRat q4) s101 = true :=
  segmentCheck_mono (by norm_num [interpRat, q4]) maxcheck_101
theorem rowseg_4_102 : sourceSegmentCheck (interpRat q4) s102 = true :=
  segmentCheck_mono (by norm_num [interpRat, q4]) maxcheck_102
theorem rowseg_4_103 : sourceSegmentCheck (interpRat q4) s103 = true :=
  segmentCheck_mono (by norm_num [interpRat, q4]) maxcheck_103
theorem rowseg_4_104 : sourceSegmentCheck (interpRat q4) s104 = true :=
  segmentCheck_mono (by norm_num [interpRat, q4]) maxcheck_104
theorem rowseg_4_105 : sourceSegmentCheck (interpRat q4) s105 = true :=
  segmentCheck_mono (by norm_num [interpRat, q4]) maxcheck_105
theorem rowseg_4_106 : sourceSegmentCheck (interpRat q4) s106 = true :=
  segmentCheck_mono (by norm_num [interpRat, q4]) maxcheck_106
theorem coverage_4 : sourceCoverFrom (4065/128) (4155/128) segments4 = true := by
  norm_num [sourceCoverFrom, segments4, s97, s98, s99, s100, s101, s102, s103, s104, s105, s106, q108, q109, q110, q111, q112, q113, q114, q115, q116, q117, q118, interpRat]
theorem piecewise_4 : certifiedPiecewiseCheck (4065/128) (4155/128) (interpRat q4) segments4 = true := by
  have hn : decide (0 < segments4.length) = true := by norm_num [segments4]
  have hs : segments4.all (sourceSegmentCheck (interpRat q4)) = true := by
    simp only [segments4, List.all_cons, List.all_nil, rowseg_4_97, rowseg_4_98, rowseg_4_99, rowseg_4_100, rowseg_4_101, rowseg_4_102, rowseg_4_103, rowseg_4_104, rowseg_4_105, rowseg_4_106, Bool.true_and]
  have hp : segments4.all (fun s => s.piece.check) = true := by
    simp only [segments4, s97, s98, s99, s100, s101, s102, s103, s104, s105, s106, List.all_cons, List.all_nil, refinementPiece160_check, refinementPiece161_check, refinementPiece162_check, refinementPiece163_check, refinementPiece164_check, refinementPiece165_check, refinementPiece166_check, refinementPiece167_check, macroPiece30_check, macroPiece31_check, Bool.true_and]
  simp [certifiedPiecewiseCheck, sourcePiecewiseCheck, hn, coverage_4, hs, hp]

theorem wire_success_4 : decodeRow qs segmentRefs catalog wire4 = some row4 := by rfl
theorem model_success_4 : interpCompactRow catalog row4 = some model4 := by rfl
theorem canonical_4 : compactRowCanonical row4 = true := by decide
def wire5 : RowRef := .floor 5 [15,16,17,18,19,20,21,22]
def row5 : CompactRow := .floor q5 [c15,c16,c17,c18,c19,c20,c21,c22]
def segments5 : List SourceSegment := [s15,s16,s17,s18,s19,s20,s21,s22]
def model5 : ModelRow := .floor (interpRat q5) segments5
theorem rowseg_5_15 : sourceSegmentCheck (interpRat q5) s15 = true :=
  segmentCheck_mono (by norm_num [interpRat, q5]) maxcheck_15
theorem rowseg_5_16 : sourceSegmentCheck (interpRat q5) s16 = true :=
  segmentCheck_mono (by norm_num [interpRat, q5]) maxcheck_16
theorem rowseg_5_17 : sourceSegmentCheck (interpRat q5) s17 = true :=
  segmentCheck_mono (by norm_num [interpRat, q5]) maxcheck_17
theorem rowseg_5_18 : sourceSegmentCheck (interpRat q5) s18 = true :=
  segmentCheck_mono (by norm_num [interpRat, q5]) maxcheck_18
theorem rowseg_5_19 : sourceSegmentCheck (interpRat q5) s19 = true :=
  segmentCheck_mono (by norm_num [interpRat, q5]) maxcheck_19
theorem rowseg_5_20 : sourceSegmentCheck (interpRat q5) s20 = true :=
  segmentCheck_mono (by norm_num [interpRat, q5]) maxcheck_20
theorem rowseg_5_21 : sourceSegmentCheck (interpRat q5) s21 = true :=
  segmentCheck_mono (by norm_num [interpRat, q5]) maxcheck_21
theorem rowseg_5_22 : sourceSegmentCheck (interpRat q5) s22 = true :=
  segmentCheck_mono (by norm_num [interpRat, q5]) maxcheck_22
theorem coverage_5 : sourceCoverFrom (825/128) (105/16) segments5 = true := by
  norm_num [sourceCoverFrom, segments5, s15, s16, s17, s18, s19, s20, s21, s22, q22, q23, q24, q25, q26, q27, q28, q29, q30, interpRat]
theorem piecewise_5 : certifiedPiecewiseCheck (825/128) (105/16) (interpRat q5) segments5 = true := by
  have hn : decide (0 < segments5.length) = true := by norm_num [segments5]
  have hs : segments5.all (sourceSegmentCheck (interpRat q5)) = true := by
    simp only [segments5, List.all_cons, List.all_nil, rowseg_5_15, rowseg_5_16, rowseg_5_17, rowseg_5_18, rowseg_5_19, rowseg_5_20, rowseg_5_21, rowseg_5_22, Bool.true_and]
  have hp : segments5.all (fun s => s.piece.check) = true := by
    simp only [segments5, s15, s16, s17, s18, s19, s20, s21, s22, List.all_cons, List.all_nil, refinementPiece11_check, refinementPiece12_check, refinementPiece13_check, refinementPiece14_check, refinementPiece15_check, refinementPiece16_check, refinementPiece17_check, refinementPiece18_check, Bool.true_and]
  simp [certifiedPiecewiseCheck, sourcePiecewiseCheck, hn, coverage_5, hs, hp]

theorem wire_success_5 : decodeRow qs segmentRefs catalog wire5 = some row5 := by rfl
theorem model_success_5 : interpCompactRow catalog row5 = some model5 := by rfl
theorem canonical_5 : compactRowCanonical row5 = true := by decide
def wire6 : RowRef := .floor 0 [23,24,25,26,27,28,29,30,31]
def row6 : CompactRow := .floor q0 [c23,c24,c25,c26,c27,c28,c29,c30,c31]
def segments6 : List SourceSegment := [s23,s24,s25,s26,s27,s28,s29,s30,s31]
def model6 : ModelRow := .floor (interpRat q0) segments6
theorem rowseg_6_23 : sourceSegmentCheck (interpRat q0) s23 = true :=
  segmentCheck_mono (by norm_num [interpRat, q0]) maxcheck_23
theorem rowseg_6_24 : sourceSegmentCheck (interpRat q0) s24 = true :=
  segmentCheck_mono (by norm_num [interpRat, q0]) maxcheck_24
theorem rowseg_6_25 : sourceSegmentCheck (interpRat q0) s25 = true :=
  segmentCheck_mono (by norm_num [interpRat, q0]) maxcheck_25
theorem rowseg_6_26 : sourceSegmentCheck (interpRat q0) s26 = true :=
  segmentCheck_mono (by norm_num [interpRat, q0]) maxcheck_26
theorem rowseg_6_27 : sourceSegmentCheck (interpRat q0) s27 = true :=
  segmentCheck_mono (by norm_num [interpRat, q0]) maxcheck_27
theorem rowseg_6_28 : sourceSegmentCheck (interpRat q0) s28 = true :=
  segmentCheck_mono (by norm_num [interpRat, q0]) maxcheck_28
theorem rowseg_6_29 : sourceSegmentCheck (interpRat q0) s29 = true :=
  segmentCheck_mono (by norm_num [interpRat, q0]) maxcheck_29
theorem rowseg_6_30 : sourceSegmentCheck (interpRat q0) s30 = true :=
  segmentCheck_mono (by norm_num [interpRat, q0]) maxcheck_30
theorem rowseg_6_31 : sourceSegmentCheck (interpRat q0) s31 = true :=
  segmentCheck_mono (by norm_num [interpRat, q0]) maxcheck_31
theorem coverage_6 : sourceCoverFrom (405/32) (825/64) segments6 = true := by
  norm_num [sourceCoverFrom, segments6, s23, s24, s25, s26, s27, s28, s29, s30, s31, q31, q32, q33, q34, q35, q36, q37, q38, q39, q40, interpRat]
theorem piecewise_6 : certifiedPiecewiseCheck (405/32) (825/64) (interpRat q0) segments6 = true := by
  have hn : decide (0 < segments6.length) = true := by norm_num [segments6]
  have hs : segments6.all (sourceSegmentCheck (interpRat q0)) = true := by
    simp only [segments6, List.all_cons, List.all_nil, rowseg_6_23, rowseg_6_24, rowseg_6_25, rowseg_6_26, rowseg_6_27, rowseg_6_28, rowseg_6_29, rowseg_6_30, rowseg_6_31, Bool.true_and]
  have hp : segments6.all (fun s => s.piece.check) = true := by
    simp only [segments6, s23, s24, s25, s26, s27, s28, s29, s30, s31, List.all_cons, List.all_nil, refinementPiece41_check, refinementPiece42_check, refinementPiece43_check, refinementPiece44_check, refinementPiece45_check, refinementPiece46_check, macroPiece9_check, macroPiece10_check, macroPiece11_check, Bool.true_and]
  simp [certifiedPiecewiseCheck, sourcePiecewiseCheck, hn, coverage_6, hs, hp]

theorem wire_success_6 : decodeRow qs segmentRefs catalog wire6 = some row6 := by rfl
theorem model_success_6 : interpCompactRow catalog row6 = some model6 := by rfl
theorem canonical_6 : compactRowCanonical row6 = true := by decide
def wire7 : RowRef := .floor 2 [40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,56,57,58]
def row7 : CompactRow := .floor q2 [c40,c41,c42,c43,c44,c45,c46,c47,c48,c49,c50,c51,c52,c53,c54,c56,c57,c58]
def segments7 : List SourceSegment := [s40,s41,s42,s43,s44,s45,s46,s47,s48,s49,s50,s51,s52,s53,s54,s56,s57,s58]
def model7 : ModelRow := .floor (interpRat q2) segments7
theorem rowseg_7_40 : sourceSegmentCheck (interpRat q2) s40 = true :=
  segmentCheck_mono (by norm_num [interpRat, q2]) maxcheck_40
theorem rowseg_7_41 : sourceSegmentCheck (interpRat q2) s41 = true :=
  segmentCheck_mono (by norm_num [interpRat, q2]) maxcheck_41
theorem rowseg_7_42 : sourceSegmentCheck (interpRat q2) s42 = true :=
  segmentCheck_mono (by norm_num [interpRat, q2]) maxcheck_42
theorem rowseg_7_43 : sourceSegmentCheck (interpRat q2) s43 = true :=
  segmentCheck_mono (by norm_num [interpRat, q2]) maxcheck_43
theorem rowseg_7_44 : sourceSegmentCheck (interpRat q2) s44 = true :=
  segmentCheck_mono (by norm_num [interpRat, q2]) maxcheck_44
theorem rowseg_7_45 : sourceSegmentCheck (interpRat q2) s45 = true :=
  segmentCheck_mono (by norm_num [interpRat, q2]) maxcheck_45
theorem rowseg_7_46 : sourceSegmentCheck (interpRat q2) s46 = true :=
  segmentCheck_mono (by norm_num [interpRat, q2]) maxcheck_46
theorem rowseg_7_47 : sourceSegmentCheck (interpRat q2) s47 = true :=
  segmentCheck_mono (by norm_num [interpRat, q2]) maxcheck_47
theorem rowseg_7_48 : sourceSegmentCheck (interpRat q2) s48 = true :=
  segmentCheck_mono (by norm_num [interpRat, q2]) maxcheck_48
theorem rowseg_7_49 : sourceSegmentCheck (interpRat q2) s49 = true :=
  segmentCheck_mono (by norm_num [interpRat, q2]) maxcheck_49
theorem rowseg_7_50 : sourceSegmentCheck (interpRat q2) s50 = true :=
  segmentCheck_mono (by norm_num [interpRat, q2]) maxcheck_50
theorem rowseg_7_51 : sourceSegmentCheck (interpRat q2) s51 = true :=
  segmentCheck_mono (by norm_num [interpRat, q2]) maxcheck_51
theorem rowseg_7_52 : sourceSegmentCheck (interpRat q2) s52 = true :=
  segmentCheck_mono (by norm_num [interpRat, q2]) maxcheck_52
theorem rowseg_7_53 : sourceSegmentCheck (interpRat q2) s53 = true :=
  segmentCheck_mono (by norm_num [interpRat, q2]) maxcheck_53
theorem rowseg_7_54 : sourceSegmentCheck (interpRat q2) s54 = true :=
  segmentCheck_mono (by norm_num [interpRat, q2]) maxcheck_54
theorem rowseg_7_56 : sourceSegmentCheck (interpRat q2) s56 = true :=
  segmentCheck_mono (by norm_num [interpRat, q2]) maxcheck_56
theorem rowseg_7_57 : sourceSegmentCheck (interpRat q2) s57 = true :=
  segmentCheck_mono (by norm_num [interpRat, q2]) maxcheck_57
theorem rowseg_7_58 : sourceSegmentCheck (interpRat q2) s58 = true :=
  segmentCheck_mono (by norm_num [interpRat, q2]) maxcheck_58
theorem coverage_7 : sourceCoverFrom (2445/128) (1245/64) segments7 = true := by
  norm_num [sourceCoverFrom, segments7, s40, s41, s42, s43, s44, s45, s46, s47, s48, s49, s50, s51, s52, s53, s54, s56, s57, s58, q49, q50, q51, q52, q53, q54, q55, q56, q57, q58, q59, q60, q61, q62, q63, q64, q66, q67, q68, interpRat]
theorem piecewise_7 : certifiedPiecewiseCheck (2445/128) (1245/64) (interpRat q2) segments7 = true := by
  have hn : decide (0 < segments7.length) = true := by norm_num [segments7]
  have hs : segments7.all (sourceSegmentCheck (interpRat q2)) = true := by
    simp only [segments7, List.all_cons, List.all_nil, rowseg_7_40, rowseg_7_41, rowseg_7_42, rowseg_7_43, rowseg_7_44, rowseg_7_45, rowseg_7_46, rowseg_7_47, rowseg_7_48, rowseg_7_49, rowseg_7_50, rowseg_7_51, rowseg_7_52, rowseg_7_53, rowseg_7_54, rowseg_7_56, rowseg_7_57, rowseg_7_58, Bool.true_and]
  have hp : segments7.all (fun s => s.piece.check) = true := by
    simp only [segments7, s40, s41, s42, s43, s44, s45, s46, s47, s48, s49, s50, s51, s52, s53, s54, s56, s57, s58, List.all_cons, List.all_nil, refinementPiece55_check, refinementPiece56_check, refinementPiece57_check, refinementPiece58_check, refinementPiece59_check, refinementPiece60_check, refinementPiece61_check, refinementPiece62_check, refinementPiece63_check, refinementPiece64_check, refinementPiece65_check, refinementPiece66_check, refinementPiece67_check, refinementPiece68_check, refinementPiece69_check, refinementPiece70_check, refinementPiece71_check, macroPiece18_check, Bool.true_and]
  simp [certifiedPiecewiseCheck, sourcePiecewiseCheck, hn, coverage_7, hs, hp]

theorem wire_success_7 : decodeRow qs segmentRefs catalog wire7 = some row7 := by rfl
theorem model_success_7 : interpCompactRow catalog row7 = some model7 := by rfl
theorem canonical_7 : compactRowCanonical row7 = true := by decide
def wire8 : RowRef := .floor 3 [59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,90,91,92,93,94,95,96]
def row8 : CompactRow := .floor q3 [c59,c60,c61,c62,c63,c64,c65,c66,c67,c68,c69,c70,c71,c72,c73,c74,c75,c76,c77,c78,c79,c80,c81,c82,c83,c84,c85,c86,c87,c88,c90,c91,c92,c93,c94,c95,c96]
def segments8 : List SourceSegment := [s59,s60,s61,s62,s63,s64,s65,s66,s67,s68,s69,s70,s71,s72,s73,s74,s75,s76,s77,s78,s79,s80,s81,s82,s83,s84,s85,s86,s87,s88,s90,s91,s92,s93,s94,s95,s96]
def model8 : ModelRow := .floor (interpRat q3) segments8
theorem rowseg_8_59 : sourceSegmentCheck (interpRat q3) s59 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_59
theorem rowseg_8_60 : sourceSegmentCheck (interpRat q3) s60 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_60
theorem rowseg_8_61 : sourceSegmentCheck (interpRat q3) s61 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_61
theorem rowseg_8_62 : sourceSegmentCheck (interpRat q3) s62 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_62
theorem rowseg_8_63 : sourceSegmentCheck (interpRat q3) s63 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_63
theorem rowseg_8_64 : sourceSegmentCheck (interpRat q3) s64 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_64
theorem rowseg_8_65 : sourceSegmentCheck (interpRat q3) s65 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_65
theorem rowseg_8_66 : sourceSegmentCheck (interpRat q3) s66 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_66
theorem rowseg_8_67 : sourceSegmentCheck (interpRat q3) s67 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_67
theorem rowseg_8_68 : sourceSegmentCheck (interpRat q3) s68 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_68
theorem rowseg_8_69 : sourceSegmentCheck (interpRat q3) s69 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_69
theorem rowseg_8_70 : sourceSegmentCheck (interpRat q3) s70 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_70
theorem rowseg_8_71 : sourceSegmentCheck (interpRat q3) s71 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_71
theorem rowseg_8_72 : sourceSegmentCheck (interpRat q3) s72 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_72
theorem rowseg_8_73 : sourceSegmentCheck (interpRat q3) s73 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_73
theorem rowseg_8_74 : sourceSegmentCheck (interpRat q3) s74 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_74
theorem rowseg_8_75 : sourceSegmentCheck (interpRat q3) s75 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_75
theorem rowseg_8_76 : sourceSegmentCheck (interpRat q3) s76 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_76
theorem rowseg_8_77 : sourceSegmentCheck (interpRat q3) s77 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_77
theorem rowseg_8_78 : sourceSegmentCheck (interpRat q3) s78 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_78
theorem rowseg_8_79 : sourceSegmentCheck (interpRat q3) s79 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_79
theorem rowseg_8_80 : sourceSegmentCheck (interpRat q3) s80 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_80
theorem rowseg_8_81 : sourceSegmentCheck (interpRat q3) s81 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_81
theorem rowseg_8_82 : sourceSegmentCheck (interpRat q3) s82 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_82
theorem rowseg_8_83 : sourceSegmentCheck (interpRat q3) s83 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_83
theorem rowseg_8_84 : sourceSegmentCheck (interpRat q3) s84 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_84
theorem rowseg_8_85 : sourceSegmentCheck (interpRat q3) s85 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_85
theorem rowseg_8_86 : sourceSegmentCheck (interpRat q3) s86 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_86
theorem rowseg_8_87 : sourceSegmentCheck (interpRat q3) s87 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_87
theorem rowseg_8_88 : sourceSegmentCheck (interpRat q3) s88 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_88
theorem rowseg_8_90 : sourceSegmentCheck (interpRat q3) s90 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_90
theorem rowseg_8_91 : sourceSegmentCheck (interpRat q3) s91 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_91
theorem rowseg_8_92 : sourceSegmentCheck (interpRat q3) s92 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_92
theorem rowseg_8_93 : sourceSegmentCheck (interpRat q3) s93 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_93
theorem rowseg_8_94 : sourceSegmentCheck (interpRat q3) s94 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_94
theorem rowseg_8_95 : sourceSegmentCheck (interpRat q3) s95 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_95
theorem rowseg_8_96 : sourceSegmentCheck (interpRat q3) s96 = true :=
  segmentCheck_mono (by norm_num [interpRat, q3]) maxcheck_96
theorem coverage_8 : sourceCoverFrom (3255/128) (1665/64) segments8 = true := by
  norm_num [sourceCoverFrom, segments8, s59, s60, s61, s62, s63, s64, s65, s66, s67, s68, s69, s70, s71, s72, s73, s74, s75, s76, s77, s78, s79, s80, s81, s82, s83, s84, s85, s86, s87, s88, s90, s91, s92, s93, s94, s95, s96, q69, q70, q71, q72, q73, q74, q75, q76, q77, q78, q79, q80, q81, q82, q83, q84, q85, q86, q87, q88, q89, q90, q91, q92, q93, q94, q95, q96, q97, q98, q99, q101, q102, q103, q104, q105, q106, q107, interpRat]
theorem piecewise_8 : certifiedPiecewiseCheck (3255/128) (1665/64) (interpRat q3) segments8 = true := by
  have hn : decide (0 < segments8.length) = true := by norm_num [segments8]
  have hs : segments8.all (sourceSegmentCheck (interpRat q3)) = true := by
    simp only [segments8, List.all_cons, List.all_nil, rowseg_8_59, rowseg_8_60, rowseg_8_61, rowseg_8_62, rowseg_8_63, rowseg_8_64, rowseg_8_65, rowseg_8_66, rowseg_8_67, rowseg_8_68, rowseg_8_69, rowseg_8_70, rowseg_8_71, rowseg_8_72, rowseg_8_73, rowseg_8_74, rowseg_8_75, rowseg_8_76, rowseg_8_77, rowseg_8_78, rowseg_8_79, rowseg_8_80, rowseg_8_81, rowseg_8_82, rowseg_8_83, rowseg_8_84, rowseg_8_85, rowseg_8_86, rowseg_8_87, rowseg_8_88, rowseg_8_90, rowseg_8_91, rowseg_8_92, rowseg_8_93, rowseg_8_94, rowseg_8_95, rowseg_8_96, Bool.true_and]
  have hp : segments8.all (fun s => s.piece.check) = true := by
    simp only [segments8, s59, s60, s61, s62, s63, s64, s65, s66, s67, s68, s69, s70, s71, s72, s73, s74, s75, s76, s77, s78, s79, s80, s81, s82, s83, s84, s85, s86, s87, s88, s90, s91, s92, s93, s94, s95, s96, List.all_cons, List.all_nil, refinementPiece84_check, refinementPiece85_check, refinementPiece86_check, refinementPiece87_check, refinementPiece88_check, refinementPiece89_check, refinementPiece90_check, refinementPiece91_check, refinementPiece92_check, refinementPiece93_check, refinementPiece94_check, refinementPiece95_check, macroPiece24_check, refinementPiece98_check, refinementPiece99_check, refinementPiece100_check, refinementPiece101_check, refinementPiece102_check, refinementPiece103_check, refinementPiece104_check, refinementPiece105_check, refinementPiece106_check, refinementPiece107_check, refinementPiece108_check, refinementPiece109_check, refinementPiece110_check, refinementPiece111_check, refinementPiece112_check, refinementPiece113_check, refinementPiece114_check, refinementPiece115_check, refinementPiece116_check, refinementPiece117_check, refinementPiece118_check, refinementPiece119_check, macroPiece25_check, Bool.true_and]
  simp [certifiedPiecewiseCheck, sourcePiecewiseCheck, hn, coverage_8, hs, hp]

theorem wire_success_8 : decodeRow qs segmentRefs catalog wire8 = some row8 := by rfl
theorem model_success_8 : interpCompactRow catalog row8 = some model8 := by rfl
theorem canonical_8 : compactRowCanonical row8 = true := by decide
def wire9 : RowRef := .floor 7 [0,1,2,3,4]
def row9 : CompactRow := .floor q7 [c0,c1,c2,c3,c4]
def segments9 : List SourceSegment := [s0,s1,s2,s3,s4]
def model9 : ModelRow := .floor (interpRat q7) segments9
theorem rowseg_9_0 : sourceSegmentCheck (interpRat q7) s0 = true :=
  segmentCheck_mono (by norm_num [interpRat, q7]) maxcheck_0
theorem rowseg_9_1 : sourceSegmentCheck (interpRat q7) s1 = true :=
  segmentCheck_mono (by norm_num [interpRat, q7]) maxcheck_1
theorem rowseg_9_2 : sourceSegmentCheck (interpRat q7) s2 = true :=
  segmentCheck_mono (by norm_num [interpRat, q7]) maxcheck_2
theorem rowseg_9_3 : sourceSegmentCheck (interpRat q7) s3 = true :=
  segmentCheck_mono (by norm_num [interpRat, q7]) maxcheck_3
theorem rowseg_9_4 : sourceSegmentCheck (interpRat q7) s4 = true :=
  segmentCheck_mono (by norm_num [interpRat, q7]) maxcheck_4
theorem coverage_9 : sourceCoverFrom (795/128) (405/64) segments9 = true := by
  norm_num [sourceCoverFrom, segments9, s0, s1, s2, s3, s4, q8, q9, q10, q11, q12, q13, interpRat]
theorem piecewise_9 : certifiedPiecewiseCheck (795/128) (405/64) (interpRat q7) segments9 = true := by
  have hn : decide (0 < segments9.length) = true := by norm_num [segments9]
  have hs : segments9.all (sourceSegmentCheck (interpRat q7)) = true := by
    simp only [segments9, List.all_cons, List.all_nil, rowseg_9_0, rowseg_9_1, rowseg_9_2, rowseg_9_3, rowseg_9_4, Bool.true_and]
  have hp : segments9.all (fun s => s.piece.check) = true := by
    simp only [segments9, s0, s1, s2, s3, s4, List.all_cons, List.all_nil, macroPiece2_check, refinementPiece0_check, refinementPiece1_check, refinementPiece2_check, refinementPiece3_check, Bool.true_and]
  simp [certifiedPiecewiseCheck, sourcePiecewiseCheck, hn, coverage_9, hs, hp]

theorem wire_success_9 : decodeRow qs segmentRefs catalog wire9 = some row9 := by rfl
theorem model_success_9 : interpCompactRow catalog row9 = some model9 := by rfl
theorem canonical_9 : compactRowCanonical row9 = true := by decide
def wire10 : RowRef := .floor 0 [23,24,25,26,27,28,29,30,31]
def row10 : CompactRow := .floor q0 [c23,c24,c25,c26,c27,c28,c29,c30,c31]
def segments10 : List SourceSegment := [s23,s24,s25,s26,s27,s28,s29,s30,s31]
def model10 : ModelRow := .floor (interpRat q0) segments10
theorem rowseg_10_23 : sourceSegmentCheck (interpRat q0) s23 = true :=
  segmentCheck_mono (by norm_num [interpRat, q0]) maxcheck_23
theorem rowseg_10_24 : sourceSegmentCheck (interpRat q0) s24 = true :=
  segmentCheck_mono (by norm_num [interpRat, q0]) maxcheck_24
theorem rowseg_10_25 : sourceSegmentCheck (interpRat q0) s25 = true :=
  segmentCheck_mono (by norm_num [interpRat, q0]) maxcheck_25
theorem rowseg_10_26 : sourceSegmentCheck (interpRat q0) s26 = true :=
  segmentCheck_mono (by norm_num [interpRat, q0]) maxcheck_26
theorem rowseg_10_27 : sourceSegmentCheck (interpRat q0) s27 = true :=
  segmentCheck_mono (by norm_num [interpRat, q0]) maxcheck_27
theorem rowseg_10_28 : sourceSegmentCheck (interpRat q0) s28 = true :=
  segmentCheck_mono (by norm_num [interpRat, q0]) maxcheck_28
theorem rowseg_10_29 : sourceSegmentCheck (interpRat q0) s29 = true :=
  segmentCheck_mono (by norm_num [interpRat, q0]) maxcheck_29
theorem rowseg_10_30 : sourceSegmentCheck (interpRat q0) s30 = true :=
  segmentCheck_mono (by norm_num [interpRat, q0]) maxcheck_30
theorem rowseg_10_31 : sourceSegmentCheck (interpRat q0) s31 = true :=
  segmentCheck_mono (by norm_num [interpRat, q0]) maxcheck_31
theorem coverage_10 : sourceCoverFrom (405/32) (825/64) segments10 = true := by
  norm_num [sourceCoverFrom, segments10, s23, s24, s25, s26, s27, s28, s29, s30, s31, q31, q32, q33, q34, q35, q36, q37, q38, q39, q40, interpRat]
theorem piecewise_10 : certifiedPiecewiseCheck (405/32) (825/64) (interpRat q0) segments10 = true := by
  have hn : decide (0 < segments10.length) = true := by norm_num [segments10]
  have hs : segments10.all (sourceSegmentCheck (interpRat q0)) = true := by
    simp only [segments10, List.all_cons, List.all_nil, rowseg_10_23, rowseg_10_24, rowseg_10_25, rowseg_10_26, rowseg_10_27, rowseg_10_28, rowseg_10_29, rowseg_10_30, rowseg_10_31, Bool.true_and]
  have hp : segments10.all (fun s => s.piece.check) = true := by
    simp only [segments10, s23, s24, s25, s26, s27, s28, s29, s30, s31, List.all_cons, List.all_nil, refinementPiece41_check, refinementPiece42_check, refinementPiece43_check, refinementPiece44_check, refinementPiece45_check, refinementPiece46_check, macroPiece9_check, macroPiece10_check, macroPiece11_check, Bool.true_and]
  simp [certifiedPiecewiseCheck, sourcePiecewiseCheck, hn, coverage_10, hs, hp]

theorem wire_success_10 : decodeRow qs segmentRefs catalog wire10 = some row10 := by rfl
theorem model_success_10 : interpCompactRow catalog row10 = some model10 := by rfl
theorem canonical_10 : compactRowCanonical row10 = true := by decide
def wire11 : RowRef := .floor 1 [32,33,34,35,36,37,38,39,41,42,43,44,45,46,47,48,49,50,51,52,53,54,56,57,58]
def row11 : CompactRow := .floor q1 [c32,c33,c34,c35,c36,c37,c38,c39,c41,c42,c43,c44,c45,c46,c47,c48,c49,c50,c51,c52,c53,c54,c56,c57,c58]
def segments11 : List SourceSegment := [s32,s33,s34,s35,s36,s37,s38,s39,s41,s42,s43,s44,s45,s46,s47,s48,s49,s50,s51,s52,s53,s54,s56,s57,s58]
def model11 : ModelRow := .floor (interpRat q1) segments11
theorem rowseg_11_32 : sourceSegmentCheck (interpRat q1) s32 = true :=
  segmentCheck_mono (by norm_num [interpRat, q1]) maxcheck_32
theorem rowseg_11_33 : sourceSegmentCheck (interpRat q1) s33 = true :=
  segmentCheck_mono (by norm_num [interpRat, q1]) maxcheck_33
theorem rowseg_11_34 : sourceSegmentCheck (interpRat q1) s34 = true :=
  segmentCheck_mono (by norm_num [interpRat, q1]) maxcheck_34
theorem rowseg_11_35 : sourceSegmentCheck (interpRat q1) s35 = true :=
  segmentCheck_mono (by norm_num [interpRat, q1]) maxcheck_35
theorem rowseg_11_36 : sourceSegmentCheck (interpRat q1) s36 = true :=
  segmentCheck_mono (by norm_num [interpRat, q1]) maxcheck_36
theorem rowseg_11_37 : sourceSegmentCheck (interpRat q1) s37 = true :=
  segmentCheck_mono (by norm_num [interpRat, q1]) maxcheck_37
theorem rowseg_11_38 : sourceSegmentCheck (interpRat q1) s38 = true :=
  segmentCheck_mono (by norm_num [interpRat, q1]) maxcheck_38
theorem rowseg_11_39 : sourceSegmentCheck (interpRat q1) s39 = true :=
  segmentCheck_mono (by norm_num [interpRat, q1]) maxcheck_39
theorem rowseg_11_41 : sourceSegmentCheck (interpRat q1) s41 = true :=
  segmentCheck_mono (by norm_num [interpRat, q1]) maxcheck_41
theorem rowseg_11_42 : sourceSegmentCheck (interpRat q1) s42 = true :=
  segmentCheck_mono (by norm_num [interpRat, q1]) maxcheck_42
theorem rowseg_11_43 : sourceSegmentCheck (interpRat q1) s43 = true :=
  segmentCheck_mono (by norm_num [interpRat, q1]) maxcheck_43
theorem rowseg_11_44 : sourceSegmentCheck (interpRat q1) s44 = true :=
  segmentCheck_mono (by norm_num [interpRat, q1]) maxcheck_44
theorem rowseg_11_45 : sourceSegmentCheck (interpRat q1) s45 = true :=
  segmentCheck_mono (by norm_num [interpRat, q1]) maxcheck_45
theorem rowseg_11_46 : sourceSegmentCheck (interpRat q1) s46 = true :=
  segmentCheck_mono (by norm_num [interpRat, q1]) maxcheck_46
theorem rowseg_11_47 : sourceSegmentCheck (interpRat q1) s47 = true :=
  segmentCheck_mono (by norm_num [interpRat, q1]) maxcheck_47
theorem rowseg_11_48 : sourceSegmentCheck (interpRat q1) s48 = true :=
  segmentCheck_mono (by norm_num [interpRat, q1]) maxcheck_48
theorem rowseg_11_49 : sourceSegmentCheck (interpRat q1) s49 = true :=
  segmentCheck_mono (by norm_num [interpRat, q1]) maxcheck_49
theorem rowseg_11_50 : sourceSegmentCheck (interpRat q1) s50 = true :=
  segmentCheck_mono (by norm_num [interpRat, q1]) maxcheck_50
theorem rowseg_11_51 : sourceSegmentCheck (interpRat q1) s51 = true :=
  segmentCheck_mono (by norm_num [interpRat, q1]) maxcheck_51
theorem rowseg_11_52 : sourceSegmentCheck (interpRat q1) s52 = true :=
  segmentCheck_mono (by norm_num [interpRat, q1]) maxcheck_52
theorem rowseg_11_53 : sourceSegmentCheck (interpRat q1) s53 = true :=
  segmentCheck_mono (by norm_num [interpRat, q1]) maxcheck_53
theorem rowseg_11_54 : sourceSegmentCheck (interpRat q1) s54 = true :=
  segmentCheck_mono (by norm_num [interpRat, q1]) maxcheck_54
theorem rowseg_11_56 : sourceSegmentCheck (interpRat q1) s56 = true :=
  segmentCheck_mono (by norm_num [interpRat, q1]) maxcheck_56
theorem rowseg_11_57 : sourceSegmentCheck (interpRat q1) s57 = true :=
  segmentCheck_mono (by norm_num [interpRat, q1]) maxcheck_57
theorem rowseg_11_58 : sourceSegmentCheck (interpRat q1) s58 = true :=
  segmentCheck_mono (by norm_num [interpRat, q1]) maxcheck_58
theorem coverage_11 : sourceCoverFrom (1215/64) (1245/64) segments11 = true := by
  norm_num [sourceCoverFrom, segments11, s32, s33, s34, s35, s36, s37, s38, s39, s41, s42, s43, s44, s45, s46, s47, s48, s49, s50, s51, s52, s53, s54, s56, s57, s58, q41, q42, q43, q44, q45, q46, q47, q48, q50, q51, q52, q53, q54, q55, q56, q57, q58, q59, q60, q61, q62, q63, q64, q66, q67, q68, interpRat]
theorem piecewise_11 : certifiedPiecewiseCheck (1215/64) (1245/64) (interpRat q1) segments11 = true := by
  have hn : decide (0 < segments11.length) = true := by norm_num [segments11]
  have hs : segments11.all (sourceSegmentCheck (interpRat q1)) = true := by
    simp only [segments11, List.all_cons, List.all_nil, rowseg_11_32, rowseg_11_33, rowseg_11_34, rowseg_11_35, rowseg_11_36, rowseg_11_37, rowseg_11_38, rowseg_11_39, rowseg_11_41, rowseg_11_42, rowseg_11_43, rowseg_11_44, rowseg_11_45, rowseg_11_46, rowseg_11_47, rowseg_11_48, rowseg_11_49, rowseg_11_50, rowseg_11_51, rowseg_11_52, rowseg_11_53, rowseg_11_54, rowseg_11_56, rowseg_11_57, rowseg_11_58, Bool.true_and]
  have hp : segments11.all (fun s => s.piece.check) = true := by
    simp only [segments11, s32, s33, s34, s35, s36, s37, s38, s39, s41, s42, s43, s44, s45, s46, s47, s48, s49, s50, s51, s52, s53, s54, s56, s57, s58, List.all_cons, List.all_nil, refinementPiece48_check, refinementPiece49_check, refinementPiece50_check, refinementPiece51_check, refinementPiece52_check, refinementPiece53_check, refinementPiece54_check, refinementPiece55_check, refinementPiece56_check, refinementPiece57_check, refinementPiece58_check, refinementPiece59_check, refinementPiece60_check, refinementPiece61_check, refinementPiece62_check, refinementPiece63_check, refinementPiece64_check, refinementPiece65_check, refinementPiece66_check, refinementPiece67_check, refinementPiece68_check, refinementPiece69_check, refinementPiece70_check, refinementPiece71_check, macroPiece18_check, Bool.true_and]
  simp [certifiedPiecewiseCheck, sourcePiecewiseCheck, hn, coverage_11, hs, hp]

theorem wire_success_11 : decodeRow qs segmentRefs catalog wire11 = some row11 := by rfl
theorem model_success_11 : interpCompactRow catalog row11 = some model11 := by rfl
theorem canonical_11 : compactRowCanonical row11 = true := by decide
def wire12 : RowRef := .floor 5 [15,16,17,18,19,20,21,22]
def row12 : CompactRow := .floor q5 [c15,c16,c17,c18,c19,c20,c21,c22]
def segments12 : List SourceSegment := [s15,s16,s17,s18,s19,s20,s21,s22]
def model12 : ModelRow := .floor (interpRat q5) segments12
theorem rowseg_12_15 : sourceSegmentCheck (interpRat q5) s15 = true :=
  segmentCheck_mono (by norm_num [interpRat, q5]) maxcheck_15
theorem rowseg_12_16 : sourceSegmentCheck (interpRat q5) s16 = true :=
  segmentCheck_mono (by norm_num [interpRat, q5]) maxcheck_16
theorem rowseg_12_17 : sourceSegmentCheck (interpRat q5) s17 = true :=
  segmentCheck_mono (by norm_num [interpRat, q5]) maxcheck_17
theorem rowseg_12_18 : sourceSegmentCheck (interpRat q5) s18 = true :=
  segmentCheck_mono (by norm_num [interpRat, q5]) maxcheck_18
theorem rowseg_12_19 : sourceSegmentCheck (interpRat q5) s19 = true :=
  segmentCheck_mono (by norm_num [interpRat, q5]) maxcheck_19
theorem rowseg_12_20 : sourceSegmentCheck (interpRat q5) s20 = true :=
  segmentCheck_mono (by norm_num [interpRat, q5]) maxcheck_20
theorem rowseg_12_21 : sourceSegmentCheck (interpRat q5) s21 = true :=
  segmentCheck_mono (by norm_num [interpRat, q5]) maxcheck_21
theorem rowseg_12_22 : sourceSegmentCheck (interpRat q5) s22 = true :=
  segmentCheck_mono (by norm_num [interpRat, q5]) maxcheck_22
theorem coverage_12 : sourceCoverFrom (825/128) (105/16) segments12 = true := by
  norm_num [sourceCoverFrom, segments12, s15, s16, s17, s18, s19, s20, s21, s22, q22, q23, q24, q25, q26, q27, q28, q29, q30, interpRat]
theorem piecewise_12 : certifiedPiecewiseCheck (825/128) (105/16) (interpRat q5) segments12 = true := by
  have hn : decide (0 < segments12.length) = true := by norm_num [segments12]
  have hs : segments12.all (sourceSegmentCheck (interpRat q5)) = true := by
    simp only [segments12, List.all_cons, List.all_nil, rowseg_12_15, rowseg_12_16, rowseg_12_17, rowseg_12_18, rowseg_12_19, rowseg_12_20, rowseg_12_21, rowseg_12_22, Bool.true_and]
  have hp : segments12.all (fun s => s.piece.check) = true := by
    simp only [segments12, s15, s16, s17, s18, s19, s20, s21, s22, List.all_cons, List.all_nil, refinementPiece11_check, refinementPiece12_check, refinementPiece13_check, refinementPiece14_check, refinementPiece15_check, refinementPiece16_check, refinementPiece17_check, refinementPiece18_check, Bool.true_and]
  simp [certifiedPiecewiseCheck, sourcePiecewiseCheck, hn, coverage_12, hs, hp]

theorem wire_success_12 : decodeRow qs segmentRefs catalog wire12 = some row12 := by rfl
theorem model_success_12 : interpCompactRow catalog row12 = some model12 := by rfl
theorem canonical_12 : compactRowCanonical row12 = true := by decide
def wire13 : RowRef := .direct 9
def row13 : CompactRow := .direct 9
def model13 : ModelRow := .direct macroPiece11
theorem wire_success_13 : decodeRow qs segmentRefs catalog wire13 = some row13 := by rfl
theorem model_success_13 : interpCompactRow catalog row13 = some model13 := by rfl
theorem canonical_13 : compactRowCanonical row13 = true := by decide
def wire14 : RowRef := .floor 5 [5,6,7,8,9,10,11,12,14,16,17,18,19,20,21,22]
def row14 : CompactRow := .floor q5 [c5,c6,c7,c8,c9,c10,c11,c12,c14,c16,c17,c18,c19,c20,c21,c22]
def segments14 : List SourceSegment := [s5,s6,s7,s8,s9,s10,s11,s12,s14,s16,s17,s18,s19,s20,s21,s22]
def model14 : ModelRow := .floor (interpRat q5) segments14
theorem rowseg_14_5 : sourceSegmentCheck (interpRat q5) s5 = true :=
  segmentCheck_mono (by norm_num [interpRat, q5]) maxcheck_5
theorem rowseg_14_6 : sourceSegmentCheck (interpRat q5) s6 = true :=
  segmentCheck_mono (by norm_num [interpRat, q5]) maxcheck_6
theorem rowseg_14_7 : sourceSegmentCheck (interpRat q5) s7 = true :=
  segmentCheck_mono (by norm_num [interpRat, q5]) maxcheck_7
theorem rowseg_14_8 : sourceSegmentCheck (interpRat q5) s8 = true :=
  segmentCheck_mono (by norm_num [interpRat, q5]) maxcheck_8
theorem rowseg_14_9 : sourceSegmentCheck (interpRat q5) s9 = true :=
  segmentCheck_mono (by norm_num [interpRat, q5]) maxcheck_9
theorem rowseg_14_10 : sourceSegmentCheck (interpRat q5) s10 = true :=
  segmentCheck_mono (by norm_num [interpRat, q5]) maxcheck_10
theorem rowseg_14_11 : sourceSegmentCheck (interpRat q5) s11 = true :=
  segmentCheck_mono (by norm_num [interpRat, q5]) maxcheck_11
theorem rowseg_14_12 : sourceSegmentCheck (interpRat q5) s12 = true :=
  segmentCheck_mono (by norm_num [interpRat, q5]) maxcheck_12
theorem rowseg_14_14 : sourceSegmentCheck (interpRat q5) s14 = true :=
  segmentCheck_mono (by norm_num [interpRat, q5]) maxcheck_14
theorem rowseg_14_16 : sourceSegmentCheck (interpRat q5) s16 = true :=
  segmentCheck_mono (by norm_num [interpRat, q5]) maxcheck_16
theorem rowseg_14_17 : sourceSegmentCheck (interpRat q5) s17 = true :=
  segmentCheck_mono (by norm_num [interpRat, q5]) maxcheck_17
theorem rowseg_14_18 : sourceSegmentCheck (interpRat q5) s18 = true :=
  segmentCheck_mono (by norm_num [interpRat, q5]) maxcheck_18
theorem rowseg_14_19 : sourceSegmentCheck (interpRat q5) s19 = true :=
  segmentCheck_mono (by norm_num [interpRat, q5]) maxcheck_19
theorem rowseg_14_20 : sourceSegmentCheck (interpRat q5) s20 = true :=
  segmentCheck_mono (by norm_num [interpRat, q5]) maxcheck_20
theorem rowseg_14_21 : sourceSegmentCheck (interpRat q5) s21 = true :=
  segmentCheck_mono (by norm_num [interpRat, q5]) maxcheck_21
theorem rowseg_14_22 : sourceSegmentCheck (interpRat q5) s22 = true :=
  segmentCheck_mono (by norm_num [interpRat, q5]) maxcheck_22
theorem coverage_14 : sourceCoverFrom (405/64) (105/16) segments14 = true := by
  norm_num [sourceCoverFrom, segments14, s5, s6, s7, s8, s9, s10, s11, s12, s14, s16, s17, s18, s19, s20, s21, s22, q13, q14, q15, q16, q17, q18, q19, q20, q21, q23, q24, q25, q26, q27, q28, q29, q30, interpRat]
theorem piecewise_14 : certifiedPiecewiseCheck (405/64) (105/16) (interpRat q5) segments14 = true := by
  have hn : decide (0 < segments14.length) = true := by norm_num [segments14]
  have hs : segments14.all (sourceSegmentCheck (interpRat q5)) = true := by
    simp only [segments14, List.all_cons, List.all_nil, rowseg_14_5, rowseg_14_6, rowseg_14_7, rowseg_14_8, rowseg_14_9, rowseg_14_10, rowseg_14_11, rowseg_14_12, rowseg_14_14, rowseg_14_16, rowseg_14_17, rowseg_14_18, rowseg_14_19, rowseg_14_20, rowseg_14_21, rowseg_14_22, Bool.true_and]
  have hp : segments14.all (fun s => s.piece.check) = true := by
    simp only [segments14, s5, s6, s7, s8, s9, s10, s11, s12, s14, s16, s17, s18, s19, s20, s21, s22, List.all_cons, List.all_nil, refinementPiece3_check, refinementPiece4_check, refinementPiece5_check, refinementPiece6_check, refinementPiece7_check, refinementPiece8_check, refinementPiece9_check, refinementPiece10_check, refinementPiece11_check, refinementPiece12_check, refinementPiece13_check, refinementPiece14_check, refinementPiece15_check, refinementPiece16_check, refinementPiece17_check, refinementPiece18_check, Bool.true_and]
  simp [certifiedPiecewiseCheck, sourcePiecewiseCheck, hn, coverage_14, hs, hp]

theorem wire_success_14 : decodeRow qs segmentRefs catalog wire14 = some row14 := by rfl
theorem model_success_14 : interpCompactRow catalog row14 = some model14 := by rfl
theorem canonical_14 : compactRowCanonical row14 = true := by decide
def rows (p : Fin 15) : CompactRow := match p.val with | 0 => row0 | 1 => row1 | 2 => row2 | 3 => row3 | 4 => row4 | 5 => row5 | 6 => row6 | 7 => row7 | 8 => row8 | 9 => row9 | 10 => row10 | 11 => row11 | 12 => row12 | 13 => row13 | _ => row14
def models (p : Fin 15) : ModelRow := match p.val with | 0 => model0 | 1 => model1 | 2 => model2 | 3 => model3 | 4 => model4 | 5 => model5 | 6 => model6 | 7 => model7 | 8 => model8 | 9 => model9 | 10 => model10 | 11 => model11 | 12 => model12 | 13 => model13 | _ => model14
def wireRows (p : Fin 15) : RowRef := match p.val with | 0 => wire0 | 1 => wire1 | 2 => wire2 | 3 => wire3 | 4 => wire4 | 5 => wire5 | 6 => wire6 | 7 => wire7 | 8 => wire8 | 9 => wire9 | 10 => wire10 | 11 => wire11 | 12 => wire12 | 13 => wire13 | _ => wire14
def box : GapBox where
  lo := fun i => match i.val with | 0 => (405/64) | 1 => (825/128) | 2 => (795/128) | 3 => (825/128) | _ => (405/64)
  hi := fun i => match i.val with | 0 => (825/128) | 1 => (105/16) | 2 => (405/64) | 3 => (105/16) | _ => (105/16)
def anchor : Fin 5 → ℚ := box.lo
def distances (p : Fin 15) : RatInterval := match p.val with | 0 => ⟨(405/64),(825/128)⟩ | 1 => ⟨(1635/128),(1665/128)⟩ | 2 => ⟨(1215/64),(2475/128)⟩ | 3 => ⟨(3255/128),(3315/128)⟩ | 4 => ⟨(4065/128),(4155/128)⟩ | 5 => ⟨(825/128),(105/16)⟩ | 6 => ⟨(405/32),(825/64)⟩ | 7 => ⟨(2445/128),(1245/64)⟩ | 8 => ⟨(3255/128),(1665/64)⟩ | 9 => ⟨(795/128),(405/64)⟩ | 10 => ⟨(405/32),(825/64)⟩ | 11 => ⟨(1215/64),(1245/64)⟩ | 12 => ⟨(825/128),(105/16)⟩ | 13 => ⟨(1635/128),(105/8)⟩ | _ => ⟨(405/64),(105/16)⟩
theorem distances_exact : ∀ p, distanceInterval box p = distances p := by
  intro p
  fin_cases p <;> simp [distanceInterval, distances, gapSupport, pairLeft, pairRight, box, Finset.sum_filter, Fin.sum_univ_five] <;> norm_num

theorem row_checked_0 : compactRowCheck catalog box (⟨0, by decide⟩ : Fin 15) row0 = true := by
  simp only [compactRowCheck, canonical_0, model_success_0, Bool.true_and, model0, modelCheck]
  rw [distances_exact]
  exact piecewise_0
theorem row_checked_1 : compactRowCheck catalog box (⟨1, by decide⟩ : Fin 15) row1 = true := by
  simp only [compactRowCheck, canonical_1, model_success_1, Bool.true_and, model1, modelCheck]
  rw [distances_exact]
  rw [macroPiece11_check]
  norm_num [distances, MacroPiece.box, macroPiece11]
theorem row_checked_2 : compactRowCheck catalog box (⟨2, by decide⟩ : Fin 15) row2 = true := by
  simp only [compactRowCheck, canonical_2, model_success_2, Bool.true_and, model2, modelCheck]
  rw [distances_exact]
  exact piecewise_2
theorem row_checked_3 : compactRowCheck catalog box (⟨3, by decide⟩ : Fin 15) row3 = true := by
  simp only [compactRowCheck, canonical_3, model_success_3, Bool.true_and, model3, modelCheck]
  rw [distances_exact]
  exact piecewise_3
theorem row_checked_4 : compactRowCheck catalog box (⟨4, by decide⟩ : Fin 15) row4 = true := by
  simp only [compactRowCheck, canonical_4, model_success_4, Bool.true_and, model4, modelCheck]
  rw [distances_exact]
  exact piecewise_4
theorem row_checked_5 : compactRowCheck catalog box (⟨5, by decide⟩ : Fin 15) row5 = true := by
  simp only [compactRowCheck, canonical_5, model_success_5, Bool.true_and, model5, modelCheck]
  rw [distances_exact]
  exact piecewise_5
theorem row_checked_6 : compactRowCheck catalog box (⟨6, by decide⟩ : Fin 15) row6 = true := by
  simp only [compactRowCheck, canonical_6, model_success_6, Bool.true_and, model6, modelCheck]
  rw [distances_exact]
  exact piecewise_6
theorem row_checked_7 : compactRowCheck catalog box (⟨7, by decide⟩ : Fin 15) row7 = true := by
  simp only [compactRowCheck, canonical_7, model_success_7, Bool.true_and, model7, modelCheck]
  rw [distances_exact]
  exact piecewise_7
theorem row_checked_8 : compactRowCheck catalog box (⟨8, by decide⟩ : Fin 15) row8 = true := by
  simp only [compactRowCheck, canonical_8, model_success_8, Bool.true_and, model8, modelCheck]
  rw [distances_exact]
  exact piecewise_8
theorem row_checked_9 : compactRowCheck catalog box (⟨9, by decide⟩ : Fin 15) row9 = true := by
  simp only [compactRowCheck, canonical_9, model_success_9, Bool.true_and, model9, modelCheck]
  rw [distances_exact]
  exact piecewise_9
theorem row_checked_10 : compactRowCheck catalog box (⟨10, by decide⟩ : Fin 15) row10 = true := by
  simp only [compactRowCheck, canonical_10, model_success_10, Bool.true_and, model10, modelCheck]
  rw [distances_exact]
  exact piecewise_10
theorem row_checked_11 : compactRowCheck catalog box (⟨11, by decide⟩ : Fin 15) row11 = true := by
  simp only [compactRowCheck, canonical_11, model_success_11, Bool.true_and, model11, modelCheck]
  rw [distances_exact]
  exact piecewise_11
theorem row_checked_12 : compactRowCheck catalog box (⟨12, by decide⟩ : Fin 15) row12 = true := by
  simp only [compactRowCheck, canonical_12, model_success_12, Bool.true_and, model12, modelCheck]
  rw [distances_exact]
  exact piecewise_12
theorem row_checked_13 : compactRowCheck catalog box (⟨13, by decide⟩ : Fin 15) row13 = true := by
  simp only [compactRowCheck, canonical_13, model_success_13, Bool.true_and, model13, modelCheck]
  rw [distances_exact]
  rw [macroPiece11_check]
  norm_num [distances, MacroPiece.box, macroPiece11]
theorem row_checked_14 : compactRowCheck catalog box (⟨14, by decide⟩ : Fin 15) row14 = true := by
  simp only [compactRowCheck, canonical_14, model_success_14, Bool.true_and, model14, modelCheck]
  rw [distances_exact]
  exact piecewise_14
def floors (p : Fin 15) : ℚ := match p.val with | 0 => interpRat q6 | 1 => interpRat q0 | 2 => interpRat q1 | 3 => interpRat q3 | 4 => interpRat q4 | 5 => interpRat q5 | 6 => interpRat q0 | 7 => interpRat q2 | 8 => interpRat q3 | 9 => interpRat q7 | 10 => interpRat q0 | 11 => interpRat q1 | 12 => interpRat q5 | 13 => interpRat q0 | _ => interpRat q5
def terms (p : Fin 15) : RankOneModel :=
  if p.val = 1 then macroPieceRankModel (fun _ => macroPiece11) p
  else if p.val = 13 then macroPieceRankModel (fun _ => macroPiece11) p
  else {base := floors p, weight := 0, offset := 0, coeff := fun _ => 0}
theorem interpreted_terms : (fun p => interpModel (models p) p) = terms := by
  funext p
  fin_cases p <;> rfl

theorem tangent_lower : rankTangentLower terms (1094977/5000000000) box anchor = (108853955129699356804065918948443215217/7812500000000000000000000000000000000000) := by
  norm_num [rankTangentLower, rankObjectiveRat, rankGradient, affineCoordinateLower, terms, floors, interpRat, q6, q0, q1, q3, q4, q5, q2, q7, anchor, box, macroPiece11, MacroPiece.box, macroPieceRankModel, wellRankModel, wellSlope, wellOffset, consecutiveCoeff, gapSupport, RankOneModel.valueRat, RankOneModel.dotRat, pairLeft, pairRight, Finset.sum_filter, Fin.sum_univ_succ, Fin.sum_univ_five]
theorem tangent_checked : rankTangentCheck (647/50000) (1094977/5000000000) box anchor terms = true := by
  have ho : box.ordered = true := by
    rw [GapBox.ordered_iff]
    intro i
    fin_cases i <;> norm_num [box]
  have ha : ∀ i, box.lo i ≤ anchor i ∧ anchor i ≤ box.hi i := by
    intro i
    fin_cases i <;> norm_num [anchor, box]
  have hw : ∀ p, 0 ≤ (terms p).weight := by
    intro p
    fin_cases p <;> norm_num [terms, floors, interpRat, q6, q0, q1, q3, q4, q5, q2, q7, macroPiece11, macroPieceRankModel, wellRankModel, wellSlope, wellOffset]
  have hm : (647/50000 : ℚ) ≤ rankTangentLower terms (1094977/5000000000) box anchor := by
    rw [tangent_lower]
    norm_num
  simp [rankTangentCheck, ho, ha, hw, hm]


theorem wire_success : ∀ p, decodeRow qs segmentRefs catalog (wireRows p) = some (rows p) := by
  intro p
  fin_cases p
  · exact wire_success_0
  · exact wire_success_1
  · exact wire_success_2
  · exact wire_success_3
  · exact wire_success_4
  · exact wire_success_5
  · exact wire_success_6
  · exact wire_success_7
  · exact wire_success_8
  · exact wire_success_9
  · exact wire_success_10
  · exact wire_success_11
  · exact wire_success_12
  · exact wire_success_13
  · exact wire_success_14
theorem model_success : ∀ p, interpCompactRow catalog (rows p) = some (models p) := by
  intro p
  fin_cases p
  · exact model_success_0
  · exact model_success_1
  · exact model_success_2
  · exact model_success_3
  · exact model_success_4
  · exact model_success_5
  · exact model_success_6
  · exact model_success_7
  · exact model_success_8
  · exact model_success_9
  · exact model_success_10
  · exact model_success_11
  · exact model_success_12
  · exact model_success_13
  · exact model_success_14
theorem all_rows : ∀ p, compactRowCheck catalog box p (rows p) = true := by
  intro p
  fin_cases p
  · exact row_checked_0
  · exact row_checked_1
  · exact row_checked_2
  · exact row_checked_3
  · exact row_checked_4
  · exact row_checked_5
  · exact row_checked_6
  · exact row_checked_7
  · exact row_checked_8
  · exact row_checked_9
  · exact row_checked_10
  · exact row_checked_11
  · exact row_checked_12
  · exact row_checked_13
  · exact row_checked_14
theorem accepted : explicitLeafCheck catalog (647/50000) (1094977/5000000000) box anchor rows models = true := by
  unfold explicitLeafCheck
  rw [interpreted_terms]
  simp [all_rows, tangent_checked]
theorem leaf_sound : ∀ ⦃g : Fin 5 → ℝ⦄, box.Holds g →
    ((647/50000 : ℚ) : ℝ) ≤ sextupleEnergy g + ((1094977/5000000000 : ℚ) : ℝ) * sextupleSpan g :=
  explicitLeafCheck_sound model_success accepted
#print axioms wire_success
#print axioms model_success
#print axioms all_rows
#print axioms tangent_checked
#print axioms accepted
#print axioms leaf_sound
#print leaf_sound
end IndependentTerminal22
