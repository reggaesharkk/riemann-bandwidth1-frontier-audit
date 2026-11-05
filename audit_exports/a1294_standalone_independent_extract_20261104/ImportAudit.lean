import StandaloneTerminal22
run_elab do
  let env ← Lean.getEnv
  for n in env.header.moduleNames do
    Lean.logInfo m!"CLOSURE {n}"
