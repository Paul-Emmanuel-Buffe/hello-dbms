## Architecture dbt — Suivi Marketing (Campagnes)

```mermaid
graph LR

subgraph Sources
    S1[brevo_raw.campaign_statistics_old_account]
    S2[brevo_raw.contacts]
    S3[clients_segmentation]
    S4[passages]
    S5[ventes]
end

subgraph dbt_Intermediate["dbt – Intermediate models"]
    I1[int_marketing_exposures\n(client × campaign)]
    I2[int_marketing_passages]
    I3[int_marketing_sales]
    I4[int_marketing_reactivation\n(inactivity → first passage)]
    I5[int_marketing_sales_attribution\n(J+0 → J+30)]
end

subgraph dbt_Mart["dbt – BI Mart"]
    M1[mart_marketing_campaigns_performance]
end

S1 --> I1
S2 --> I1
S3 --> I1

S4 --> I2
S5 --> I3
S3 --> I4

I1 --> I4
I2 --> I4

I1 --> I5
I3 --> I5

I4 --> M1
I5 --> M1

