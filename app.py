import streamlit as st
import pandas as pd
import json

# Konfigurasjon av siden
st.set_page_config(
    page_title="Zenith AI & Security GRC Engine",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ Zenith AI & Security GRC Compliance Engine")
st.markdown("""
Velkommen til din interaktive plattform for **Governance, Risk, and Compliance (GRC)**.
Dette verktøyet evaluerer AI-systemer og programvare mot ISO 27001, GDPR og EU AI Act.
""")

# Layout: To kolonner
col1, col2 = st.columns([1, 1.2], gap="large")

with col1:
    st.header("📋 Prosjekt & Risikovurdering")
    st.write("Fyll ut detaljene for å starte en automatisert sikkerhetsrevisjon.")
    
    project_name = st.text_input("Prosjekt / Systemnavn", placeholder="f.eks. Oda-Customer-Support-LLM")
    department = st.selectbox("Avdeling / Team", ["Data Science & AI", "Platform Engineering", "Commercial Systems", "Logistics & Supply Chain"])
    
    st.divider()
    st.subheader("🔍 Kontrollmatrise & Rammeverk")
    
    data_privacy = st.checkbox("Behandler personopplysninger (PII / GDPR-omfang)")
    explainability = st.checkbox("Modellen er forklarbar og auditérbar (EU AI Act)", value=True)
    bias_monitoring = st.checkbox("Aktiv overvåking av bias og datadrift", value=False)
    access_control = st.checkbox("Streng tilgangskontroll (IAM) og revisjonslogging på datapipelines", value=True)

    st.divider()
    calculate_button = st.button("🚀 Kjør Risikovurdering", type="primary")

with col2:
    st.header("📊 Analyseresultater & Styringsrapport")
    
    if calculate_button and project_name:
        # GRC Logikk og vekting
        base_risk_score = 0
        max_score = 100
        gaps = []
        recommendations = []
        
        if data_privacy:
            base_risk_score += 35
            gaps.append("⚠️ **Høy Risiko:** Systemet håndterer PII (Underlagt GDPR).")
            recommendations.append("🔒 *Tiltak:* Implementer dataminimering og sørg for at tekstfelt tokeniseres før de lagres.")
            
        if not explainability:
            base_risk_score += 25
            gaps.append("⚠️ **Etterlevelsesgap:** Svart-boks-modell identifisert. Kan bryte med EU AI Act.")
            recommendations.append("📄 *Tiltak:* Generer standardiserte systemkort og dokumenter treningsparametere.")
            
        if not bias_monitoring:
            base_risk_score += 20
            gaps.append("⚠️ **Operasjonell Risiko:** Mangler varsling for modellskeivhet (bias) og drift.")
            recommendations.append("📈 *Tiltak:* Integrer overvåkningsverktøy i CI/CD-løpet for å sjekke produksjonsdata kontinuerlig.")
            
        if not access_control:
            base_risk_score += 20
            gaps.append("⚠️ **Sikkerhetsgap:** Ubeskyttet eller ulogget produksjonsmiljø.")
            recommendations.append("🔑 *Tiltak:* Håndhev 'Least Privilege' via IAM-roller og skru på fullstendig CloudTrail-logging.")

        # Endelig Status-dom
        if base_risk_score >= 70:
            st.error(f"❌ **VURDERING: AVVIST – Kritiske sikkerhetstiltak må utbedres**")
            risk_tier = "CRITICAL RISK"
        elif base_risk_score >= 40:
            st.warning(f"⚠️ **VURDERING: GODKJENT MED STRENGE VILKÅR**")
            risk_tier = "MEDIUM RISK"
        else:
            st.success(f"✅ **VURDERING: GODKJENT FOR PRODUKSJON**")
            risk_tier = "LOW RISK"
            
        # Visuelle målere (Metrics)
        m1, m2 = st.columns(2)
        m1.metric(label="Risikoscore (Inherent Risk)", value=f"{base_risk_score} / {max_score}")
        m2.metric(label="Risikonivå (Risk Tier)", value=risk_tier)
        
        st.divider()
        
        # --- NY VISUELL APP-RAPPORT UTEN NOTEPAD ---
        st.subheader("📝 Offisiell GRC Sign-Off Rapport (Forhåndsvisning)")
        
        # Her bygger vi rapporten live på skjermen i en ren, pen boks
        report_text = f"""
======================================================================
🛡️ OFFICIAL GRC SECURITY AUDIT REPORT: {project_name.upper()}
======================================================================
Ansvarlig avdeling : {department}
Kalkulert risiko   : {base_risk_score} / 100
Risikoklassifisering: {risk_tier}
----------------------------------------------------------------------
IDENTIFISERTE AVVIK & ETTERLEVELSESGAP:
"""
        for gap in gaps:
            report_text += f" - {gap}\n"
            
        report_text += "\nPÅKREVDE SIKKERHETSTILTAK (REMEDIATION PLAN):\n"
        for rec in recommendations:
            report_text += f" - {rec}\n"
            
        report_text += f"""----------------------------------------------------------------------
ENDELIG KONKLUSJON: {risk_tier} - PROSESSERT AUTOMATISK AV AVAN DAWOODI
======================================================================
"""
        
        # Viser rapporten i en profesjonell kode-blokk i appen
        st.code(report_text, language="text")
        
        # Enkel nedlastingsknapp for ren tekstfil (.txt) som garantert virker i Windows
        st.download_button(
            label="📥 Last ned signert rapport (.txt)",
            file_name=f"GRC_Rapport_{project_name.replace(' ', '_')}.txt",
            mime="text/plain",
            data=report_text
        )
        
    elif calculate_button and not project_name:
        st.info("💡 Vennligst skriv inn et 'Prosjekt / Systemnavn' i venstre felt før du kjører verktøyet.")
    else:
        st.info("ℹ️ Fyll ut kontrollene til venstre og trykk på knappen for å generere den offisielle rapporten her.")