import Zeta23.ThmD.Sextuple.CompositionalLeaf
run_elab do
  let env ← Lean.getEnv
  for n in env.header.moduleNames do
    Lean.logInfo m!"CLOSURE {n}"
