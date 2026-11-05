import Terminal18Compositional
import Terminal18CatalogConnection
open Zeta23.ThmD.Sextuple A1294FifteenBridge A1294Compact
namespace Terminal18HistoricalAcceptance

theorem accepted_on_historical_catalog : compactQuadraticLeafCheck
    Catalog18TerminalLiteral.historicalTerminal18Catalog
    (647/50000) (1094977/5000000000)
    AuthenticCompact18.box AuthenticCompact18.anchor AuthenticCompact18.rows = true := by
  have hlocal : Catalog18.original = AuthenticCompact18.catalog := by rfl
  have h : Catalog18TerminalLiteral.historicalTerminal18Catalog = AuthenticCompact18.catalog :=
    Catalog18TerminalLiteral.historicalTerminal18_eq_original.trans hlocal
  rw [h]
  exact AuthenticCompact18.accepted

theorem leaf_sound_on_historical_catalog : ∀ ⦃g : Fin 5 → ℝ⦄,
    AuthenticCompact18.box.Holds g →
    ((647/50000 : ℚ) : ℝ) ≤ sextupleEnergy g +
      ((1094977/5000000000 : ℚ) : ℝ) * sextupleSpan g := by
  exact compactQuadraticLeafCheck_sound accepted_on_historical_catalog

#print Terminal18HistoricalAcceptance.accepted_on_historical_catalog
#print axioms Terminal18HistoricalAcceptance.accepted_on_historical_catalog
#print axioms Terminal18HistoricalAcceptance.leaf_sound_on_historical_catalog
end Terminal18HistoricalAcceptance
