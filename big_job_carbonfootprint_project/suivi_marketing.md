Campagnes envoyées
        │
        ▼
Clients exposés
(int_marketing_exposures)
        │
        ├───────────────┬──────────────────┐
        │               │                  │
        ▼               ▼                  ▼
Ventes              Passages        Analyse activité
(int_marketing_sales) (int_marketing_passages)
        │               │                  │
        ▼               ▼                  ▼
Attribution ventes   Attribution passages  Avant / Après exposition
(J+30)               (J+30)                (dernier / prochain passage)
        │               │                  │
        ▼               ▼                  ▼
Performance CA       Performance fréquentation
(mart_campaigns)     (mart_passages)


# Pipeline FLOWS 

flows_input (CSV source)
        │
        ▼
int_flows_sequences
        │
        ▼
int_flows_sequences_clients
        │
        ├───────────────┬───────────────────
        │               │
        ▼               ▼
int_flows_sequences_passages   int_flows_sequences_sales

